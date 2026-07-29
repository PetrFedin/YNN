# H57 — Prefill реестров (усиление данными)

**Дата:** 2026-07-29  
**Зачем:** owners просили «реестры» — пустой шаблон слабый. Предзаполнили **48 строк** bank payments по 4 OVERBANK месяцам + worksheet bank lines для топ-5 MD surname.  
**Не делаем:** Accept / auto maps_to_channel=IM.

---

## 1. Overbank register prefill

| Месяц | Строк | POS match | TBank match | Важно |
|-------|-------|-----------|-------------|--------|
| 2024-08 | 8 | Y | Y | «Декор 180k» = **аренда** INTERNAL, не эквайринг |
| 2025-01 | 11 | Y (0) | Y | POS=0 — только TBank |
| 2025-10 | 14 | Y | Y | «Декор 90k» = **аренда** INTERNAL |
| 2026-03 | 15 | Y | Y | POS pool большой — не лить в IM |

Файлы:
- `im_overbank_register_prefill_all.csv`
- `im_overbank_register_prefill_YYYY-MM.csv`
- `im_overbank_prefill_summary.csv`
- в Wave A: `12_*` / `13_*`

Owner fills: `maps_to_channel`, `im_share_rub`, `other_*`.  
Forbidden: `ADD_POS_TO_IM` на OVERBANK.

### Находка (коррекция H52)
`dekor_inflow` в acquiring map для 2024-08/2025-10 = платежи аренды ООО Декор → Салон (`INTERNAL`), **не** эквайринг IM. В prefill помечены `DEKOR_INTERNAL_RENT`.

---

## 2. MD invoice top-5 bank lines

`md_invoice_top5_bank_lines.csv` — 11 bank hits по Кулишова/Ахмедова/Сейдак/Седых/Коган.  
Owner: проставить `md_order_id_filled` + `link_strength` (R1–R6). Не Accept.

Wave A: `14_md_invoice_top5_bank_lines.csv`

---

## Оценка

**9.4/10**: первый data-prefill поверх WO — снимает ручной поиск выписки; честно чинит dekor-артефакт.
