# Risk-Adjusted Risk and Reserve Portfolio

## Сводная матрица ограничений, рисков и потенциальных резервов YANINA

Updated: 2026-08-06  
Статус: **финальная содержательная клиентская редакция; numerical freeze после закрытия P0**

> Матрица не суммирует все выявленные суммы как гарантированную экономию. Она разделяет подтверждённый факт, exposure, возможный механизм эффекта и реализованный benefit. Для каждой зоны отдельно оцениваются финансовый маршрут, доказательность, управляемость, срок эффекта и риск ошибочного решения.

---

# 1. Основной принцип

В диагностике необходимо различать четыре понятия.

## 1.1. Подтверждённый факт

Факт, непосредственно подтверждённый источниками:

- сумма остатка;
- количество операций;
- наличие документа;
- факт платежа;
- расхождение между реестрами;
- отсутствие сквозной модели.

## 1.2. Exposure

Сумма или процесс, подверженные риску, но ещё не являющиеся доказанной потерей.

Примеры:

- долгий остаток;
- открытые B2B-расчёты;
- WIP без полной оценки;
- выплаты без подтверждённого статуса;
- нерасшифрованный owner cash.

## 1.3. Потенциальный резерв

Механизм, способный дать экономический эффект:

- повышение цены;
- предотвращение закупки;
- ускорение collection;
- снижение rework;
- высвобождение мощности;
- улучшение tax economics;
- снижение риска.

## 1.4. Реализованный benefit

Эффект признаётся только после:

- baseline;
- управленческого действия;
- evidence;
- отражения в cash/P&L/risk metric;
- проверки отсутствия двойного счёта;
- finance validation.

> **Exposure не равен потере, а резерв не равен реализованной экономии.**

---

# 2. Критерии приоритизации

Каждая зона оценивается по семи параметрам:

1. **материальность** — влияние на прибыль, капитал или cash;
2. **срочность** — скорость превращения проблемы в кассовое давление;
3. **доказательность** — качество фактической базы;
4. **управляемость** — способность бизнеса воздействовать на причину;
5. **время до эффекта** — период от решения до результата;
6. **implementation risk** — риск ухудшить бизнес неправильным действием;
7. **dependency** — какие данные и процессы должны быть закрыты раньше.

Приоритеты:

- **P0** — критично для достоверности финального вывода или ликвидности;
- **P1** — высокий потенциальный эффект и необходимая управленческая перестройка;
- **P2** — масштабирование, автоматизация или долгосрочная оптимизация после P0/P1.

---

# 3. Сводный risk-adjusted portfolio

| № | Зона | Подтверждённый факт / exposure | Финансовый маршрут | Доказательность | Управляемость | Время до эффекта | Приоритет | Главный риск неправильного решения |
|---:|---|---|---|---|---|---|---:|---|
| 1 | Unit economics couture | главный доходный контур не имеет полной order economics | слабая цена → низкий contribution → слабое покрытие fixed costs → cash pressure | высокая по gap, средняя по размеру эффекта | высокая | 1–3 мес. пилот | P1 | сокращение продаж/людей вместо монетизации сложности |
| 2 | Два экономических контура | bespoke и goods смешиваются; shared costs не закреплены | искажённый P&L → ошибочное capital allocation | высокая | высокая | 2–4 мес. | P1 | закрытие полезного направления по методологическому артефакту |
| 3 | Cash architecture | нет полного obligation-led forecast и management balance | авансы/остаток переоцениваются → поздний cash gap → owner funding | высокая | высокая | 2–6 недель | P0 | распределение денег по банковскому остатку |
| 4 | Owner flows | подтверждены встречные движения, классификация неполна | искажение operating cash и структуры капитала | высокая по факту, средняя по net value | высокая | 2–4 недели после данных | P0 | считать все переводы дивидендами или все внесения доходом |
| 5 | Long inventory | 1 339 matched SKU / 29,9 млн ₽; 668 SKU / 12,87 млн ₽ >365 дней | inventory absorption → cash tied up → impairment risk | высокая по exposure | средняя/высокая | 1–6 мес. | P0/P1 | считать 12,87 млн ₽ гарантированным cash release |
| 6 | WIP | нет полного регистра стоимости и cost to complete | незавершённые обязательства → отложенный cash → недооценённая capital need | высокая по gap | высокая | 1–3 мес. | P1 | оценивать liquidity без будущей стоимости исполнения |
| 7 | B2B open | 15 документов / около 2,51 млн ₽ open | AR → задержка inflow → возможные резервы/споры | высокая по open status, средняя по collectible amount | высокая | 2–8 недель | P0/P1 | считать всю сумму бесспорной просроченной задолженностью |
| 8 | Rework and failure cost | ФОТ не связан с заказом; rework не выделен | рост COGS + потеря capacity + задержка revenue | средняя/высокая по механизму | высокая | 2–4 мес. | P1 | линейно сокращать ФОТ без process redesign |
| 9 | Procurement governance | закупка не связана полностью со свободным остатком и назначением | лишняя закупка → inventory → cash outflow | высокая по process gap | высокая | 2–8 недель | P1 | вводить жёсткий no-buy без контроля material readiness |
| 10 | Channel economics | IM/B2B/TSUM имеют разные margin views и cost coverage | gross margin искажает contribution и capital return | высокая по методологии, средняя по full contribution | высокая | 1–3 мес. | P1 | закрывать/масштабировать канал по одной gross margin |
| 11 | Tax economics | около 45,4 млн ₽ tax cash; нет полной accrual/effective model | tax cost влияет на price, purchase cost, inventory and cash timing | высокая по cash, средняя по optimization potential | средняя | 2–4 мес. | P0/P1 | выбирать режим по номинальной ставке |
| 12 | HR/payment mismatch | 38 UNFORMAL, 36 paid; 27 recipients outside roster | неполный labor cost + compliance and tax exposure | высокая по register mismatch | высокая | 1–3 мес. | P0/P1 | считать все расхождения нарушением без проверки основания |
| 13 | Reporting latency | fragmented files; 18/30 released, 12 with gaps | позднее решение → repeat leakage → manual coordination cost | высокая | высокая | 1–3 мес. | P1 | покупать BI/ERP до freeze методологии |
| 14 | End-to-end accountability | сквозные результаты не всегда имеют одного Accountable | отклонения между функциями → owner escalation → delayed correction | высокая качественно | высокая | 2–8 недель | P1 | назначать нескольких совместно ответственных |
| 15 | Growth readiness | продукт масштабируется быстрее economics/capacity/cash control | рост WIP и capital need быстрее contribution | высокая по архитектурному gap | высокая | немедленный gate | P1 | считать рост выручки автоматическим улучшением устойчивости |

---

# 4. Портфель ликвидности и возврата капитала

## 4.1. Долгий остаток тканей

### Подтверждено

- matched inventory около 29,9 млн ₽;
- 668 положительных matched SKU около 12,87 млн ₽ без движения более 365 дней.

### Не подтверждено

- физическое наличие каждой позиции;
- полная пригодность;
- возможность продажи по балансовой стоимости;
- срок использования;
- сумма возможного cash release.

### Возможные механизмы эффекта

1. предотвращённая новая закупка;
2. использование в заказе или коллекции;
3. продажа/обмен;
4. возврат поставщику;
5. переработка;
6. очистка физического расхождения;
7. списание экономически утраченного остатка.

### Риск двойного счёта

Одна позиция не может одновременно считаться:

- cash release;
- avoided purchase;
- снижением COGS;
- уменьшением inventory;
- и отдельным benefit закупок.

### Критерий реализации

Для позиции зафиксированы действие, сумма, дата, evidence и финансовый эффект.

---

## 4.2. B2B open

### Подтверждено

15 документов на сумму около 2,51 млн ₽ требуют closure.

### Возможные статусы

- оплачено на другом счёте;
- подтверждённая дебиторская задолженность;
- частичная оплата;
- возврат;
- корректировка;
- спор;
- технический дубль;
- закрыто иным документом.

### Возможный эффект

Cash collection признаётся только по фактическому поступлению. Исправление реестра без поступления является data-quality benefit, но не cash benefit.

---

## 4.3. WIP и финальные оплаты

### Exposure

Финансовый масштаб полного WIP не определён.

### Механизмы эффекта

- ускорение завершения;
- получение финальной оплаты;
- снижение rework;
- прекращение слабого заказа;
- освобождение материалов и мощности;
- снижение cost to complete.

### Ключевой риск

Ускорение WIP без контроля качества и причины задержки способно увеличить rework. Приоритет должен определяться economic and client risk, а не только возрастом.

---

## 4.4. Owner flows

### Подтверждено

Существуют withdrawals и injections, включая внесение 1,2 млн ₽ для арендных платежей.

### Потенциальный резерв

Не «сокращение выплат собственнику» само по себе, а:

- корректный FCF;
- формальная funding policy;
- отделение займа и распределения;
- снижение emergency funding;
- предотвращение использования авансов как свободного cash.

---

# 5. Портфель повышения маржи

## 5.1. Price and complexity recovery

### Механизмы

- complexity coefficient;
- rush premium;
- paid changes;
- normative fittings;
- material premium;
- margin floor;
- discount governance.

### Доказательность

Архитектурная необходимость подтверждена. Размер эффекта требует пилота 20–30 заказов.

### Benefit metric

- expected vs actual contribution;
- unbilled changes;
- complexity recovery;
- contribution per bottleneck-hour.

---

## 5.2. Failure cost reduction

### Механизмы

- rework reason register;
- design freeze;
- stage gates;
- material readiness;
- устранение повторного ввода;
- один Accountable.

### Риск

Недопустимо считать весь косвенный труд неэффективным. Часть необходима для качества, сервиса и уникального продукта.

---

## 5.3. Channel contribution

### Механизмы

- единый net-sales bridge;
- commission normalization;
- returns and markdown;
- direct logistics/acquiring;
- channel marketing;
- inventory capital.

### Benefit metric

`contribution after direct channel costs / average invested capital`.

---

# 6. Портфель снижения риска

## 6.1. Tax and legal structure

Резерв может состоять в:

- снижении невозмещаемого VAT cost;
- улучшении timing;
- корректировке B2C/B2B pricing;
- упрощении юридической структуры;
- сокращении административной стоимости;
- устранении документных gaps.

Однако без фактического VAT register, declaration history и legal review нельзя обещать сумму оптимизации.

## 6.2. People and payments

Резерв состоит в:

- полном roster;
- корректном contract basis;
- синхронизации начислений и выплат;
- точной labor economics;
- снижении compliance risk;
- управляемом capacity planning.

## 6.3. Data and reporting

Резерв состоит не только в экономии времени. Более значимый эффект — предотвращение слабого решения до возникновения расхода.

---

# 7. Приоритеты реализации

## Wave 0. Не допустить новых утечек

Срок: немедленно.

- growth gate;
- expected economics для крупных/нестандартных заказов;
- stock check до закупки;
- cash gate до распределения;
- verified basis для новых выплат;
- stop на новые системы до methodology freeze.

## Wave 1. Вернуть контроль над cash и капиталом

Срок: 0–60 дней.

- bank deduplication;
- net owner cash flow;
- 13-week forecast;
- item-level inventory A-class;
- B2B closure;
- WIP pilot;
- tax completeness;
- unified roster.

## Wave 2. Улучшить качество маржи

Срок: 30–120 дней.

- order economics;
- complexity pricing;
- change-order recovery;
- rework analytics;
- channel contribution;
- tax scenarios.

## Wave 3. Обеспечить повторяемость

Срок: 90–180 дней.

- two-contour P&L;
- management balance;
- D+10 close;
- end-to-end RACI;
- early-warning cockpit;
- benefit governance.

---

# 8. Top management portfolio

| Направление | Основной тип эффекта | Первичный owner | Главная зависимость | Критерий успеха |
|---|---|---|---|---|
| Cash architecture | предотвращение cash gap | finance/treasury | full bank perimeter | weekly forecast and buffer compliance |
| Order economics | P&L improvement | commercial + finance | order master and pilot data | expected/actual contribution |
| Inventory capital | cash release / cost avoidance | procurement/warehouse/product | physical and purpose validation | item-level realised benefit |
| WIP | cash acceleration / capacity release | production | unified order register | WIP days and final collections |
| Channel portfolio | P&L + capital return | commercial/finance | cost methodology | capital-adjusted contribution |
| Tax economics | P&L/cash/risk | finance/tax | VAT and entity data | validated scenario decision |
| People and payments | cost transparency/risk | HR/finance | unified roster | 100% matched recipients |
| Reporting and governance | prevention and repeatability | CFO/CEO | methodology freeze | D+10 and exception closure |

---

# 9. Что можно утверждать заказчику

Корректные формулировки:

- выявлены материальные зоны exposure;
- подтверждены механизмы потери стоимости;
- определены no-regret controls;
- сформирована программа проверки и реализации резервов;
- конкретная сумма benefit требует baseline и реализации;
- наиболее быстрый эффект ожидается от cash discipline, B2B closure, inventory decisions and prevention of new leakage;
- наиболее крупный долгосрочный эффект потенциально находится в качестве экономики couture-заказа.

Некорректные формулировки:

- компания гарантированно сэкономит сумму всех exposure;
- весь старый запас можно превратить в cash;
- ФОТ необходимо сократить на конкретный процент без productivity analysis;
- налоговая оптимизация имеет известную сумму;
- любой канал с низкой reported margin должен быть закрыт.

---

# 10. Итоговое заключение

Потенциал улучшения YANINA находится в трёх разных плоскостях:

1. **остановить новые утечки** — встроить economic gates до решения;
2. **вернуть связанный капитал** — inventory, WIP, AR and owner-flow control;
3. **повысить качество будущей прибыли** — complexity pricing, capacity, channel and tax economics.

> **Наиболее профессиональный подход состоит не в обещании одной суммы экономии, а в управлении портфелем эффектов с различной доказательностью, сроком, риском и финансовым механизмом.**
