# 11 — Помесячная карта качества (gate & gaps)

Updated: 2026-07-27  
Источники: `live/marts/release_gate_month.csv`, `release_gate_fails.csv`, `domain_gap_board.csv`

---

## 1. Сводка

| Verdict | Месяцев |
|---------|--------:|
| RELEASED | **18** |
| BLOCKED | **12** |

Fail controls (строк fails=14): IM_ACQ_COMBO **6** · BANK_DDS_CORE **5** · TSUM_NET_MODEL **2** · TAX_CASH_BANK **1**

---

## 2. BLOCKED месяцы — что ломает

| Месяц | Fail controls | Типовой смысл |
|-------|---------------|---------------|
| 2024-01 | BANK_DDS + TAX | WIDE_GAP касса + налоговый GAP |
| 2024-06 | BANK_DDS | WIDE_GAP |
| 2024-08 | IM_ACQ | OPEN эквайринг |
| 2024-12 | BANK_DDS | WIDE_GAP |
| 2025-01 | IM_ACQ | OPEN эквайринг |
| 2025-08 | IM_ACQ | OPEN эквайринг |
| 2025-10 | IM_ACQ | OPEN эквайринг |
| 2026-02 | BANK_DDS | WIDE_GAP |
| 2026-03 | IM_ACQ | OPEN эквайринг |
| 2026-04 | IM_ACQ | OPEN эквайринг |
| 2026-05 | TSUM_NET | OPEN net-rate модель |
| 2026-06 | TSUM_NET + BANK_DDS | OPEN net-rate + **BANK_ONLY** (нет июня в ДДС) |

---

## 3. Domain gap board (14 тикетов)

Все с owner **Сливяк** (ACCEPTED domain), priority P1:

- BANK_DDS WIDE_GAP ×4 (+ BANK_ONLY ×1)  
- IM_ACQ OPEN ×6  
- TSUM_NET OPEN ×2  
- TAX GAP ×1  

Это **операционный backlog закрытия месяцев**, не список «убытков».

---

## 4. Как использовать

1. Перед цитированием месяца — `verdict` в gate.  
2. Если BLOCKED — указать `fail_controls` и owner.  
3. Закрытие S1 = закрытие этих 14 fails, не новый отчёт.
