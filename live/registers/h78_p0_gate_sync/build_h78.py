#!/usr/bin/env python3
"""H78 — P0 gate sync after H73–H77 (packaging only).

Зачем: data-ops P2 закрыт; owners всё ещё смотрят устаревший Today/TAX path.
Синхронизируем Today Top5, critical path, tail checklist, unlock simulation,
handoff и coverage — без fake Accept и без нового forensic.
"""
# Canonical builder lives as re-runnable script; logic mirrored from packaging run.
from __future__ import annotations

import csv
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h78_p0_gate_sync_20260729"
SIGN = ROOT / "live/client_pack/sign_session_pack"
WAVE_A = ROOT / "live/client_pack/execution_wave_a"
WAVE_C = ROOT / "live/client_pack/execution_wave_c"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> dict:
    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)

    today = [
        dict(
            board_rank="1",
            priority_band="P0_GATE",
            source="H78",
            exec_tag="MEET",
            action="Провести sign session 15–20 мин (00_SIGN_SESSION_15MIN, H76 TAX в async)",
            owner="ведущий / Янина",
            unlocks="весь gate path",
            gate_effect="unlocks signing",
        ),
        dict(
            board_rank="2",
            priority_band="P0_GATE",
            source="H68/H78",
            exec_tag="E02",
            action="E02 soft-slice: 2025-08=37 328 ₽ + 2026-04=509 351 ₽ (не весь POS)",
            owner="Сливяк / Мамушкина",
            unlocks="IM soft",
            gate_effect="18→20",
        ),
        dict(
            board_rank="3",
            priority_band="P0_GATE",
            source="H70/H78",
            exec_tag="E08",
            action="E08 Path A: подписать core−card D-H58-BANK-01",
            owner="Янина / Сливяк",
            unlocks="BANK policy",
            gate_effect="24→26",
        ),
        dict(
            board_rank="4",
            priority_band="P0_GATE",
            source="H76/H78",
            exec_tag="TAX",
            action="TAX: подписать Salon→УФК perimeter (14_TAX_SOFT) + 36k confirm",
            owner="Сливяк / Янина",
            unlocks="TAX_CASH_BANK",
            gate_effect="26→27",
        ),
        dict(
            board_rank="5",
            priority_band="P0_GATE",
            source="H71/H78",
            exec_tag="FILES",
            action="Файлы: DDS June + Feb dump + Mercury/July bank",
            owner="Сливяк",
            unlocks="Feb/Mercury/June",
            gate_effect="27→30",
        ),
    ]
    write_csv(REG / "today_top5_p0.csv", today)

    crit = [
        dict(
            step="0",
            gate_from="18",
            gate_to="18",
            action="AS_IS CURRENT",
            owner="—",
            artifact="NOW.md / sign_session_pack/00_SIGN_SESSION_15MIN.md",
            status="NOW",
            depends="",
        ),
        dict(
            step="1",
            gate_from="18",
            gate_to="20",
            action="E02 soft-slice Accept 37k+509k",
            owner="Сливяк/Мамушкина",
            artifact="sign_session_pack/07_E02_EVIDENCE_BRIEF.md",
            status="WAITING_SIGN",
            depends="MEET",
        ),
        dict(
            step="2",
            gate_from="20",
            gate_to="24",
            action="E07 overbank confirm hypotheses ×4",
            owner="Сливяк",
            artifact="execution_wave_a/20_im_overbank_hypothesis_prefill.csv",
            status="WAITING_SIGN",
            depends="E02",
        ),
        dict(
            step="3",
            gate_from="24",
            gate_to="26",
            action="E08 Path A core−card OR Path B map card→DDS",
            owner="Янина/Сливяк",
            artifact="sign_session_pack/10_E08_DUAL_PATH_CHECKLIST.csv",
            status="WAITING_SIGN",
            depends="E07",
        ),
        dict(
            step="4",
            gate_from="26",
            gate_to="27",
            action="TAX: Salon UFK perimeter (H76) + 36k map to ENP",
            owner="Сливяк",
            artifact="sign_session_pack/14_TAX_SOFT_PERIMETER_H76.csv + 11_TAX_36K_*",
            status="WAITING_SIGN",
            depends="E08",
        ),
        dict(
            step="5",
            gate_from="27",
            gate_to="28",
            action="Feb 2026 DDS>bank article recon (−1.50M)",
            owner="Сливяк",
            artifact="execution_wave_c/27_feb2026_recon_work_order.csv",
            status="WAITING_FILE",
            depends="TAX",
        ),
        dict(
            step="6",
            gate_from="28",
            gate_to="29",
            action="Mercury May payment / July bank refresh",
            owner="Сливяк",
            artifact="execution_wave_c/26_mercury_intake_work_orders.csv",
            status="WAITING_FILE",
            depends="Feb",
        ),
        dict(
            step="7",
            gate_from="29",
            gate_to="30",
            action="Mercury June window + DDS June residual",
            owner="Сливяк/Мамушкина",
            artifact="execution_wave_c/07_tsum_missing_payment_tracker.csv + DDS June file",
            status="WAITING_FILE",
            depends="Mercury",
        ),
    ]
    write_csv(REG / "gate_critical_path.csv", crit)

    sim = [
        dict(scenario="AS_IS", gate_score="18/30", delta="0", requires="—", note="Current", so_t="N"),
        dict(
            scenario="E02_SIGNED",
            gate_score="20/30",
            delta="+2",
            requires="07_E02 soft-slice signs",
            note="Soft only, not full POS",
            so_t="N",
        ),
        dict(
            scenario="E02_E07",
            gate_score="24/30",
            delta="+4",
            requires="overbank hypothesis confirms",
            note="Wave A prefill",
            so_t="N",
        ),
        dict(
            scenario="E02_E07_E08",
            gate_score="26/30",
            delta="+2",
            requires="E08 Path A preferred",
            note="core−card policy",
            so_t="N",
        ),
        dict(
            scenario="PLUS_TAX_PERIMETER",
            gate_score="27/30",
            delta="+1",
            requires="14_TAX_SOFT + 11_TAX_36K",
            note="Salon UFK in TAX_CASH_BANK",
            so_t="N",
        ),
        dict(
            scenario="PLUS_FEB_FILE",
            gate_score="28/30",
            delta="+1",
            requires="Feb DDS article dump",
            note="No FORCE_CLOSE",
            so_t="N",
        ),
        dict(
            scenario="PLUS_MERCURY",
            gate_score="29/30",
            delta="+1",
            requires="Mercury May + July bank",
            note="Intake WO",
            so_t="N",
        ),
        dict(
            scenario="PLUS_JUNE_DDS",
            gate_score="30/30",
            delta="+1",
            requires="DDS 2026 full June",
            note="Stage1 gate closed",
            so_t="N",
        ),
    ]
    write_csv(REG / "gate_unlock_simulation.csv", sim)

    tail = [
        dict(
            order="1",
            exec="TAX_PERIMETER",
            action="Sign Salon→УФК into TAX_CASH_BANK perimeter (closes 36k/147k/77k deltas)",
            artifact="14_TAX_SOFT_PERIMETER_H76.csv",
            signer="Сливяк/Янина",
            check="☐",
            signature="",
            date="",
            do_not_auto_accept="YES",
        ),
        dict(
            order="2",
            exec="TAX36k",
            action="Confirm map 36k UFK → «Единый налоговый платеж, НСипЗ» (Salon Sber) OR show existing DDS line",
            artifact="11_TAX_36K_EVIDENCE.csv",
            signer="Сливяк",
            check="☐",
            signature="",
            date="",
            do_not_auto_accept="YES",
        ),
        dict(
            order="3",
            exec="FEB2026",
            action="Provide DDS Feb article dump; close −1.50M vs bank core",
            artifact="27_feb2026_recon_work_order.csv",
            signer="Сливяк",
            check="☐",
            signature="",
            date="",
            do_not_auto_accept="YES",
        ),
        dict(
            order="4",
            exec="MERCURY_MAY",
            action="July bank refresh + Mercury AR for May sales (~2.58M net expected)",
            artifact="26_mercury_intake_work_orders.csv",
            signer="Сливяк",
            check="☐",
            signature="",
            date="",
            do_not_auto_accept="YES",
        ),
        dict(
            order="5",
            exec="DDS_JUNE",
            action="Upload DDS 2026 with full June",
            artifact="01_bank_dds_work_orders.csv",
            signer="Сливяк",
            check="☐",
            signature="",
            date="",
            do_not_auto_accept="YES",
        ),
    ]
    write_csv(REG / "gate_tail_checklist.csv", tail)

    handoff = [
        dict(bucket="DONE", item="H52–H60 packs (enable/NOW/TAX36k/gate path)", ref="39–47"),
        dict(bucket="DONE", item="H61–H67 source freeze / collections / fabric / person-cost", ref="48–54"),
        dict(bucket="DONE", item="H68–H72 master P0 + overbank + card/DDS + gate tail + sign sync", ref="55–59"),
        dict(bucket="DONE", item="H73–H75 designers/цех/stock sell-through bridges", ref="60–62"),
        dict(bucket="DONE", item="H76 tax SOFT=Salon UFK perimeter + H77 SALES↔budget sanity", ref="63–64"),
        dict(bucket="DONE", item="H78 P0 gate sync (today/path/simulation)", ref="65"),
        dict(bucket="WAITING", item="Owner signatures / file fills / calls", ref="NOW.md + sign_session_pack"),
        dict(bucket="WAITING", item="Mercury May cash / DDS June / Feb dump", ref="wave_c 26–27 + checklist"),
        dict(bucket="BLOCKED", item="MD unit-econ 2024–25", ref="E12 constraint"),
        dict(bucket="BLOCKED", item="Audited company P&L", ref="Stage 2+"),
    ]
    write_csv(REG / "handoff_done_waiting_blocked.csv", handoff)

    cov_old = list(csv.DictReader((MAPS / "coverage_done_vs_missing.csv").open(encoding="utf-8")))
    updates = {
        "Tax cash": dict(
            area="Tax cash",
            status="READY_FOR_SIGN",
            evidence="H76: 3/4 SOFT/GAP = Salon UFK; 36k evidence",
            missing="Owner perimeter sign",
            unblock="14_TAX_SOFT + 11_TAX_36K",
        )
    }
    extra = [
        dict(
            area="Payroll designers↔collections",
            status="DONE_INDICATIVE",
            evidence="H73 KPI/smetka bridge",
            missing="—",
            unblock="Wave B 34–37",
        ),
        dict(
            area="Payroll цех↔collections/stock",
            status="DONE_INDICATIVE",
            evidence="H74 portn bridge ~2.51M",
            missing="stock hit rare (expected)",
            unblock="Wave B 38–42",
        ),
        dict(
            area="Goods stock↔IM/TSUM sell-through",
            status="DONE_INDICATIVE",
            evidence="H75 226 STOCK_NO_SALES; 36 HIGH",
            missing="owner markdown decisions",
            unblock="Wave B 43–46",
        ),
        dict(
            area="SALES↔budget income sanity",
            status="DONE_INDICATIVE",
            evidence="H77 MATCH 2026-02..05; Jan=deposit",
            missing="June 2026 fact",
            unblock="DDS June file",
        ),
    ]
    new_cov = []
    seen = set()
    for r in cov_old:
        a = r["area"]
        if a in updates:
            new_cov.append(updates[a])
        else:
            new_cov.append(r)
        seen.add(a)
    for e in extra:
        if e["area"] not in seen:
            new_cov.append(e)
    write_csv(REG / "coverage_done_vs_missing.csv", new_cov)

    board = [
        dict(
            board_rank="1",
            priority_band="P0_GATE",
            exec_tag="MEET",
            status="WAITING",
            action=today[0]["action"],
            owner=today[0]["owner"],
            gate_effect=today[0]["gate_effect"],
            artifact="sign_session_pack/00_SIGN_SESSION_15MIN.md",
            source="H78",
        ),
        dict(
            board_rank="2",
            priority_band="P0_GATE",
            exec_tag="E02",
            status="WAITING",
            action=today[1]["action"],
            owner=today[1]["owner"],
            gate_effect=today[1]["gate_effect"],
            artifact="sign_session_pack/07_E02_EVIDENCE_BRIEF.md",
            source="H68",
        ),
        dict(
            board_rank="3",
            priority_band="P0_GATE",
            exec_tag="E07",
            status="WAITING",
            action="Confirm overbank hypotheses (TBANK→IM, POS→HOLD)",
            owner="Сливяк",
            gate_effect="20→24",
            artifact="execution_wave_a/20_im_overbank_hypothesis_prefill.csv",
            source="H69",
        ),
        dict(
            board_rank="4",
            priority_band="P0_GATE",
            exec_tag="E08",
            status="WAITING",
            action=today[2]["action"],
            owner=today[2]["owner"],
            gate_effect=today[2]["gate_effect"],
            artifact="sign_session_pack/10_E08_DUAL_PATH_CHECKLIST.csv",
            source="H70",
        ),
        dict(
            board_rank="5",
            priority_band="P0_GATE",
            exec_tag="TAX",
            status="WAITING",
            action=today[3]["action"],
            owner=today[3]["owner"],
            gate_effect=today[3]["gate_effect"],
            artifact="sign_session_pack/14_TAX_SOFT_PERIMETER_H76.csv",
            source="H76",
        ),
        dict(
            board_rank="6",
            priority_band="P0_GATE",
            exec_tag="FEB",
            status="WAITING_FILE",
            action="Feb DDS article dump (−1.5M)",
            owner="Сливяк",
            gate_effect="27→28",
            artifact="execution_wave_c/27_feb2026_recon_work_order.csv",
            source="H71",
        ),
        dict(
            board_rank="7",
            priority_band="P0_GATE",
            exec_tag="MERCURY_JUNE",
            status="WAITING_FILE",
            action="Mercury + DDS June / July bank",
            owner="Сливяк",
            gate_effect="28→30",
            artifact="execution_wave_c/26_* + 01_bank_dds_*",
            source="H71",
        ),
        dict(
            board_rank="8",
            priority_band="P2_DATA_DONE",
            exec_tag="DATA",
            status="DONE",
            action="H73–H77 data bridges complete (no further empty forensic)",
            owner="analytics",
            gate_effect="none",
            artifact="60–64 client packs",
            source="H78",
        ),
    ]
    write_csv(REG / "master_p0_action_board.csv", board)

    meta = {
        "horizon": "H78",
        "date": str(date.today()),
        "title": "P0 gate sync after H73–H77 — today/path/simulation/coverage",
        "gate_now": "18/30",
        "gate_if_full_path": "30/30",
        "p0_actions_n": 7,
        "data_ops_closed": "H73-H77",
        "no_fake_accept": True,
        "so_t": False,
        "note": "Packaging only — owners/files move the score",
    }
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    publish = {
        "today_top5_p0.csv": [
            SIGN / "08_TODAY_TOP5_P0.csv",
            WAVE_A / "19_today_top5_p0.csv",
            MARTS / "today_top5_p0.csv",
            MAPS / "today_top5_p0.csv",
        ],
        "gate_critical_path.csv": [
            SIGN / "13_GATE_CRITICAL_PATH.csv",
            MARTS / "gate_critical_path_unified.csv",
            MAPS / "gate_critical_path_unified.csv",
            WAVE_C / "10_gate_critical_path_unified.csv",
        ],
        "gate_unlock_simulation.csv": [
            SIGN / "15_GATE_UNLOCK_SIMULATION_H78.csv",
            MARTS / "gate_unlock_simulation.csv",
            MAPS / "gate_unlock_simulation.csv",
        ],
        "gate_tail_checklist.csv": [
            SIGN / "12_GATE_TAIL_CHECKLIST.csv",
            MARTS / "gate_tail_checklist.csv",
            WAVE_C / "29_gate_tail_checklist.csv",
        ],
        "handoff_done_waiting_blocked.csv": [
            MARTS / "handoff_done_waiting_blocked.csv",
            MAPS / "handoff_done_waiting_blocked.csv",
        ],
        "coverage_done_vs_missing.csv": [MAPS / "coverage_done_vs_missing.csv"],
        "master_p0_action_board.csv": [
            SIGN / "09_MASTER_P0_ACTION_BOARD.csv",
            MARTS / "master_p0_action_board.csv",
            MAPS / "master_p0_action_board.csv",
            WAVE_A / "18_master_p0_action_board.csv",
        ],
        "meta.json": [MARTS / "h78_meta.json", MAPS / "h78_meta.json", EV / "meta.json"],
    }
    for name, dests in publish.items():
        src = REG / name
        if name != "meta.json":
            shutil.copy2(src, EV / name)
        for d in dests:
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, d)

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


if __name__ == "__main__":
    main()
