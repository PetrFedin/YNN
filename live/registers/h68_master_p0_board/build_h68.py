#!/usr/bin/env python3
"""H68: Master P0 action board + E02 soft-slice evidence pack.

Highest leverage after H67: reduce owner friction for gate 18→20.
Not SoT. Does not auto-Accept. Does not invent new forensic.
"""
from __future__ import annotations

import csv
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if not (ROOT / "live/registers/00_SOURCE_CATALOG_107.csv").exists():
    ROOT = Path.cwd()
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h68_master_p0_board_20260729"
WAVE_A = ROOT / "live/client_pack/execution_wave_a"
SIGN = ROOT / "live/client_pack/sign_session_pack"


def write_csv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def read(path: Path):
    return list(csv.DictReader(path.open()))


def main():
    for d in (REG, MARTS, MAPS, EV, WAVE_A, SIGN):
        d.mkdir(parents=True, exist_ok=True)

    recon = {
        r["period_month"]: r
        for r in read(MARTS / "recon_channel_cash_month.csv")
        if r["channel"] == "IM" and r["period_month"] in {"2025-08", "2026-04"}
    }
    sign = {r["period_month"]: r for r in read(SIGN / "06_IM_SOFT_SLICE_SIGN_CARD.csv")}
    slices = {r["period_month"]: r for r in read(WAVE_A / "02_im_pos_slices.csv")}

    e02_rows = []
    for month in ("2025-08", "2026-04"):
        r, s, sl = recon[month], sign[month], slices[month]
        sales = float(r["sales_revenue_rub"])
        bank = float(r["best_bank_in_rub"])
        gap = float(r["best_gap_rub"])
        soft = float(s["amount_to_accept_into_im_rub"])
        full = float(s["payment_full_amount_rub"])
        leave = float(s["leave_unclassified_rub"])
        e02_rows.append(
            {
                "exec_id": s["exec_id"],
                "period_month": month,
                "pattern": sl.get("pattern", "UNDERBANKED"),
                "im_sales_rub": round(sales, 2),
                "bank_acq_best_rub": round(bank, 2),
                "gap_bank_minus_sales_rub": round(gap, 2),
                "gap_pct": r["gap_pct"],
                "recon_status": r["status"],
                "payment_id": s["bank_payment_id"],
                "payment_date": s["payment_date"],
                "payment_full_rub": round(full, 2),
                "soft_slice_accept_rub": round(soft, 2),
                "leave_unclassified_rub": round(leave, 2),
                "soft_vs_gap_coverage_pct": round(100 * soft / abs(gap), 1) if gap else "",
                "decision_required": "ACCEPT_SOFT_SLICE",
                "forbidden": "ACCEPT_FULL_PAYMENT_AS_IM",
                "signer": s["signer"],
                "why_soft_not_full": (
                    f"Полный платёж {full:,.0f} ₽ даст overshoot {leave:,.0f} ₽ в IM; "
                    f"soft {soft:,.0f} ₽ закрывает долю underbank gap {abs(gap):,.0f} ₽ без ложного POS→IM."
                ),
                "gate_effect": "18→20 (вместе оба месяца)",
                "sign_artifact": "sign_session_pack/06_IM_SOFT_SLICE_SIGN_CARD.csv",
                "check": "☐",
                "signature": "",
                "date": "",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    board = []
    gate_map = {
        1: ("18→ready Waves", "SIGN"),
        2: ("18→20", "E02"),
        3: ("→24", "E07"),
        4: ("→26", "E08"),
        5: ("→27", "TAX"),
        6: ("BANK 2026-06", "FILE"),
        7: ("→29", "MERCURY"),
        8: ("cash/margin", "OPS"),
    }
    minutes = {1: 15, 2: 10, 3: 30, 4: 20, 5: 15, 6: 5, 7: 10, 8: 60}
    for r in read(MARTS / "only_owner_moves_metrics.csv"):
        rank = int(r["rank"])
        ge, tag = gate_map.get(rank, ("", ""))
        board.append(
            {
                "board_rank": rank,
                "priority_band": "P0_GATE" if rank <= 7 else "P0_OPS",
                "source": "only_owner_moves",
                "exec_tag": tag,
                "action": r["action"],
                "owner": "см. sign_session / wave owners",
                "unlocks": r["unlocks"],
                "gate_effect": ge,
                "artifact": r["artifact"],
                "minutes_est": minutes.get(rank, 20),
                "depends_on": "sign session" if rank > 1 else "—",
                "status": "WAITING_OWNER",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    rank = 100
    for r in read(MARTS / "master_execution_board.csv"):
        if str(r.get("status", "")).startswith("DONE"):
            continue
        title = r["title"]
        low = title.lower()
        if any(k in low for k in ["soft-slice", "soft slice", "overbank", "mercury", "dds june", "tax 36"]):
            continue
        rank += 1
        board.append(
            {
                "board_rank": rank,
                "priority_band": "P0_EXEC" if r["priority"] == "P0" else "P1_EXEC",
                "source": "master_execution_board",
                "exec_tag": r["exec_id"],
                "action": title,
                "owner": r.get("owner_primary") or "",
                "unlocks": r.get("unlocks") or "",
                "gate_effect": r.get("gate_delta") or "",
                "artifact": r.get("artifact") or "",
                "minutes_est": 10 if "RACI" in title or "CONFIRM" in title else 30,
                "depends_on": r.get("depends_on") or "",
                "status": r.get("status") or "WAITING_OWNER",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    rank = 200
    for r in read(MARTS / "residual_p0_owner_actions.csv"):
        rank += 1
        board.append(
            {
                "board_rank": rank,
                "priority_band": r["priority_band"],
                "source": "H66",
                "exec_tag": "H66",
                "action": f"{r['article_norm']}: {r['owner_action'][:100]}",
                "owner": "производство / MD cost",
                "unlocks": "MD cost proxy coverage",
                "gate_effect": "",
                "artifact": "execution_wave_b/23_residual_p0_owner_actions.csv",
                "minutes_est": 5,
                "depends_on": "не блокирует gate",
                "status": "WAITING_OWNER",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    h67 = read(MARTS / "fabric_procurement_owner_actions.csv")
    list_only = [r for r in h67 if r["action_type"] == "SUPPLIER_NO_BANK"]
    a_band = [r for r in h67 if r["action_type"] == "FABRIC_SUPPLIER_A_BAND"]
    board.append(
        {
            "board_rank": 300,
            "priority_band": "P1_WC",
            "source": "H67",
            "exec_tag": "H67",
            "action": f"Fabric WC: {len(a_band)} A-band bank payees + {len(list_only)} list-only suppliers to check",
            "owner": "Янина / закупки",
            "unlocks": "WC тканей transparency",
            "gate_effect": "",
            "artifact": "execution_wave_b/29_fabric_procurement_owner_actions.csv",
            "minutes_est": 20,
            "depends_on": "не блокирует gate",
            "status": "WAITING_OWNER",
            "do_not_auto_accept": "YES",
            "so_t": "N",
        }
    )

    board_sorted = sorted(
        board,
        key=lambda x: (
            0
            if x["priority_band"].startswith("P0_GATE")
            else 1
            if x["priority_band"].startswith("P0_")
            else 2
            if x["priority_band"].startswith("P1")
            else 3,
            x["board_rank"],
        ),
    )
    for i, r in enumerate(board_sorted, 1):
        r["board_rank"] = i

    today = [r for r in board_sorted if r["priority_band"] in {"P0_GATE", "P0_EXEC"}][:5]

    meta = {
        "horizon": "H68",
        "date": str(date.today()),
        "title": "Master P0 board + E02 soft-slice evidence",
        "board_n": len(board_sorted),
        "p0_gate_n": sum(1 for r in board_sorted if r["priority_band"] == "P0_GATE"),
        "e02_months": ["2025-08", "2026-04"],
        "e02_soft_total_rub": round(sum(float(r["soft_slice_accept_rub"]) for r in e02_rows), 2),
        "e02_gap_total_rub": round(sum(abs(float(r["gap_bank_minus_sales_rub"])) for r in e02_rows), 2),
        "gate_now": "18/30",
        "gate_if_e02_signed": "20/30",
        "no_fake_accept": True,
        "so_t": False,
        "note": "Does not move gate alone — owners must sign. Reduces friction.",
    }

    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "master_p0_action_board.csv", list(board_sorted[0].keys()), board_sorted)
    write_csv(REG / "e02_soft_slice_evidence_pack.csv", list(e02_rows[0].keys()), e02_rows)
    write_csv(REG / "today_top5_p0.csv", list(today[0].keys()), today)

    for name in ["master_p0_action_board.csv", "e02_soft_slice_evidence_pack.csv", "today_top5_p0.csv", "meta.json"]:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h68_meta.json")
            shutil.copy2(src, MAPS / "h68_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    shutil.copy2(REG / "master_p0_action_board.csv", WAVE_A / "17_master_p0_action_board.csv")
    shutil.copy2(REG / "e02_soft_slice_evidence_pack.csv", WAVE_A / "18_e02_soft_slice_evidence_pack.csv")
    shutil.copy2(REG / "today_top5_p0.csv", WAVE_A / "19_today_top5_p0.csv")
    shutil.copy2(REG / "e02_soft_slice_evidence_pack.csv", SIGN / "07_E02_SOFT_SLICE_EVIDENCE.csv")
    shutil.copy2(REG / "today_top5_p0.csv", SIGN / "08_TODAY_TOP5_P0.csv")
    shutil.copy2(REG / "master_p0_action_board.csv", SIGN / "09_MASTER_P0_ACTION_BOARD.csv")

    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
