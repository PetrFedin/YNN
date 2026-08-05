# YANINA — Этап 2

## Scope, deliverables and acceptance criteria

Updated: 2026-08-05  
Статус: клиентская проектная редакция по итогам диагностики Этапа 1

> Документ определяет рекомендуемый состав Этапа 2. Это не автоматическое обязательство на внедрение всех инициатив. Итоговый объём должен быть утверждён собственником после согласования приоритетов, ресурсов, сроков и допустимого уровня изменений.

---

# 1. Цель Этапа 2

Перевести выводы диагностики в работающую систему экономического управления, которая позволяет:

- видеть прибыльность заказа и канала;
- прогнозировать ликвидность;
- отделять свободный cash от обязательств;
- управлять WIP и запасами;
- контролировать стоимость сложности;
- снижать зависимость от собственника и ключевых сотрудников;
- закрывать месяц в установленный срок;
- оценивать полную налоговую стоимость модели;
- подтверждать фактический экономический эффект изменений.

Главный результат:

> **Каждый существенный заказ, запас, канал и денежный поток имеет понятную экономику, владельца, контрольный показатель и управленческое решение.**

---

# 2. Принципы выполнения

## 2.1. Сначала методология, затем автоматизация

Нельзя автоматизировать показатель, если не утверждены:

- определение;
- источник;
- единица анализа;
- владелец;
- правила корректировки;
- период закрытия.

## 2.2. Один источник правды для каждой метрики

Каждая headline-метрика должна иметь один утверждённый register и owner.

## 2.3. Пилот перед масштабированием

Unit-экономика, WIP и новые контрольные процессы сначала тестируются на ограниченном периметре.

## 2.4. Эффект подтверждается bridge

Ни одна потенциальная экономия не считается реализованной без:

- baseline;
- зафиксированного действия;
- периода сравнения;
- исключения внешних факторов;
- подтверждения P&L, cash или balance-sheet effect.

## 2.5. Персональные данные не включаются в публичный контур

Employee-level, bank-level и tax-level данные хранятся в защищённом периметре. В клиентском и публичном GitHub используются агрегированные и редактированные выводы.

---

# 3. Workstream A — Finance, Treasury and Liquidity

## 3.1. Задача

Создать единый денежный и финансовый контур, который отделяет операционный результат от внутренних переводов, owner flows и изменения оборотного капитала.

## 3.2. Deliverables

1. Единый реестр всех банковских счетов и карт.
2. Нормализованный transaction-level bank register.
3. Дедупликация PDF, Excel и альтернативных выгрузок.
4. Классификатор операций:
   - operating inflow;
   - operating outflow;
   - tax;
   - payroll;
   - supplier;
   - rent;
   - capex;
   - owner injection;
   - owner withdrawal;
   - interaccount transfer;
   - FX conversion;
   - unresolved cash withdrawal;
   - loan in/repayment;
   - refund;
   - unknown.
5. Расчёт net owner cash flow по месяцам.
6. 13-недельный rolling cash forecast.
7. Cash waterfall и минимальный liquidity buffer.
8. Двухконтурный ДДС.
9. Bridge «операционный результат → изменение cash».
10. Политика наличных и owner flows.

## 3.3. Входные данные

- все банковские выписки;
- реестр счетов;
- ДДС;
- эквайринг;
- B2B settlements;
- платежи ЦУМ;
- owner explanations;
- документы по займам и внесениям;
- авансовые отчёты.

## 3.4. Acceptance criteria

- 100% счетов имеют владельца, валюту, период и статус;
- дубликаты помечены и исключены;
- не менее 95% суммы банковских операций классифицировано;
- 100% внутренних переводов исключено из доходов и расходов;
- owner flows рассчитаны отдельно от operating cash;
- forecast обновляется еженедельно;
- forecast variance объясняется не менее чем на 90% суммы отклонения;
- установлен и утверждён cash buffer;
- месяц может быть закрыт без ручного поиска отсутствующих выписок.

## 3.5. KPI

- classified bank share;
- unknown transaction share;
- forecast accuracy;
- minimum cash coverage;
- owner funding dependency;
- overdue mandatory payments;
- weeks of fixed-cost coverage.

---

# 4. Workstream B — Two-Contour P&L and Management Balance

## 4.1. Задача

Сформировать доказательный финансовый результат индивидуального пошива, товарного бизнеса и компании в целом.

## 4.2. Deliverables

1. P&L индивидуального пошива.
2. P&L товарного бизнеса по каналам.
3. Shared-cost layer.
4. Правила распределения общих расходов.
5. Консолидированный P&L.
6. Управленческий баланс.
7. AR/AP register.
8. WIP and inventory bridge.
9. Monthly close calendar D+10.
10. Management commentary по отклонениям.

## 4.3. Методологические решения

Необходимо утвердить:

- момент признания дохода;
- правила авансов;
- direct и indirect costs;
- allocation drivers;
- WIP valuation;
- inventory changes;
- treatment of owner flows;
- intercompany operations;
- FX differences;
- tax accruals.

## 4.4. Acceptance criteria

- два P&L сходятся в консолидированный результат;
- shared costs имеют утверждённый driver;
- ДДС, P&L и баланс логически связаны;
- unexplained bridge не превышает утверждённый порог;
- месяц закрывается до D+10 два последовательных периода;
- каждая headline-метрика имеет owner и источник;
- open items имеют статус FINAL / ESTIMATE / OPEN.

## 4.5. KPI

- close cycle days;
- unexplained P&L-to-cash bridge;
- share of estimated costs;
- overhead allocation coverage;
- management balance completeness.

---

# 5. Workstream C — Unit Economics of Bespoke Orders

## 5.1. Задача

Создать экономику главного продукта на уровне заказа.

## 5.2. Пилотный периметр

20–30 заказов, включающих:

- разные ценовые уровни;
- разную сложность;
- стандартные и срочные заказы;
- заказы с изменениями;
- разные типы материалов;
- успешные и проблемные сроки;
- разные клиентские сценарии.

## 5.3. Deliverables

1. Order economics card.
2. Expected margin до принятия заказа.
3. Actual margin после закрытия.
4. Complexity coefficients.
5. Rush premium logic.
6. Change-order policy.
7. Discount approval rules.
8. Rework register.
9. Make-or-buy decision model.
10. Post-order profitability review.

## 5.4. Поля карточки заказа

- клиентский идентификатор;
- тип изделия;
- цена;
- скидка;
- аванс;
- материал;
- фурнитура;
- прямой труд;
- внешние работы;
- число примерок;
- изменения;
- срочность;
- логистика;
- накладные;
- expected completion;
- actual completion;
- expected margin;
- actual margin;
- variance reason.

## 5.5. Acceptance criteria

- не менее 90% пилотных заказов имеют полный expected cost;
- не менее 80% закрытых пилотных заказов имеют actual cost;
- отклонение expected/actual объяснено по основным драйверам;
- утверждён минимальный margin threshold;
- утверждены правила скидки, срочности и изменений;
- каждый новый пилотный заказ проходит margin and capacity gate;
- rework имеет причину и владельца.

## 5.6. KPI

- expected gross contribution;
- actual gross contribution;
- margin variance;
- rework cost rate;
- unbilled change value;
- order cycle time;
- final payment delay;
- bottleneck hours per order.

---

# 6. Workstream D — WIP and Capacity Management

## 6.1. Задача

Показать стоимость, сроки и риски всех открытых заказов, а также доступную производственную мощность.

## 6.2. Deliverables

1. WIP register.
2. Stage model заказа.
3. Expected completion date.
4. Future cost to complete.
5. Material readiness status.
6. Bottleneck load model.
7. Weekly WIP review.
8. Capacity gate.
9. Delay root-cause register.
10. Escalation rules.

## 6.3. Acceptance criteria

- 100% активных заказов присутствуют в WIP register;
- каждый заказ имеет стадию, срок, владельца и future cost;
- просроченные заказы имеют причину и corrective action;
- bottleneck capacity видна минимум на 8 недель;
- новые заказы не принимаются без capacity check;
- WIP aging обновляется еженедельно.

## 6.4. KPI

- WIP value;
- WIP aging;
- on-time completion;
- bottleneck utilization;
- overdue order count;
- future cost to complete;
- rework hours.

---

# 7. Workstream E — Inventory and Working Capital

## 7.1. Задача

Перевести запас из учётного остатка в управляемый портфель капитала.

## 7.2. Deliverables

1. Единый inventory register.
2. Item-level review 668 долгих позиций.
3. Классификация:
   - strategic;
   - reserved;
   - usable for bespoke;
   - capsule/rework;
   - sell/return;
   - archive;
   - write-off candidate;
   - physically missing.
4. ABC/aging.
5. Reservation logic.
6. No-buy-if-stock rule.
7. Trims register.
8. Finished goods aging.
9. Monthly working-capital committee.
10. Benefit register по предотвращённым закупкам и возвращённому cash.

## 7.3. Acceptance criteria

- 100% A-class долгого остатка физически подтверждено;
- 100% A-class имеет owner decision;
- позиции имеют назначение и дату следующего review;
- новая закупка содержит проверку свободного остатка;
- дорогая и критичная фурнитура включена в register;
- B2B open закрыт документно;
- inventory benefit не смешивается с бухгалтерским списанием.

## 7.4. KPI

- inventory without decision;
- >365 day stock value;
- prevented purchase value;
- stock utilization from old inventory;
- B2B overdue;
- WIP and stock cash absorption;
- inventory write-off rate.

---

# 8. Workstream F — Procurement and Supplier Management

## 8.1. Задача

Связать закупку с подтверждённой потребностью, полным landed cost и сроком возврата капитала.

## 8.2. Deliverables

1. Supplier master.
2. Purchase request form.
3. Stock availability check.
4. Total landed cost.
5. Lead-time tracking.
6. MOQ impact.
7. Supplier scorecard.
8. FX and import bridge.
9. Approval matrix.
10. Post-purchase review.

## 8.3. Acceptance criteria

- каждый поставщик имеет единый идентификатор;
- закупка связана с заказом, коллекцией или утверждённым stock policy;
- до закупки проверяется остаток;
- импортная закупка включает FX, пошлины, НДС и логистику;
- срочная закупка выделяется отдельно;
- supplier performance оценивается минимум по цене, сроку и качеству.

## 8.4. KPI

- emergency purchase share;
- purchase price variance;
- supplier lead-time variance;
- MOQ excess value;
- stock-backed purchase share;
- supplier defect rate.

---

# 9. Workstream G — Channel and Product Economics

## 9.1. Задача

Оценивать каналы и товарные инвестиции по contribution и скорости возврата капитала.

## 9.2. Deliverables

1. Channel P&L.
2. Product margin and reported margin.
3. ЦУМ dual view.
4. Return and commission bridge.
5. Sell-through by collection.
6. Markdown exposure.
7. Capital-adjusted contribution.
8. Investment limit per collection.
9. Stop-loss rules.
10. Channel owner review.

## 9.3. Acceptance criteria

- каждый канал имеет единое определение net sales;
- комиссия и возвраты отражаются последовательно;
- SKU имеет единую себестоимость;
- инвестиции в партию имеют лимит;
- повторное производство основано на sell-through;
- закрытие/масштабирование канала не принимается по одной gross margin.

## 9.4. KPI

- net sales;
- contribution margin;
- sell-through;
- return rate;
- markdown rate;
- inventory days;
- capital-adjusted contribution.

---

# 10. Workstream H — Governance, Reporting and Data

## 10.1. Задача

Перевести управление от персональной памяти и ручной координации к единому ритму решений.

## 10.2. Deliverables

1. End-to-end RACI.
2. KPI dictionary.
3. Data owners.
4. Master-data model.
5. Close calendar.
6. Weekly cash/WIP meeting.
7. Monthly performance review.
8. Working-capital committee.
9. Decision log.
10. Early-warning dashboard.

## 10.3. Acceptance criteria

- каждый critical outcome имеет одного Accountable;
- KPI имеют определение, источник и action;
- управленческие встречи завершаются decision log;
- просроченное действие эскалируется;
- один показатель не рассчитывается разными способами в разных файлах;
- новые IT-требования основаны на утверждённой методологии.

## 10.4. KPI

- action closure rate;
- data timeliness;
- metric reconciliation issues;
- close cycle;
- manual adjustment count;
- unresolved exceptions.

---

# 11. Workstream I — People, Payments and Capacity

## 11.1. Задача

Согласовать фактическую модель людей, договоров, выплат и производственной мощности.

## 11.2. Deliverables

1. Unified roster.
2. Role and department mapping.
3. Legal-entity mapping.
4. Contract and payment basis.
5. Regular/one-off payment control.
6. Bottleneck skill map.
7. Key-person risk map.
8. Productivity framework.
9. Contractor/self-employed register.
10. Payment approval gate.

## 11.3. Acceptance criteria

- каждый получатель выплат присутствует в roster;
- у каждой выплаты есть основание;
- статус человека и юридический контур подтверждены;
- функции связаны с cost center/order where relevant;
- key-person risks имеют mitigation;
- персональные данные защищены.

## 11.4. KPI

- unmatched recipient count;
- payment without basis count;
- roster completeness;
- bottleneck vacancy/overload;
- productive vs rework hours;
- contractor compliance coverage.

---

# 12. Workstream J — Tax Management Diagnostic and Scenarios

## 12.1. Задача

Сформировать управленческое понимание полной налоговой стоимости текущей и альтернативных моделей.

## 12.2. Deliverables

1. Tax passport по каждому юридическому лицу.
2. Реестр деклараций и обязательств.
3. Начисление ↔ декларация ↔ ЕНС ↔ платёж.
4. Effective tax burden.
5. VAT scenario model.
6. Input VAT and import bridge.
7. Intercompany operations map.
8. Cash and personnel risk map.
9. Closure plan по неактивным контурам.
10. Memo для внешнего налогового консультанта.

## 12.3. Acceptance criteria

- обязательные документы имеют статус HAVE / OPEN / SCAN;
- начисления и платежи сверены;
- ЕНС объяснён;
- сценарии сравниваются по полной экономической стоимости;
- юридические выводы не выдаются без профильной экспертизы;
- налоговый эффект не смешивается с временным cash timing.

## 12.4. KPI

- filing completeness;
- tax reconciliation gap;
- effective tax burden;
- VAT cash cost;
- unutilized input VAT where applicable;
- open tax items;
- compliance action closure.

---

# 13. Рекомендуемые волны реализации

## Wave 0 — Data and Control Foundation, 2–4 недели

- bank register;
- deduplication;
- owner-flow classification;
- unified roster;
- KPI definitions;
- WIP population;
- A-class inventory list;
- Stage 2 governance.

## Wave 1 — Liquidity and Unit Economics, 4–8 недель

- 13-week cash forecast;
- order economics pilot;
- WIP review;
- B2B closure;
- inventory decisions;
- cash and owner policies.

## Wave 2 — P&L, Balance and Operating Model, 8–16 недель

- two-contour P&L;
- management balance;
- close D+10;
- channel contribution;
- supplier scorecard;
- tax scenarios;
- early-warning system.

## Wave 3 — Scale and Automation, after methodology freeze

- system requirements;
- ERP/PLM/BI selection;
- automation;
- scaled unit economics;
- benefit tracking;
- controlled growth.

---

# 14. Decision gates

Переход к следующей волне осуществляется только при выполнении gate.

## Gate 1 — Data readiness

- полные счета;
- дедупликация;
- утверждённые definitions;
- владельцы данных.

## Gate 2 — Economic visibility

- expected margin;
- WIP;
- cash forecast;
- owner flow;
- inventory decisions.

## Gate 3 — Management close

- P&L;
- balance;
- contribution;
- D+10 close;
- action owners.

## Gate 4 — Automation readiness

- стабильный процесс минимум два периода;
- утверждённые master data;
- низкая доля ручных корректировок;
- согласованные requirements.

---

# 15. Benefit tracking

Каждый эффект должен классифицироваться:

- P&L benefit;
- cash benefit;
- balance-sheet release;
- capacity release;
- risk reduction;
- avoided cost.

Обязательные поля benefit register:

- initiative;
- owner;
- baseline;
- calculation method;
- start date;
- gross effect;
- implementation cost;
- net effect;
- cash timing;
- evidence;
- finance validation;
- status.

Запрещается двойной учёт, например:

- prevented purchase и inventory cash release как двух разных эффектов для одной позиции;
- снижение rework и высвобождение часов без проверки, были ли часы реально использованы;
- налоговый timing и постоянная налоговая экономия;
- collected B2B receivable и revenue growth.

---

# 16. Роли сторон

## Заказчик

- предоставляет полные данные;
- назначает process owners;
- принимает методологические решения;
- обеспечивает участие команды;
- утверждает policies;
- реализует кадровые и юридические изменения;
- принимает риск-аппетит.

## Консультант

- разрабатывает методологию;
- консолидирует и анализирует данные;
- формирует модели и шаблоны;
- фасилитирует решения;
- контролирует качество;
- обучает owners;
- подтверждает benefit logic;
- фиксирует ограничения.

## Внешние специалисты

Профильный налоговый консультант, юрист, бухгалтер или IT-интегратор привлекаются для вопросов, выходящих за границы управленческой диагностики.

---

# 17. Что не входит автоматически

Без отдельного согласования не входят:

- юридическое налоговое заключение;
- подача уточнённых деклараций;
- судебная или претензионная работа;
- физическая инвентаризация силами консультанта;
- кадровое переоформление;
- бухгалтерское восстановление;
- разработка ERP;
- лицензии и интеграционные расходы;
- постоянное казначейство;
- управление компанией вместо менеджмента.

---

# 18. Финальный критерий успеха Этапа 2

Этап 2 считается успешным не тогда, когда создано много таблиц, а когда руководство может регулярно и доказательно ответить:

1. сколько бизнес заработал;
2. какой заказ и канал создал результат;
3. сколько денег свободно;
4. сколько связано обязательствами;
5. какой капитал находится в WIP и запасах;
6. где возникло отклонение;
7. кто владелец;
8. какое действие принято;
9. какой эффект подтверждён;
10. может ли бизнес расти без увеличения зависимости от собственника.

> **Результат Этапа 2 — не отчётность как архив прошлого, а система, которая повышает качество решения до того, как деньги и ресурс уже потрачены.**
