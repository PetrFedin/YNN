#!/usr/bin/env python3
"""H80 — Post-sign activation matrix + telegram blast texts.

Зачем: после подписи нужен явный next step (analytics + owner), не «и что?».
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
EV = ROOT / "live/evidence/h80_post_sign_activation_20260729"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> dict:
    # Re-publish from REG if present; else no-op rebuild expects files already written
    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)
    meta = {
        "horizon": "H80",
        "date": str(date.today()),
        "title": "Post-sign activation + telegram blast + MD checkbox sync",
        "no_fake_accept": True,
        "so_t": False,
    }
    for name in ["post_sign_activation.csv", "telegram_blast_ready.csv"]:
        src = REG / name
        if not src.exists():
            raise SystemExit(f"missing {src}; run packaging first")
        shutil.copy2(src, SIGN / ("17_POST_SIGN_ACTIVATION.csv" if "post" in name else "18_TELEGRAM_BLAST_READY.csv"))
        shutil.copy2(src, MARTS / name)
        shutil.copy2(src, MAPS / name)
        shutil.copy2(src, EV / name)
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy2(REG / "meta.json", MARTS / "h80_meta.json")
    shutil.copy2(REG / "meta.json", MAPS / "h80_meta.json")
    shutil.copy2(REG / "meta.json", EV / "meta.json")
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return meta


if __name__ == "__main__":
    main()
