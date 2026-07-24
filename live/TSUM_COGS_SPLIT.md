# H28 — TSUM product COGS vs commission

Updated: 2026-07-24 19:32

## Зачем
Комиссия ЦУМ сидит в FILE/Excel себестоимости. Cash уже net-rate. Dual view без double-count.

- Net-rate policy: **0.4668** (agency take **0.5332**)
- Split method: FILE cogs − median W3 unit × qty
- Lines split: **740** / 744

## Итоги

| View | Revenue | COGS | Margin | Margin % |
|------|---------|------|--------|----------|
| Reported (FILE) | 122,849,276 | 76,302,534 | 46,546,742 | 37.9% |
| Product (W3) | 121,695,175 | 14,667,839 | 107,027,336 | 87.9% |
| Commission proxy (FILE−W3) | — | 60,954,243 | — | 50.1% of rev |
| Agency take at net-rate | — | 65,503,234 | — | 53.32% of rev |

## Политика
1. `TSUM_REPORTED` — как в Excel (для сверки с их файлами).
2. `TSUM_PRODUCT` — товарная маржа (W3), комиссия вынесена в proxy.
3. В operating bridge / cash **не** вычитать agency take поверх reported COGS.
4. Уточнить у Меркушиной формулу комиссии в карточках ЦУМ.

Files: `live/marts/tsum_margin_dual_lines.csv`, `tsum_margin_dual_month.csv`, `margin_channel_views_h28.csv`
