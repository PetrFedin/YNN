# Contract Scope Alignment and Deliverable Coverage

## Соответствие текущего пакета исходному коммерческому предложению и границы Этапов 1–2

**YANINA — комплексная диагностика бизнеса**  
Updated: 2026-08-06  
Статус: **client-scope alignment draft; требуется терминологическое утверждение до release**

> Документ сопоставляет исходно заявленный периметр проекта с фактически сформированным клиентским пакетом. Его задача — исключить риск, что заказчик воспримет различие в названиях этапов как отсутствие части работ, а также отделить аналитические результаты диагностики от фактического внедрения управленческой системы.

---

# 1. Главная терминологическая проблема

В исходном коммерческом предложении проект представлен как программа из пяти последовательных этапов:

1. первичная диагностика бизнеса;
2. финансовая диагностика и анализ оборотного капитала;
3. операционная диагностика;
4. разработка целевой модели;
5. программа трансформации и внедрения.

В текущем репозитории используется другая логика:

- **Этап 1 — комплексная диагностика бизнеса**;
- **Этап 2 — построение и внедрение скорректированной модели управления**.

Фактически текущий Этап 1 включает:

- содержание исходных этапов 1–3;
- аналитическое проектирование значительной части исходного этапа 4;
- предварительный roadmap, KPI, decision architecture и acceptance criteria для исходного этапа 5.

При этом фактическое внедрение, регулярное сопровождение и подтверждение реализованного эффекта остаются Этапом 2.

> **Без прямого пояснения заказчик может ошибочно сопоставить текущий «Этап 1» только с первичной диагностикой из коммерческого предложения и решить, что финансовая и операционная диагностика не выполнены.**

---

# 2. Рекомендуемая единая терминология

Для финального клиентского пакета рекомендуется использовать двухуровневую модель.

## Этап 1. Комплексная диагностика и проектирование целевой модели

Включает:

- первичную диагностику;
- финансовую диагностику;
- анализ ликвидности и оборотного капитала;
- операционную диагностику;
- диагностику процессов и управления;
- налогово-экономическую оценку;
- интегрированный диагноз;
- risk-adjusted карту резервов;
- целевую финансовую и операционную архитектуру;
- решения собственника;
- scope и acceptance criteria Этапа 2.

## Этап 2. Внедрение, пилотирование и подтверждение эффекта

Включает:

- unit-economics pilot;
- two-contour P&L;
- management balance;
- rolling treasury;
- WIP and inventory governance;
- process gates;
- KPI and management cadence;
- tax scenarios and selected legal review;
- dashboards and automation requirements;
- implementation support;
- benefit validation.

---

# 3. Матрица покрытия обещанных результатов

| Результат из исходного предложения | Текущий статус | Что уже есть | Что ещё требуется |
|---|---|---|---|
| Executive Summary для собственника | ГОТОВО ПО СОДЕРЖАНИЮ | Board Report, heatmap, board conclusions | numerical freeze, copyedit, DOCX/PDF |
| Комплексная финансовая диагностика | ГОТОВО ПО СОДЕРЖАНИЮ | Master Report, financial model, QoE, impact bridge | final metrics freeze, bank/owner closure |
| Карта причин кассовых разрывов | ГОТОВО | causal synthesis, liquidity diagnosis, value-leakage map | итоговая редакционная консолидация |
| Анализ ликвидности | ГОТОВО С ОГРАНИЧЕНИЯМИ | bank register, reconciliations, liquidity findings | full bank deduplication, net owner flow, common cut-off |
| Анализ оборотного капитала | ГОТОВО С ОГРАНИЧЕНИЯМИ | fabrics aging, B2B open, inventory exposure | full WIP, trims, AR/AP, item-level decisions |
| Анализ прибыльности клиентов | ЧАСТИЧНО | общая логика клиентской и order economics | customer-level profitability requires Stage 2 data model |
| Анализ прибыльности каналов | ЧАСТИЧНО/ВЫСОКАЯ ГОТОВНОСТЬ | IM, B2B, TSUM margin views | full direct costs, capital-adjusted contribution |
| Анализ прибыльности продуктовых направлений | ЧАСТИЧНО | two-contour logic, goods analysis | full bespoke order economics, product/customer allocation |
| Карта процессов AS IS | ГОТОВО НА ДИАГНОСТИЧЕСКОМ УРОВНЕ | causal maps, process findings, control gaps | detailed BPMN/value-stream mapping where needed |
| Карта процессов TO BE | ГОТОВО КАК АРХИТЕКТУРА | target operating model, target financial architecture, gates | detailed procedures, pilots and implementation |
| Реестр инициатив | ГОТОВО | findings-to-actions, decision agenda, priority matrix | owner confirmation and launch sequencing |
| Финансовая модель потенциального эффекта | ГОТОВО КАК GOVERNANCE | risk-adjusted reserve portfolio, benefit governance | quantified baseline and pilot evidence |
| Дорожная карта внедрения | ГОТОВО | Stage 2 scope, 30/90/180-day priorities | calendar, named owners, approved resources |
| KPI Framework | ГОТОВО КАК DESIGN | early-warning architecture and KPI set | operational dashboards and recurring reporting |
| Матрица ответственности | ГОТОВО КАК TARGET | target RACI and accountability principles | owner confirmation and formal regulations |
| Комплект управленческих дашбордов | НЕ ВНЕДРЁН | dashboard logic and metric architecture | actual dashboard build after methodology freeze |
| Сопровождение внедрения | НЕ ОТНОСИТСЯ К ЗАВЕРШЕНИЮ ЭТАПА 1 | Stage 2 scope and workshop protocol | separate implementation engagement |

---

# 4. Что покрыто полностью на уровне Этапа 1

## 4.1. Диагностический диагноз

Сформировано доказательное объяснение:

- почему высокий оборот не равен прибыли;
- почему значительные поступления не равны свободному cash;
- почему бизнес может испытывать кассовое давление при сильном продукте;
- где капитал связан в inventory, WIP и открытых расчётах;
- как complexity, rework, capacity и tax влияют на financial outcome;
- почему текущая reporting architecture запаздывает.

## 4.2. Корневые причины

Выявлены первичные механизмы:

- economic checks after the decision;
- отсутствие order-level economics;
- смешение двух экономических контуров;
- использование авансов как общего cash pool;
- отсутствие назначения части капитала в запасах;
- неполный WIP and cost-to-complete;
- fragmented data and delayed close;
- owner as informal treasury;
- несинхронизированные people/payment/tax contours.

## 4.3. Целевая архитектура

Сформированы:

- target financial architecture;
- target operating model;
- management cadence;
- decision gates;
- risk-adjusted reserve portfolio;
- Stage 2 workstreams;
- acceptance criteria;
- benefit governance.

---

# 5. Что покрыто частично и требует прямого раскрытия

## 5.1. Полный P&L и EBITDA

Полный доказательный P&L компании не сформирован, поскольку отсутствует order-level COGS главного доходного контура и полный management balance.

Поэтому нельзя заявлять:

- точную EBITDA;
- точную чистую прибыль;
- окончательную прибыльность bespoke;
- нормализованный free cash flow.

## 5.2. Клиентская прибыльность

Данные позволяют сформировать методологию и гипотезы, но не полный рейтинг клиентов по contribution и capital use.

## 5.3. Производственная производительность

Выявлены сильные индикаторы rework, bottleneck and coordination cost, но отсутствует time/activity model для точной оценки эффекта.

## 5.4. Полный working capital

Ткани и B2B проанализированы глубоко. Фурнитура, WIP и полный AR/AP требуют дальнейшей постановки.

## 5.5. Налоговая оптимизация

Подготовлена tax-economics assessment, но конкретная реструктуризация требует scenario model и юридического налогового заключения.

---

# 6. Что не должно быть представлено как выполненное внедрение

Следующие результаты спроектированы, но ещё не функционируют как регулярная система:

- еженедельный 13-week cash forecast;
- two-contour monthly P&L;
- management balance;
- order economics for all orders;
- unified WIP register;
- working-capital committee;
- D+10 close for two consecutive months;
- operational KPI dashboards;
- formal end-to-end RACI;
- tax scenario implementation;
- realised benefit tracking.

Корректная формулировка:

> Этап 1 сформировал целевую архитектуру, методологию, приоритеты и программу внедрения. Регулярное функционирование системы и доказательство эффекта являются предметом Этапа 2.

---

# 7. Главный риск коммерческого несоответствия

В исходном предложении встречаются формулировки:

- рост EBITDA;
- высвобождение капитала;
- комплект дашбордов;
- карта TO BE;
- программа трансформации;
- сопровождение внедрения.

В финальном отчёте необходимо ясно разделить:

1. **diagnostic finding**;
2. **potential effect**;
3. **designed solution**;
4. **implemented process**;
5. **realised financial result**.

Нельзя использовать эти категории как взаимозаменяемые.

> **Разработанная модель не равна внедрённой модели, а выявленный резерв не равен реализованному финансовому эффекту.**

---

# 8. Что необходимо сделать до передачи

1. Утвердить единую терминологию Этапов 1–2.
2. Добавить в Board Report раздел «Соответствие заявленному периметру».
3. Указать, какие deliverables готовы, готовы с ограничениями, спроектированы или перенесены в implementation.
4. Удалить обещания EBITDA или cash release без подтверждённого bridge.
5. Зафиксировать границы customer profitability, WIP, productivity and tax optimisation.
6. Согласовать, входит ли фактическая сборка dashboards в текущий договор или Этап 2.
7. Привязать Stage 2 scope к исходным этапам 4–5 коммерческого предложения.
8. В decision workshop письменно подтвердить acceptance текущего диагностического периметра.

---

# 9. Рекомендуемая формулировка для заказчика

> В рамках Этапа 1 выполнена комплексная финансовая, операционная и управленческая диагностика, соответствующая диагностическому периметру исходного предложения. Дополнительно сформированы целевая архитектура, приоритеты изменений и требования к внедрению. Фактическая постановка регулярного P&L, treasury, WIP, KPI, dashboards и подтверждение реализованного финансового эффекта относятся к Этапу 2.

---

# 10. Итоговое заключение

Текущий пакет по содержанию существенно шире первичной диагностики и покрывает основной аналитический периметр исходного коммерческого предложения.

Главный оставшийся вопрос — не объём анализа, а корректная коммерческая упаковка:

- единая терминология;
- явная матрица покрытия deliverables;
- раскрытие ограничений;
- разделение диагностики, проектирования, внедрения и realised benefit.

> **До release необходимо доказать заказчику не только качество выводов, но и соответствие результата обещанному периметру — без завышения фактической степени внедрения.**
