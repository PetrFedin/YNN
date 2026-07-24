#!/usr/bin/env python3
"""
W1b: парсер VTB PDF выписок → bank_payments (догрузка к Alfa).

Формат ВТБ (text extract): блоки начинаются с DD.MM.YYYY, далее №док, ВО, ИНН, БИК, счёт,
многострочное имя контрагента, затем «Дебет Кредит» как два числа *.00 и назначение.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "documents"
OUT = Path(__file__).resolve().parent
EV = ROOT / "live/evidence/w1_bank_cash_20260723"

VTB_FILES = [
    ("VTB_BankStatement_40702810804000008482_01.01.2024-22.06.2026_376277.pdf", "40702810804000008482", "FILE-008", "LE-OOO-DEKOR"),
    ("VTB_BankStatement_40802810404000000049_01.01.2024-22.06.2026_417016.pdf", "40802810404000000049", "FILE-009", "LE-IP-YANINA"),
    ("VTB_BankStatement_40802810500000006196_01.01.2024-22.06.2026_417014.pdf", "40802810500000006196", "FILE-010", "LE-IP-YANINA"),
]

AMT = r"(\d{1,3}(?:[\s\u00a0]\d{3})*(?:[.,]\d{2})|\d+[.,]\d{2}|\d+)"
# date at line start, then doc, VO, INN, BIK, account (loose)
HEAD = re.compile(
    rf"^(\d{{2}}\.\d{{2}}\.\d{{4}})\s+(\d+)\s+(\d+)\s+(\d{{10,12}})\s+(\d{{9}})\s+(\d{{20}})\s*(.*)$"
)
TWO_AMT = re.compile(rf"{AMT}\s+{AMT}")


def sha16(*parts) -> str:
    raw = "|".join("" if p is None else str(p) for p in parts)
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:16]


def parse_amt(s: str) -> float:
    s = s.replace("\u00a0", " ").replace(" ", "").replace(",", ".")
    return float(s)


def pdf_text(path: Path) -> str:
    r = PdfReader(str(path))
    parts = []
    for p in r.pages:
        parts.append(p.extract_text() or "")
    return "\n".join(parts)


def parse_vtb(path: Path, account_id: str, source_file_id: str, legal_entity_id: str) -> list[dict]:
    text = pdf_text(path)
    lines = [ln.rstrip() for ln in text.splitlines()]
    payments = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        m = HEAD.match(line)
        if not m:
            i += 1
            continue
        d_s, doc_no, vo, inn, bik, acct, rest = m.groups()
        d = datetime.strptime(d_s, "%d.%m.%Y").date()
        # accumulate until we find two amounts
        buf = [rest]
        j = i + 1
        debit = credit = None
        purpose_parts = []
        found_at = None
        while j < len(lines) and j < i + 12:
            ln = lines[j].strip()
            # stop if next transaction header
            if HEAD.match(ln) and j > i:
                break
            am = TWO_AMT.search(ln.replace("\u00a0", " "))
            if am and debit is None:
                # prefer the last two amounts on a line that looks like debit/credit
                # take first TWO_AMT match that has .xx style if possible
                all_am = list(TWO_AMT.finditer(ln.replace("\u00a0", " ")))
                pick = all_am[-1] if all_am else am
                try:
                    debit = parse_amt(pick.group(1))
                    credit = parse_amt(pick.group(2))
                    # purpose after amounts on same line
                    after = ln[pick.end() :].strip()
                    if after:
                        purpose_parts.append(after)
                    found_at = j
                    j += 1
                    # following lines until next header = purpose continuation / name was before
                    while j < len(lines) and j < found_at + 8:
                        nxt = lines[j].strip()
                        if HEAD.match(nxt):
                            break
                        if nxt and not TWO_AMT.fullmatch(nxt.replace("\u00a0", " ").strip()):
                            # skip pure amount lines
                            if not re.fullmatch(rf"{AMT}\s+{AMT}", nxt.replace("\u00a0", " ")):
                                purpose_parts.append(nxt)
                        j += 1
                    break
                except ValueError:
                    buf.append(ln)
                    j += 1
                    continue
            else:
                buf.append(ln)
                j += 1
        if debit is None:
            i += 1
            continue
        # counterparty name: text in buf before amounts (exclude account leftovers)
        name = " ".join(x for x in buf if x).strip()
        name = re.sub(r"\s+", " ", name)
        purpose = re.sub(r"\s+", " ", " ".join(purpose_parts)).strip()
        direction = "in" if credit and credit > 0 and (not debit or debit == 0) else "out"
        if credit and credit > 0 and debit and debit > 0:
            # unusual both — treat larger as direction? keep out if debit>=credit
            direction = "out" if debit >= credit else "in"
        amount = credit if direction == "in" else debit
        bank_payment_id = sha16("VTB", account_id, d.isoformat(), doc_no, debit, credit, purpose[:40])
        payments.append(
            {
                "bank_payment_id": bank_payment_id,
                "bank_account_id": account_id,
                "legal_entity_id": legal_entity_id,
                "payment_date": d.isoformat(),
                "period_month": d.strftime("%Y-%m"),
                "doc_no": doc_no,
                "direction": direction,
                "amount": amount,
                "debit": debit if debit else "",
                "credit": credit if credit else "",
                "currency": "RUB",
                "counterparty_raw": name[:200],
                "counterparty_inn": inn,
                "counterparty_id": "",
                "purpose": purpose[:500],
                "doc_type": f"VTB_VO_{vo}",
                "source_file_id": source_file_id,
                "source_row_id": f"pdf:{d_s}:{doc_no}",
                "match_status": "UNMATCHED",
                "cash_line_id": "",
                "source_bank": "VTB",
            }
        )
        i = j if found_at is not None else i + 1
    return payments


def reload_recon(payments, cash_path):
    cash = list(csv.DictReader(open(cash_path, encoding="utf-8")))
    bank_out = defaultdict(float)
    bank_in = defaultdict(float)
    by_src = Counter()
    for p in payments:
        by_src[p.get("source_bank") or p.get("source_file_id", "?")] += 1
        m = p["period_month"]
        if p["direction"] == "out":
            bank_out[m] += float(p["amount"] or 0)
        else:
            bank_in[m] += float(p["amount"] or 0)
    dds_bn = defaultdict(float)
    for c in cash:
        if c["ledger"] != "B":
            continue
        if "б/нал" not in (c.get("cash_type") or "").lower():
            continue
        m = c["period_month"]
        dds_bn[m] += float(c["amount_rub"] or 0)
    rows = []
    for m in sorted(set(bank_out) | set(bank_in) | set(dds_bn)):
        bo, bi, db = bank_out[m], bank_in[m], dds_bn[m]
        status = "N/A"
        delta = ""
        if bo and db:
            delta = round(bo - db, 2)
            tol = max(1000.0, 0.02 * max(bo, db))
            if abs(bo - db) <= tol:
                status = "CLOSE"
            elif abs(bo - db) / max(bo, db) <= 0.10:
                status = "SOFT_GAP"
            else:
                status = "GAP"
        elif bo and not db:
            status = "BANK_ONLY"
        elif db and not bo:
            status = "DDS_ONLY"
        rows.append(
            {
                "period_month": m,
                "bank_out_rub": round(bo, 2),
                "bank_in_rub": round(bi, 2),
                "dds_b_bn_rub": round(db, 2),
                "delta_bank_out_vs_dds_bn": delta,
                "status": status,
            }
        )
    return rows, by_src


def main():
    catalog = {r["file_name"]: r for r in csv.DictReader(open(ROOT / "live/registers/00_SOURCE_CATALOG_93.csv", encoding="utf-8-sig"))}
    vtb_all = []
    stats = {}
    for fname, acc, fallback, legal in VTB_FILES:
        path = DOCS / fname
        fid = catalog.get(fname, {}).get("master_file_id") or fallback
        print("parsing", fname, "...")
        pays = parse_vtb(path, acc, fid, legal)
        stats[acc] = len(pays)
        print("  ->", len(pays), "payments")
        vtb_all.extend(pays)

    # merge with existing Alfa payments
    alfa_path = OUT / "bank_payments.csv"
    alfa = list(csv.DictReader(open(alfa_path, encoding="utf-8")))
    for a in alfa:
        a["source_bank"] = a.get("source_bank") or "ALFA"
    # drop previous VTB if re-run
    alfa_only = [a for a in alfa if a.get("source_bank") != "VTB" and not str(a.get("source_file_id", "")).startswith("FILE-008") and a.get("source_file_id") not in ("FILE-008", "FILE-009", "FILE-010")]
    # cleaner: keep only Alfa account
    alfa_only = [a for a in alfa if a.get("bank_account_id") == "40802810202620002686"]
    for a in alfa_only:
        a["source_bank"] = "ALFA"

    merged = alfa_only + vtb_all
    # dedupe by bank_payment_id
    seen = set()
    uniq = []
    for p in merged:
        if p["bank_payment_id"] in seen:
            continue
        seen.add(p["bank_payment_id"])
        uniq.append(p)

    fields = [
        "bank_payment_id", "bank_account_id", "legal_entity_id", "payment_date", "period_month",
        "doc_no", "direction", "amount", "debit", "credit", "currency", "counterparty_raw",
        "counterparty_inn", "counterparty_id", "purpose", "doc_type", "source_file_id",
        "source_row_id", "match_status", "cash_line_id", "source_bank",
    ]
    with open(OUT / "bank_payments.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(uniq)

    # update accounts status
    acc_rows = list(csv.DictReader(open(OUT / "bank_accounts.csv", encoding="utf-8")))
    for a in acc_rows:
        if a["bank_account_id"] in stats:
            a["status"] = "ACTIVE_PARSED_VTB_PDF"
            a["notes"] = f"VTB PDF parsed: {stats[a['bank_account_id']]} payments"
    with open(OUT / "bank_accounts.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["bank_account_id", "legal_entity_id", "bank_name", "currency", "status", "notes"])
        w.writeheader()
        w.writerows(acc_rows)

    recon, by_src = reload_recon(uniq, OUT / "cash_lines.csv")
    with open(OUT / "recon_bank_vs_dds_month.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(recon[0].keys()))
        w.writeheader()
        w.writerows(recon)

    status_c = Counter(r["status"] for r in recon)
    summary = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "wave": "W1b",
        "vtb_payments_by_account": stats,
        "vtb_payments_total": len(vtb_all),
        "alfa_payments": len(alfa_only),
        "bank_payments_merged": len(uniq),
        "recon_status_counts": dict(status_c),
        "close_or_soft_months": [r["period_month"] for r in recon if r["status"] in ("CLOSE", "SOFT_GAP")],
        "finding": (
            f"VTB PDF + Alfa: {len(uniq)} payments. "
            f"Recon statuses {dict(status_c)}. "
            "Full DDS Б/Нал vs all bank accounts still may GAP (нал/корп.карта/прочие банки)."
        ),
    }
    json.dump(summary, open(OUT / "w1b_summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    EV.mkdir(parents=True, exist_ok=True)
    json.dump(summary, open(EV / "w1b_summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    # merge into w1_summary
    w1 = json.load(open(OUT / "w1_summary.json"))
    w1.update(
        {
            "w1b": summary,
            "bank_payments_parsed": len(uniq),
            "recon_status_counts": dict(status_c),
            "soft_months": summary["close_or_soft_months"],
        }
    )
    json.dump(w1, open(OUT / "w1_summary.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("--- sample recon 2025-08 / 2026-04 ---")
    for r in recon:
        if r["period_month"] in ("2025-08", "2026-04", "2024-06", "2025-02"):
            print(r)


if __name__ == "__main__":
    main()
