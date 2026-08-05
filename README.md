# YNN — YANINA Business Diagnostic Workspace

Репозиторий комплексной управленческой диагностики бизнеса **YANINA**.

Статус: **QA-2 завершён; Board Report, Master Report, maturity heatmap и tax economics assessment сформированы; numerical freeze, privacy review и copyedit остаются P0**.

> Репозиторий содержит управленческую диагностику и доказательную базу. Это не аудиторское заключение, не бухгалтерский P&L и не юридический налоговый аудит.

---

# Основная точка входа

## [`live/client_pack/final_stage1/`](live/client_pack/final_stage1/)

Официальный клиентский пакет Этапа 1.

Начать с:

1. [`00_FINAL_PACKAGE_STRUCTURE.md`](live/client_pack/final_stage1/00_FINAL_PACKAGE_STRUCTURE.md) — официальный состав и статус пакета.
2. [`29_CLIENT_BOARD_REPORT.md`](live/client_pack/final_stage1/29_CLIENT_BOARD_REPORT.md) — основной отчёт для собственника.
3. [`35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md`](live/client_pack/final_stage1/35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md) — зрелость, ограничения и приоритеты.
4. [`28_CLIENT_DELIVERABLE_MASTER_REPORT.md`](live/client_pack/final_stage1/28_CLIENT_DELIVERABLE_MASTER_REPORT.md) — полный клиентский master report.
5. [`36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md`](live/client_pack/final_stage1/36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md) — налоговая экономика и юридическая структура.
6. [`30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md`](live/client_pack/final_stage1/30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md) — scope и критерии приёмки Этапа 2.
7. [`31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md`](live/client_pack/final_stage1/31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md) — связь выводов с действиями.
8. [`23_CLIENT_BOARD_PACKAGE_INDEX.md`](live/client_pack/final_stage1/23_CLIENT_BOARD_PACKAGE_INDEX.md) — структура передачи и итоговой встречи.
9. [`34_FINAL_FREEZE_AND_CLIENT_RELEASE_PROTOCOL.md`](live/client_pack/final_stage1/34_FINAL_FREEZE_AND_CLIENT_RELEASE_PROTOCOL.md) — правила final freeze and release.

---

# Главный диагностический вывод

> **YANINA создаёт сильную клиентскую и продуктовую ценность, но действующая система управления не обеспечивает её устойчивого преобразования в подтверждённую маржу, возврат капитала и свободный денежный поток.**

Основной разрыв находится между:

- высокой продуктовой зрелостью;
- доказанной способностью формировать спрос и поступления;
- недостаточной зрелостью unit-экономики, cash architecture, управления мощностью, оборотным капиталом, ответственностью, отчётностью и налогово-юридической моделью.

---

# Интегрированная оценка зрелости

| Контур | Оценка | Главный разрыв |
|---|---:|---|
| Финансовая модель и качество прибыли | 1,5 / 5 | нет полного P&L главного доходного контура и management balance |
| Денежный поток и ликвидность | 2,0 / 5 | cash виден лучше, чем обязательства и свободный поток |
| Затраты и производительность | 2,0 / 5 | расходы не связаны полностью с заказом, мощностью и результатом |
| Запасы и оборотный капитал | 2,0 / 5 | стоимость видна лучше, чем назначение и возврат капитала |
| Закупки, производство и планирование | 2,0 / 5 | отсутствуют единые economic/capacity/material gates |
| Управление и ответственность | 2,5 / 5 | end-to-end accountability неполна |
| Отчётность и data governance | 2,0 / 5 | решения запаздывают из-за ручной сверки и конфликтов версий |
| Налоговая и юридическая модель | 2,5 / 5 | платежи видны лучше, чем начисления и полная экономическая стоимость |
| Кадровый и платёжный контур | 2,0 / 5 | roster, договоры и выплаты не объединены |
| Готовность к масштабированию | 2,0 / 5 | продукт масштабируется быстрее системы управления |

Подробно:

- [`35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md`](live/client_pack/final_stage1/35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md).

---

# Профессиональная причинная модель

Финансовое давление воспроизводится через семь циклов:

1. сложность заказа не полностью монетизируется;
2. аванс воспринимается как свободный cash;
3. потребность повторно финансируется через старый запас и новую закупку;
4. собственник заменяет формальное казначейство;
5. отчётность поздно выявляет отклонение;
6. кадровый и налоговый formalization догоняет фактическую деятельность;
7. смешение экономических контуров искажает прибыльность.

Подробно:

- [`32_CROSS_FUNCTIONAL_CAUSAL_SYNTHESIS.md`](live/client_pack/final_stage1/32_CROSS_FUNCTIONAL_CAUSAL_SYNTHESIS.md).

---

# Налоговый вывод

Налоговая модель оценивается не по минимальной ставке, а по полной экономической стоимости:

- налог с реализации;
- невозмещаемый входной и ввозной НДС;
- влияние на B2C/B2B цену;
- стоимость импорта;
- timing авансов и обязательств;
- влияние на запас и WIP;
- стоимость нескольких юридических контуров;
- кадровые начисления;
- административная нагрузка;
- юридическая защищённость.

Подробно:

- [`07_TAX_DIAGNOSTIC.md`](live/client_pack/final_stage1/07_TAX_DIAGNOSTIC.md);
- [`07A_TAX_LEGISLATION_UPDATE_2026-07.md`](live/client_pack/final_stage1/07A_TAX_LEGISLATION_UPDATE_2026-07.md);
- [`36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md`](live/client_pack/final_stage1/36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md).

---

# Периметр Этапа 1

Диагностика охватывает:

- финансовую модель;
- денежный поток и ликвидность;
- owner flows;
- качество прибыли и cash conversion;
- структуру затрат и производительность;
- себестоимость индивидуального пошива и товара;
- запасы, WIP и оборотный капитал;
- закупки и поставщиков;
- производство и планирование мощности;
- коммерческие каналы;
- ФОТ и кадровый контур;
- управление и RACI;
- управленческую отчётность и data governance;
- налоговую нагрузку и юридические контуры;
- strategic options and growth readiness;
- stress test;
- early warning architecture;
- value realization and benefit governance.

Этап 1 не является внедрённой системой управленческого учёта, ERP/PLM, налоговой реструктуризацией или постоянным сопровождением изменений.

---

# Ключевые client-facing документы

## Board and strategy

- [`29_CLIENT_BOARD_REPORT.md`](live/client_pack/final_stage1/29_CLIENT_BOARD_REPORT.md);
- [`35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md`](live/client_pack/final_stage1/35_INTEGRATED_DIAGNOSTIC_HEATMAP_AND_MANAGEMENT_PRIORITIES.md);
- [`27_FINAL_CONSULTING_CONCLUSIONS_AND_RECOMMENDATIONS.md`](live/client_pack/final_stage1/27_FINAL_CONSULTING_CONCLUSIONS_AND_RECOMMENDATIONS.md);
- [`20_BOARD_LEVEL_STRATEGIC_SYNTHESIS.md`](live/client_pack/final_stage1/20_BOARD_LEVEL_STRATEGIC_SYNTHESIS.md);
- [`24_STRATEGIC_OPTIONS_AND_GROWTH_READINESS.md`](live/client_pack/final_stage1/24_STRATEGIC_OPTIONS_AND_GROWTH_READINESS.md);
- [`14_MANAGEMENT_DECISION_AGENDA.md`](live/client_pack/final_stage1/14_MANAGEMENT_DECISION_AGENDA.md);
- [`19_TARGET_OPERATING_MODEL.md`](live/client_pack/final_stage1/19_TARGET_OPERATING_MODEL.md).

## Diagnostic depth

- [`28_CLIENT_DELIVERABLE_MASTER_REPORT.md`](live/client_pack/final_stage1/28_CLIENT_DELIVERABLE_MASTER_REPORT.md);
- [`22_QUALITY_OF_EARNINGS_AND_CASH_CONVERSION.md`](live/client_pack/final_stage1/22_QUALITY_OF_EARNINGS_AND_CASH_CONVERSION.md);
- [`32_CROSS_FUNCTIONAL_CAUSAL_SYNTHESIS.md`](live/client_pack/final_stage1/32_CROSS_FUNCTIONAL_CAUSAL_SYNTHESIS.md);
- [`36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md`](live/client_pack/final_stage1/36_TAX_ECONOMICS_AND_STRUCTURAL_ASSESSMENT.md);
- [`26_SCENARIO_STRESS_TEST_AND_BUSINESS_RESILIENCE.md`](live/client_pack/final_stage1/26_SCENARIO_STRESS_TEST_AND_BUSINESS_RESILIENCE.md);
- [`25_EARLY_WARNING_AND_MANAGEMENT_CONTROL_SYSTEM.md`](live/client_pack/final_stage1/25_EARLY_WARNING_AND_MANAGEMENT_CONTROL_SYSTEM.md);
- [`33_VALUE_REALIZATION_ROADMAP_AND_BENEFIT_GOVERNANCE.md`](live/client_pack/final_stage1/33_VALUE_REALIZATION_ROADMAP_AND_BENEFIT_GOVERNANCE.md).

## Stage 2

- [`30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md`](live/client_pack/final_stage1/30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md);
- [`31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md`](live/client_pack/final_stage1/31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md).

## Evidence and QA

- [`03_EVIDENCE_REGISTER.md`](live/client_pack/final_stage1/03_EVIDENCE_REGISTER.md);
- [`12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md`](live/client_pack/final_stage1/12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md);
- [`15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md`](live/client_pack/final_stage1/15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md);
- [`34_FINAL_FREEZE_AND_CLIENT_RELEASE_PROTOCOL.md`](live/client_pack/final_stage1/34_FINAL_FREEZE_AND_CLIENT_RELEASE_PROTOCOL.md);
- [`appendices/01_FINAL_METRICS_REGISTER.csv`](live/client_pack/final_stage1/appendices/01_FINAL_METRICS_REGISTER.csv).

---

# Headline facts

- индивидуальный пошив формирует около 83–84% используемого доходного периметра;
- полного P&L компании пока нет;
- товарная выручка с подтверждённой себестоимостью за 2025 год составляет около 72,9 млн ₽;
- 1 339 SKU сопоставлены со складским остатком около 29,9 млн ₽;
- 668 положительных сопоставленных остатков на сумму около 12,87 млн ₽ не показывают движения более 365 дней;
- около 2,51 млн ₽ находится в открытом B2B-контуре;
- базовый банковский регистр включает около 4 933 операций;
- налоговый cash в диагностическом 30-месячном периметре составляет около 45,4 млн ₽;
- собственник как получал средства из бизнеса, так и вносил их обратно;
- roster, договорной и платёжный контуры расходятся.

Эти показатели сопровождаются методологическими ограничениями и не должны интерпретироваться вне соответствующих документов.

---

# P0 перед FINAL CONTENT

1. Интеграция и дедупликация нового банковского intake.
2. Transaction-level расчёт net owner cash flow.
3. Единая дата среза и периоды headline figures.
4. Подтверждение denominator доли 83–84%.
5. Подтверждение единиц исторической управленческой модели.
6. НДС Q2 2026, РСВ Q2 2026 и ЕНС — получить либо раскрыть limitation.
7. Document-level closure B2B open.
8. Проверка оснований HR/payments.
9. Обновление Final Metrics Register.
10. Privacy review.
11. Copyedit.
12. Финальный cross-document number scan.

---

# Итоговый принцип

> Финальный пакет должен быть устойчивым к проверке: каждый ключевой вывод имеет доказательство, ограничение, экономическое значение, управленческое решение и понятное продолжение на Этапе 2.
