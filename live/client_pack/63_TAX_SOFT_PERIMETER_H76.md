# H76 — Tax SOFT/GAP ↔ Salon UFK perimeter

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (P2 с прямым эффектом на gate TAX→27)
`recon_tax_cash_bank`: **26 CLOSE / 3 SOFT / 1 GAP**.  
До H76 казалось, что «налоги не бьются». На деле **3 из 4** дельт = платежи **Salon Sber → УФК**, которых нет в `bank_tax_like` (фильтр смотрел IP/Декор).

## Находка
| Месяц | Сейчас | Delta ₽ | Платёж Salon→УФК | Если включить в perimeter |
|-------|--------|--------:|------------------|---------------------------|
| **2024-01** | GAP | **36 000** | `56f8574ddc801765` | **CLOSE** → unlock TAX→27 |
| **2024-10** | SOFT | **147 180** | `0b9757804c39de25` | **CLOSE** |
| **2025-08** | SOFT | **77 410** | `67d44e4ba5bd8469` | **CLOSE** |
| **2026-06** | SOFT | **−30 900** | пошлина ТЗ `8de4ec31…` 76 500 в tax-like | residual после exclude (не Salon) |

Суммы дельт **точно** совпадают со строками tax_cash и с `sber_salon_tax_payments`.

## Что сделать owners
1. Подписать: **Salon→УФК входит в периметр TAX_CASH_BANK** (карточка `14_TAX_SOFT_PERIMETER_H76.csv`).  
2. 2024-01 = тот же 36k, что уже в `11_TAX_36K_EVIDENCE*` — теперь с полным контекстом soft-хвоста.  
3. 2026-06: исключить пошлину товарного знака из tax-like; остаток разобрать отдельно.  
4. **Запрет:** FORCE_CLOSE без подписи периметра.

## PDF (якоря, не месячная касса)
Extract: HIGH **14** / LOW **5** / N/A **6**.  
УСН/НДС/6-НДФЛ — годовые/квартальные обязательства; **не** равны monthly tax_cash.

## Артефакты
- Register: `live/registers/h76_tax_soft_perimeter/` (+ `build_h76.py`)
- Wave C: `30–33_tax_*`
- Sign: `sign_session_pack/14_TAX_SOFT_PERIMETER_H76.csv`
- Map: `live/maps/47_TAX_SOFT_PERIMETER_MAP.md`

## Gate
Подпись периметра на **2024-01** — прямой путь **TAX→27**. Score сам H76 не двигает.
