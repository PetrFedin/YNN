#!/usr/bin/env python3
"""H85: tax filing completeness matrix (catalog ↔ obligations ↔ H76 soft).

tax_list PDF — сканы без текста (OCR blocked). Комплектность строим по
именам файлов catalog 107 + tax_pdf_obligation_anchors + soft perimeter.
Не SoT. Не auto-Accept. Dual contour IP / Decor.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
DL = Path("/Users/petr/Downloads/YANINA документы")
AS_OF = "2026-07-29"

# Ожидаемые слоты Stage1 (indicative calendar; не юрзаключение).
# status later: HAVE / MISSING / NOT_DUE / N_A / DUPLICATE_RISK
EXPECTED = [
    # IP Yanina
    {"le": "LE-IP-YANINA", "tax_type": "USN", "period": "2024", "due": "Y", "why": "годовая УСН"},
    {"le": "LE-IP-YANINA", "tax_type": "USN", "period": "2025", "due": "Y", "why": "годовая УСН"},
    {"le": "LE-IP-YANINA", "tax_type": "USN", "period": "2026", "due": "N", "why": "NOT_DUE до конца 2026"},
    {"le": "LE-IP-YANINA", "tax_type": "6NDFL", "period": "2024", "due": "Y", "why": "годовой 6-НДФЛ"},
    {"le": "LE-IP-YANINA", "tax_type": "6NDFL", "period": "2025", "due": "Y", "why": "годовой 6-НДФЛ"},
    {"le": "LE-IP-YANINA", "tax_type": "6NDFL", "period": "2026", "due": "N", "why": "NOT_DUE (год не закрыт)"},
    {"le": "LE-IP-YANINA", "tax_type": "RSV", "period": "2024", "due": "Y", "why": "годовой РСВ"},
    {"le": "LE-IP-YANINA", "tax_type": "RSV", "period": "2025", "due": "Y", "why": "годовой РСВ"},
    {"le": "LE-IP-YANINA", "tax_type": "RSV", "period": "2026-Q1", "due": "Y", "why": "квартальный РСВ"},
    {"le": "LE-IP-YANINA", "tax_type": "RSV", "period": "2026-Q2", "due": "Y", "why": "срок ~25.07.2026 — as_of 29.07"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2025-Q1", "due": "Y", "why": "НДС квартал"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2025-Q2", "due": "Y", "why": "НДС квартал"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2025-Q3", "due": "Y", "why": "НДС квартал"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2025-Q4", "due": "Y", "why": "НДС квартал"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2026-Q1", "due": "Y", "why": "НДС квартал"},
    {"le": "LE-IP-YANINA", "tax_type": "NDS", "period": "2026-Q2", "due": "Y", "why": "срок ~25.07.2026 — as_of 29.07"},
    # Decor
    {"le": "LE-OOO-DEKOR", "tax_type": "USN", "period": "2024", "due": "Y", "why": "годовая УСН Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "USN", "period": "2025", "due": "Y", "why": "годовая УСН Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "USN", "period": "2026", "due": "N", "why": "NOT_DUE"},
    {"le": "LE-OOO-DEKOR", "tax_type": "6NDFL", "period": "2024", "due": "Y", "why": "6-НДФЛ Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "6NDFL", "period": "2025", "due": "Y", "why": "6-НДФЛ Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "RSV", "period": "2024", "due": "Y", "why": "РСВ Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "RSV", "period": "2025", "due": "Y", "why": "РСВ Decor"},
    {"le": "LE-OOO-DEKOR", "tax_type": "NDS", "period": "ANY", "due": "N", "why": "N_A — в пакете нет НДС Decor (УСН contour)"},
    # Meta docs
    {"le": "BOTH", "tax_type": "REPORT_LIST", "period": "2024", "due": "Y", "why": "список ФНС (scan)"},
    {"le": "BOTH", "tax_type": "REPORT_LIST", "period": "2025", "due": "Y", "why": "список ФНС (scan)"},
    {"le": "BOTH", "tax_type": "REPORT_LIST", "period": "2026", "due": "Y", "why": "список ФНС (scan)"},
    {"le": "BOTH", "tax_type": "ENS", "period": "CURRENT", "due": "Y", "why": "сальдо/справка ЕНС (scan)"},
]


def wcsv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def parse_le(name: str) -> str:
    n = name.lower()
    if "декор" in n or "decor" in n:
        return "LE-OOO-DEKOR"
    if "янина" in n or "ип" in n:
        return "LE-IP-YANINA"
    return "UNKNOWN"


def parse_type(name: str, category: str) -> str:
    n = name.lower()
    if "6-ндфл" in n or "6ндфл" in n or category == "tax_6ndfl":
        return "6NDFL"
    if "ндс" in n or category == "tax_nds":
        return "NDS"
    if "усн" in n or category == "tax_usn":
        return "USN"
    if "страховым" in n or "рсв" in n or "несч" in n or category == "tax_insurance":
        return "RSV"
    if "список" in n or category == "tax_list":
        return "REPORT_LIST"
    if "енс" in n or "исполнении обязан" in n or category == "tax_ens":
        return "ENS"
    return "OTHER"


def parse_period(name: str, tax_type: str) -> str:
    n = name.lower()
    # quarter
    mq = re.search(r"(\d)\s*квартал\s*(\d{4})", n)
    if mq:
        return f"{mq.group(2)}-Q{mq.group(1)}"
    # year
    my = re.search(r"за\s+(\d{4})", n)
    if my:
        y = my.group(1)
        if tax_type in ("REPORT_LIST",):
            return y
        return y
    my2 = re.search(r"(20\d{2})", n)
    if tax_type == "REPORT_LIST" and my2:
        return my2.group(1)
    if tax_type == "ENS":
        return "CURRENT"
    if "25.06.2026" in n or "на 25.06.2026" in n:
        return "2026"
    return ""


def main() -> None:
    REG.mkdir(parents=True, exist_ok=True)
    MARTS.mkdir(parents=True, exist_ok=True)

    catalog = [
        r
        for r in csv.DictReader(open(ROOT / "live/registers/00_SOURCE_CATALOG_107.csv"))
        if r["category"].startswith("tax")
    ]
    anchors = list(csv.DictReader(open(MARTS / "tax_pdf_obligation_anchors.csv")))
    extracts = list(csv.DictReader(open(MARTS / "tax_pdf_extract_confident.csv")))
    soft = list(csv.DictReader(open(MARTS / "tax_soft_gate_sign_card.csv")))

    # inventory from catalog
    inv = []
    for r in catalog:
        name = r["file_name"]
        p = Path(r["path"])
        if not p.exists():
            p = DL / name
        ttype = parse_type(name, r["category"])
        le = parse_le(name)
        if ttype in ("REPORT_LIST", "ENS") and le == "UNKNOWN":
            le = "BOTH"
        period = parse_period(name, ttype)
        # text extractability probe for list/ens
        text_ok = "N/A"
        if ttype in ("REPORT_LIST", "ENS") and p.exists():
            try:
                from pypdf import PdfReader

                reader = PdfReader(str(p))
                text = "\n".join((pg.extract_text() or "") for pg in reader.pages)
                text_ok = "OCR_NEEDED" if len(text.strip()) < 20 else "TEXT_OK"
            except Exception:
                text_ok = "OCR_NEEDED"
        inv.append(
            {
                "source_file_id": r.get("source_file_id", ""),
                "category": r["category"],
                "file_name": name,
                "legal_entity_id": le,
                "tax_type": ttype,
                "period": period,
                "bytes": p.stat().st_size if p.exists() else 0,
                "exists": "YES" if p.exists() else "NO",
                "text_extract": text_ok,
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    # index have
    def key(le, ttype, period):
        return (le, ttype, period)

    have_map: dict[tuple, list[dict]] = defaultdict(list)
    for row in inv:
        have_map[key(row["legal_entity_id"], row["tax_type"], row["period"])].append(row)
        if row["legal_entity_id"] in ("LE-IP-YANINA", "LE-OOO-DEKOR"):
            have_map[key("BOTH", row["tax_type"], row["period"])].append(row)

    # anchor amounts
    anchor_amt = {}
    for a in anchors:
        anchor_amt[(a["legal_entity_id"] or "BOTH", a["tax_type"], a["period"] or "CURRENT")] = a.get(
            "amount_rub", ""
        )

    matrix = []
    for slot in EXPECTED:
        le, ttype, period = slot["le"], slot["tax_type"], slot["period"]
        if period == "ANY":
            hits = [r for r in inv if r["legal_entity_id"] == le and r["tax_type"] == ttype]
            status = "N_A_NO_FILES" if not hits else "UNEXPECTED_HAVE"
            files = " | ".join(h["file_name"][:40] for h in hits) if hits else ""
            matrix.append(
                {
                    "legal_entity_id": le,
                    "tax_type": ttype,
                    "period": period,
                    "expected_due": slot["due"],
                    "status": status if slot["due"] == "N" else ("MISSING" if not hits else "HAVE"),
                    "files_n": len(hits),
                    "files": files,
                    "amount_rub_anchor": "",
                    "text_extract": "",
                    "why": slot["why"],
                    "owner_action": "keep Decor without NDS unless Accept says otherwise",
                    "blocks_gate": "N",
                    "do_not_auto_accept": "YES",
                    "so_t": "N",
                }
            )
            continue

        hits = have_map.get(key(le, ttype, period), [])
        # ALSO match UNKNOWN le for ENS/list
        if not hits and le == "BOTH":
            hits = [r for r in inv if r["tax_type"] == ttype and r["period"] in (period, "CURRENT", "")]

        if slot["due"] == "N":
            status = "NOT_DUE" if not hits else "HAVE_EARLY"
        elif not hits:
            status = "MISSING"
        elif len(hits) > 1 and ttype not in ("ENS",):
            status = "HAVE_DUP"
        else:
            status = "HAVE"

        text_ex = ""
        if hits:
            text_ex = hits[0].get("text_extract", "")
            if text_ex == "OCR_NEEDED":
                status = "HAVE_SCAN_NO_TEXT" if status.startswith("HAVE") else status

        amt = anchor_amt.get((le, ttype, period), "")
        if not amt and le == "BOTH":
            amt = anchor_amt.get(("", ttype, period), "") or anchor_amt.get(("BOTH", ttype, period), "")

        owner_action = ""
        blocks = "N"
        if status == "MISSING" and ttype in ("NDS", "RSV") and period.startswith("2026-Q2"):
            owner_action = "Запросить у Сливяк файл декларации/расчёта 2026-Q2"
            blocks = "SOFT"  # completeness, not hard gate score alone
        elif status == "HAVE_SCAN_NO_TEXT":
            owner_action = "OCR/перевыгрузка текстового PDF для сверки списка ФНС"
            blocks = "N"
        elif status == "HAVE_DUP":
            owner_action = "Оставить один master; второй в quarantine duplicate"
            blocks = "N"
        elif status == "HAVE":
            owner_action = "OK — в пакете"
        elif status == "NOT_DUE":
            owner_action = "не требовать сейчас"
        else:
            owner_action = "review"

        matrix.append(
            {
                "legal_entity_id": le,
                "tax_type": ttype,
                "period": period,
                "expected_due": slot["due"],
                "status": status,
                "files_n": len(hits),
                "files": " | ".join(h["file_name"] for h in hits),
                "amount_rub_anchor": amt,
                "text_extract": text_ex,
                "why": slot["why"],
                "owner_action": owner_action,
                "blocks_gate": blocks,
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    # gaps only
    gaps = [r for r in matrix if r["status"] in ("MISSING", "HAVE_SCAN_NO_TEXT", "HAVE_DUP")]

    # LE rollup
    le_rows = []
    for le in ("LE-IP-YANINA", "LE-OOO-DEKOR", "BOTH"):
        sub = [r for r in matrix if r["legal_entity_id"] == le]
        le_rows.append(
            {
                "legal_entity_id": le,
                "slots_n": len(sub),
                "have_n": sum(1 for r in sub if r["status"].startswith("HAVE")),
                "missing_n": sum(1 for r in sub if r["status"] == "MISSING"),
                "scan_n": sum(1 for r in sub if r["status"] == "HAVE_SCAN_NO_TEXT"),
                "not_due_n": sum(1 for r in sub if r["status"] == "NOT_DUE"),
                "contour_note": {
                    "LE-IP-YANINA": "Salon/IP money + NDS contour",
                    "LE-OOO-DEKOR": "Decor separate — не смешивать с IP P&L",
                    "BOTH": "lists/ENS meta",
                }[le],
            }
        )

    # soft perimeter bridge
    soft_bridge = []
    for s in soft:
        soft_bridge.append(
            {
                "check_id": s["check_id"],
                "period_month": s["period_month"],
                "status_now": s["status_now"],
                "delta_rub": s["delta_rub"],
                "hypothesis": s["hypothesis"],
                "sim_status": s["sim_status"],
                "signature": s.get("signature", ""),
                "completeness_link": "H85 matrix ≠ cash recon; soft sign still required for TAX→27",
                "owner": "Сливяк",
                "approver": "Янина",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    actions = [
        {
            "priority": "P0",
            "action_id": "H85-A1",
            "what": "Подписать TAX perimeter (H76) — 2024-01/10, 2025-08, trademark 2026-06",
            "who": "Сливяк + Янина",
            "evidence": "14_TAX_SOFT + tax_completeness_soft_bridge.csv",
            "unlocks": "gate 26→27",
            "gate_delta": "YES",
        },
        {
            "priority": "P1",
            "action_id": "H85-A2",
            "what": "Догрузить MISSING 2026-Q2: НДС + РСВ (IP) — срок уже прошёл as_of 29.07",
            "who": "Сливяк",
            "evidence": "tax_completeness_gaps.csv",
            "unlocks": "полнота пакета 2026; не путать с monthly tax_cash",
            "gate_delta": "SOFT",
        },
        {
            "priority": "P1",
            "action_id": "H85-A3",
            "what": "OCR/текст: Списки отчётности 2024–2026 + ЕНС справки",
            "who": "Сливяк",
            "evidence": "HAVE_SCAN_NO_TEXT in matrix",
            "unlocks": "сверка ФНС list ↔ наш pack без догадок",
            "gate_delta": "N",
        },
        {
            "priority": "P2",
            "action_id": "H85-A4",
            "what": "Разрешить дубликаты (1) в именах 6-НДФЛ/УСН 2025",
            "who": "Сливяк / Data",
            "evidence": "HAVE_DUP rows",
            "unlocks": "один master на obligation",
            "gate_delta": "N",
        },
        {
            "priority": "P2",
            "action_id": "H85-A5",
            "what": "Держать Decor contour отдельно (нет НДС в пакете = OK unless Accept)",
            "who": "Янина",
            "evidence": "LE-OOO-DEKOR NDS ANY = N_A",
            "unlocks": "dual contour discipline",
            "gate_delta": "N",
        },
    ]

    status_counts = Counter(r["status"] for r in matrix)
    summary = [
        {"metric": "tax_catalog_files", "value": len(inv), "note": "category tax_*"},
        {"metric": "matrix_slots", "value": len(matrix), "note": "expected calendar"},
        {"metric": "have", "value": status_counts.get("HAVE", 0) + status_counts.get("HAVE_EARLY", 0), "note": ""},
        {"metric": "have_dup", "value": status_counts.get("HAVE_DUP", 0), "note": ""},
        {"metric": "have_scan_no_text", "value": status_counts.get("HAVE_SCAN_NO_TEXT", 0), "note": "lists/ENS"},
        {"metric": "missing", "value": status_counts.get("MISSING", 0), "note": "incl 2026-Q2"},
        {"metric": "not_due", "value": status_counts.get("NOT_DUE", 0), "note": ""},
        {"metric": "soft_sign_open", "value": sum(1 for s in soft if not (s.get("signature") or "").strip()), "note": "H76"},
        {"metric": "as_of", "value": AS_OF, "note": ""},
    ]

    wcsv(MARTS / "tax_filing_inventory.csv", inv)
    wcsv(MARTS / "tax_completeness_matrix.csv", matrix)
    wcsv(MARTS / "tax_completeness_gaps.csv", gaps)
    wcsv(MARTS / "tax_completeness_le_rollup.csv", le_rows)
    wcsv(MARTS / "tax_completeness_soft_bridge.csv", soft_bridge)
    wcsv(MARTS / "tax_completeness_owner_actions.csv", actions)
    wcsv(MARTS / "tax_completeness_summary.csv", summary)

    for name in [
        "tax_filing_inventory.csv",
        "tax_completeness_matrix.csv",
        "tax_completeness_gaps.csv",
        "tax_completeness_le_rollup.csv",
        "tax_completeness_soft_bridge.csv",
        "tax_completeness_owner_actions.csv",
        "tax_completeness_summary.csv",
    ]:
        (REG / name).write_text((MARTS / name).read_text(encoding="utf-8"), encoding="utf-8")

    meta = {
        "hypothesis": "H85",
        "title": "tax_filing_completeness",
        "do_not_auto_accept": True,
        "not_sot": True,
        "gate": "18/30",
        "as_of": AS_OF,
        "status_counts": dict(status_counts),
        "summary": {r["metric"]: r["value"] for r in summary},
        "note": "tax_list/ENS are image PDFs — completeness by filename+anchors; OCR separate",
        "dual_contour": True,
    }
    (MARTS / "h85_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (REG / "h85_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(meta["summary"], ensure_ascii=False, indent=2))
    print("status", status_counts)
    print("GAPS:")
    for g in gaps:
        print(f"  {g['status']:18} {g['legal_entity_id']:16} {g['tax_type']:12} {g['period']:8} | {g['owner_action'][:60]}")


if __name__ == "__main__":
    main()
