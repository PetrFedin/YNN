# YNN — YANINA Business Diagnostic Workspace

Репозиторий комплексной управленческой диагностики бизнеса **YANINA**.

Статус: **консалтинговая редакция Этапа 1 сформирована; strategic options, early warning и stress-test добавлены; final freeze после закрытия P0**.

> Репозиторий содержит управленческую диагностику и доказательную базу. Это не аудиторское заключение, не бухгалтерский P&L и не юридический налоговый аудит.

---

# Основная точка входа

## [`live/client_pack/final_stage1/`](live/client_pack/final_stage1/)

Официальный клиентский пакет Этапа 1.

Начать с:

1. [`00_FINAL_PACKAGE_STRUCTURE.md`](live/client_pack/final_stage1/00_FINAL_PACKAGE_STRUCTURE.md) — навигация по пакету.
2. [`23_CLIENT_BOARD_PACKAGE_INDEX.md`](live/client_pack/final_stage1/23_CLIENT_BOARD_PACKAGE_INDEX.md) — рекомендуемая структура передачи заказчику.
3. [`01_EXECUTIVE_SUMMARY_FOR_OWNERS.md`](live/client_pack/final_stage1/01_EXECUTIVE_SUMMARY_FOR_OWNERS.md) — выводы для собственника.
4. [`20_BOARD_LEVEL_STRATEGIC_SYNTHESIS.md`](live/client_pack/final_stage1/20_BOARD_LEVEL_STRATEGIC_SYNTHESIS.md) — стратегический синтез.
5. [`24_STRATEGIC_OPTIONS_AND_GROWTH_READINESS.md`](live/client_pack/final_stage1/24_STRATEGIC_OPTIONS_AND_GROWTH_READINESS.md) — варианты развития и готовность к росту.
6. [`02_FULL_BUSINESS_DIAGNOSTIC_REPORT.md`](live/client_pack/final_stage1/02_FULL_BUSINESS_DIAGNOSTIC_REPORT.md) — полный интегрированный отчёт.
7. [`14_MANAGEMENT_DECISION_AGENDA.md`](live/client_pack/final_stage1/14_MANAGEMENT_DECISION_AGENDA.md) — board decision memo.
8. [`19_TARGET_OPERATING_MODEL.md`](live/client_pack/final_stage1/19_TARGET_OPERATING_MODEL.md) — целевая operating model.
9. [`25_EARLY_WARNING_AND_MANAGEMENT_CONTROL_SYSTEM.md`](live/client_pack/final_stage1/25_EARLY_WARNING_AND_MANAGEMENT_CONTROL_SYSTEM.md) — система ранних сигналов.
10. [`26_SCENARIO_STRESS_TEST_AND_BUSINESS_RESILIENCE.md`](live/client_pack/final_stage1/26_SCENARIO_STRESS_TEST_AND_BUSINESS_RESILIENCE.md) — стресс-тест и устойчивость.

---

# Главный диагностический вывод

> **YANINA создаёт высокую клиентскую и продуктовую ценность, но действующая управленческая модель не обеспечивает её системного преобразования в подтверждённую прибыль, свободный денежный поток и воспроизводимый рост.**

Основной разрыв находится между:

- высокой продуктовой зрелостью;
- подтверждённой способностью формировать спрос и поступления;
- недостаточной зрелостью unit-экономики, управления капиталом, ответственности и отчётности.

---

# Главные профессиональные выводы

- Продуктовая зрелость опережает экономическую.
- Основной доходный контур не имеет устойчивой expected/actual unit-экономики.
- Рост может увеличивать потребность в финансировании быстрее, чем contribution.
- Собственник остаётся неформальным казначеем и стабилизатором ликвидности.
- Запасы отражают качество capital allocation, а не только работу склада.
- ФОТ необходимо разделять на value-creating, complexity и failure labor.
- Управленческая отчётность преимущественно объясняет прошлое, а не предотвращает слабые решения.
- Налоговая эффективность определяется полной экономической стоимостью, а не минимальной номинальной ставкой.
- Наиболее опасна комбинация задержки оплаты, роста стоимости материалов и перегрузки мощности.

---

# Периметр Этапа 1

Диагностика охватывает:

- финансовую модель;
- доходы и структуру затрат;
- денежный поток и ликвидность;
- поток собственника;
- качество прибыли и cash conversion;
- себестоимость индивидуального пошива и товара;
- запасы, WIP и оборотный капитал;
- закупки и поставщиков;
- производство и планирование мощности;
- коммерческие каналы;
- ФОТ и кадровый контур;
- систему управления и RACI;
- управленческую отчётность и качество данных;
- налоговую нагрузку и юридические контуры;
- стратегические варианты;
- готовность к росту;
- стрессоустойчивость;
- систему раннего предупреждения.

Этап 1 формирует:

- интегрированный диагноз;
- корневые причины;
- карту утечки стоимости;
- Quality of Earnings;
- стратегические варианты и growth gates;
- stress test;
- карту рисков и резервов;
- value creation logic;
- target operating model;
- early warning architecture;
- решения собственника;
- программу Этапа 2.

Этап 1 не является фактическим внедрением управленческого учёта, ERP/PLM, налоговой реструктуризацией или постоянным сопровождением изменений.

---

# Структура репозитория

| Путь | Содержание |
|---|---|
| [`live/client_pack/final_stage1/`](live/client_pack/final_stage1/) | официальный клиентский пакет |
| [`live/client_pack/`](live/client_pack/) | тематические диагностические записки H-серии |
| [`live/marts/`](live/marts/) | расчётные витрины |
| [`live/registers/`](live/registers/) | регистры, builders и контрольные слои |
| [`live/maps/`](live/maps/) | карты данных и процессов |
| [`live/client_pack/sign_session_pack/`](live/client_pack/sign_session_pack/) | подтверждения owners и контрольные карточки |
| [`live/OPTIMIZATION_SCENARIOS.md`](live/OPTIMIZATION_SCENARIOS.md) | сценарии оптимизации |
| [`STATUS.md`](STATUS.md) | технический статус проекта |
| [`HANDOFF.md`](HANDOFF.md) | навигация для передачи контура |

---

# Доказательность

Каждый существенный вывод получает статус:

- `CONFIRMED`;
- `STRONG INDICATION`;
- `PARTIAL`;
- `NOT PROVEN`;
- `REFUTED`;
- `QUARANTINE`.

Ключевые документы:

- [`03_EVIDENCE_REGISTER.md`](live/client_pack/final_stage1/03_EVIDENCE_REGISTER.md);
- [`12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md`](live/client_pack/final_stage1/12_METHODOLOGY_DATA_QUALITY_AND_LIMITATIONS.md);
- [`15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md`](live/client_pack/final_stage1/15_CONTENT_QA_AND_CONSISTENCY_REVIEW.md);
- [`appendices/01_FINAL_METRICS_REGISTER.csv`](live/client_pack/final_stage1/appendices/01_FINAL_METRICS_REGISTER.csv).

---

# Headline facts

По текущей диагностической базе:

- индивидуальный пошив является главным доходным контуром;
- бизнес объединяет как минимум две экономически разные модели;
- нет подтверждённой полной unit-экономики индивидуального заказа;
- около **29,9 млн ₽** находится в сопоставленном остатке тканей;
- около **12,87 млн ₽** относится к материалам без подтверждённого движения более 365 дней;
- около **2,51 млн ₽** находится в открытом B2B-контуре;
- собственник как получал средства из бизнеса, так и вносил их обратно;
- штатный, договорной и платёжный контуры расходятся;
- значительная часть управления зависит от ручной координации и персонального знания.

Эти показатели сопровождаются методологическими ограничениями и не должны интерпретироваться вне соответствующих документов.

---

# P0 перед final freeze

1. Интеграция и дедупликация новых банковских выписок.
2. Transaction-level расчёт net owner cash flow.
3. Единая дата среза headline figures.
4. Подтверждение НДС и РСВ 2026-Q2 либо оговорка.
5. Проверка ЕНС.
6. Междокументная сверка ключевых цифр.
7. Согласование формы кадровых и персональных выводов.
8. Финальный metrics freeze.

---

# Принцип дальнейшей работы

Следующая работа должна быть направлена не на создание новых параллельных отчётов, а на:

- закрытие P0;
- обновление headline figures;
- сокращение повторов;
- фиксацию единой клиентской версии;
- подготовку приложений;
- сборку DOCX/PDF;
- подготовку презентации и протокола решений Этапа 2.
