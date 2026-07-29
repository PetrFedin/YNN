#!/usr/bin/env python3
"""H81 — Waiting-on-owners checkpoint + sign pack print index."""
from __future__ import annotations

import json
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
SIGN = ROOT / "live/client_pack/sign_session_pack"
CLIENT = ROOT / "live/client_pack"
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h81_waiting_owners_checkpoint_20260729"


def main() -> dict:
    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)
    meta = {
        "horizon": "H81",
        "date": str(date.today()),
        "title": "Waiting-on-owners checkpoint + sign pack print index",
        "gate_now": "18/30",
        "analytics_status": "EXHAUSTED_PENDING_OWNERS",
        "no_fake_accept": True,
        "so_t": False,
    }
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    mapping = {
        "sign_pack_print_index.csv": SIGN / "19_SIGN_PACK_PRINT_INDEX.csv",
        "waiting_on_owners.csv": SIGN / "20_WAITING_ON_OWNERS.csv",
        "stop_doing_list.csv": MARTS / "stop_doing_list.csv",
    }
    for name, dest in mapping.items():
        src = REG / name
        if not src.exists():
            raise SystemExit(f"missing {src}")
        shutil.copy2(src, dest)
        shutil.copy2(src, MARTS / name)
        shutil.copy2(src, MAPS / name)
        shutil.copy2(src, EV / name)
    shutil.copy2(REG / "waiting_on_owners.csv", CLIENT / "68_WAITING_ON_OWNERS_H81.csv")
    shutil.copy2(REG / "meta.json", MARTS / "h81_meta.json")
    shutil.copy2(REG / "meta.json", MAPS / "h81_meta.json")
    shutil.copy2(REG / "meta.json", EV / "meta.json")
    shutil.copy2(REG / "stop_doing_list.csv", MAPS / "stop_doing_list.csv")
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


if __name__ == "__main__":
    main()
