# Этап 1 — Комплексная диагностика бизнеса YANINA
## Пакет результатов для заказчика

**Срок контура данных:** staging по состоянию на 2026-07-24…27  
**Статус:** диагностический этап · **не** внедрение · **не** SoT / не аудит  
**Периметр:** ИП Янина Ю.Ф. · ООО «Салон Юлия Янина» · ООО «Декор»  
**Состав пакета**

| # | Документ | Назначение |
|---|----------|------------|
| 00 | этот README | Навигация и границы этапа |
| 01 | `01_DIAGNOSTIC_REPORT.md` | Системный диагностический отчёт (блоки 1–6) |
| 02 | `02_CONSTRAINTS_MAP.md` | Карта ключевых ограничений |
| 03 | `03_RESERVES_MAP.md` | Карта резервов эффективности / капитала |
| 04 | `04_PRIORITY_MATRIX.md` | Матрица приоритетов инициатив |
| 05 | `05_RECOMMENDATIONS_NEXT.md` | Рекомендации и план дальнейших этапов |
| + | `STAGE1_PLUS_WHAT_WE_CAN_ADD.md` | Что можно добавить из «вне ТЗ» на текущих данных |
| 06 | `06_FIN_MODEL_SKELETON_2025.md` | Скелет финмодели dual-contour 2025 |
| 07 | `07_KPI_CATALOG_DRAFT.md` | Каталог KPI (черновик, не система) |
| 08 | `08_POLICY_DRAFTS.md` | Черновики политик P-A…P-F |
| 09 | `09_DATA_LINEAGE_ONEPAGER.md` | Карта данных one-pager |
| 10 | `10_RISK_REGISTER.md` | Реестр рисков |
| 11 | `11_FULL_ANALYTICAL_DETAIL.md` | **Детальное приложение со всеми цифрами** |
| 12 | `12_DEEP_DIVE_ALL_CONTOURS.md` | **Углубление:** причинность контуров + действия |
| 13 | `13_LAYER2_FINDINGS.md` | **Layer 2:** МД cost forensic, ФОТ +93%, SKU, exhaustion |
| 14 | `14_LAYER3_FINDINGS.md` | **Layer 3:** OTHER_IN/POS ~62M, payroll lines, TSUM≠IM cash |
| 15 | `15_LAYER4_RECLASS_IMPACT.md` | **Layer 4:** impact — 62M POS не закрывает 6 IM OPEN влоб (1/6) |
| 16 | `16_LAYER5_SCORECARD.md` | **Layer 5:** единый статус; POS=только ИП; invoice↔МД ~40% |
| 17 | `17_EXECUTION_PACK.md` | **Стоп narrative** → пакет решений owners + CSV |
| 18 | `18_MASTER_SCHEME_CLIENT.md` | **Мастер-схема:** данные↔связи↔результат↔S1–S4 / модель |
| 19 | `19_COVERAGE_DONE_VS_MISSING.md` | **Полный перечень:** что сделано / чего нет (+ CSV) |
| 20 | `20_CONSULTANT_VERDICT_NO_MORE_DOCS.md` | **Честный вывод:** Этап 1 при «документов больше не будет» |
| 21 | `21_BUSINESS_RUNNING_DIAGNOSIS_AND_PLAN.md` | **Ведение бизнеса:** разбор тезиса + план A→E |
| 22 | `22_DIAGNOSIS_DETAILED_EXPLAINER.md` | **Детальная расшифровка** 4 тезисов + арифметика −74% |
| 23 | `23_GROUPS_TO_DATA_MAP_CONCLUSIONS.md` | **По группам:** лежит / посчитано / досчёт / карта / выводы |
| G1 | `G1_BANK_GROUP_DETAIL.md` | **Детально группа Банк** + `group_G1_bank_files.csv` |
| G2 | `G2_DDS_OPEX_SALES_GROUP_DETAIL.md` | **Детально ДДС/расходы/SALES** + `group_G2_*.csv` |
| G3 | `G3_SALES_CHANNELS_GROUP_DETAIL.md` | **Детально IM/B2B/ЦУМ** + `group_G3_*.csv` |
| G4 | `G4_COST_MD_GROUP_DETAIL.md` | **Детально себестоимость/МД** + `group_G4_*.csv` |
| G5 | `G5_NOMENCLATURE_COLLECTIONS_GROUP_DETAIL.md` | **Детально номенклатура/коллекции** + `group_G5_*.csv` |
| G6 | `G6_FABRICS_WAREHOUSES_PURCHASES_GROUP_DETAIL.md` | **Детально ткани/склады/закупки** + `group_G6_*.csv` |
| G7 | `G7_PAYROLL_GROUP_DETAIL.md` | **Детально персонал/ЗП** + `group_G7_*.csv` |
| G8 | `G8_TAX_PDF_GROUP_DETAIL.md` | **Детально налоги PDF** + `group_G8_*.csv` |
| G9 | `G9_CONTRACTS_RACI_GROUP_DETAIL.md` | **Детально договоры/RACI** + `group_G9_*.csv` |
| **24** | `24_DEEP_DOJIM_FULL_107_AND_OWNER_PACKS.md` | **H37:** полный scan 107 + tax HIGH + owner packs |
| **25** | `25_CONTINUE_DOJIM_H38.md` | **H38:** IM×POS, bank/DDS gaps, FOT drivers, fabric ABC indicative |
| **26** | `26_PRIORITY_GATE_IM_POS_H39.md` | **H39 приоритет:** Gate IM/POS — slice Accept → 20–24/30 |
| **27** | `27_PRIORITY_GATE_BANK_DDS_H40.md` | **H40 приоритет:** Gate BANK↔DDS — card alt + ДДС июнь → 26–28/30 |
| **28** | `28_PRIORITY_GATE_TSUM_NET_H41.md` | **H41 приоритет:** Gate TSUM_NET — лаг +1 мес / Меркурий → 30/30 |
| **29** | `29_PRIORITY_B2B_COLLECT_H42.md` | **H42 приоритет:** B2B collect 2.51M — топ-3 / aging / bank hypotheses |
| **30** | `30_PRIORITY_RACI_ASSIGN_H43.md` | **H43 приоритет:** RACI 10 OPEN — confirm H27 кандидатов (лист Яниной) |
| **31** | `31_PRIORITY_ALIAS_ACCEPT_H44.md` | **H44 приоритет:** Alias Accept — 16 PENDING / топ-5 ≈3.04M (Коновалова) |
| **32** | `32_PRIORITY_PAYROLL_QUARANTINE_H45.md` | **H45 приоритет:** ЗП янв–фев quarantine — root cause #REF! в Распределение |
| **33** | `33_PRIORITY_IM_POS_ACCEPT_H46.md` | **H46 приоритет:** IM POS Accept — slices 509k+37k → gate 20/30 |
| **34** | `34_PRIORITY_MD_UNIT_ECON_H47.md` | **H47 приоритет:** MD unit-econ — 24–25 BLOCKED / пилот 2026 shop+salon |
| **35** | `35_MASTER_OWNER_EXECUTION_H48.md` | **H48 Master Board:** E01–E12 исполнение owners (freeze анализа) |
| **36** | `36_STAGE1_HANDOFF_H49.md` | **H49 Handoff:** сдача Stage 1 + decision log (не новый анализ) |
| **37** | `37_EXEC_READINESS_H50.md` | **H50:** аудит артефактов 12/12 READY + Wave A checklist |
| **38** | `38_DRAFT_DECISIONS_H51.md` | **H51:** черновик решений Wave A на подпись (не Accept) |
| **39** | `39_GAP_MAPS_H52.md` | **H52:** недостающие карты — calendar / IM acq / MD cost to-be / RACI |
| **40** | `40_PRIORITY_OPS_H53.md` | **H53:** WO overbank + очередь MD↔invoice + граф unlock |
| **41** | `41_WAVE_B_READY_H54.md` | **H54:** Wave B pack — B2B/alias/cost/BANK/TSUM + ladder |
| **42** | `42_EXEC_ENABLE_H55.md` | **H55:** sign 15мин + пинги + SLA + Stage2 entry + Wave C |
| **43** | `43_COMMAND_CENTER_H56.md` | **H56:** NOW / weekly ops / stop-doing — точка входа |
| **44** | `44_PREFILL_REGISTERS_H57.md` | **H57:** prefill overbank 48 строк + MD top5 bank lines |
| **45** | `45_BANK_B2B_PREFILL_H58.md` | **H58:** card→DDS 89 строк + B2B worksheet + dekor fix |
| **46** | `46_ALIAS_TSUM_ZP_H59.md` | **H59:** alias evidence + Mercury missing + soft-slice/ZP |
| **47** | `47_BOARD_SYNC_TAX_H60.md` | **H60:** board sync + TAX 36k + unified gate 18→30 |
| **48** | `48_SOURCE_FREEZE_VERIFY_H61.md` | **H61:** 107/107 SHA OK — stop packaging, owners only |
| **49** | `49_COLLECTIONS_MARGIN_H62.md` | **H62:** коллекции/showroom → маржа + MD crosswalk |
| **50** | `50_BUDGET_VS_FACT_H63.md` | **H63:** бюджет plan/fact + opex bridge |
| 06 | `06_FIN_MODEL_SKELETON_2025.md` | Скелет финмодели multi-year (обновлён) |
| — | `_data_snapshot.json` | Машиночитаемый снимок расчётов |
| A1 | `../OPTIMIZATION_SCENARIOS.md` | Приложение: сценарии S1–S4 |
| A2 | `../OPTIMIZATION_FROM_AVAILABLE_DATA.md` | Приложение: выводы H/M/L |
| A3 | `../CFO_EXEC_MEMO.md` | Приложение: memo собственнику |
| A4 | `../MATURITY_ASSESSMENT.md` | Приложение: зрелость данных |
| M0 | `../maps/00_MAPS_INDEX.md` | **Карты системы:** процессы, документы, данные, сущности, контроли, value stream |
| M1 | `../maps/07_CROSSWALK_MATRIX.md` | Сопоставление процесс↔док↔регистр↔mart |
| M2 | `../maps/08_UNIFIED_ALGORITHM.md` | Единый алгоритм чтения / close / оптимизации |
| M3 | `../maps/09_PROBLEMS_PLUS_MINUS.md` | Углублённый ± и приоритеты P0–P2 |

---

## Границы этапа 1 (как в ТЗ)

**Входит:** объективная картина, ограничения, зоны потерь, предварительные резервы, приоритеты, рекомендации «что дальше».

**Не входит (следующие этапы):** финансовые модели, KPI-система, дашборды внедрения, регламенты, инструменты контроля «в бою», сопровождение изменений.

---

## Покрытие диагностики по блокам ТЗ

| Блок ТЗ | Покрытие | Комментарий |
|---------|----------|-------------|
| 1. Финансовая диагностика | **Высокое / с оговоркой** | Два контура (МД + товар); единого P&L компании нет (методологически правильно) |
| 2. Запасы и ОКК | **Среднее** | Ткани/склады есть; фурнитура и остатки МД — нет в учёте |
| 3. Ассортиментная эффективность | **Среднее+** | Товарные каналы B2B/IM/TSUM; МД — без unit-econ |
| 4. Бизнес-процессы | **Среднее** | По брифу + разрывам данных/сврок |
| 5. Система управления | **Высокое** | RACI, gate, отчётность, зрелость |
| 6. Налоговый и орг. анализ | **Среднее+** | Модель LE/налогов по брифу + cash tax; суммы из PDF не полностью извлечены |

**Итоговая готовность этапа 1 как вводного:** достаточна для управленческих решений о **направлении** следующих этапов; недостаточна для утверждения единого audited P&L.
