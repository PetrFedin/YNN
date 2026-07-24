# Finance Recommendations (H20)

Updated: 2026-07-24 17:46

Гипотезы для Owners. **Не SoT. COGS не менялись.**

## REC-0-2497 — `0-2497`
- Proposed: **OK_COMMERCIAL_LOSS** (confidence HIGH)
- Action: `A-FIN-0-2497`
- Impact: revenue 70000.04 / margin -25055.34
- Why: Цена ровно ~10 000 на всех строках = оптовый/партнёрский прайс, не случайная ошибка ввода. У соседнего 0-2493 B2B≈10K при IM/TSUM в разы выше — каналная лестница. Автоправка cost запрещена: cost из остатков (DERIVED), не BOM; риск сломать маржу.
- Do not: Не подменять cost на BOM без версии; не исключать из продаж
- If accepted: FLAG_WHOLESALE_EXCEPTION (оставить в revenue, пометить margin)
- Evidence: B2B unit≈10000.01 vs cost≈13579.34 (gap -3579.33); cost source FILE/H5 DERIVED_STOCK_MOVEMENT; sibling 0-2493 ladder B2B=10000.0 / IM=54050.0 / TSUM=108100.0; B2B lines with ~10k price: 10/230.

## REC-0-2496 — `0-2496`
- Proposed: **OK_COMMERCIAL_LOSS** (confidence HIGH)
- Action: `A-FIN-0-2496`
- Impact: revenue 60000.05 / margin -14155.57
- Why: Цена ровно ~10 000 на всех строках = оптовый/партнёрский прайс, не случайная ошибка ввода. У соседнего 0-2493 B2B≈10K при IM/TSUM в разы выше — каналная лестница. Автоправка cost запрещена: cost из остатков (DERIVED), не BOM; риск сломать маржу.
- Do not: Не подменять cost на BOM без версии; не исключать из продаж
- If accepted: FLAG_WHOLESALE_EXCEPTION (оставить в revenue, пометить margin)
- Evidence: B2B unit≈10000.01 vs cost≈12359.27 (gap -2359.26); cost source FILE/H5 DERIVED_STOCK_MOVEMENT; sibling 0-2493 ladder B2B=10000.0 / IM=54050.0 / TSUM=108100.0; B2B lines with ~10k price: 10/230.

## REC-0-2493A — `0-2493A`
- Proposed: **OK_COMMERCIAL_LOSS** (confidence HIGH)
- Action: `A-FIN-0-2493A`
- Impact: revenue 30000.0 / margin -5884.56
- Why: Цена ровно ~10 000 на всех строках = оптовый/партнёрский прайс, не случайная ошибка ввода. У соседнего 0-2493 B2B≈10K при IM/TSUM в разы выше — каналная лестница. Автоправка cost запрещена: cost из остатков (DERIVED), не BOM; риск сломать маржу.
- Do not: Не подменять cost на BOM без версии; не исключать из продаж
- If accepted: FLAG_WHOLESALE_EXCEPTION (оставить в revenue, пометить margin)
- Evidence: B2B unit≈10000.0 vs cost≈11961.52 (gap -1961.52); cost source FILE/H5 DERIVED_STOCK_MOVEMENT; sibling 0-2493 ladder B2B=10000.0 / IM=54050.0 / TSUM=108100.0; B2B lines with ~10k price: 10/230.

## REC-0-3243 — `0-3243`
- Proposed: **KEEP_QUARANTINE_NEED_COST_VERSION** (confidence HIGH)
- Action: `A-FIN-0-3243`
- Impact: revenue 30250.0 / margin 
- Why: Продажа = свитшот «Be a poem»; единственный cost 0-3243 = худи (Худи из плотного футера|33555.869999999995). 0-3244 = юбка ~43160 — ещё хуже. Cost с 'poem' в имени: 0. Релинк запрещён.
- Do not: Не брать cost 0-3244; не возвращать худи-COGS на свитшот
- If accepted: KEEP_EXCLUDED_FROM_COGS_UNTIL_COST_EXISTS
- Evidence: quarantine SL-ed909efc193b9f4c; old_cogs 33555.87 (hoodie) removed; revenue 30250 kept in sales, COGS blank

## REC-PORTFOLIO — `PORTFOLIO`
- Proposed: **ACCEPT_AS_POLICY_EXCEPTION_SET** (confidence HIGH)
- Action: `A-FIN-WATCH-01`
- Impact: revenue 160000.09 / margin -45095.47
- Why: Суммарная отриц. маржа тройки ≈ -45,095 ₽ на ~160K выручки. На overall GM ~53% влияние точечное. Лучше политика исключения, чем «чинить» cost.
- Do not: Не раздувать в системный rewrite cost master
- If accepted: POLICY_FLAG
- Evidence: finance_neg_sku_review + sales_lines B2B May/Jun 2025-2026

## Как принять

1. Открыть Owner Packet → лист `RECOMMENDATIONS_H20`
2. Колонка `owner_decision_ACCEPT_REJECT` = ACCEPT или REJECT
3. Прислать файл в чат — после ACCEPT можно пометить exceptions в marts
