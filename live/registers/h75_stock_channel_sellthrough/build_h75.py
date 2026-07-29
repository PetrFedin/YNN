#!/usr/bin/env python3
"""H75 — Goods stock end-qty ↔ IM/TSUM sales (channel sell-through).

Зачем:
  После H74 ясно: цех почти не попадает в goods stock. Остаётся вопрос:
  что лежит на Склад ИМ / Остатки ЦУМ и продаётся ли это в каналах.

Правила:
  - stock snapshot = qty_end из h6 stock_by_warehouse_full (indicative)
  - sales = w4 sales_lines (IM/TSUM/B2B)
  - warehouse→channel map soft; OTHER warehouses = context only
  - do_not_auto_accept=YES · so_t=N · не company P&L
"""
from __future__ import annotations

import csv
import json
import shutil
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
MAPS = ROOT / "live/maps"
EV = ROOT / "live/evidence/h75_stock_channel_sellthrough_20260729"
WAVE_B = ROOT / "live/client_pack/execution_wave_b"

STOCK_PATH = ROOT / "live/registers/h6_marts/stock_by_warehouse_full.csv"
SALES_PATH = ROOT / "live/registers/w4_sales_settle/sales_lines.csv"

WH_CHANNEL = {
    "Склад ИМ (Основное подразделение)": "IM",
    "Остатки ЦУМ (Основное подразделение)": "TSUM",
    "Склад оптовых продаж (Основное подразделение)": "B2B",
    "Салон (Лена М.) (Основное подразделение)": "SALON",
    "ДЕМИ (Основное подразделение)": "DEMI",
    "Подарки (Основное подразделение)": "GIFTS",
    "Aldo Coppola (Основное подразделение)": "ALDO",
}


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def fnum(x) -> float:
    try:
        return float(x) if x not in (None, "") else 0.0
    except (TypeError, ValueError):
        return 0.0


def short_wh(name: str) -> str:
    return name.replace(" (Основное подразделение)", "").strip()


def main() -> dict:
    # --- stock aggregate by sku × warehouse ---
    stock_rows = list(csv.DictReader(STOCK_PATH.open(encoding="utf-8")))
    by_sku_wh = defaultdict(
        lambda: {"qty_end": 0.0, "qty_in": 0.0, "qty_out": 0.0, "name": "", "article_raw": ""}
    )
    by_sku = defaultdict(
        lambda: {
            "qty_end": 0.0,
            "whs": set(),
            "im_qty": 0.0,
            "tsum_qty": 0.0,
            "b2b_qty": 0.0,
            "name": "",
        }
    )
    for r in stock_rows:
        sku = (r.get("canonical_sku") or r.get("article_raw") or "").strip()
        if not sku:
            continue
        wh = r["warehouse"]
        qe = fnum(r.get("qty_end"))
        qi = fnum(r.get("qty_in"))
        qo = fnum(r.get("qty_out"))
        key = (sku, wh)
        b = by_sku_wh[key]
        b["qty_end"] += qe
        b["qty_in"] += qi
        b["qty_out"] += qo
        b["name"] = r.get("name") or b["name"]
        b["article_raw"] = r.get("article_raw") or b["article_raw"]
        s = by_sku[sku]
        s["qty_end"] += qe
        s["whs"].add(wh)
        s["name"] = r.get("name") or s["name"]
        ch = WH_CHANNEL.get(wh, "OTHER")
        if ch == "IM":
            s["im_qty"] += qe
        elif ch == "TSUM":
            s["tsum_qty"] += qe
        elif ch == "B2B":
            s["b2b_qty"] += qe

    # --- sales aggregate by sku × channel ---
    sales_rows = list(csv.DictReader(SALES_PATH.open(encoding="utf-8")))
    sales_by = defaultdict(
        lambda: {"qty": 0.0, "rev": 0.0, "lines": 0, "months": set(), "channels": set()}
    )
    sales_ch = defaultdict(lambda: {"qty": 0.0, "rev": 0.0, "lines": 0})
    for r in sales_rows:
        sku = (r.get("canonical_sku") or r.get("article_raw") or "").strip()
        if not sku:
            continue
        ch = r.get("channel") or "UNK"
        qty = fnum(r.get("qty"))
        rev = fnum(r.get("revenue_rub"))
        sales_by[sku]["qty"] += qty
        sales_by[sku]["rev"] += rev
        sales_by[sku]["lines"] += 1
        sales_by[sku]["months"].add(r.get("period_month") or "")
        sales_by[sku]["channels"].add(ch)
        sales_ch[(sku, ch)]["qty"] += qty
        sales_ch[(sku, ch)]["rev"] += rev
        sales_ch[(sku, ch)]["lines"] += 1

    all_skus = set(by_sku) | set(sales_by)

    bridge = []
    for sku in sorted(all_skus):
        st = by_sku.get(sku)
        sa = sales_by.get(sku)
        im_s = sales_ch.get((sku, "IM"), {"qty": 0.0, "rev": 0.0, "lines": 0})
        tsum_s = sales_ch.get((sku, "TSUM"), {"qty": 0.0, "rev": 0.0, "lines": 0})
        b2b_s = sales_ch.get((sku, "B2B"), {"qty": 0.0, "rev": 0.0, "lines": 0})

        in_stock = st is not None and st["qty_end"] > 0
        in_sales = sa is not None and sa["qty"] > 0
        if in_stock and in_sales:
            cls = "STOCK_AND_SALES"
        elif in_stock and not in_sales:
            cls = "STOCK_NO_SALES"
        elif not in_stock and in_sales:
            cls = "SALES_NO_STOCK"
        else:
            # нулевой остаток без продаж — шум snapshot, не в bridge
            continue

        # sell-through proxy: sales qty / (sales qty + end qty) when both
        end_q = st["qty_end"] if st else 0.0
        sold_q = sa["qty"] if sa else 0.0
        if end_q + sold_q > 0:
            st_proxy = round(sold_q / (sold_q + end_q), 4)
        else:
            st_proxy = ""

        # channel alignment flags
        align = []
        if st and st["im_qty"] > 0 and im_s["qty"] > 0:
            align.append("IM_ALIGNED")
        if st and st["tsum_qty"] > 0 and tsum_s["qty"] > 0:
            align.append("TSUM_ALIGNED")
        if st and st["im_qty"] > 0 and im_s["qty"] == 0 and in_sales:
            align.append("IM_STOCK_SOLD_ELSEWHERE")
        if st and st["tsum_qty"] > 0 and tsum_s["qty"] == 0 and in_sales:
            align.append("TSUM_STOCK_SOLD_ELSEWHERE")
        if st and st["im_qty"] > 0 and not in_sales:
            align.append("IM_DEAD_CANDIDATE")
        if st and st["tsum_qty"] > 0 and not in_sales:
            align.append("TSUM_DEAD_CANDIDATE")

        priority = "LOW"
        if cls == "STOCK_NO_SALES" and end_q >= 3:
            priority = "HIGH"
        elif cls == "STOCK_NO_SALES" and end_q >= 1:
            priority = "MED"
        elif "IM_DEAD_CANDIDATE" in align or "TSUM_DEAD_CANDIDATE" in align:
            priority = "MED"
        elif cls == "STOCK_AND_SALES" and end_q >= 5 and st_proxy != "" and st_proxy < 0.3:
            priority = "MED"

        bridge.append(
            {
                "canonical_sku": sku,
                "name": (st["name"] if st else "") or "",
                "class": cls,
                "priority": priority,
                "stock_qty_end": round(end_q, 2),
                "stock_im_qty": round(st["im_qty"], 2) if st else 0.0,
                "stock_tsum_qty": round(st["tsum_qty"], 2) if st else 0.0,
                "stock_b2b_qty": round(st["b2b_qty"], 2) if st else 0.0,
                "warehouses": "|".join(sorted(short_wh(w) for w in st["whs"])) if st else "",
                "sales_qty": round(sold_q, 2),
                "sales_revenue_rub": round(sa["rev"], 2) if sa else 0.0,
                "sales_lines_n": sa["lines"] if sa else 0,
                "sales_channels": "|".join(sorted(sa["channels"])) if sa else "",
                "im_sales_qty": round(im_s["qty"], 2),
                "im_sales_rev_rub": round(im_s["rev"], 2),
                "tsum_sales_qty": round(tsum_s["qty"], 2),
                "tsum_sales_rev_rub": round(tsum_s["rev"], 2),
                "b2b_sales_qty": round(b2b_s["qty"], 2),
                "sellthrough_proxy": st_proxy,
                "align_flags": "|".join(align) if align else "",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    # warehouse focus rollup
    wh_focus = []
    for (sku, wh), b in by_sku_wh.items():
        ch = WH_CHANNEL.get(wh, "OTHER")
        if ch not in ("IM", "TSUM", "B2B"):
            continue
        sa_ch = sales_ch.get((sku, ch if ch != "B2B" else "B2B"), {"qty": 0.0, "rev": 0.0})
        # B2B channel key is B2B
        qe = b["qty_end"]
        sold = sa_ch["qty"]
        if qe <= 0 and sold <= 0:
            continue
        if qe > 0 and sold > 0:
            cls = "WH_STOCK_AND_CH_SALES"
        elif qe > 0:
            cls = "WH_STOCK_NO_CH_SALES"
        else:
            cls = "WH_CH_SALES_NO_STOCK"
        wh_focus.append(
            {
                "canonical_sku": sku,
                "warehouse": short_wh(wh),
                "channel_map": ch,
                "qty_end": round(qe, 2),
                "channel_sales_qty": round(sold, 2),
                "channel_sales_rev_rub": round(sa_ch["rev"], 2),
                "class": cls,
                "name": b["name"][:80],
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )

    # owner actions: HIGH dead stock on IM/TSUM
    actions = []
    for r in bridge:
        if r["priority"] not in ("HIGH", "MED"):
            continue
        if r["class"] != "STOCK_NO_SALES" and "DEAD" not in r["align_flags"]:
            if not (r["class"] == "STOCK_AND_SALES" and r["priority"] == "MED"):
                continue
        reason = []
        if r["stock_im_qty"] > 0 and r["im_sales_qty"] == 0:
            reason.append("IM_stock_no_IM_sales")
        if r["stock_tsum_qty"] > 0 and r["tsum_sales_qty"] == 0:
            reason.append("TSUM_stock_no_TSUM_sales")
        if r["class"] == "STOCK_NO_SALES":
            reason.append("no_sales_any_channel")
        if r["class"] == "STOCK_AND_SALES" and r["sellthrough_proxy"] != "" and float(r["sellthrough_proxy"]) < 0.3:
            reason.append("low_sellthrough_proxy")
        if not reason:
            continue
        actions.append(
            {
                "canonical_sku": r["canonical_sku"],
                "priority": r["priority"],
                "stock_qty_end": r["stock_qty_end"],
                "stock_im_qty": r["stock_im_qty"],
                "stock_tsum_qty": r["stock_tsum_qty"],
                "sales_qty": r["sales_qty"],
                "sales_revenue_rub": r["sales_revenue_rub"],
                "sellthrough_proxy": r["sellthrough_proxy"],
                "reason": "|".join(reason),
                "owner_ask": "Confirm markdown / move / write-off / missing sales file",
                "do_not_auto_accept": "YES",
                "so_t": "N",
            }
        )
    actions.sort(key=lambda x: (-{"HIGH": 2, "MED": 1, "LOW": 0}[x["priority"]], -float(x["stock_qty_end"])))

    # class rollup
    from collections import Counter

    cls_c = Counter(r["class"] for r in bridge)
    rollup = []
    for cls, n in cls_c.most_common():
        sub = [r for r in bridge if r["class"] == cls]
        rollup.append(
            {
                "class": cls,
                "skus_n": n,
                "stock_qty_end_sum": round(sum(float(r["stock_qty_end"]) for r in sub), 2),
                "sales_qty_sum": round(sum(float(r["sales_qty"]) for r in sub), 2),
                "sales_revenue_rub_sum": round(sum(float(r["sales_revenue_rub"]) for r in sub), 2),
                "so_t": "N",
            }
        )

    wh_cls = Counter(r["class"] for r in wh_focus)
    wh_rollup = [
        {
            "channel_map": ch,
            "rows_n": sum(1 for r in wh_focus if r["channel_map"] == ch),
            "stock_no_ch_sales_n": sum(
                1 for r in wh_focus if r["channel_map"] == ch and r["class"] == "WH_STOCK_NO_CH_SALES"
            ),
            "qty_end_no_ch_sales": round(
                sum(
                    float(r["qty_end"])
                    for r in wh_focus
                    if r["channel_map"] == ch and r["class"] == "WH_STOCK_NO_CH_SALES"
                ),
                2,
            ),
            "aligned_n": sum(
                1 for r in wh_focus if r["channel_map"] == ch and r["class"] == "WH_STOCK_AND_CH_SALES"
            ),
            "so_t": "N",
        }
        for ch in ("IM", "TSUM", "B2B")
    ]

    meta = {
        "horizon": "H75",
        "date": str(date.today()),
        "title": "Goods stock end-qty ↔ IM/TSUM channel sell-through",
        "stock_rows_n": len(stock_rows),
        "sales_rows_n": len(sales_rows),
        "bridge_skus_n": len(bridge),
        "stock_and_sales_n": cls_c.get("STOCK_AND_SALES", 0),
        "stock_no_sales_n": cls_c.get("STOCK_NO_SALES", 0),
        "sales_no_stock_n": cls_c.get("SALES_NO_STOCK", 0),
        "owner_actions_n": len(actions),
        "owner_actions_high_n": sum(1 for r in actions if r["priority"] == "HIGH"),
        "im_stock_no_ch_sales_qty": next(r["qty_end_no_ch_sales"] for r in wh_rollup if r["channel_map"] == "IM"),
        "tsum_stock_no_ch_sales_qty": next(
            r["qty_end_no_ch_sales"] for r in wh_rollup if r["channel_map"] == "TSUM"
        ),
        "no_fake_accept": True,
        "so_t": False,
        "note": "qty_end snapshot vs multi-period sales; sellthrough_proxy is indicative only",
    }

    REG.mkdir(parents=True, exist_ok=True)
    EV.mkdir(parents=True, exist_ok=True)
    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "stock_channel_bridge.csv", bridge)
    write_csv(REG / "stock_channel_class_rollup.csv", rollup)
    write_csv(REG / "stock_warehouse_channel_focus.csv", wh_focus)
    write_csv(REG / "stock_warehouse_channel_rollup.csv", wh_rollup)
    write_csv(REG / "stock_channel_owner_actions.csv", actions[:80] if actions else [{"canonical_sku": "", "priority": "", "note": "none", "so_t": "N"}])

    for name in [
        "stock_channel_bridge.csv",
        "stock_channel_class_rollup.csv",
        "stock_warehouse_channel_focus.csv",
        "stock_warehouse_channel_rollup.csv",
        "stock_channel_owner_actions.csv",
        "meta.json",
    ]:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h75_meta.json")
            shutil.copy2(src, MAPS / "h75_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    shutil.copy2(REG / "stock_channel_bridge.csv", WAVE_B / "43_stock_channel_bridge.csv")
    shutil.copy2(REG / "stock_channel_class_rollup.csv", WAVE_B / "44_stock_channel_class_rollup.csv")
    shutil.copy2(REG / "stock_warehouse_channel_rollup.csv", WAVE_B / "45_stock_warehouse_channel_rollup.csv")
    shutil.copy2(REG / "stock_channel_owner_actions.csv", WAVE_B / "46_stock_channel_owner_actions.csv")

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    print("rollup", rollup)
    print("wh_rollup", wh_rollup)
    print("top actions", actions[:5])
    return meta


if __name__ == "__main__":
    main()
