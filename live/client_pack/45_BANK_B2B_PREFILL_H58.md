# H58 — BANK card prefill + B2B worksheet + коррекция dekor

**Дата:** 2026-07-29  
**Зачем:** следующий data-gap после H57 — карточные строки для BANK↔DDS и единый B2B confirm-лист; плюс правка acquiring map.  
**Не делаем:** fake ACCEPT alt-view / auto-link B2B.

---

## 1. Коррекция IM acquiring (dekor)

В open-focus и `im_acquiring_month_map_corrected.csv`:
- 2024-08 / 2025-10: «dekor_inflow» = **аренда INTERNAL**, не эквайринг  
- Добавлены `dekor_rent_internal_rub`, `acq_pool_ex_dekor_rent_rub`, `dekor_note`  
- Primary `im_acquiring_open_months_focus.csv` обновлён

## 2. BANK card → DDS prefill (**89** строк)

| Месяц | Строк | ₽ | Match matrix | ex-card gate |
|-------|-------|---|--------------|--------------|
| 2024-01 | 18 | 667 396 | Y | CLOSE |
| 2024-06 | 15 | 493 671 | Y | SOFT |
| 2024-12 | 12 | 886 166 | Y | SOFT |
| 2026-02 | 6 | 39 498 | Y | всё ещё WIDE (не карта) |
| 2026-06 | 38 | 102 929 | Y | нужен файл ДДС |

Wave C: `04_bank_card_dds_map_prefill.csv` · `05_…summary` · `06_…policy_draft`  
Owner: `dds_article_filled` **или** подпись draft policy core−card.

## 3. B2B collect confirm worksheet

6 документов топ-3 + bank hypothesis IDs + script + outcome fields.  
Wave B: `10_b2b_collect_confirm_worksheet.csv`  
`do_not_auto_accept=YES`.

---

## Оценка

**9.5/10**: закрывает BANK/B2B data-prep и чинит dekor в SoT-adjacent map без Accept.
