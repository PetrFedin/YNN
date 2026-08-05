# YNN — YANINA Business Diagnostic Workspace

Репозиторий комплексной управленческой диагностики бизнеса **YANINA**.

Статус: **master client deliverables Этапа 1 сформированы; inventory/cash QA исправлен; final numerical freeze после закрытия P0**.

> Репозиторий содержит управленческую диагностику и доказательную базу. Это не аудиторское заключение, не бухгалтерский P&L и не юридический налоговый аудит.

---

# Основные документы для заказчика

## 1. Board Report

[`live/client_pack/final_stage1/29_CLIENT_BOARD_REPORT.md`](live/client_pack/final_stage1/29_CLIENT_BOARD_REPORT.md)

Краткий документ для собственника: диагноз, ключевые выводы, резервы, решения и последовательность действий.

## 2. Full Master Diagnostic Report

[`live/client_pack/final_stage1/28_CLIENT_DELIVERABLE_MASTER_REPORT.md`](live/client_pack/final_stage1/28_CLIENT_DELIVERABLE_MASTER_REPORT.md)

Полный клиентский отчёт по финансовой модели, ликвидности, затратам, запасам, процессам, отчётности, людям и налогам.

## 3. Stage 2 Scope

[`live/client_pack/final_stage1/30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md`](live/client_pack/final_stage1/30_STAGE2_SCOPE_DELIVERABLES_AND_ACCEPTANCE.md)

Workstreams, deliverables, acceptance criteria, KPI, decision gates и роли сторон.

## 4. Findings-to-Actions Matrix

[`live/client_pack/final_stage1/31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md`](live/client_pack/final_stage1/31_FINDINGS_TO_ACTIONS_AND_STAGE2_TRACEABILITY_MATRIX.md)

Связь каждого вывода Этапа 1 с решением, результатом Этапа 2 и критерием приёмки.

Полная навигация:

- [`00_FINAL_PACKAGE_STRUCTURE.md`](live/client_pack/final_stage1/00_FINAL_PACKAGE_STRUCTURE.md);
- [`23_CLIENT_BOARD_PACKAGE_INDEX.md`](live/client_pack/final_stage1/23_CLIENT_BOARD_PACKAGE_INDEX.md).

---

# Главный диагностический вывод

> **YANINA создаёт высокую клиентскую и продуктовую ценность, но действующая управленческая модель не обеспечивает её системного преобразования в подтверждённую прибыль, свободный денежный поток и воспроизводимый рост.**

Основной разрыв находится между:

- высокой продуктовой зрелостью;
- способностью формировать спрос и существенные поступления;
- недостаточной зрелостью unit-экономики;
- управлением оборотным капиталом;
- прогнозированием обязательств;
- end-to-end ответственностью;
- качеством управленческой отчётности;
- формальным кадровым и налоговым контуром.

---

# Ключевые профессиональные выводы

- Индивидуальный пошив и товарный бизнес требуют разных моделей прибыли.
- Главный доходный продукт не имеет устойчивой expected/actual unit-экономики.
- Кассовый разрыв является поздним следствием более ранних решений.
- Собственник остаётся неформальным казначеем и источником стабилизации.
- Запасы являются портфелем незавершённых решений по капиталу.
- Реальный резерв ФОТ находится в снижении failure cost, а не в механическом сокращении мастерства.
- Рост без margin, capacity и cash gates может ухудшать устойчивость.
- Каналы необходимо оценивать по capital-adjusted contribution.
- Отчётность должна предотвращать отклонения, а не только объяснять прошлое.
- Налоговая эффективность определяется полной экономической стоимостью модели.

---

# QA-корректировки

## Inventory

В клиентском пакете теперь чётко разделены:

- **2 227 SKU / 7 736 строк** — universe движения;
- **1 339 SKU** — позиции, сопоставленные со складским остатком;
- **668 SKU / около 12,87 млн ₽** — положительные сопоставленные остатки без движения более 365 дней.

## Cash-flow intake

Дополнительные банковские документы получены в конце июля 2026 года и по состоянию на 5 августа находились в процессе интеграции. Некорректная формулировка о получении пакета «в августе» удалена.

## Bespoke share

Для клиентских выводов используется формулировка **около 83–84% дохода в используемом периметре**.

---

# Структура репозитория

| Путь | Содержание |
|---|---|
| [`live/client_pack/final_stage1/`](live/client_pack/final_stage1/) | официальный клиентский пакет |
| [`live/client_pack/`](live/client_pack/) | тематические диагностические записки H-серии |
| [`live/marts/`](live/marts/) | расчётные витрины |
| [`live/registers/`](live/registers/) | регистры и контрольные слои |
| [`live/maps/`](live/maps/) | карты данных и процессов |
| [`live/client_pack/sign_session_pack/`](live/client_pack/sign_session_pack/) | подтверждения owners и контрольные карточки |
| [`STATUS.md`](STATUS.md) | технический статус |
| [`HANDOFF.md`](HANDOFF.md) | передача контура |

---

# Доказательность

Статусы выводов:

- `CONFIRMED`;
- `STRONG INDICATION`;
- `PARTIAL`;
- `NOT PROVEN`;
- `REFUTED`;
- `QUARANTINE`.

Основные доказательные документы:

- [`03_EVIDENCE_REGISTER.md`](live/client_pack/final_stage1/03_EVIDENCE_REGISTER.md);
- [`12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md`](live/client_pack/final_stage1/12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md);
- [`15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md`](live/client_pack/final_stage1/15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md);
- [`appendices/01_FINAL_METRICS_REGISTER.csv`](live/client_pack/final_stage1/appendices/01_FINAL_METRICS_REGISTER.csv).

---

# P0 перед final freeze

1. Интеграция и дедупликация новых банковских выписок.
2. Transaction-level расчёт net owner cash flow.
3. Единая дата среза headline figures.
4. Подтверждение НДС и РСВ 2026-Q2 либо оговорка.
5. Проверка ЕНС.
6. Обновление Final Metrics Register.
7. Междокументная QA-2.
8. Очистка чувствительных данных.

---

# Следующий формат выпуска

После numerical freeze:

- Board Report — DOCX/PDF;
- Full Diagnostic Report — DOCX/PDF;
- Stage 2 Scope — DOCX/PDF;
- Evidence Appendix;
- презентация для итоговой встречи;
- протокол решений собственника.
