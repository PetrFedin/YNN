#!/usr/bin/env python3
"""H83: HR policy ↔ штатка ↔ payroll streams (P2).

Связывает Положение об оплате + Приложение 1 с roster (штатка) и фактом выплат
(w2 payroll_lines 2026 + designers/shop). Не SoT. Не auto-Accept.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REG = Path(__file__).resolve().parent
MARTS = ROOT / "live/marts"
W2 = ROOT / "live/registers/w2_payroll"
DL = Path("/Users/petr/Downloads/YANINA документы")

# Ожидаемая система оплаты по ключевым словам роли (из Положения).
POLICY_TIME = [  # повременная / оклад
    "управляющ", "исполнительн", "главн бухгал", "бухгалтер", "операцион",
    "дизайнер одежд", "дизайнер им", "товаровед", "завсклад", "заведующ склад",
    "закройщик", "художник по вышив", "помощник худож", "дизайнер-программист",
    "руководитель проект", "инженер-конструктор", "конфикционер",
    "технолог", "портной-лабора", "снабжен", "охрана", "эксплуатац",
    "маркировк", "проектная помощь", "уборщ",
]
POLICY_SALARY_BONUS = [  # окладно-премиальная
    "вышивальщ", "конструктор", "оператор машинной вышив",
    "менеджер по развит", "менеджер по работе с клиент", "менеджер по продаж",
]
POLICY_PIECE = [  # сдельно-премиальная
    "портн", "мастер", "цех",
]

GROUP_TO_POLICY = {
    "SALARY": "TIME_SALARY",
    "EMBROIDERY": "SALARY_BONUS",
    "DESIGNERS": "SALARY_BONUS",
    "MASTERS": "PIECE_BONUS",
}

POLICY_OPEN_ITEMS = [
    {
        "item_id": "POL-OPEN-01",
        "topic": "наставничество доплата",
        "status": "BLANK_ON_DISCUSSION",
        "evidence": "Положение: размер и условия — НА ОБСУЖДЕНИЕ!!!",
        "owner_hint": "Сливяк + Янина",
        "priority": "P1",
    },
    {
        "item_id": "POL-OPEN-02",
        "topic": "совмещение / расширение зоны — размер доплаты",
        "status": "BLANK_ON_DISCUSSION",
        "evidence": "Положение: РАЗМЕР!!! НА ОБСУЖДЕНИЕ!!!",
        "owner_hint": "Сливяк + Мамушкина",
        "priority": "P1",
    },
    {
        "item_id": "POL-OPEN-03",
        "topic": "командировки лимиты (проезд/жильё/суточные)",
        "status": "BLANK_ON_DISCUSSION",
        "evidence": "Положение: поля пустые + НА ОБСУЖДЕНИЕ!!!",
        "owner_hint": "Мамушкина",
        "priority": "P2",
    },
    {
        "item_id": "POL-FIXED-01",
        "topic": "проезд дом↔работа",
        "status": "FIXED_IN_POLICY",
        "evidence": "3500 ₽/мес с учётом факт. дней",
        "owner_hint": "Сливяк (свод)",
        "priority": "P2",
    },
    {
        "item_id": "POL-FIXED-02",
        "topic": "график выплат",
        "status": "FIXED_IN_POLICY",
        "evidence": "20-е = 40%; 5-е след. месяца = 60%; карта",
        "owner_hint": "Сливяк",
        "priority": "P2",
    },
    {
        "item_id": "POL-APP1-01",
        "topic": "сдельные расценки (Приложение 1)",
        "status": "EXISTS_FABRIC_GROUPS",
        "evidence": "группы материалов I–… + расценки для портных",
        "owner_hint": "Мокеева / цех",
        "priority": "P2",
    },
]


def norm_fio(s: str) -> str:
    s = re.sub(r"\s+", " ", (s or "").strip())
    s = s.replace("ё", "е").replace("Ё", "Е")
    return s.upper()


def fio_key(s: str) -> str:
    parts = norm_fio(s).replace(".", " ").split()
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0].lower()
    return f"{parts[0].lower()}|{parts[1][:1].lower()}"


def expected_policy(role: str, section: str = "") -> str:
    blob = f"{role} {section}".lower().replace("ё", "е")
    for k in POLICY_PIECE:
        if k in blob:
            return "PIECE_BONUS"
    for k in POLICY_SALARY_BONUS:
        if k in blob:
            return "SALARY_BONUS"
    for k in POLICY_TIME:
        if k in blob:
            return "TIME_SALARY"
    # section fallbacks
    if "вышив" in blob:
        return "SALARY_BONUS"
    if "конструктор" in blob:
        return "SALARY_BONUS"
    if "мастер" in blob:
        return "PIECE_BONUS"
    if "ауп" in blob or "оклад" in blob:
        return "TIME_SALARY"
    return "UNKNOWN"


def policy_vs_group(expected: str, groups: set[str]) -> str:
    if not groups:
        return "NO_PAY_2026"
    mapped = {GROUP_TO_POLICY.get(g, "UNKNOWN") for g in groups}
    if expected == "UNKNOWN":
        return "POLICY_UNKNOWN"
    if expected in mapped:
        return "ALIGN"
    # soft: DESIGNERS file vs CONSTRUCTOR role etc.
    if expected == "SALARY_BONUS" and mapped & {"SALARY_BONUS", "TIME_SALARY"}:
        return "SOFT_ALIGN"
    if expected == "TIME_SALARY" and "TIME_SALARY" in mapped:
        return "ALIGN"
    if expected == "PIECE_BONUS" and ("PIECE_BONUS" in mapped or "TIME_SALARY" in mapped):
        # мастера иногда в monthly MASTERS и/или цех
        return "SOFT_ALIGN" if "PIECE_BONUS" in mapped else "MISMATCH"
    return "MISMATCH"


def wcsv(path: Path, rows: list[dict]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def load_policy_excerpt() -> str:
    """Короткий excerpt Положения через textutil (macOS)."""
    candidates = list(DL.glob("Положение об оплате*.doc"))
    if not candidates:
        return ""
    try:
        out = subprocess.check_output(
            ["textutil", "-convert", "txt", "-stdout", str(candidates[0])],
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out[:2500]
    except Exception:
        return ""


def main() -> None:
    REG.mkdir(parents=True, exist_ok=True)
    MARTS.mkdir(parents=True, exist_ok=True)

    shtatka = list(csv.DictReader(open(MARTS / "contracts_shtatka_coverage.csv")))
    lines = list(csv.DictReader(open(W2 / "payroll_lines.csv")))
    lines_2026 = [l for l in lines if (l.get("accrual_month") or "").startswith("2026")]

    # designers + shop as extra streams (2026)
    designers = list(csv.DictReader(open(MARTS / "designer_kpi_monthly.csv")))
    shop = list(csv.DictReader(open(MARTS / "shop_pay_totals.csv")))

    pay_agg: dict[str, dict] = {}
    for l in lines_2026:
        k = l.get("fio_key") or fio_key(l.get("fio", ""))
        if not k:
            continue
        a = pay_agg.setdefault(
            k,
            {
                "fio_sample": l.get("fio", ""),
                "months": set(),
                "groups": set(),
                "gross_sum": 0.0,
                "card_sum": 0.0,
                "cash_sum": 0.0,
                "lines_n": 0,
                "sources": {"MONTHLY_ZP"},
            },
        )
        a["months"].add(l["accrual_month"])
        a["groups"].add(l.get("group") or "")
        a["gross_sum"] += float(l.get("gross_accrual") or 0)
        a["card_sum"] += float(l.get("card_amount") or 0)
        a["cash_sum"] += float(l.get("cash_amount") or 0)
        a["lines_n"] += 1

    for d in designers:
        if not (d.get("period_month") or "").startswith("2026"):
            continue
        k = fio_key(d.get("constructor_full") or d.get("constructor_surname") or "")
        if not k:
            continue
        a = pay_agg.setdefault(
            k,
            {
                "fio_sample": d.get("constructor_full") or d.get("constructor_surname"),
                "months": set(),
                "groups": set(),
                "gross_sum": 0.0,
                "card_sum": 0.0,
                "cash_sum": 0.0,
                "lines_n": 0,
                "sources": set(),
            },
        )
        a["months"].add(d["period_month"])
        a["groups"].add("DESIGNERS")
        a["gross_sum"] += float(d.get("pay_net_rub") or 0)
        a["lines_n"] += 1
        a["sources"].add("DESIGNERS_KPI")

    for s in shop:
        if not (s.get("period_month") or "").startswith("2026"):
            continue
        k = fio_key(s.get("tailor_full") or s.get("tailor_surname") or "")
        if not k:
            continue
        a = pay_agg.setdefault(
            k,
            {
                "fio_sample": s.get("tailor_full") or s.get("tailor_surname"),
                "months": set(),
                "groups": set(),
                "gross_sum": 0.0,
                "card_sum": 0.0,
                "cash_sum": 0.0,
                "lines_n": 0,
                "sources": set(),
            },
        )
        a["months"].add(s["period_month"])
        a["groups"].add("MASTERS")
        a["gross_sum"] += float(s.get("pay_total_rub") or 0)
        a["lines_n"] += 1
        a["sources"].add("SHOP_PORTN")

    sht_by_key = {}
    for p in shtatka:
        sht_by_key[fio_key(p["fio"])] = p

    people_rows = []
    # 1) everyone in shtatka
    seen = set()
    for p in shtatka:
        k = fio_key(p["fio"])
        seen.add(k)
        pay = pay_agg.get(k)
        groups = pay["groups"] if pay else set()
        expected = expected_policy(p.get("role", ""), p.get("section", ""))
        align = policy_vs_group(expected, groups)
        unformal = p.get("employment_flag") == "UNFORMAL"
        paid = bool(pay)
        if unformal and paid:
            risk = "HIGH_UNFORMAL_PAID"
        elif unformal and not paid:
            risk = "MED_UNFORMAL_NO_PAY"
        elif paid and not unformal:
            risk = "OK_FORMAL_PAID" if align in ("ALIGN", "SOFT_ALIGN") else "MED_POLICY_MISMATCH"
        elif not paid:
            risk = "LOW_SHTATKA_ONLY"
        else:
            risk = "REVIEW"
        people_rows.append(
            {
                "fio": p["fio"],
                "fio_key": k,
                "in_shtatka": "YES",
                "shtatka_role": p.get("role", ""),
                "shtatka_section": p.get("section", ""),
                "employment_flag": p.get("employment_flag", ""),
                "policy_expected": expected,
                "in_payroll_2026": "YES" if paid else "NO",
                "pay_groups": "|".join(sorted(g for g in groups if g)),
                "pay_sources": "|".join(sorted(pay["sources"])) if pay else "",
                "months_n": len(pay["months"]) if pay else 0,
                "months": "|".join(sorted(pay["months"])) if pay else "",
                "gross_sum_2026_rub": round(pay["gross_sum"], 2) if pay else 0.0,
                "policy_vs_pay": align,
                "risk_flag": risk,
                "raci_mentioned": p.get("mentioned_in_finance_raci", ""),
                "do_not_auto_accept": "YES",
            }
        )

    # 2) payroll-only (not in shtatka)
    for k, pay in pay_agg.items():
        if k in seen:
            continue
        groups = pay["groups"]
        # infer expected from groups
        mapped = {GROUP_TO_POLICY.get(g, "UNKNOWN") for g in groups}
        expected = next(iter(mapped)) if len(mapped) == 1 else "MIXED"
        people_rows.append(
            {
                "fio": pay["fio_sample"],
                "fio_key": k,
                "in_shtatka": "NO",
                "shtatka_role": "",
                "shtatka_section": "FROM_PAYROLL_ONLY",
                "employment_flag": "MISSING_IN_SHTATKA",
                "policy_expected": expected,
                "in_payroll_2026": "YES",
                "pay_groups": "|".join(sorted(g for g in groups if g)),
                "pay_sources": "|".join(sorted(pay["sources"])),
                "months_n": len(pay["months"]),
                "months": "|".join(sorted(pay["months"])),
                "gross_sum_2026_rub": round(pay["gross_sum"], 2),
                "policy_vs_pay": "PAYROLL_NOT_IN_ROSTER",
                "risk_flag": "MED_PAY_WITHOUT_SHTATKA",
                "raci_mentioned": "NO",
                "do_not_auto_accept": "YES",
            }
        )

    # risk rollup
    risk_counts = defaultdict(int)
    for r in people_rows:
        risk_counts[r["risk_flag"]] += 1

    # unformal paid detail (P0-ish compliance for owners, not gate)
    unformal_paid = [r for r in people_rows if r["risk_flag"] == "HIGH_UNFORMAL_PAID"]
    unformal_paid.sort(key=lambda x: -float(x["gross_sum_2026_rub"]))

    # stream rollup: policy system × pay group
    stream_rows = []
    for expected in ("TIME_SALARY", "SALARY_BONUS", "PIECE_BONUS", "UNKNOWN", "MIXED"):
        sub = [r for r in people_rows if r["policy_expected"] == expected]
        paid = [r for r in sub if r["in_payroll_2026"] == "YES"]
        stream_rows.append(
            {
                "policy_system": expected,
                "people_n": len(sub),
                "paid_2026_n": len(paid),
                "unformal_n": sum(1 for r in sub if r["employment_flag"] == "UNFORMAL"),
                "unformal_paid_n": sum(1 for r in sub if r["risk_flag"] == "HIGH_UNFORMAL_PAID"),
                "gross_sum_2026_rub": round(sum(float(r["gross_sum_2026_rub"]) for r in paid), 2),
                "align_n": sum(1 for r in sub if r["policy_vs_pay"] == "ALIGN"),
                "mismatch_n": sum(1 for r in sub if r["policy_vs_pay"] == "MISMATCH"),
                "payroll_not_roster_n": sum(1 for r in sub if r["policy_vs_pay"] == "PAYROLL_NOT_IN_ROSTER"),
                "linked_artifacts": {
                    "TIME_SALARY": "ЗП monthly!окладники + RACI ФОТ Сливяк",
                    "SALARY_BONUS": "вышивальщицы + зп_конструкторы (H73) + Прил.1 частично",
                    "PIECE_BONUS": "ЗП_ЦЕХ portn (H74) + Приложение 1 расценки",
                    "UNKNOWN": "уточнить роль в штатке/Положении",
                    "MIXED": "несколько групп выплат",
                }.get(expected, ""),
            }
        )

    # month quality reminder (from existing mart)
    month_q = []
    mq_path = MARTS / "payroll_2026_month_quality.csv"
    if mq_path.exists():
        month_q = list(csv.DictReader(open(mq_path)))

    actions = [
        {
            "priority": "P1",
            "action_id": "H83-A1",
            "what": f"Разбор UNFORMAL+paid 2026: {len(unformal_paid)} чел / "
            f"~{round(sum(float(r['gross_sum_2026_rub']) for r in unformal_paid)/1e6, 2)}M ₽",
            "who": "Сливяк + Мамушкина",
            "evidence": "hr_unformal_paid_2026.csv",
            "why": "compliance + корректность ФОТ/6-НДФЛ контура",
            "gate_delta": "0 (не score; риск Stage1)",
        },
        {
            "priority": "P1",
            "action_id": "H83-A2",
            "what": "Закрыть бланки Положения: наставничество / совмещение / командировки",
            "who": "Янина + Сливяк",
            "evidence": "hr_policy_open_items.csv",
            "why": "локальный акт неполный → споры при Wave B HR",
            "gate_delta": "0",
        },
        {
            "priority": "P1",
            "action_id": "H83-A3",
            "what": "Сверить payroll-only vs штатка (нет в roster, есть выплаты)",
            "who": "Сливяк",
            "evidence": "hr_people_bridge.csv risk=MED_PAY_WITHOUT_SHTATKA",
            "why": "roster drift; мешает RACI/owner checks",
            "gate_delta": "0",
        },
        {
            "priority": "P2",
            "action_id": "H83-A4",
            "what": "Не снимать quarantine янв/фев 2026 ЗП (#REF!) до фикса Distribution",
            "who": "Сливяк",
            "evidence": "payroll_quarantine_p0_jan_feb.csv",
            "why": "lines_vs_dds WIDE_GAP; person-level не SoT",
            "gate_delta": "0",
        },
        {
            "priority": "P2",
            "action_id": "H83-A5",
            "what": "Сдельные: Прил.1 ↔ ЗП_ЦЕХ (H74) — выборочный контроль топ портных",
            "who": "Мокеева",
            "evidence": "hr_policy_stream_rollup.csv PIECE_BONUS",
            "why": "policy↔факт для цеха",
            "gate_delta": "0",
        },
    ]

    # coverage summary card
    summary = [
        {
            "metric": "shtatka_people",
            "value": len(shtatka),
            "note": "H82 roster",
        },
        {
            "metric": "shtatka_unformal",
            "value": sum(1 for p in shtatka if p["employment_flag"] == "UNFORMAL"),
            "note": "employment flag",
        },
        {
            "metric": "unformal_paid_2026",
            "value": len(unformal_paid),
            "note": "HIGH risk",
        },
        {
            "metric": "unformal_paid_gross_2026_rub",
            "value": round(sum(float(r["gross_sum_2026_rub"]) for r in unformal_paid), 2),
            "note": "indicative sum across streams",
        },
        {
            "metric": "payroll_people_2026",
            "value": len(pay_agg),
            "note": "monthly+designers+shop keys",
        },
        {
            "metric": "payroll_not_in_shtatka",
            "value": sum(1 for r in people_rows if r["in_shtatka"] == "NO"),
            "note": "roster gap",
        },
        {
            "metric": "shtatka_not_paid_2026",
            "value": sum(1 for r in people_rows if r["in_shtatka"] == "YES" and r["in_payroll_2026"] == "NO"),
            "note": "may be left / unpaid / other LE",
        },
        {
            "metric": "policy_mismatch",
            "value": sum(1 for r in people_rows if r["policy_vs_pay"] == "MISMATCH"),
            "note": "expected system vs pay group",
        },
        {
            "metric": "payroll_lines_2026",
            "value": len(lines_2026),
            "note": "w2 monthly sheets only",
        },
    ]

    wcsv(MARTS / "hr_people_bridge.csv", people_rows)
    wcsv(MARTS / "hr_unformal_paid_2026.csv", unformal_paid)
    wcsv(MARTS / "hr_policy_stream_rollup.csv", stream_rows)
    wcsv(MARTS / "hr_policy_open_items.csv", POLICY_OPEN_ITEMS)
    wcsv(MARTS / "hr_payroll_owner_actions.csv", actions)
    wcsv(MARTS / "hr_bridge_summary.csv", summary)

    for name in [
        "hr_people_bridge.csv",
        "hr_unformal_paid_2026.csv",
        "hr_policy_stream_rollup.csv",
        "hr_policy_open_items.csv",
        "hr_payroll_owner_actions.csv",
        "hr_bridge_summary.csv",
    ]:
        (REG / name).write_text((MARTS / name).read_text(encoding="utf-8"), encoding="utf-8")

    excerpt = load_policy_excerpt()
    meta = {
        "hypothesis": "H83",
        "title": "hr_policy_shtatka_payroll_bridge",
        "do_not_auto_accept": True,
        "not_sot": True,
        "gate": "18/30",
        "sources": {
            "policy": "Положение об оплате труда и премировании в ИП Янина.doc",
            "appendix": "Приложение 1 к положению.docx",
            "shtatka": "Штатка ИП.xlsx (via H82)",
            "payroll_lines": "w2_payroll/payroll_lines.csv",
            "designers": "designer_kpi_monthly.csv (H73)",
            "shop": "shop_pay_totals.csv (H74)",
        },
        "risk_counts": dict(risk_counts),
        "summary": {r["metric"]: r["value"] for r in summary},
        "month_quality_note": "jan/feb 2026 quarantine (#REF!) — person totals indicative",
        "policy_excerpt_chars": len(excerpt),
    }
    (MARTS / "h83_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (REG / "h83_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    if excerpt:
        (REG / "policy_excerpt.txt").write_text(excerpt, encoding="utf-8")

    print(json.dumps(meta["summary"], ensure_ascii=False, indent=2))
    print("risk", meta["risk_counts"])
    print("top unformal paid:")
    for r in unformal_paid[:8]:
        print(f"  {r['fio']}: {r['gross_sum_2026_rub']} | {r['pay_groups']} | {r['shtatka_role']}")


if __name__ == "__main__":
    main()
