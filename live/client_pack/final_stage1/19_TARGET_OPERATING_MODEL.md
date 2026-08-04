# Target Operating Model — целевая модель управления YANINA

**Этап 1: архитектура целевого состояния**  
Updated: 2026-08-05  
Статус: клиентская аналитическая редакция  

> Документ не является детальным планом внедрения. Он определяет, какой должна стать система управления бизнесом, чтобы сильный продукт превращался в предсказуемую маржу, управляемый капитал и устойчивый денежный поток.

---

# 1. Принципы целевой модели

Целевая operating model должна соответствовать пяти принципам.

## Принцип 1. Управление по экономическому результату

Единицей управления является не только функция или статья расхода, а результат:

- заказ;
- изделие;
- коллекция;
- канал;
- клиент;
- капитал.

## Принцип 2. Решение принимается до возникновения расхода

Контроль должен происходить:

- до принятия заказа;
- до обещания срока;
- до закупки;
- до запуска производства;
- до выплаты собственнику;
- до изменения налоговой структуры.

## Принцип 3. Один результат — один Accountable

Несколько функций могут участвовать, но итоговый результат имеет одного владельца.

## Принцип 4. Данные являются частью процесса

Источник, идентификатор, статус и срок обновления определяются вместе с процессом, а не восстанавливаются после его завершения.

## Принцип 5. Исключение имеет отдельную цену и маршрут

Уникальность продукта сохраняется, но отклонение от стандартного процесса:

- распознаётся;
- оценивается;
- согласуется;
- монетизируется;
- получает owner.

---

# 2. Текущая и целевая модель

| Область | Текущее состояние | Целевое состояние |
|---|---|---|
| Финансовая модель | кассовые и функциональные срезы | заказ/SKU/channel P&L + consolidated P&L |
| Ликвидность | управление по остатку и срочным приоритетам | 13-недельный forecast + cash waterfall |
| Индивидуальный заказ | цена и исполнение управляются экспертно | expected/actual margin + change-order control |
| Производство | высокая ручная координация | capacity gate + WIP control + exception management |
| Закупки | локальная потребность и срочность | demand-backed purchase gate + stock check |
| Запасы | остаток виден, назначение неполно | portfolio of capital with mandatory disposition |
| ФОТ | сумма известна, причинность ограничена | value-creating vs complexity/failure labor |
| Каналы | несколько версий маржи | channel contribution + capital employed |
| Собственник | интегратор и финансовый стабилизатор | стратегический capital allocator и exception approver |
| Налоги | платежи и документы по контурам | tax economics, calendar, EНС и legal-entity passport |
| Отчётность | восстановление факта | decision-driven alerts + D+10 close |
| Данные | разные файлы и идентификаторы | единые master data и data ownership |

---

# 3. Архитектура управленческих контуров

Целевая модель состоит из восьми взаимосвязанных контуров.

## Контур 1. Commercial and Order Governance

Отвечает за:

- квалификацию заказа;
- сложность;
- pricing;
- скидки;
- условия оплаты;
- срок;
- change orders;
- expected margin.

### Обязательные контрольные точки

1. client brief approved;
2. complexity class assigned;
3. preliminary cost calculated;
4. capacity confirmed;
5. material confirmed;
6. commercial terms approved;
7. cash schedule agreed.

### Основной результат

Заказ не принимается без экономического и производственного подтверждения.

---

## Контур 2. Product Development and Production Control

Отвечает за:

- техническую разработку;
- маршрут изделия;
- плановую трудоёмкость;
- загрузку;
- WIP;
- качество;
- переделки;
- завершение.

### Ключевые статусы

- brief;
- design approved;
- materials ready;
- construction;
- sample/mock-up;
- fitting;
- production;
- finishing;
- QC;
- ready;
- delivered;
- closed.

### Основной результат

Для каждого заказа видны стадия, blocker, remaining cost, next action и дата финального cash collection.

---

## Контур 3. Procurement and Supplier Management

Отвечает за:

- потребность;
- проверку склада;
- резерв;
- выбор поставщика;
- цену;
- MOQ;
- срок;
- landed cost;
- качество;
- претензии.

### Purchase gate

Закупка не утверждается без:

- заказа или утверждённого плана;
- проверки доступного аналога;
- подтверждённого количества;
- полной стоимости;
- cash impact;
- owner approval.

### Основной результат

Закупка поддерживает подтверждённую маржу и не создаёт необоснованный запас.

---

## Контур 4. Inventory and Working Capital Governance

Отвечает за:

- сырьё;
- фурнитуру;
- материалы у подрядчиков;
- WIP;
- готовый товар;
- AR/AP;
- aging;
- disposition decisions.

### Capital committee

Ежемесячно рассматривает:

- старый запас;
- незавершённые заказы;
- B2B overdue;
- закупки при наличии аналога;
- slow-moving finished goods;
- supplier advances;
- customer advances.

### Основной результат

У каждого существенного актива есть владелец, назначение и ожидаемая дата возврата в cash.

---

## Контур 5. Finance, Treasury and Performance Management

Отвечает за:

- P&L;
- ДДС;
- баланс;
- forecast;
- payment calendar;
- cash buffer;
- owner flows;
- deviation analysis.

### Управленческая архитектура

1. MD/order economics;
2. goods/channel economics;
3. shared costs;
4. legal entity view;
5. consolidated view.

### Основной результат

Руководство видит не только факт денег, но прибыль, капитал, обязательства и прогноз.

---

## Контур 6. People and Capacity Management

Отвечает за:

- roster;
- роли;
- договоры;
- оплату;
- мощность;
- загрузку;
- дефицитные навыки;
- производительность;
- succession risk.

### Основной принцип

ФОТ управляется через стоимость создаваемого результата, а не через общий процент сокращения.

### Основной результат

Компания понимает:

- какая мощность доступна;
- где узкое место;
- сколько стоит операция;
- какие часы создают ценность;
- где возникают переделки и ожидание.

---

## Контур 7. Tax and Legal Entity Governance

Отвечает за:

- налоговый паспорт;
- начисления;
- платежи;
- ЕНС;
- НДС;
- импорт;
- кадровые основания;
- межконтурные договоры;
- завершение неактивных юридических лиц.

### Основной результат

Юридическая и налоговая модель соответствует фактическим функциям и полной экономической стоимости бизнеса.

---

## Контур 8. Data and Management Reporting

Отвечает за:

- master data;
- единые идентификаторы;
- KPI dictionary;
- качество данных;
- release status;
- D+10 close;
- dashboard and alerts.

### Основной результат

Один показатель имеет одну формулу, один источник, одного владельца и понятное управленческое применение.

---

# 4. Целевая end-to-end модель индивидуального заказа

## Этап 1. Commercial qualification

Выход:

- brief;
- complexity class;
- preliminary price;
- payment schedule;
- target margin;
- target date.

## Этап 2. Economic and capacity gate

Проверяются:

- материал;
- трудоёмкость;
- внешние работы;
- мощность;
- срок;
- cash requirement;
- risk reserve.

Выход — approve / reprice / redesign / reject.

## Этап 3. Development

Контролируются:

- эскиз;
- конструкция;
- технические изменения;
- frozen specification;
- planned material and labor.

## Этап 4. Production

Контролируются:

- WIP stage;
- actual consumption;
- actual labor;
- blocker;
- rework;
- quality;
- expected completion.

## Этап 5. Commercial close

Контролируются:

- delivery;
- final payment;
- discount/change reconciliation;
- customer acceptance.

## Этап 6. Economic close

Формируются:

- actual margin;
- variance by root cause;
- lessons learned;
- client/order profitability;
- update of norms.

---

# 5. Целевая модель управленческого ритма

## Еженедельно

### Cash and commitments meeting

- 13-week cash forecast;
- обязательные платежи;
- owner flows;
- supplier risk;
- customer collections;
- cash buffer.

### WIP and capacity meeting

- overdue orders;
- critical blockers;
- capacity conflicts;
- rework;
- final payments at risk.

## Ежемесячно

### D+10 performance review

- P&L;
- cash bridge;
- balance;
- order margin;
- channel contribution;
- inventory aging;
- B2B overdue;
- payroll and productivity;
- taxes;
- benefit register.

### Capital committee

- old inventory;
- purchase avoidance;
- WIP capital;
- AR/AP;
- investment requests;
- owner distribution capacity.

## Ежеквартально

### Portfolio and strategy review

- client and order profitability;
- collection performance;
- channel portfolio;
- capacity investment;
- tax scenarios;
- legal structure;
- transformation benefits.

---

# 6. Decision rights

| Решение | Function owner | Approver / Accountable | Escalation trigger |
|---|---|---|---|
| стандартный заказ | commercial/order owner | delegated approver | margin или complexity ниже/выше порога |
| скидка | commercial | margin owner | contribution ниже threshold |
| срочный заказ | production + finance | designated director | capacity/cash breach |
| новая закупка | procurement | inventory capital owner | нет заказа, высокий MOQ, старый аналог |
| старый запас | inventory committee | owner of capital | A-class, >age threshold |
| owner distribution | treasury | собственник | cash buffer breach |
| налоговая структура | finance/tax | собственник | legal opinion required |
| найм | function | capacity owner | fixed-cost threshold |
| автоматизация | process owner | transformation sponsor | process not stabilized |

---

# 7. Целевая система KPI

## Клиент и коммерция

- order conversion;
- expected margin;
- average discount;
- paid complexity;
- final payment delay.

## Производство

- WIP days;
- on-time delivery;
- rework hours;
- capacity utilization;
- actual vs planned labor.

## Материалы и закупки

- material variance;
- stock reuse;
- purchase avoided;
- supplier OTIF;
- landed-cost variance.

## Финансы

- contribution margin;
- free cash flow;
- forecast accuracy;
- cash buffer breaches;
- cash conversion cycle.

## Запасы

- inventory aging;
- disposition coverage;
- WIP capital;
- AR overdue;
- AP overdue.

## Люди

- direct/indirect labor;
- contribution per bottleneck hour;
- rework share;
- roster completeness;
- key-person dependency.

## Налоги

- effective tax rate;
- obligations paid on time;
- EНС reconciliation;
- input VAT coverage;
- open compliance gaps.

---

# 8. Минимальные управленческие продукты

Целевая модель должна регулярно выпускать:

1. 13-week cash forecast;
2. payment calendar;
3. owner cash-flow statement;
4. order economics report;
5. WIP register;
6. inventory aging and disposition report;
7. B2B collection report;
8. channel contribution report;
9. P&L by contour;
10. management balance sheet;
11. tax calendar and EНС reconciliation;
12. management action log;
13. benefit register.

---

# 9. Зрелость внедрения

## Level 1. Visible

Данные собраны и основные потоки видны.

## Level 2. Controlled

Есть owner, правила, сроки и контроль отклонений.

## Level 3. Predictable

Финансовый и операционный результат прогнозируется с приемлемой точностью.

## Level 4. Optimized

Ресурсы перераспределяются по contribution и return on capital.

## Level 5. Scalable

Рост объёма не требует пропорционального роста ручной координации.

### Текущая позиция

Большинство управленческих контуров находятся между Level 1 и Level 2; продуктовая экспертиза и способность исполнения — выше.

### Цель Этапа 2

Перевести критические финансовые и операционные контуры в Level 2–3.

---

# 10. Что необходимо стандартизировать, а что сохранить индивидуальным

## Стандартизировать

- финансовую методологию;
- идентификаторы;
- статусы;
- approval points;
- планирование мощности;
- закупочный gate;
- change-order process;
- WIP;
- закрытие месяца;
- налоговый календарь;
- responsibility and escalation.

## Сохранить индивидуальным

- творческую концепцию;
- клиентскую персонализацию;
- художественные решения;
- работу с редкими материалами;
- уникальные techniques;
- стратегические исключения.

> Целевая модель не должна бюрократизировать творчество. Она должна стандартизировать экономическую и операционную инфраструктуру вокруг творчества.

---

# 11. Условия успешного перехода

1. Собственник утверждает decision rights и cash policy.
2. Назначены owners сквозных результатов.
3. Финансовая и процессная методология утверждается до IT.
4. Пилот проводится на реальных заказах.
5. Baseline фиксируется до изменений.
6. Исключения не скрываются, а классифицируются.
7. Показатели используются для решений, а не только для отчётности.
8. Внедрение идёт волнами Stabilize → Control → Scale.

---

# 12. Итог

Целевая модель YANINA должна сохранить уникальность продукта и высокий уровень профессионального мастерства, но убрать зависимость экономического результата от неформальных связей, памяти сотрудников и ежедневного вмешательства собственника.

> **Целевое состояние — это бизнес, в котором сложность продукта является источником оплачиваемой ценности, а не источником непрозрачных затрат и кассовой волатильности.**
