#!/usr/bin/env python3
"""Layer 4: OTHER_IN reclass candidates + crude IM impact (so_t=N).

Не меняет bank_in_classified / gate. Только пишет candidate marts.
Запуск из корня репо: python3 live/maps/build_layer4_reclass_impact.py
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MART = ROOT / "live" / "marts"
MAPS = ROOT / "live" / "maps"
IM_OPEN = {"2024-08", "2025-01", "2025-08", "2025-10", "2026-03", "2026-04"}


def fnum(x) -> float:
    try:
        return float(str(x).replace(" ", "").replace(",", "."))
    except Exception:
        return 0.0


def propose(row: dict) -> tuple[str, str, str] | tuple[None, None, None]:
    if row.get("in_class") != "OTHER_IN":
        return None, None, None
    p = (row.get("purpose") or "").upper()
    if (
        ("ВОЗМЕЩЕНИЕ" in p and ("ПОС" in p or "ФРКК" in p or "ДОГОВОРУ" in p))
        or "ПОС-ФРКК" in p
        or (
            "ВОЗМЕЩЕНИЕ" in p
            and ("КОМ-СИЯ ПО ОПЕРАЦИЯМ" in p or "КОМИССИЯ ПО ОПЕРАЦИЯМ" in p)
        )
    ):
        return "ACQ_IM_CANDIDATE", "HIGH", "POS_REIMBURSEMENT_PURPOSE"
    if "ЭКВАЙР" in p:
        return "ACQ_IM_CANDIDATE", "HIGH", "EXPLICIT_ACQ_WORD"
    if "ОПЛАТА ПО СЧЕТ" in p or "ОПЛАТА ПО СЧЁТ" in p:
        return "CLIENT_INVOICE_CANDIDATE", "MED", "INVOICE_PAYMENT"
    if "ЗАКАЗ" in p and "ДОГОВОР" in p:
        return "CLIENT_ORDER_CANDIDATE", "MED", "ORDER_CONTRACT"
    if "ВОЗВРАТ" in p:
        return "REFUND_CANDIDATE", "MED", "REFUND"
    return "OTHER_IN_KEEP", "LOW", "NO_RULE"


def main() -> None:
    bank = list(csv.DictReader((MART / "bank_in_classified.csv").open(encoding="utf-8")))
    im = list(csv.DictReader((MART / "recon_im_combo.csv").open(encoding="utf-8")))

    cands = []
    for r in bank:
        prop, conf, rule = propose(r)
        if prop is None:
            continue
        cands.append(
            {
                **r,
                "proposed_class": prop,
                "confidence": conf,
                "rule_id": rule,
                "so_t": "N",
                "status": "CANDIDATE",
            }
        )

    fields = [
        "bank_payment_id",
        "period_month",
        "payment_date",
        "amount",
        "counterparty_raw",
        "purpose",
        "source_bank",
        "legal_entity_id",
        "in_class",
        "proposed_class",
        "confidence",
        "rule_id",
        "so_t",
        "status",
    ]
    for dest in (MART, MAPS):
        with (dest / "bank_in_reclass_candidates.csv").open(
            "w", encoding="utf-8", newline=""
        ) as fh:
            w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            w.writerows(cands)

    by_prop: Counter[str] = Counter()
    amt_prop: dict[str, float] = defaultdict(float)
    acq_by_m: dict[str, float] = defaultdict(float)
    for r in cands:
        by_prop[r["proposed_class"]] += 1
        amt_prop[r["proposed_class"]] += fnum(r["amount"])
        if r["proposed_class"] == "ACQ_IM_CANDIDATE":
            acq_by_m[r["period_month"]] += fnum(r["amount"])

    acq_now: dict[str, float] = defaultdict(float)
    for r in bank:
        if r.get("in_class") == "ACQ_IM":
            acq_now[r["period_month"]] += fnum(r["amount"])

    impact = []
    for r in im:
        pm = r["period_month"]
        sales = fnum(r.get("sales_revenue_rub"))
        bank_best = fnum(r.get("bank_in_best_rub") or r.get("best_bank_in_rub") or 0)
        add = acq_by_m.get(pm, 0.0)
        hyp = bank_best + add
        gap_pct = ((hyp - sales) / sales * 100) if sales else None
        if sales > 0 and gap_pct is not None:
            ap = abs(gap_pct)
            hyp_st = "CLOSE" if ap <= 10 else ("SOFT" if ap <= 30 else "OPEN")
        else:
            hyp_st = "NA"
        impact.append(
            {
                "period_month": pm,
                "status_as_is": r.get("status"),
                "sales_revenue_rub": round(sales, 2),
                "bank_acq_im_as_is": round(acq_now.get(pm, 0), 2),
                "bank_in_best_as_is": round(bank_best, 2),
                "acq_candidate_add_rub": round(add, 2),
                "bank_hyp_best_plus_cand": round(hyp, 2),
                "gap_hyp_pct": round(gap_pct, 1) if gap_pct is not None else "",
                "status_hyp_crude": hyp_st,
                "is_gate_open_month": "Y" if pm in IM_OPEN else "N",
                "note": "hyp crude ±10/30; NOT gate policy; candidates not applied",
            }
        )

    for dest in (MART, MAPS):
        with (dest / "im_acq_reclass_impact.csv").open(
            "w", encoding="utf-8", newline=""
        ) as fh:
            w = csv.DictWriter(fh, fieldnames=list(impact[0].keys()))
            w.writeheader()
            w.writerows(impact)

    open_impact = [x for x in impact if x["is_gate_open_month"] == "Y"]
    changed = sum(
        1
        for x in open_impact
        if x["status_as_is"] == "OPEN" and x["status_hyp_crude"] != "OPEN"
    )
    summary = {
        "candidates_n": len(cands),
        "by_proposed_class_n": dict(by_prop),
        "by_proposed_class_rub": {k: round(v, 2) for k, v in amt_prop.items()},
        "acq_im_candidate_rub": round(amt_prop.get("ACQ_IM_CANDIDATE", 0), 2),
        "acq_im_candidate_n": by_prop.get("ACQ_IM_CANDIDATE", 0),
        "im_open_months": sorted(IM_OPEN),
        "im_open_months_with_candidate_add": {
            m: round(acq_by_m.get(m, 0), 2) for m in sorted(IM_OPEN)
        },
        "im_open_hyp_improved_crude_n": changed,
        "im_open_detail": open_impact,
        "rule_gap_vs_h10": "h10 misses ВОЗМЕЩЕНИЕ СР-В ПО ДОГОВОРУ … ПОС-ФРКК",
        "proposed_h10_rule_patch": (
            "if 'ВОЗМЕЩЕНИЕ' in pur and ('ПОС' in pur or 'ФРКК' in pur): "
            "return 'ACQ_IM'  # prefer new class ACQ_POS after ACCEPT"
        ),
        "so_t": "N",
        "status": "CANDIDATE_IMPACT_ONLY",
    }
    (MAPS / "depth_layer4_reclass_impact.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        f"candidates={len(cands)} acq_cand_rub={summary['acq_im_candidate_rub']} "
        f"open_improved_crude={changed}/6"
    )


if __name__ == "__main__":
    main()
