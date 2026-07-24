# H29 — Канал МД / индивидуальный пошив

Updated: 2026-07-24 19:35

## Зачем
Бриф: 83% выручки — услуги инд.пошива. В W4 goods этого канала нет.
Берём уже разобранный SALES DDS (`Salon+Shop`) + opex «Модный дом».

## 2025 income mix (EUR, SALES DDS)

- **MD_INDIVIDUAL**: 83.9% (бриф 83.0%)
- **TSUM_B2B**: 8.0% (бриф 9.0%)
- **IM**: 7.7% (бриф 8.0%)

- FX policy: EUR×**100.0**
- MD opex months: **29**

## Политика
1. `MD_INDIVIDUAL` — услуги (income EUR), не путать с B2B/IM/TSUM goods.
2. `margin_channel_total` — только товар + COGS.
3. Bridge MD income@100 − DDS Модный дом — indicative, возможен overlap с COGS/payroll.
4. Следующий шаг: line-level из `МД — копия.xlsx` (H30), если нужны заказы.

Files:
- `live/marts/md_income_month_eur.csv`
- `live/marts/channel_mix_income_eur.csv`
- `live/marts/md_opex_month.csv`
- `live/marts/md_bridge_month.csv`
