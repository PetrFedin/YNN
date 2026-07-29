# H52 — Недостающие карты / усиление (gap fill)

**Дата:** 2026-07-29  
**Зачем:** закрыть пробелы из инвентаря (календарь close, эквайринг IM, to-be cost МД, RACI formal↔кандидат).  
**Не делаем:** fake ACCEPT; новый forensic ради слоя.

---

## Что добавлено

| # | Артефакт | Закрывает пробел |
|---|----------|------------------|
| 1 | `ops_close_calendar.csv` | Operating close calendar |
| 2 | `im_acquiring_month_map.csv` + `im_acquiring_open_months_focus.csv` | Карта эквайринга IM |
| 3 | `md_cost_process_tobe_2026.csv` | To-be процесс cost МД 2026+ |
| 4 | `raci_formal_vs_candidate_map.csv` | As-signed vs candidate RACI |

Пути: `live/marts/` · `live/maps/` · `live/registers/h52_gap_maps/`

---

## 1. Календарь close (до 05.09)

Wave A на этой неделе → B2B/alias/реестры в августе → gate path к концу августа.  
См. `ops_close_calendar.csv` (☐ done_flag).

## 2. Эквайринг IM (6 OPEN)

| Месяц | Паттерн | POS pool | Действие |
|-------|---------|----------|----------|
| 2025-08, 2026-04 | UNDERBANKED | есть | soft-slice Accept (H46/H51) |
| 2024-08, 2025-01, 2025-10, 2026-03 | OVERBANKED | разный | **реестр**, POS не лить |

2025-01: POS_VTB в месяце **0** — surplus не лечится POS-slice.

## 3. MD cost to-be (7 шагов)

ORDER → COST до fitting → FITTING → DELIVERY (запрет без cost) → MONTH_CLOSE → PILOT_GM → OUT_OF_SCOPE 2024–25.  
KPI сейчас: salon 78.2% (цель ≥80, **26** дыр) · shop 90.5% (держать).

## 4. RACI dual

5 доменов **NEED_YANINA_CONFIRM**: PRODUCT, COST, PRODUCTION, B2B, DATA.  
CASH/BANK/TAX/PAYROLL — FORMAL_OK. Draft ФИО — в H51.

---

## Что ещё усилить после H52 (owners)

1. Подпись H51 / календарь ☐  
2. Реестры на 4 overbank  
3. Payment-level MD↔invoice (следующий data-gap, нужен ручной match)  
4. BPMN to-be / Phase C — Stage 2+, не сейчас  

---

## Оценка

**9.3/10** как gap-fill: закрывает 4 явных «не хватает карты» без шума анализа.
