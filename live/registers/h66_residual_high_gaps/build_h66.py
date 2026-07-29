#!/usr/bin/env python3
"""H66: residual HIGH collection gaps after H65 person-cost.

Priority: close the last owner-actionable holes without fabricating Accept.
- stem/variant recovery (0-3167/2 → 0-3167)
- MD STRONG/WEAK evidence pack
- quarantine marketing labels (ICONIC / АКЦИЯ / КЛ-2024)
- ranked owner worksheet for the remaining true blanks

Not SoT. do_not_auto_accept=YES.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
if not (ROOT / "live/registers/00_SOURCE_CATALOG_107.csv").exists():
    ROOT = Path.cwd()
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h66_residual_high_gaps_20260729"
WAVE_B = ROOT / "live/client_pack/execution_wave_b"

QUARANTINE_LABELS = {"ICONIC", "АКЦИЯ", "КЛ-2024", "АКЦИЯ", "ACTION", "PROMO"}


def write_csv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def base_art(a: str) -> str:
    s = str(a or "").strip().upper().replace(" ", "").replace("Ё", "Е")
    s = re.sub(r"/\d+$", "", s)
    # unify lookalike Cyrillic letters often used in articles
    s = s.replace("А", "A").replace("В", "B").replace("С", "C").replace("Е", "E").replace("Т", "T")
    return s


def stem_art(a: str) -> str:
    s = base_art(a)
    m = re.match(r"^(0-\d+|T-\d+|\d{2}-\d{2})", s)
    return m.group(1) if m else s


def index_arts(arts) -> dict[str, set[str]]:
    d: dict[str, set[str]] = defaultdict(set)
    for a in arts:
        d[stem_art(a)].add(a)
        d[base_art(a)].add(a)
    return d


def best_md(rows: list[dict]) -> dict:
    rank = {"STRONG": 3, "WEAK": 2, "WEAK_ARTICLE_ONLY": 1, "NONE": 0}
    return max(rows, key=lambda r: (rank.get(r.get("link_type", ""), -1), float(r.get("score") or 0)))


def main():
    for d in (REG, MARTS, MAPS, EV, WAVE_B):
        d.mkdir(parents=True, exist_ok=True)

    high_ws = list(csv.DictReader((MARTS / "high_gap_owner_worksheet.csv").open()))
    residual = [r for r in high_ws if r["person_cost_hit"] == "N"]

    pc = {r["article_norm"]: r for r in csv.DictReader((MARTS / "person_cost_collection_bridge.csv").open())}
    sku = {r["article_norm"]: r for r in csv.DictReader((MARTS / "sku_master_normalized.csv").open()) if r["article_norm"]}
    stock_arts = {r["article_norm"] for r in csv.DictReader((MARTS / "stock_cost_articles.csv").open()) if r.get("article_norm")}
    col_bridge = {r["article_norm"]: r for r in csv.DictReader((MARTS / "collection_sku_stock_bridge.csv").open())}

    pc_idx = index_arts(pc)
    sku_idx = index_arts(sku)
    stock_idx = index_arts(stock_arts)

    # MD links by article_norm
    md_by: dict[str, list[dict]] = defaultdict(list)
    for r in csv.DictReader((MARTS / "collection_md_links.csv").open()):
        a = str(r.get("article") or "").strip().upper().replace(" ", "")
        if a:
            md_by[a].append(r)

    # collection descriptions / clients for residual
    col_lines: dict[str, list[dict]] = defaultdict(list)
    for r in csv.DictReader((MARTS / "collection_order_lines.csv").open()):
        a = r["article_norm"]
        if a in {x["article_norm"] for x in residual}:
            col_lines[a].append(r)

    rows_out = []
    for r in residual:
        art = r["article_norm"]
        st = stem_art(art)
        ba = base_art(art)
        related_pc = sorted((pc_idx.get(st) or set()) | (pc_idx.get(ba) or set()))
        related_sku = sorted((sku_idx.get(st) or set()) | (sku_idx.get(ba) or set()))
        related_stock = sorted((stock_idx.get(st) or set()) | (stock_idx.get(ba) or set()))

        md_rows = md_by.get(art, [])
        md = best_md(md_rows) if md_rows else {}
        lines = col_lines.get(art, [])
        desc_sample = ""
        clients = []
        for ln in lines[:8]:
            if not desc_sample and ln.get("description"):
                desc_sample = str(ln["description"]).strip()[:80]
            if ln.get("client_surname"):
                clients.append(ln["client_surname"])
        clients = sorted(set(clients))[:5]

        # known marketing / promo labels — not real SKU codes
        is_quarantine = art in QUARANTINE_LABELS or art.upper() in {x.upper() for x in QUARANTINE_LABELS}

        if is_quarantine:
            resolution = "QUARANTINE_LABEL"
            owner_action = "Не артикул — маркетинговый ярлык; исключить из SKU/cost bridge или разнести по моделям"
            priority_band = "P2_CLEANUP"
        elif related_pc:
            resolution = "STEM_PERSON_COST"
            owner_action = f"Confirm variant→person-cost proxy: {', '.join(related_pc[:3])} (не Accept)"
            priority_band = "P0_CONFIRM"
        elif md.get("link_type") == "STRONG":
            resolution = "MD_STRONG_ONLY"
            owner_action = f"Confirm MD STRONG line {md.get('md_line_id','')} / {md.get('md_client','')} as cost evidence; need workshop card"
            priority_band = "P0_CONFIRM"
        elif related_sku or related_stock:
            resolution = "STEM_SKU_OR_STOCK"
            owner_action = "Сверить stem с SKU/stock; завести alias candidate если имя совпадает"
            priority_band = "P1_ALIAS"
        elif md.get("link_type") in {"WEAK", "WEAK_ARTICLE_ONLY"}:
            resolution = "MD_WEAK_ONLY"
            owner_action = "Слабый MD hit — нужна карточка пошива или alias; не Accept"
            priority_band = "P1_ALIAS"
        else:
            resolution = "TRUE_BLANK"
            owner_action = "Нет PC/SKU/stock/MD cost — запросить workshop card или исключить из HIGH до появления файла"
            priority_band = "P0_REQUEST_FILE"

        sale = float(r["collection_sale_eur"] or 0)
        rows_out.append(
            {
                "article_norm": art,
                "article_stem": st,
                "article_base": ba,
                "collection_types": r["collection_types"],
                "collection_sale_eur": round(sale, 2),
                "orders_n": col_bridge.get(art, {}).get("collection_orders_n", len(lines)),
                "description_sample": desc_sample,
                "clients_sample": "|".join(clients),
                "related_person_cost_arts": "|".join(related_pc[:5]),
                "related_sku_arts": "|".join(related_sku[:5]),
                "related_stock_arts": "|".join(related_stock[:5]),
                "md_best_link_type": md.get("link_type", ""),
                "md_best_score": md.get("score", ""),
                "md_line_id": md.get("md_line_id", ""),
                "md_client": md.get("md_client", ""),
                "md_total_amount": md.get("md_total_amount", ""),
                "md_cost_amount": md.get("md_cost_amount", ""),
                "md_period_month": md.get("md_period_month", ""),
                "resolution": resolution,
                "priority_band": priority_band,
                "owner_action": owner_action,
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    rows_out.sort(key=lambda x: (-{"P0_CONFIRM": 3, "P0_REQUEST_FILE": 2, "P1_ALIAS": 1, "P2_CLEANUP": 0}.get(x["priority_band"], -1), -float(x["collection_sale_eur"])))

    # summary by resolution
    by_res: dict[str, dict] = defaultdict(lambda: {"n": 0, "sale_eur": 0.0})
    for r in rows_out:
        by_res[r["resolution"]]["n"] += 1
        by_res[r["resolution"]]["sale_eur"] += float(r["collection_sale_eur"])
    res_rows = [
        {"resolution": k, "articles_n": v["n"], "sale_eur": round(v["sale_eur"], 2)}
        for k, v in sorted(by_res.items(), key=lambda x: -x[1]["sale_eur"])
    ]

    # owner top actions (exclude quarantine from P0 file request noise in separate sheet)
    p0 = [r for r in rows_out if r["priority_band"].startswith("P0")]
    stem_closed = [r for r in rows_out if r["resolution"] == "STEM_PERSON_COST"]
    true_blank = [r for r in rows_out if r["resolution"] == "TRUE_BLANK"]
    quarantine = [r for r in rows_out if r["resolution"] == "QUARANTINE_LABEL"]

    meta = {
        "horizon": "H66",
        "date": str(date.today()),
        "title": "Residual HIGH gaps after H65 — stem/MD/quarantine pack",
        "residual_high_n": len(rows_out),
        "residual_sale_eur": round(sum(float(r["collection_sale_eur"]) for r in rows_out), 2),
        "stem_person_cost_n": len(stem_closed),
        "stem_person_cost_sale_eur": round(sum(float(r["collection_sale_eur"]) for r in stem_closed), 2),
        "md_strong_only_n": sum(1 for r in rows_out if r["resolution"] == "MD_STRONG_ONLY"),
        "true_blank_n": len(true_blank),
        "true_blank_sale_eur": round(sum(float(r["collection_sale_eur"]) for r in true_blank), 2),
        "quarantine_n": len(quarantine),
        "quarantine_sale_eur": round(sum(float(r["collection_sale_eur"]) for r in quarantine), 2),
        "p0_owner_actions_n": len(p0),
        "resolutions": res_rows,
        "no_fake_accept": True,
        "so_t": False,
    }

    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "residual_high_gap_pack.csv", list(rows_out[0].keys()), rows_out)
    write_csv(REG / "residual_high_gap_resolution_summary.csv", list(res_rows[0].keys()), res_rows)
    write_csv(REG / "residual_p0_owner_actions.csv", list(p0[0].keys()) if p0 else ["article_norm"], p0)
    write_csv(REG / "residual_true_blanks.csv", list(true_blank[0].keys()) if true_blank else ["article_norm"], true_blank)
    write_csv(REG / "residual_quarantine_labels.csv", list(quarantine[0].keys()) if quarantine else ["article_norm"], quarantine)
    write_csv(REG / "residual_stem_person_cost_hits.csv", list(stem_closed[0].keys()) if stem_closed else ["article_norm"], stem_closed)

    for name in [
        "residual_high_gap_pack.csv",
        "residual_high_gap_resolution_summary.csv",
        "residual_p0_owner_actions.csv",
        "residual_true_blanks.csv",
        "residual_quarantine_labels.csv",
        "residual_stem_person_cost_hits.csv",
        "meta.json",
    ]:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h66_meta.json")
            shutil.copy2(src, MAPS / "h66_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    shutil.copy2(REG / "residual_high_gap_pack.csv", WAVE_B / "22_residual_high_gap_pack.csv")
    shutil.copy2(REG / "residual_p0_owner_actions.csv", WAVE_B / "23_residual_p0_owner_actions.csv")
    shutil.copy2(REG / "residual_true_blanks.csv", WAVE_B / "24_residual_true_blanks.csv")
    shutil.copy2(REG / "residual_stem_person_cost_hits.csv", WAVE_B / "25_residual_stem_person_cost_hits.csv")

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    print("P0 sample:")
    for r in p0[:10]:
        print(r["priority_band"], r["article_norm"], r["collection_sale_eur"], r["resolution"], r["owner_action"][:70])


if __name__ == "__main__":
    main()
