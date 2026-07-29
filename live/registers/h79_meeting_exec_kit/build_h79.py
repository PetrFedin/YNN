#!/usr/bin/env python3
"""H79 — Meeting execution kit: checkboxes/pings/SLA/script with TAX+E07.

Зачем: после H78 в 01_SIGN_CHECKBOXES не было TAX/E07 — нельзя отметить на встрече.
"""
from __future__ import annotations

import csv
import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
SIGN = ROOT / "live/client_pack/sign_session_pack"
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h79_meeting_exec_kit_20260729"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> dict:
    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)

    boxes = [
        dict(order="1", exec_id="E01", decision="CONFIRM DOM-B2B = Коптева", signer="Янина", options="CONFIRM|REPLACE_FIO|DEFER", recommended="CONFIRM", check="☐", signature="", date="", when="meet"),
        dict(order="2", exec_id="E03a", decision="CONFIRM DOM-PRODUCT = Коновалова", signer="Янина", options="CONFIRM|REPLACE|DEFER", recommended="CONFIRM", check="☐", signature="", date="", when="meet"),
        dict(order="3", exec_id="E03b", decision="CONFIRM DOM-COST = Мокеева", signer="Янина", options="CONFIRM|REPLACE|DEFER", recommended="CONFIRM", check="☐", signature="", date="", when="meet"),
        dict(order="4", exec_id="E03c", decision="CONFIRM DOM-DATA = Сливяк", signer="Янина", options="CONFIRM|REPLACE|DEFER", recommended="CONFIRM", check="☐", signature="", date="", when="meet"),
        dict(order="5", exec_id="E12", decision="NO unit-econ promise MD 2024–25", signer="Янина", options="ACCEPT_CONSTRAINT|DEFER", recommended="ACCEPT_CONSTRAINT", check="☐", signature="", date="", when="meet"),
        dict(order="6", exec_id="FRAME1", decision="Dual contour mandatory in reports", signer="Янина", options="YES|NO", recommended="YES", check="☐", signature="", date="", when="meet"),
        dict(order="7", exec_id="FRAME2", decision="Ban goods −58/−74% as company P&L", signer="Янина", options="YES|NO", recommended="YES", check="☐", signature="", date="", when="meet"),
        dict(order="8", exec_id="E08", decision="ACCEPT core−card policy D-H58-BANK-01 (Path A) OR defer to card→DDS map", signer="Янина + Сливяк", options="PATH_A_CORE_CARD|PATH_B_MAP|DEFER", recommended="PATH_A_CORE_CARD", check="☐", signature="", date="", when="meet"),
        dict(order="9", exec_id="E02a", decision="ACCEPT soft-slice IM 2026-04 = 509351.08", signer="Сливяк+Мамушкина", options="ACCEPT_SOFT_SLICE|REJECT|DEFER", recommended="ACCEPT_SOFT_SLICE", check="☐", signature="", date="", when="meet"),
        dict(order="10", exec_id="E02b", decision="ACCEPT soft-slice IM 2025-08 = 37327.69", signer="Сливяк+Мамушкина", options="ACCEPT_SOFT_SLICE|REJECT|DEFER", recommended="ACCEPT_SOFT_SLICE", check="☐", signature="", date="", when="meet"),
        dict(order="11", exec_id="E06", decision="ZP #REF! fix by 2026-08-04", signer="Сливяк", options="YES_WITH_DATE|DEFER", recommended="YES_WITH_DATE", check="☐", signature="", date="", when="meet"),
        dict(order="12", exec_id="E07", decision="CONFIRM overbank hypotheses (TBANK→IM; POS→HOLD; not TSUM_NET)", signer="Сливяк", options="CONFIRM_HYP|REJECT|DEFER", recommended="CONFIRM_HYP", check="☐", signature="", date="", when="async_ok"),
        dict(order="13", exec_id="TAX_PERIMETER", decision="INCLUDE Salon→УФК payments in TAX_CASH_BANK perimeter (H76)", signer="Сливяк + Янина", options="INCLUDE_PERIMETER|REJECT|DEFER", recommended="INCLUDE_PERIMETER", check="☐", signature="", date="", when="async_or_meet"),
        dict(order="14", exec_id="TAX36k", decision="CONFIRM 36k 2024-01 Salon Sber UFK → ENP/tax cash map", signer="Сливяк", options="CONFIRM_MAP|ALREADY_IN_DDS|DEFER", recommended="CONFIRM_MAP", check="☐", signature="", date="", when="async_or_meet"),
    ]
    write_csv(REG / "sign_checkboxes.csv", boxes)

    # Prefer re-using published pings/sla/script from REG if regenerating — write same as packaging
    # Load from SIGN if already written this session
    for src_name, dst_name in [
        ("owner_ping_messages.csv", "owner_ping_messages.csv"),
        ("sla_escalation.csv", "sla_escalation.csv"),
        ("meeting_minute_script.csv", "meeting_minute_script.csv"),
    ]:
        src = REG / src_name
        if not src.exists():
            # copy back from SIGN published names
            mapping = {
                "owner_ping_messages.csv": SIGN / "02_OWNER_PING_MESSAGES.csv",
                "sla_escalation.csv": SIGN / "03_SLA_ESCALATION.csv",
                "meeting_minute_script.csv": SIGN / "16_MEETING_MINUTE_SCRIPT.csv",
            }
            shutil.copy2(mapping[src_name], src)

    meta = {
        "horizon": "H79",
        "date": str(date.today()),
        "title": "Meeting execution kit — checkboxes/pings/SLA/script with TAX",
        "checkboxes_n": len(boxes),
        "added_exec": ["E07", "TAX_PERIMETER", "TAX36k"],
        "no_fake_accept": True,
        "so_t": False,
        "note": "Closes gap: TAX/E07 missing from 01_SIGN_CHECKBOXES",
    }
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    shutil.copy2(REG / "sign_checkboxes.csv", SIGN / "01_SIGN_CHECKBOXES.csv")
    if (REG / "owner_ping_messages.csv").exists():
        shutil.copy2(REG / "owner_ping_messages.csv", SIGN / "02_OWNER_PING_MESSAGES.csv")
    if (REG / "sla_escalation.csv").exists():
        shutil.copy2(REG / "sla_escalation.csv", SIGN / "03_SLA_ESCALATION.csv")
    if (REG / "meeting_minute_script.csv").exists():
        shutil.copy2(REG / "meeting_minute_script.csv", SIGN / "16_MEETING_MINUTE_SCRIPT.csv")

    for name in ["sign_checkboxes.csv", "owner_ping_messages.csv", "sla_escalation.csv", "meeting_minute_script.csv", "meta.json"]:
        src = REG / name
        if not src.exists():
            continue
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h79_meta.json")
            shutil.copy2(src, MAPS / "h79_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


if __name__ == "__main__":
    main()
