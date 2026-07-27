# 02 — Карта ключевых ограничений (детальная)

Updated: 2026-07-27 · evidence-linked

| ID | Ограничение | Доказательство в документах | Бьёт по | P | Снимается чем |
|----|-------------|----------------------------|---------|---|---------------|
| C01 | Смешение контуров A/B в «прибыли» | Bridge 2025 −54M/−74% при MD DDS 232.6M вне базы | Решения FTE/каналы | P0 | P-A; KPI K10 |
| C02 | Нет unit-econ МД | Бриф: нет остатков/движения МД; COGS_A=N/A в модели | Contribution ядра | P0 | Пилот I07 |
| C03 | Комиссия ЦУМ в COGS | Dual 37.9% vs 87.9%; proxy ~61M/30м; бриф УНФ | Ложные решения по ЦУМ | P0 | I08 + C-режим |
| C04 | Фурнитура вне 1С | Model flag MF-NO-FURNITURE; бриф | WC/потери | P1 | Мини-регистр I10 |
| C05 | IM acquiring дыры | 6 OPEN; fail_freq IM=6 в gate | Касса/gate | P1 | I04 |
| C06 | B2B open | 15 шт / 2.514M; топ Бекеева 0.83M | Cash | P1 | I03 |
| C07 | Bank↔DDS core | fail_freq BANK_DDS=5; forensic Salon 510/510 → не «нет выписки» | CF картина | P1 | Memo статей |
| C08 | ФОТ без split | Payroll 19.6→37.8M (2024→2025) на падающем goods | Опасность S4 | P1 | I09 |
| C09 | Нет баланса | Бриф: баланса нет | Классический WC | P2 | Этап 2+ |
| C10 | Decor 2026 без тегов | Бриф wind-down; flag OPEN_MODEL | Шум KPI | P2 | I06 |
| C11 | Tax PDF amounts | NOT_EXTRACTED на части 6-НДФЛ/НДС | Tax provision | P2 | Extraction |
| C12 | ЗП lines неполные | OWNER_ACTIONS deferred | Person payroll | P2 | Ведомости |
| C13 | FX@100 | Бриф; flag | RUB↔EUR | P2 | fx_policy |
| C14 | Нет ABC тканей | Склады ~29.8M без aging | Точный неликвид | P2 | I11 |
| C15 | DDS_LAG 2026-06 | MD recon: workbook 125k EUR vs DDS 0 | MD income | P1 | I05 |
| C16 | TSUM agent_allocated=0 | 2026-05/06 gap −100% vs model | Gate TSUM | P1 | Агентские файлы |
| C17 | B2B объём схлопнулся | 10.9M (2024) → 2.9M (2025) → ~0 | Не путать с ЦУМ | P2 | Таксономия брифа |

Топ для собственника: **C01 → C02 → C03 → C05/C06/C15 → C08**.
