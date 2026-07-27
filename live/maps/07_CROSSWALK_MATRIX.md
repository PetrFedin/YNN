# 07 — Матрица сопоставлений (crosswalk)

Updated: 2026-07-27  
CSV: `process_document_register_crosswalk.csv`  
Канон процессов: `01_PROCESS_MAP.md` (P01–P12)

---

## Как читать

Строка = **один процесс**. Связывает:
документы → регистры → marts / контроли → owner → gap.

---

## Сводная матрица

| ID | Процесс | Документы | Регистр | Контроль / mart | Owner | Gap |
|----|---------|-----------|---------|-----------------|-------|-----|
| P01 | МД / инд. пошив | SALES DDS, МД xlsx | CASH, SALES, md_* | MD↔DDS 29/30 | Мамушкина | нет unit-econ / WIP |
| P02 | Продажи IM | IM sales, эквайринг | SALES, BANK | IM_ACQ 80%; gate×6 | Сливяк | BLOCKED months |
| P03 | ЦУМ агент | TSUM sales/cost | SALES, COST, BANK | dual 37.9/87.9; NET 93% | Коптева/Мокеева | COGS+комиссия в Excel |
| P04 | B2B wholesale | B2B sales/settle | SALES, SETTLE, BANK | open 2.51M | Коптева | 15 open docs |
| P05 | Закупка тканей | Ткани 1С, SUP | MAT, SUP | stock ~30M | Дендерина/Мокеева | нет ABC |
| P06 | Закупка фурнитуры | только ДДС | EXP, CASH | opex articles | Дендерина | невидимо в 1С |
| P07 | Производство / cost | Cost excel W3 | COST, PROD, SKU | aliases cand. | Мокеева | нет costing 1С; МД дыра |
| P08 | ФОТ | ЗП файлы | PAYROLL, EMP, BANK | MULTI 100% | Сливяк | lines partial |
| P09 | Opex / аренда | Расходы, бюджет | EXP, BUD, BANK | MULTI 100% | Сливяк | нет аллокации на каналы |
| P10 | Налоги | PDF + банк УФК | TAX, BANK | CASH 97% | Сливяк / Янина | PDF amounts |
| P11 | Казначейство | Bank, DDS, карта, Salon | BANK, CASH | BANK_DDS 83%; gate | Мамушкина/Сливяк | fail ×5; Salon 510/510 OK |
| P12 | Упр. отчётность | Excel CF/P&L, marts, pack | all → marts | gate / client_pack | Янина / Сливяк | риск смешения A/B |

---

## Документ → домен → год / сущность

- `document_domain_category.csv`
- `document_by_entity.csv`
- `document_by_year.csv`
- `document_catalog_slim.csv`

## Архитектура as-is / to-be

- `edges_199.csv` · `field_lineage_644.csv` · `register_wave_map.csv` · `marts_inventory.csv`

---

## Правило сопоставления (анти-ошибка)

1. **Один ключ — один hop**: SKU, INN, period, doc_id.  
2. **Не джойнить** МД services в goods COGS.  
3. **Не читать** goods operating bridge как P&L компании.  
4. **Не считать** Excel GM ЦУМ = product GM без dual view.  
5. **Не принимать** BLOCKED месяц за «убыток».  
6. **ID процессов** только из `01_PROCESS_MAP` — не перенумеровывать.
