# H30 — МД workbook (заказы / платежи)

Updated: 2026-07-24 19:37

Source: `МД — копия.xlsx`

- Payments: **6663**
- Salon order lines: **4194**
- Shop sale lines: **11173**
- Recon 2025 CLOSE+SOFT: **12/12**
- 2025 payments EUR: **2,319,617** vs DDS **2,325,846** (gap -6,229)

## Политика
1. Платежи (`финансы`) — cash/income proxy для MD_INDIVIDUAL.
2. Салон/маг — operational detail; валюта исторически смешанная → hint EUR_LIKELY_POST2020.
3. Не джойнить в W4 goods COGS (остатков МД нет).

Files: `md_payments.csv`, `md_salon_orders.csv`, `md_shop_sales.csv`, `recon_md_payments_vs_dds.csv`
