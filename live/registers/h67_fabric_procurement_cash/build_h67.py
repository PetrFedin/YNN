#!/usr/bin/env python3
"""H67: fabric/procurement cash ABC — suppliers ↔ bank ↔ expense ↔ inventory.

Priority after H66: G6 working capital. Uses existing W5 suppliers + H1 bank edges
+ H64 fabric ABC. Not SoT. Does not fabricate Accept or company P&L.
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
EV = ROOT / "live/evidence/h67_fabric_procurement_cash_20260729"
WAVE_B = ROOT / "live/client_pack/execution_wave_b"
W5 = ROOT / "live/registers/w5_sup_exp_mat"
H1 = ROOT / "live/registers/h1_spine_links"

FAB_RE = re.compile(
    r"ткан|фурнит|материал|шелк|шерст|кож|атлас|креп|шифон|кружев|нитки|"
    r"текстил|textile|maritex|errepi|бархат|прикладн|петромикс|галамакс",
    re.I,
)
MONTHS_ORDER = None  # unused; keep simple


def write_csv(path: Path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def norm_name(s: str) -> str:
    s = (s or "").upper().replace("Ё", "Е")
    s = re.sub(r'^ООО\s*"?|"?$', "", s)
    s = re.sub(r"^ИП\s+", "", s)
    return re.sub(r"[^A-ZА-Я0-9]+", "", s)


def abc_rows(items: list[tuple[float, dict]], value_key: str = "_value") -> list[dict]:
    items = sorted(items, key=lambda x: -x[0])
    total = sum(v for v, _ in items) or 1.0
    cum = 0.0
    out = []
    for i, (v, row) in enumerate(items, 1):
        cum += v
        share = cum / total
        band = "A" if share <= 0.8 else ("B" if share <= 0.95 else "C")
        out.append(
            {
                **row,
                "abc_rank": i,
                "abc_value_rub": round(v, 2),
                "abc_cum_share_pct": round(100 * share, 2),
                "abc_band": band,
            }
        )
    return out


def main():
    for d in (REG, MARTS, MAPS, EV, WAVE_B):
        d.mkdir(parents=True, exist_ok=True)

    suppliers = list(csv.DictReader((W5 / "suppliers.csv").open()))
    edges = list(csv.DictReader((H1 / "sup_bank_payment_edges.csv").open()))
    expenses = [
        r
        for r in csv.DictReader((W5 / "expense_lines.csv").open())
        if r["line_class"] == "EXPENSE"
    ]
    fabric_inv = list(csv.DictReader((MARTS / "fabric_inventory_abc.csv").open()))

    # --- bank edges by supplier ---
    by_sup: dict[str, dict] = defaultdict(
        lambda: {
            "amount_rub": 0.0,
            "payments_n": 0,
            "inn": "",
            "counterparty_id": "",
            "months": set(),
            "fabric_amount_rub": 0.0,
            "fabric_payments_n": 0,
            "purposes": [],
        }
    )
    for e in edges:
        name = e["supplier_name"]
        amt = float(e["amount"] or 0)
        b = by_sup[name]
        b["amount_rub"] += amt
        b["payments_n"] += 1
        b["inn"] = e.get("inn") or b["inn"]
        b["counterparty_id"] = e.get("counterparty_id") or b["counterparty_id"]
        if e.get("period_month"):
            b["months"].add(e["period_month"])
        blob = f"{name} {e.get('purpose','')}"
        if FAB_RE.search(blob):
            b["fabric_amount_rub"] += amt
            b["fabric_payments_n"] += 1
            if len(b["purposes"]) < 3:
                b["purposes"].append((e.get("purpose") or "")[:80])

    # coverage vs procurement list
    edge_norms = {norm_name(n): n for n in by_sup}
    coverage = []
    for s in suppliers:
        nn = norm_name(s["name"])
        hit_name = None
        for en, original in edge_norms.items():
            if not nn or not en:
                continue
            if nn in en or en in nn or (len(nn) > 6 and nn[:8] in en):
                hit_name = original
                break
        bank = by_sup.get(hit_name) if hit_name else None
        coverage.append(
            {
                "supplier_name": s["name"],
                "inn": s["inn"],
                "has_inn": s["has_inn"],
                "contact": (s.get("contact") or "")[:60],
                "in_bank_edges": "Y" if bank else "N",
                "bank_supplier_name": hit_name or "",
                "bank_amount_rub": round(bank["amount_rub"], 2) if bank else "",
                "bank_fabric_amount_rub": round(bank["fabric_amount_rub"], 2) if bank else "",
                "bank_payments_n": bank["payments_n"] if bank else "",
                "coverage_status": (
                    "BANK_MATCHED"
                    if bank
                    else ("FOREIGN_OR_NO_INN" if s["has_inn"] == "N" else "LIST_ONLY_NO_BANK")
                ),
                "owner_action": (
                    "OK — bank spine linked"
                    if bank
                    else (
                        "Иностранный/без ИНН — отдельный импортный контур; не ждать РФ-выписку"
                        if s["has_inn"] == "N"
                        else "Есть в списке закупок, нет в bank edges — проверить оплату наличными/картой/другим юрлицом"
                    )
                ),
                "source_file_id": s["source_file_id"],
                "so_t": "N",
            }
        )

    # supplier bank ABC (all matched)
    all_abc = abc_rows(
        [
            (
                info["amount_rub"],
                {
                    "supplier_name": name,
                    "inn": info["inn"],
                    "counterparty_id": info["counterparty_id"],
                    "payments_n": info["payments_n"],
                    "months_n": len(info["months"]),
                    "fabric_amount_rub": round(info["fabric_amount_rub"], 2),
                    "fabric_share_pct": round(100 * info["fabric_amount_rub"] / info["amount_rub"], 1)
                    if info["amount_rub"]
                    else 0,
                    "purpose_sample": " | ".join(info["purposes"]),
                    "so_t": "N",
                },
            )
            for name, info in by_sup.items()
        ]
    )

    fabric_abc = abc_rows(
        [
            (
                info["fabric_amount_rub"],
                {
                    "supplier_name": name,
                    "inn": info["inn"],
                    "fabric_payments_n": info["fabric_payments_n"],
                    "all_payments_amount_rub": round(info["amount_rub"], 2),
                    "purpose_sample": " | ".join(info["purposes"]),
                    "so_t": "N",
                },
            )
            for name, info in by_sup.items()
            if info["fabric_amount_rub"] > 0
        ]
    )

    # expense fabric articles
    fab_exp = defaultdict(lambda: {"amount_rub": 0.0, "lines_n": 0, "months": set()})
    for r in expenses:
        if FAB_RE.search(r["article_name"] or ""):
            fab_exp[r["article_name"]]["amount_rub"] += float(r["amount_rub"] or 0)
            fab_exp[r["article_name"]]["lines_n"] += 1
            fab_exp[r["article_name"]]["months"].add(r["period_month"])
    exp_abc = abc_rows(
        [
            (
                v["amount_rub"],
                {
                    "expense_article": name,
                    "lines_n": v["lines_n"],
                    "months_n": len(v["months"]),
                    "so_t": "N",
                    "note": "Opex article from Расходы — not invoice-level supplier",
                },
            )
            for name, v in fab_exp.items()
        ]
    )

    # inventory A-band summary (from H64)
    inv_a = [r for r in fabric_inv if r.get("abc_band") == "A"]
    inv_total = sum(float(r.get("abc_value_rub") or 0) for r in fabric_inv)
    inv_a_total = sum(float(r.get("abc_value_rub") or 0) for r in inv_a)

    bank_fab_total = sum(float(r["abc_value_rub"]) for r in fabric_abc)
    exp_fab_total = sum(float(r["abc_value_rub"]) for r in exp_abc)
    bank_all_total = sum(float(r["abc_value_rub"]) for r in all_abc)

    bridge = [
        {
            "metric": "procurement_list_n",
            "value": len(suppliers),
            "unit": "count",
            "note": "Список контрагентов по закупке",
        },
        {
            "metric": "procurement_with_bank_edge_n",
            "value": sum(1 for r in coverage if r["in_bank_edges"] == "Y"),
            "unit": "count",
            "note": "Name-matched to H1 supplier↔bank edges",
        },
        {
            "metric": "procurement_list_only_n",
            "value": sum(1 for r in coverage if r["coverage_status"] == "LIST_ONLY_NO_BANK"),
            "unit": "count",
            "note": "Need payment path check",
        },
        {
            "metric": "procurement_foreign_or_no_inn_n",
            "value": sum(1 for r in coverage if r["coverage_status"] == "FOREIGN_OR_NO_INN"),
            "unit": "count",
            "note": "Import contour — expected no RF bank edge",
        },
        {
            "metric": "bank_matched_suppliers_n",
            "value": len(all_abc),
            "unit": "count",
            "note": "Unique suppliers in bank edges",
        },
        {
            "metric": "bank_matched_suppliers_rub",
            "value": round(bank_all_total, 2),
            "unit": "RUB",
            "note": "All matched supplier payments (not fabric-only)",
        },
        {
            "metric": "bank_fabric_like_rub",
            "value": round(bank_fab_total, 2),
            "unit": "RUB",
            "note": "Purpose/name heuristic fabric|textile|fur|materials",
        },
        {
            "metric": "expense_fabric_articles_rub",
            "value": round(exp_fab_total, 2),
            "unit": "RUB",
            "note": "Расходы articles matching ткань/фурнитура (mgmt class, not invoices)",
        },
        {
            "metric": "expense_vs_bank_fabric_delta_rub",
            "value": round(exp_fab_total - bank_fab_total, 2),
            "unit": "RUB",
            "note": "Positive ⇒ opex class > fabric-tagged bank; expected (cash vs class, FX, card)",
        },
        {
            "metric": "fabric_inventory_total_rub",
            "value": round(inv_total, 2),
            "unit": "RUB",
            "note": "H64 snapshot 2026-05-31 filtered",
        },
        {
            "metric": "fabric_inventory_A_band_rub",
            "value": round(inv_a_total, 2),
            "unit": "RUB",
            "note": f"A-band n={len(inv_a)} — WC watch",
        },
        {
            "metric": "do_not_mix_contours",
            "value": 1,
            "unit": "flag",
            "note": "Inventory ₽ ≠ goods stock qty ≠ company P&L",
        },
    ]

    # owner actions ranked
    owner_actions = []
    # top A fabric bank payees
    for r in fabric_abc:
        if r["abc_band"] != "A":
            continue
        owner_actions.append(
            {
                "priority_band": "P1_WATCH",
                "action_type": "FABRIC_SUPPLIER_A_BAND",
                "subject": r["supplier_name"],
                "amount_rub": r["abc_value_rub"],
                "action": "Держать в WC-watch: A-band тканевый payee по банку",
                "artifact": "26_fabric_supplier_bank_abc.csv",
                "so_t": "N",
            }
        )
    for r in coverage:
        if r["coverage_status"] == "LIST_ONLY_NO_BANK":
            owner_actions.append(
                {
                    "priority_band": "P1_CHECK",
                    "action_type": "SUPPLIER_NO_BANK",
                    "subject": r["supplier_name"],
                    "amount_rub": "",
                    "action": r["owner_action"],
                    "artifact": "28_procurement_bank_coverage.csv",
                    "so_t": "N",
                }
            )
    owner_actions.append(
        {
            "priority_band": "P0_CONTEXT",
            "action_type": "DELTA_EXPENSE_VS_BANK",
            "subject": "ткани/фурнитура",
            "amount_rub": round(exp_fab_total - bank_fab_total, 2),
            "action": "Не закрывать delta как ошибку — разные контуры (класс расходов vs bank purpose). Использовать для запросов, не для P&L.",
            "artifact": "27_fabric_cash_bridge_metrics.csv",
            "so_t": "N",
        }
    )

    # refresh person cards: append procurement note for Янина/закупки owner if file exists
    person_cards = list(csv.DictReader((MARTS / "person_action_cards.csv").open()))
    # add/replace a procurement WC card
    person_cards = [r for r in person_cards if "H67" not in (r.get("actions") or "")]
    person_cards.append(
        {
            "person": "Янина / закупки",
            "minutes": "20",
            "wave": "B",
            "actions": "H67: сверить LIST_ONLY_NO_BANK поставщиков + A-band тканевых payees; не смешивать с goods P&L",
            "artifact": "execution_wave_b/29_fabric_procurement_owner_actions.csv",
            "blocks_if_skip": "WC тканей без cash-owner",
        }
    )

    meta = {
        "horizon": "H67",
        "date": str(date.today()),
        "title": "Fabric/procurement cash ABC + coverage",
        "suppliers_list_n": len(suppliers),
        "bank_edges_n": len(edges),
        "bank_suppliers_n": len(all_abc),
        "bank_fabric_suppliers_n": len(fabric_abc),
        "bank_fabric_rub": round(bank_fab_total, 2),
        "expense_fabric_rub": round(exp_fab_total, 2),
        "inventory_total_rub": round(inv_total, 2),
        "inventory_A_rub": round(inv_a_total, 2),
        "coverage_matched_n": sum(1 for r in coverage if r["in_bank_edges"] == "Y"),
        "coverage_list_only_n": sum(1 for r in coverage if r["coverage_status"] == "LIST_ONLY_NO_BANK"),
        "coverage_foreign_n": sum(1 for r in coverage if r["coverage_status"] == "FOREIGN_OR_NO_INN"),
        "no_fake_accept": True,
        "so_t": False,
    }

    (REG / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(REG / "suppliers_master.csv", list(suppliers[0].keys()), suppliers)
    write_csv(REG / "supplier_bank_abc.csv", list(all_abc[0].keys()), all_abc)
    write_csv(REG / "fabric_supplier_bank_abc.csv", list(fabric_abc[0].keys()), fabric_abc)
    write_csv(REG / "fabric_expense_abc.csv", list(exp_abc[0].keys()) if exp_abc else ["expense_article"], exp_abc)
    write_csv(REG / "fabric_cash_bridge_metrics.csv", list(bridge[0].keys()), bridge)
    write_csv(REG / "procurement_bank_coverage.csv", list(coverage[0].keys()), coverage)
    write_csv(REG / "fabric_procurement_owner_actions.csv", list(owner_actions[0].keys()), owner_actions)
    write_csv(REG / "person_action_cards_h67.csv", list(person_cards[0].keys()), person_cards)

    for name in [
        "suppliers_master.csv",
        "supplier_bank_abc.csv",
        "fabric_supplier_bank_abc.csv",
        "fabric_expense_abc.csv",
        "fabric_cash_bridge_metrics.csv",
        "procurement_bank_coverage.csv",
        "fabric_procurement_owner_actions.csv",
        "meta.json",
    ]:
        src = REG / name
        if name == "meta.json":
            shutil.copy2(src, MARTS / "h67_meta.json")
            shutil.copy2(src, MAPS / "h67_meta.json")
            shutil.copy2(src, EV / "meta.json")
        else:
            shutil.copy2(src, MARTS / name)
            shutil.copy2(src, MAPS / name)
            shutil.copy2(src, EV / name)

    # update live person_action_cards
    write_csv(MARTS / "person_action_cards.csv", list(person_cards[0].keys()), person_cards)
    write_csv(WAVE_B / "08_person_action_cards.csv", list(person_cards[0].keys()), person_cards)

    shutil.copy2(REG / "suppliers_master.csv", WAVE_B / "26_suppliers_master.csv")
    shutil.copy2(REG / "fabric_supplier_bank_abc.csv", WAVE_B / "27_fabric_supplier_bank_abc.csv")
    shutil.copy2(REG / "procurement_bank_coverage.csv", WAVE_B / "28_procurement_bank_coverage.csv")
    shutil.copy2(REG / "fabric_procurement_owner_actions.csv", WAVE_B / "29_fabric_procurement_owner_actions.csv")
    shutil.copy2(REG / "fabric_cash_bridge_metrics.csv", WAVE_B / "30_fabric_cash_bridge_metrics.csv")

    print(json.dumps(meta, ensure_ascii=False, indent=2))
    print("TOP fabric bank A:")
    for r in fabric_abc[:8]:
        if r["abc_band"] == "A":
            print(r["abc_band"], r["abc_value_rub"], r["supplier_name"])


if __name__ == "__main__":
    main()
