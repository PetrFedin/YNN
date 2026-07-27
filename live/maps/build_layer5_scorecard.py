#!/usr/bin/env python3
"""Layer 5: system scorecard + POS by LE/month + MD invoice surname links (so_t=N)."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MART = ROOT / "live" / "marts"
MAPS = ROOT / "live" / "maps"


def fnum(x) -> float:
    try:
        return float(str(x).replace(" ", "").replace(",", "."))
    except Exception:
        return 0.0


def tokens(s: str) -> list[str]:
    s = (s or "").upper()
    s = re.sub(r"[^0-9A-ZА-ЯЁ]+", " ", s)
    stop = {
        "ООО",
        "ИП",
        "АО",
        "ПАО",
        "ЗАО",
        "Г",
        "Д",
        "УЛ",
        "ГР",
        "РОССИЯ",
        "МОСКВА",
        "САНКТ",
        "ПЕТЕРБУРГ",
        "ОБЛ",
        "КВ",
        "ДОМ",
        "КОРП",
        "НАБ",
        "ПЕР",
        "РЕКИ",
        "СБЕРБАНК",
        "БАНК",
    }
    return [t for t in s.split() if len(t) >= 3 and t not in stop and not t.isdigit()]


def surname_key(s: str) -> str:
    t = tokens(s)
    return t[0] if t else ""


def main() -> None:
    cands = list(
        csv.DictReader((MAPS / "bank_in_reclass_candidates.csv").open(encoding="utf-8"))
    )
    md = list(csv.DictReader((MART / "md_payments.csv").open(encoding="utf-8")))

    md_by_sur: dict[str, dict] = defaultdict(
        lambda: {"eur": 0.0, "names": Counter(), "n": 0}
    )
    for r in md:
        if (r.get("period_month") or "") < "2024-01":
            continue
        sur = surname_key(r.get("client") or "")
        if len(sur) < 4:
            continue
        md_by_sur[sur]["eur"] += fnum(r.get("amount_eur"))
        md_by_sur[sur]["names"][r.get("client") or ""] += 1
        md_by_sur[sur]["n"] += 1

    inv = [r for r in cands if r["proposed_class"] == "CLIENT_INVOICE_CANDIDATE"]
    inv_by_sur: dict[str, dict] = defaultdict(
        lambda: {"rub": 0.0, "n": 0, "samples": []}
    )
    for r in inv:
        sur = surname_key(r.get("counterparty_raw") or "")
        if len(sur) < 4:
            continue
        inv_by_sur[sur]["rub"] += fnum(r["amount"])
        inv_by_sur[sur]["n"] += 1
        if len(inv_by_sur[sur]["samples"]) < 2:
            inv_by_sur[sur]["samples"].append((r.get("counterparty_raw") or "")[:60])

    links = []
    for sur, b in inv_by_sur.items():
        if sur not in md_by_sur:
            continue
        m = md_by_sur[sur]
        if m["eur"] < 500:
            continue
        links.append(
            {
                "surname": sur,
                "bank_invoice_rub": round(b["rub"], 2),
                "bank_payments_n": b["n"],
                "md_payments_eur": round(m["eur"], 2),
                "md_payments_rub_fx100": round(m["eur"] * 100, 2),
                "md_payments_n": m["n"],
                "md_client_top": m["names"].most_common(1)[0][0],
                "bank_sample": b["samples"][0] if b["samples"] else "",
                "link_type": "SURNAME_MD_INVOICE",
                "confidence": "MED",
                "so_t": "N",
                "note": "surname match only; not payment-level reconcile",
            }
        )
    links.sort(key=lambda x: -x["bank_invoice_rub"])

    pos = [r for r in cands if r["proposed_class"] == "ACQ_IM_CANDIDATE"]
    by_le_ym: dict[tuple[str, str], float] = defaultdict(float)
    for r in pos:
        by_le_ym[(r.get("legal_entity_id") or "?", r.get("period_month") or "?")] += (
            fnum(r["amount"])
        )
    pos_rows = [
        {
            "legal_entity_id": le,
            "period_month": ym,
            "pos_candidate_rub": round(a, 2),
            "proposed_class": "ACQ_POS_CANDIDATE",
            "so_t": "N",
        }
        for (le, ym), a in sorted(by_le_ym.items())
    ]

    scorecard = [
        {
            "area": "MD_CASH",
            "status": "STRONG",
            "evidence": "payments↔DDS 29/30",
            "blocker": "",
            "next": "keep",
        },
        {
            "area": "MD_UNIT_ECON",
            "status": "BLOCKED",
            "evidence": "cost fill 0% 2024-25",
            "blocker": "no order cost data",
            "next": "request cost format",
        },
        {
            "area": "GOODS_MARGIN",
            "status": "STRONG",
            "evidence": "dual TSUM; IM GM high",
            "blocker": "aliases/watchlist",
            "next": "Product review",
        },
        {
            "area": "B2B_OPEN",
            "status": "ACTION",
            "evidence": "2.51M / 15 docs",
            "blocker": "collect",
            "next": "S1 collect",
        },
        {
            "area": "IM_GATE",
            "status": "ACTION",
            "evidence": "6 OPEN months",
            "blocker": "acq registers + POS alloc",
            "next": "registers; not blind POS→IM",
        },
        {
            "area": "OTHER_IN_POS",
            "status": "MEASURED",
            "evidence": "62.3M POS on IP only; 1/6 OPEN blind",
            "blocker": "ACCEPT class ACQ_POS",
            "next": "new class+alloc",
        },
        {
            "area": "OTHER_IN_INVOICE",
            "status": "PARTIAL",
            "evidence": f"{len(links)} surname links / partial of 38.6M",
            "blocker": "payment-level match",
            "next": "reconcile top surnames to MD",
        },
        {
            "area": "PAYROLL_TOTAL",
            "status": "STRONG",
            "evidence": "multi CLOSE; +18.2M YoY",
            "blocker": "19 NO_LINES",
            "next": "payroll files",
        },
        {
            "area": "TSUM_CASH",
            "status": "EXPECTED_OPEN",
            "evidence": "23/30 OPEN channel-cash",
            "blocker": "agent model",
            "next": "net-rate/dual",
        },
        {
            "area": "FABRIC_WC",
            "status": "VISIBLE",
            "evidence": "~28.6M end trusted",
            "blocker": "no ABC",
            "next": "ABC",
        },
        {
            "area": "NARRATIVE_DEPTH",
            "status": "EXHAUSTED",
            "evidence": "layers 1-5",
            "blocker": "no new files/ACCEPT",
            "next": "execution only",
        },
    ]

    inv_total = sum(fnum(r["amount"]) for r in inv)
    link_rub = sum(x["bank_invoice_rub"] for x in links)
    summary = {
        "pos_total_rub": round(sum(fnum(r["amount"]) for r in pos), 2),
        "pos_by_le": {
            k: round(sum(fnum(r["amount"]) for r in pos if r.get("legal_entity_id") == k), 2)
            for k in sorted({r.get("legal_entity_id") for r in pos})
        },
        "invoice_total_rub": round(inv_total, 2),
        "surname_links_n": len(links),
        "surname_links_bank_rub": round(link_rub, 2),
        "surname_links_coverage_pct_of_invoice": round(100 * link_rub / inv_total, 1)
        if inv_total
        else 0,
        "top_links": links[:10],
        "scorecard": scorecard,
        "so_t": "N",
        "layer": 5,
    }

    for dest in (MAPS, MART):
        with (dest / "md_invoice_surname_links.csv").open(
            "w", encoding="utf-8", newline=""
        ) as fh:
            w = csv.DictWriter(fh, fieldnames=list(links[0].keys()) if links else ["surname"])
            w.writeheader()
            w.writerows(links)
        with (dest / "pos_candidate_by_le_month.csv").open(
            "w", encoding="utf-8", newline=""
        ) as fh:
            w = csv.DictWriter(
                fh,
                fieldnames=[
                    "legal_entity_id",
                    "period_month",
                    "pos_candidate_rub",
                    "proposed_class",
                    "so_t",
                ],
            )
            w.writeheader()
            w.writerows(pos_rows)
        with (dest / "system_scorecard.csv").open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(
                fh, fieldnames=["area", "status", "evidence", "blocker", "next"]
            )
            w.writeheader()
            w.writerows(scorecard)

    (MAPS / "depth_layer5_scorecard.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"links={len(links)} rub={summary['surname_links_bank_rub']} "
        f"cov={summary['surname_links_coverage_pct_of_invoice']}% "
        f"pos_ip={summary['pos_by_le']}"
    )


if __name__ == "__main__":
    main()
