#!/usr/bin/env python3
"""H69: Overbank channel-share HYPOTHESIS prefill (not Accept) + ping refresh.

Fills empty maps_to_channel / im_share on E07 overbank WO with confirm-only hypotheses.
Forbidden: ADD_POS_TO_IM on overbank months. Not SoT.
"""
from __future__ import annotations

import csv
import json
import shutil
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if not (ROOT / "live/registers/00_SOURCE_CATALOG_107.csv").exists():
    ROOT = Path.cwd()
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h69_overbank_hypothesis_20260729"
WAVE_A = ROOT / "live/client_pack/execution_wave_a"
SIGN = ROOT / "live/client_pack/sign_session_pack"


def write_csv(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def hyp(r: dict) -> dict:
    sc, amt, cls = r["source_channel"], float(r["amount_rub"]), r["in_class_now"]
    if sc == "TBANK" and cls == "ACQ_IM":
        return {
            "maps_to_channel_hypothesis": "IM",
            "im_share_rub_hypothesis": round(amt, 2),
            "other_channel_share_rub_hypothesis": 0,
            "other_channel_name_hypothesis": "",
            "hypothesis_confidence": "HIGH",
            "hypothesis_rule": "TBANK C_139035 IP YANINA acquiring → IM 100% until register says otherwise",
        }
    if sc == "ACQ_IM_ALREADY":
        return {
            "maps_to_channel_hypothesis": "IM",
            "im_share_rub_hypothesis": round(amt, 2),
            "other_channel_share_rub_hypothesis": 0,
            "other_channel_name_hypothesis": "",
            "hypothesis_confidence": "HIGH",
            "hypothesis_rule": "Already classified ACQ_IM (G-3030) — confirm keep IM; do not double-count",
        }
    if sc == "DEKOR_INTERNAL_RENT":
        return {
            "maps_to_channel_hypothesis": "INTERNAL",
            "im_share_rub_hypothesis": 0,
            "other_channel_share_rub_hypothesis": round(amt, 2),
            "other_channel_name_hypothesis": "DEKOR_RENT",
            "hypothesis_confidence": "HIGH",
            "hypothesis_rule": "Internal rent DEKOR — NOT IM",
        }
    if sc == "POS_VTB":
        return {
            "maps_to_channel_hypothesis": "POS_HOLD_NOT_IM",
            "im_share_rub_hypothesis": 0,
            "other_channel_share_rub_hypothesis": round(amt, 2),
            "other_channel_name_hypothesis": "POS_VTB_UNALLOCATED",
            "hypothesis_confidence": "HIGH_FOR_EXCLUSION",
            "hypothesis_rule": "OVERBANK month: forbid ADD_POS_TO_IM; need register to split",
        }
    return {
        "maps_to_channel_hypothesis": "UNKNOWN",
        "im_share_rub_hypothesis": "",
        "other_channel_share_rub_hypothesis": "",
        "other_channel_name_hypothesis": "",
        "hypothesis_confidence": "LOW",
        "hypothesis_rule": "No safe rule — owner fill",
    }


def main():
    for d in (REG, MARTS, MAPS, EV, WAVE_A, SIGN):
        d.mkdir(parents=True, exist_ok=True)

    # Prefer pre-hypothesis backup if present; else current 12 (may already be hypothesized)
    base = WAVE_A / "12_im_overbank_register_prefill_all.csv"
    rows_in = list(csv.DictReader(base.open()))
    # strip prior hyp cols if re-running
    base_fields = [
        "work_order_id",
        "period_month",
        "settle_date",
        "bank_le",
        "source_channel",
        "channel_confidence",
        "payment_id_or_ref",
        "amount_rub",
        "currency",
        "counterparty_short",
        "purpose_short",
        "in_class_now",
        "maps_to_channel",
        "im_share_rub",
        "other_channel_share_rub",
        "other_channel_name",
        "timing_lag_days",
        "owner_comment",
        "status",
        "instruction_ru",
    ]
    clean = []
    for r in rows_in:
        clean.append({k: r.get(k, "") for k in base_fields if k in r or k in base_fields})
        for k in base_fields:
            clean[-1].setdefault(k, "")

    summary = list(csv.DictReader((WAVE_A / "13_im_overbank_prefill_summary.csv").open()))
    # tolerate already-enriched summary
    surplus_by = {r["period_month"]: float(r["surplus_rub"]) for r in summary}

    enriched = []
    for r in clean:
        h = hyp(r)
        nr = dict(r)
        nr["maps_to_channel"] = h["maps_to_channel_hypothesis"]
        nr["im_share_rub"] = h["im_share_rub_hypothesis"]
        nr["other_channel_share_rub"] = h["other_channel_share_rub_hypothesis"]
        nr["other_channel_name"] = h["other_channel_name_hypothesis"]
        nr["status"] = "HYPOTHESIS_PREFILL_WAITING_CONFIRM"
        nr["instruction_ru"] = (
            f"ГИПОТЕЗА ({h['hypothesis_confidence']}): {h['hypothesis_rule']}. "
            f"Подтвердить/править. НЕ auto-Accept."
        )
        nr.update(
            {
                "hypothesis_confidence": h["hypothesis_confidence"],
                "hypothesis_rule": h["hypothesis_rule"],
                "owner_must_confirm": "YES",
                "do_not_auto_accept": "YES",
                "surplus_month_rub": surplus_by.get(r["period_month"], ""),
                "so_t": "N",
            }
        )
        enriched.append(nr)

    by_m: dict = defaultdict(lambda: {"im_hyp": 0.0, "not_im_hyp": 0.0, "n": 0, "pos_hold": 0.0, "tbank_im": 0.0, "rent": 0.0})
    for r in enriched:
        m = r["period_month"]
        by_m[m]["n"] += 1
        im = float(r["im_share_rub"] or 0)
        oth = float(r["other_channel_share_rub"] or 0)
        by_m[m]["im_hyp"] += im
        by_m[m]["not_im_hyp"] += oth
        if r["maps_to_channel"] == "POS_HOLD_NOT_IM":
            by_m[m]["pos_hold"] += oth
        if r["source_channel"] == "TBANK":
            by_m[m]["tbank_im"] += im
        if r["source_channel"] == "DEKOR_INTERNAL_RENT":
            by_m[m]["rent"] += oth

    month_rows = []
    for m, v in sorted(by_m.items()):
        month_rows.append(
            {
                "period_month": m,
                "lines_n": v["n"],
                "hyp_im_share_sum_rub": round(v["im_hyp"], 2),
                "hyp_not_im_sum_rub": round(v["not_im_hyp"], 2),
                "hyp_pos_hold_rub": round(v["pos_hold"], 2),
                "hyp_tbank_im_rub": round(v["tbank_im"], 2),
                "hyp_dekor_rent_rub": round(v["rent"], 2),
                "surplus_rub": surplus_by.get(m, 0),
                "owner_next": "CONFIRM hypotheses; POS_HOLD stays out of IM; never ADD_POS_TO_IM",
                "gate_effect": "→24 after owner confirm (E07)",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    checks = [
        {
            "period_month": r["period_month"],
            "check_tbank_im": "☐",
            "check_pos_hold_not_im": "☐",
            "check_rent_internal": "☐",
            "check_surplus_explained": "☐",
            "signer": "Сливяк / Мамушкина",
            "forbidden": "ADD_POS_TO_IM on overbank months",
            "artifact": "20_im_overbank_hypothesis_prefill.csv",
            "signature": "",
            "date": "",
            "do_not_auto_accept": "YES",
        }
        for r in month_rows
    ]

    # enrich summary keeping original keys
    sum_out = []
    hyp_by = {r["period_month"]: r for r in month_rows}
    for r in summary:
        nr = {k: v for k, v in r.items() if not k.startswith("hyp_")}
        h = hyp_by[r["period_month"]]
        nr.update(
            {
                "hyp_im_share_sum_rub": h["hyp_im_share_sum_rub"],
                "hyp_pos_hold_rub": h["hyp_pos_hold_rub"],
                "hyp_dekor_rent_rub": h["hyp_dekor_rent_rub"],
                "hyp_status": "WAITING_CONFIRM",
                "owner_next": h["owner_next"],
                "do_not_auto_accept": "YES",
            }
        )
        sum_out.append(nr)

    meta = {
        "horizon": "H69",
        "date": str(date.today()),
        "title": "Overbank channel-share hypothesis prefill + ping refresh",
        "lines_n": len(enriched),
        "months_n": len(month_rows),
        "hyp_by_confidence": dict(Counter(r["hypothesis_confidence"] for r in enriched)),
        "gate_now": "18/30",
        "gate_if_e02_and_e07": "24/30",
        "no_fake_accept": True,
        "so_t": False,
    }
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "im_overbank_hypothesis_prefill.csv", enriched)
    write_csv(REG / "im_overbank_hypothesis_month_rollup.csv", month_rows)
    write_csv(REG / "im_overbank_hypothesis_confirm_checklist.csv", checks)

    for name in [
        "im_overbank_hypothesis_prefill.csv",
        "im_overbank_hypothesis_month_rollup.csv",
        "im_overbank_hypothesis_confirm_checklist.csv",
        "meta.json",
    ]:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h69_meta.json")
            shutil.copy2(src, MAPS / "h69_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    shutil.copy2(REG / "im_overbank_hypothesis_prefill.csv", WAVE_A / "20_im_overbank_hypothesis_prefill.csv")
    shutil.copy2(REG / "im_overbank_hypothesis_month_rollup.csv", WAVE_A / "21_im_overbank_hypothesis_month_rollup.csv")
    shutil.copy2(REG / "im_overbank_hypothesis_confirm_checklist.csv", WAVE_A / "22_im_overbank_hypothesis_confirm_checklist.csv")
    shutil.copy2(REG / "im_overbank_hypothesis_prefill.csv", WAVE_A / "12_im_overbank_register_prefill_all.csv")
    write_csv(WAVE_A / "13_im_overbank_prefill_summary.csv", sum_out)
    write_csv(MARTS / "im_overbank_prefill_summary.csv", sum_out)

    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
