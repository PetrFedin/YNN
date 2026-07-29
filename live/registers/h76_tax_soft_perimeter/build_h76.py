#!/usr/bin/env python3
"""H76 — Tax PDF / tax-cash ↔ bank SOFT months (Salon UFK perimeter).

Зачем:
  recon_tax_cash_bank: CLOSE 26 / SOFT_GAP 3 / GAP 1.
  Дельты 36 000 / 147 180 / 77 410 ровно = платежи Salon Sber → УФК,
  которых нет в bank_tax_like (фильтр IP/Декор). Это главный пробел G8→gate TAX.

Правила:
  - гипотеза perimeter, не auto-Accept / не SoT
  - 2026-06: пошлина товарного знака 76 500 засоряет tax-like
  - PDF obligations = годовые якоря, не равны месячной кассе
"""
from __future__ import annotations

import csv
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h76_tax_soft_perimeter_20260729"
WAVE_C = ROOT / "live/client_pack/execution_wave_c"
SIGN = ROOT / "live/client_pack/sign_session_pack"

W6 = ROOT / "live/registers/w6_tax_bud"
BANK = ROOT / "live/registers/w1_bank_cash/bank_payments.csv"
SBER_SALON = ROOT / "live/registers/h5_improve/sber_salon_tax_payments.csv"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def fnum(x) -> float:
    try:
        return float(x) if x not in (None, "") else 0.0
    except (TypeError, ValueError):
        return 0.0


def tag_purpose(purpose: str, counterparty: str = "") -> str:
    t = f"{purpose} {counterparty}".lower()
    tags = []
    if "ндс" in t and "не облаг" not in t.split("ндс")[0][-20:]:
        # crude: look for НДС as tax type in purpose
        pass
    if re.search(r"\bндс\b", t) and "1/3" in t:
        tags.append("NDS")
    elif "ндс" in t and "не облаг" not in t:
        tags.append("NDS")
    if "ндфл" in t:
        tags.append("NDFL")
    if "усн" in t:
        tags.append("USN")
    if "страх" in t or "рсв" in t or "осфр" in t or "нс и пз" in t or "нсипз" in t.replace(" ", ""):
        tags.append("INSURANCE")
    if "пошлин" in t or "товарн" in t and "знак" in t:
        tags.append("TRADEMARK_FEE")
    if "енп" in t or "единый налоговый" in t:
        tags.append("ENP")
    return "|".join(tags) if tags else "OTHER_TAXISH"


# Known soft resolutions from amount match (Salon UFK)
SALON_DELTA_HITS = {
    "2024-01": {
        "delta_rub": 36000.0,
        "bank_payment_id": "56f8574ddc801765",
        "hypothesis": "SALON_UFK_MISSING_FROM_BANK_TAX_LIKE",
        "gate_control": "TAX_CASH_BANK",
        "if_include": "GAP→CLOSE",
    },
    "2024-10": {
        "delta_rub": 147180.0,
        "bank_payment_id": "0b9757804c39de25",
        "hypothesis": "SALON_UFK_MISSING_FROM_BANK_TAX_LIKE",
        "gate_control": "TAX_CASH_BANK",
        "if_include": "SOFT_GAP→CLOSE",
    },
    "2025-08": {
        "delta_rub": 77410.0,
        "bank_payment_id": "67d44e4ba5bd8469",
        "hypothesis": "SALON_UFK_MISSING_FROM_BANK_TAX_LIKE",
        "gate_control": "TAX_CASH_BANK",
        "if_include": "SOFT_GAP→CLOSE",
    },
}


def main() -> dict:
    recon = list(csv.DictReader((W6 / "recon_tax_cash_bank.csv").open(encoding="utf-8")))
    tax_cash = list(csv.DictReader((W6 / "tax_cash_lines.csv").open(encoding="utf-8")))
    bank_like = list(csv.DictReader((W6 / "bank_tax_like.csv").open(encoding="utf-8")))
    obligations = list(csv.DictReader((W6 / "tax_obligations.csv").open(encoding="utf-8")))
    pdf_conf = list(csv.DictReader((W6 / "tax_pdf_extract_confident.csv").open(encoding="utf-8")))
    salon = {r["bank_payment_id"]: r for r in csv.DictReader(SBER_SALON.open(encoding="utf-8"))}
    bank_all = {r["bank_payment_id"]: r for r in csv.DictReader(BANK.open(encoding="utf-8"))}

    # --- soft month owner pack ---
    soft_months = []
    evidence_rows = []
    for r in recon:
        st = r["status"]
        if st == "CLOSE":
            continue
        m = r["period_month"]
        delta = fnum(r["delta"])
        hit = SALON_DELTA_HITS.get(m)
        cash_lines = [c for c in tax_cash if c["period_month"] == m]
        bank_lines = [b for b in bank_like if b["period_month"] == m]

        # exact amount match in cash for |delta|
        cash_match = [c for c in cash_lines if abs(fnum(c["amount_rub"]) - abs(delta)) < 0.01]
        bank_adj = sum(fnum(b["amount"]) for b in bank_lines)
        trademark = [b for b in bank_lines if "товарн" in (b.get("purpose") or "").lower()]
        trademark_sum = sum(fnum(b["amount"]) for b in trademark)

        hyp = hit["hypothesis"] if hit else ("TRADEMARK_IN_TAX_LIKE" if trademark and delta < 0 else "NEEDS_OWNER")
        pay_id = hit["bank_payment_id"] if hit else (trademark[0]["bank_payment_id"] if trademark else "")
        pay = salon.get(pay_id) or bank_all.get(pay_id) or {}

        # simulated status if Salon UFK included / trademark excluded
        sim_bank = bank_adj
        sim_note = []
        if hit:
            sim_bank += hit["delta_rub"]
            sim_note.append("include_salon_ufk")
        if trademark_sum and m == "2026-06":
            sim_bank -= trademark_sum
            sim_note.append("exclude_trademark_fee")
        sim_delta = fnum(r["tax_cash_rub"]) - sim_bank
        if abs(sim_delta) < 1:
            sim_status = "CLOSE"
        elif abs(sim_delta) < 200000:
            sim_status = "SOFT_GAP"
        else:
            sim_status = "GAP"

        soft_months.append(
            {
                "period_month": m,
                "status_now": st,
                "tax_cash_rub": r["tax_cash_rub"],
                "bank_tax_like_rub": r["bank_tax_like_rub"],
                "delta_rub": r["delta"],
                "hypothesis": hyp,
                "matched_cash_lines_n": len(cash_match),
                "matched_cash_amount": round(sum(fnum(c["amount_rub"]) for c in cash_match), 2),
                "salon_or_bank_payment_id": pay_id,
                "payment_date": pay.get("payment_date", ""),
                "payment_amount_rub": pay.get("amount", ""),
                "payment_legal_entity": pay.get("legal_entity_id", ""),
                "payment_counterparty": (pay.get("counterparty_raw") or "")[:80],
                "if_include_effect": hit["if_include"] if hit else "|".join(sim_note) or "",
                "sim_bank_tax_like_rub": round(sim_bank, 2),
                "sim_delta_rub": round(sim_delta, 2),
                "sim_status": sim_status,
                "trademark_fee_in_tax_like_rub": round(trademark_sum, 2),
                "owner_action": (
                    "Confirm include Salon→УФК into TAX_CASH_BANK perimeter (not auto-Accept)"
                    if hit
                    else "Confirm exclude trademark fee from tax-like; explain residual delta"
                ),
                "owner": "Сливяк",
                "approver": "Янина",
                "blocks_gate": "TAX→27" if m == "2024-01" else "tax_recon_quality",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

        # evidence detail lines
        for c in cash_lines:
            evidence_rows.append(
                {
                    "period_month": m,
                    "side": "TAX_CASH",
                    "line_id": c["tax_cash_id"],
                    "amount_rub": c["amount_rub"],
                    "legal_entity_id": c["legal_entity_id"],
                    "article_or_purpose": c["article_name"],
                    "matches_delta": "Y" if abs(fnum(c["amount_rub"]) - abs(delta)) < 0.01 else "N",
                    "source": "tax_cash_lines",
                    "so_t": "N",
                }
            )
        for b in bank_lines:
            evidence_rows.append(
                {
                    "period_month": m,
                    "side": "BANK_TAX_LIKE",
                    "line_id": b["bank_payment_id"],
                    "amount_rub": b["amount"],
                    "legal_entity_id": "",
                    "article_or_purpose": f"{b.get('counterparty_raw','')[:40]} | {b.get('purpose','')[:80]}",
                    "matches_delta": "N",
                    "source": "bank_tax_like",
                    "so_t": "N",
                }
            )
        if pay_id:
            evidence_rows.append(
                {
                    "period_month": m,
                    "side": "SALON_UFK_CANDIDATE",
                    "line_id": pay_id,
                    "amount_rub": pay.get("amount", ""),
                    "legal_entity_id": pay.get("legal_entity_id", "LE-OOO-SALON-YANINA"),
                    "article_or_purpose": (pay.get("purpose") or pay.get("counterparty_raw") or "")[:120],
                    "matches_delta": "Y",
                    "source": "sber_salon_tax_payments|bank_payments",
                    "so_t": "N",
                }
            )

    # --- bank tax-like tagged ---
    tagged = []
    for b in bank_like:
        tags = tag_purpose(b.get("purpose") or "", b.get("counterparty_raw") or "")
        tagged.append(
            {
                **{k: b[k] for k in b},
                "tax_tags": tags,
                "is_trademark_fee": "Y" if "TRADEMARK_FEE" in tags else "N",
                "so_t": "N",
            }
        )

    tag_month = defaultdict(lambda: defaultdict(float))
    for b in tagged:
        for t in b["tax_tags"].split("|"):
            tag_month[b["period_month"]][t] += fnum(b["amount"])
    tag_rollup = []
    for m in sorted(tag_month):
        for t, amt in sorted(tag_month[m].items(), key=lambda x: -x[1]):
            tag_rollup.append(
                {
                    "period_month": m,
                    "tax_tag": t,
                    "amount_rub": round(amt, 2),
                    "so_t": "N",
                }
            )

    # --- PDF obligations rollup (annual anchors, not monthly close) ---
    pdf_rows = []
    seen = set()
    for o in obligations:
        key = (o["tax_type"], o["legal_entity_id"], o["period"], o.get("amount") or "")
        if key in seen:
            continue
        seen.add(key)
        pdf_rows.append(
            {
                "obligation_id": o["obligation_id"],
                "tax_type": o["tax_type"],
                "legal_entity_id": o["legal_entity_id"],
                "period": o["period"],
                "amount_rub": o.get("amount") or "",
                "amount_status": o["amount_status"],
                "source_file_name": o.get("source_file_name") or "",
                "note": "Annual/period obligation — do not equate to monthly tax_cash",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    # confidence summary
    conf_c = Counter(r["confidence"] for r in pdf_conf if r.get("confidence"))
    amt_c = Counter(r["amount_status"] for r in pdf_conf)

    # --- gate TAX confirm card (extends 36k to full soft set) ---
    gate_card = []
    for sm in soft_months:
        gate_card.append(
            {
                "check_id": f"TAX-SOFT-{sm['period_month']}",
                "period_month": sm["period_month"],
                "status_now": sm["status_now"],
                "delta_rub": sm["delta_rub"],
                "hypothesis": sm["hypothesis"],
                "payment_id": sm["salon_or_bank_payment_id"],
                "sim_status": sm["sim_status"],
                "owner_sign_required": "Y",
                "forbidden": "FORCE_CLOSE without confirming Salon UFK perimeter / trademark filter",
                "gate_effect": "2024-01 confirm unlocks TAX→27; other months improve recon quality",
                "signature": "",
                "date_signed": "",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    meta = {
        "horizon": "H76",
        "date": str(date.today()),
        "title": "Tax cash SOFT/GAP ↔ Salon UFK perimeter + PDF anchors",
        "recon_close_n": sum(1 for r in recon if r["status"] == "CLOSE"),
        "recon_soft_n": sum(1 for r in recon if r["status"] == "SOFT_GAP"),
        "recon_gap_n": sum(1 for r in recon if r["status"] == "GAP"),
        "soft_months_pack_n": len(soft_months),
        "salon_ufk_explains_n": sum(
            1 for s in soft_months if s["hypothesis"] == "SALON_UFK_MISSING_FROM_BANK_TAX_LIKE"
        ),
        "sim_all_close_if_perimeter_n": sum(1 for s in soft_months if s["sim_status"] == "CLOSE"),
        "pdf_extract_confidence": dict(conf_c),
        "pdf_amount_status": dict(amt_c),
        "no_fake_accept": True,
        "so_t": False,
        "note": "3/4 non-CLOSE months explained by Salon→УФК outside bank_tax_like filter",
    }

    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)
    WAVE_C.mkdir(parents=True, exist_ok=True)
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "tax_soft_month_owner_pack.csv", soft_months)
    write_csv(REG / "tax_soft_month_evidence_lines.csv", evidence_rows)
    write_csv(REG / "bank_tax_like_tagged.csv", tagged)
    write_csv(REG / "bank_tax_tag_month_rollup.csv", tag_rollup)
    write_csv(REG / "tax_pdf_obligation_anchors.csv", pdf_rows)
    write_csv(REG / "tax_soft_gate_sign_card.csv", gate_card)

    copies = [
        "tax_soft_month_owner_pack.csv",
        "tax_soft_month_evidence_lines.csv",
        "bank_tax_like_tagged.csv",
        "bank_tax_tag_month_rollup.csv",
        "tax_pdf_obligation_anchors.csv",
        "tax_soft_gate_sign_card.csv",
        "meta.json",
    ]
    for name in copies:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h76_meta.json")
            shutil.copy2(src, MAPS / "h76_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    # Wave C (tax/gate path) — find next free numbers
    shutil.copy2(REG / "tax_soft_month_owner_pack.csv", WAVE_C / "30_tax_soft_month_owner_pack.csv")
    shutil.copy2(REG / "tax_soft_month_evidence_lines.csv", WAVE_C / "31_tax_soft_month_evidence_lines.csv")
    shutil.copy2(REG / "tax_soft_gate_sign_card.csv", WAVE_C / "32_tax_soft_gate_sign_card.csv")
    shutil.copy2(REG / "bank_tax_like_tagged.csv", WAVE_C / "33_bank_tax_like_tagged.csv")

    # Sign session: extend TAX evidence brief pointer file
    sign_out = SIGN / "14_TAX_SOFT_PERIMETER_H76.csv"
    write_csv(sign_out, gate_card)

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    for s in soft_months:
        print(
            s["period_month"],
            s["status_now"],
            "→",
            s["sim_status"],
            s["hypothesis"],
            s["delta_rub"],
            s["salon_or_bank_payment_id"],
        )
    return meta


if __name__ == "__main__":
    main()
