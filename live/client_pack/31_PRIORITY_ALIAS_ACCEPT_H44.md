# H44 — Приоритет: Alias Accept (DOM-PRODUCT)

**Горизонт:** H44 · **дата:** 2026-07-28  
**Зачем:** после H43 (RACI) следующий P0 по качеству маржи — **product review alias**.  
**Не делаем:** auto-ACCEPT; rewrite sales без отдельного apply; reopen H23 exceptions.

---

## Вердикт одной строкой

Из «20» в dojim реально на review **16 PENDING**; **4 уже H23 ACCEPT** (wholesale/quarantine) — SKIP. Топ-5 SKU ≈ **3.04M ₽** выручки; Accept ≠ apply на sales.

---

## Срез

| Корзина | N | Rev (mart) | Действие |
|---------|---|------------|----------|
| **PENDING review** | **16** | **6.47M** | ACCEPT / REJECT / DEFER |
| KEEP_H23 (не reopen) | 4 | — | 0-2493A/2496/2497 + 0-3243 |
| applied_to_sales сейчас | 0 | — | всё ещё **N** |

Fix types (pending): в основном **CATEGORY_MISMATCH** (+1 UNIT_RATIO T-3178).

---

## Топ-5 (P0_REVIEW_FIRST)

| Rank | SKU | Fix | Flagged lines | Revenue |
|------|-----|-----|---------------|---------|
| 1 | T-2750B | CATEGORY_MISMATCH | 15 | 1.01M |
| 2 | T-2750C | CATEGORY_MISMATCH | 7 | 0.31M |
| 3 | T-3187A | CATEGORY_MISMATCH | 6 | 0.81M |
| 4 | T-2973A | CATEGORY_MISMATCH | 5 | 0.55M |
| 5 | T-3069B | CATEGORY_MISMATCH | 5 | 0.36M |

Хинт: сверить `sale_name` vs `cost_name` → одна модель? Да = ACCEPT preferred CV; нет = REJECT.

---

## Owner actions

1. **H44-A1** — H43 CONFIRM DOM-PRODUCT (Коновалова), если ещё нет.  
2. **H44-A2** — review топ-5 по `alias_konovalova_decision_sheet.csv`.  
3. **H44-A3** — batch остальные 11 pending (SLA 10д).  
4. **H44-A4** — apply-pass только после Accept + DOM-DATA (отдельный горизонт).  
5. **H44-A5** — не трогать 4 H23 exceptions.

---

## Симуляция

| Сценарий | Эффект |
|----------|--------|
| S1 ACCEPT топ-5 | registry; sales ещё N; ~3.04M contig |
| S2 ACCEPT все 16 | registry complete |
| S3 + apply-pass | переписывает COGS/margin — только с DOM-DATA |

---

## Артефакты

| Файл | Назначение |
|------|------------|
| `live/marts/alias_konovalova_decision_sheet.csv` | **Лист решений Product** |
| `live/marts/alias_review_ranked.csv` | 16 pending + 4 skip |
| `live/marts/alias_fix_type_summary.csv` | типы |
| `live/marts/alias_accept_simulation.csv` | S0–S3 |
| `live/marts/alias_accept_owner_actions.csv` | 5 действий |
| `live/marts/alias_exceptions_keep.csv` | H23 keep |
| `live/registers/h44_alias_accept/` | регистр |
| `live/evidence/h44_alias_accept_20260728/` | evidence |

---

## Оценка

**9.2/10** для post-RACI приоритета: концентрирует Product на 5 SKU с max impact, честно отделяет уже принятое, не ломает sales.  
Связи: H43 DOM-PRODUCT → H44; G5; W3 cost versions; apply later ↔ DOM-DATA.

---

## Следующий блок

**Quarantine ЗП янв–фев 2026** (Payroll Approver / Мамушкина) — или apply-pass alias после Accept.
