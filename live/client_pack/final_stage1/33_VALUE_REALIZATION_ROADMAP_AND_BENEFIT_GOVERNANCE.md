# Value Realization Roadmap and Benefit Governance

## План реализации резервов и правила подтверждения экономического эффекта

Updated: 2026-08-05  
Статус: клиентская аналитическая редакция

> Документ переводит выявленные резервы в управляемую программу. Он не обещает гарантированную сумму эффекта. Каждый резерв должен пройти путь от диагностического exposure до подтверждённого cash/P&L результата с baseline, владельцем, сроком и запретом двойного счёта.

---

# 1. Главный принцип

Диагностика выявляет зоны потенциальной стоимости, но не должна подменять доказательство результата.

Корректная логика:

`диагностический exposure → гипотеза механизма → baseline → действие → измерение → подтверждение → фиксация эффекта`.

Некорректная логика:

`видимая сумма проблемы = гарантированная экономия`.

Примеры:

- 12,87 млн ₽ долгого остатка — это exposure, а не гарантированный cash release;
- 2,51 млн ₽ B2B open — это зона документной сверки, а не автоматически взысканная дебиторская задолженность;
- 11,56 млн ₽ выплат по UNFORMAL-контуру — это зона formalization и cost visibility, а не доказанная сумма сокращения;
- 45,4 млн ₽ налогового cash — это масштаб налогового контура, а не доказанная переплата.

> **Профессиональная value agenda должна отделять размер выявленной зоны от суммы реально созданного эффекта.**

---

# 2. Типы экономического эффекта

Для YANINA необходимо разделять как минимум пять типов эффекта.

## 2.1. Cash release

Высвобождение уже связанного капитала:

- взыскание задолженности;
- сокращение запаса;
- ускорение WIP;
- отказ от лишней закупки;
- изменение условий поставщика.

## 2.2. P&L improvement

Улучшение текущей прибыльности:

- повышение цены сложности;
- сокращение rework;
- снижение срочных закупок;
- снижение комиссии/логистики;
- сокращение повторных операций.

## 2.3. Cost avoidance

Предотвращение будущего расхода:

- использование существующего материала вместо новой закупки;
- отказ от экономически слабого заказа;
- предотвращение штрафа или налоговой пени;
- предотвращение срочного внешнего подряда.

## 2.4. Risk avoidance

Снижение вероятности потерь:

- formalization кадрового контура;
- налоговый календарь;
- контроль наличных;
- единый supplier master;
- key-person risk mitigation.

## 2.5. Capacity release

Высвобождение дефицитной профессиональной мощности:

- сокращение rework;
- уменьшение ожидания;
- устранение повторного ввода;
- ограничение неоплаченной сложности;
- отказ от низкоценностных исключений.

Эти эффекты нельзя складывать механически. Например, отказ от закупки материала может одновременно быть cost avoidance и cash preservation, но не должен учитываться дважды как две независимые выгоды.

---

# 3. Value stream 1. Экономика индивидуального заказа

## Диагностический exposure

- основной доходный продукт не имеет устойчивой expected/actual unit-экономики;
- сложность, срочность и изменения монетизируются непоследовательно;
- rework и дополнительные трудозатраты не выделяются как отдельная причина отклонения;
- дефицитная мощность распределяется без единого contribution-per-hour критерия.

## Механизмы эффекта

1. complexity pricing;
2. rush premium;
3. лимит бесплатных изменений;
4. material and capacity gate;
5. minimum contribution threshold;
6. rework root-cause reduction;
7. actual vs expected margin review;
8. make-or-buy decision for selected operations.

## Как возникает эффект

### P&L

- повышение realized price;
- снижение прямого перерасхода;
- сокращение unpaid labor;
- снижение срочного подряда.

### Cash

- более ранние и структурированные платежи;
- меньшая потребность в дополнительном финансировании;
- ускорение закрытия заказа;
- снижение стоимости незавершённого исполнения.

### Capacity

- больше contribution на один час bottleneck-role;
- высвобождение времени от переделок;
- снижение числа конфликтующих приоритетов.

## Baseline

До запуска требуется определить за пилотную выборку 20–30 заказов:

- price;
- expected direct cost;
- actual direct cost;
- direct labor hours;
- rework hours;
- number of fittings;
- changes after approval;
- payment timing;
- completion timing;
- contribution.

## KPI

- доля заказов с expected margin;
- margin variance;
- rework cost / revenue;
- complexity premium capture;
- contribution per bottleneck-hour;
- average WIP days;
- on-time completion.

## Правило признания эффекта

Эффект признаётся только после сравнения:

- сопоставимых заказов до и после изменения;
- одинакового уровня сложности;
- одинакового определения direct cost;
- фактической оплаты, если эффект заявлен как cash.

## Риск двойного счёта

Нельзя одновременно полностью учитывать:

- повышение цены как margin improvement;
- и тот же эффект как cash release;
- и высвобождённую мощность как отдельную денежную выгоду,

если не доказано, что высвобождённая мощность была продана дополнительному заказу.

---

# 4. Value stream 2. Запасы и оборотный капитал

## Диагностический exposure

- 1 339 SKU сопоставлены со складским остатком стоимостью около 29,9 млн ₽;
- 668 положительных сопоставленных остатков на сумму около 12,87 млн ₽ не показывают движения более 365 дней;
- фурнитура не имеет полного регистра;
- WIP индивидуального пошива не оценён полностью;
- закупка не всегда начинается с видимого свободного остатка.

## Механизмы эффекта

1. item-level classification;
2. использование существующего материала вместо новой закупки;
3. продажа, возврат или обмен части запаса;
4. переработка и повторное коммерческое использование;
5. WIP acceleration;
6. supplier term improvement;
7. резервирование и контроль свободного остатка;
8. запрет закупки без stock check.

## Как возникает эффект

### Cash release

- поступление денег от продажи/возврата;
- ускорение финального расчёта по завершённым заказам;
- взыскание открытого B2B;
- сокращение закупочного оттока.

### P&L

- снижение хранения и потерь;
- снижение срочной закупки;
- снижение списаний в будущем.

### Cost avoidance

- отказ от новой закупки за счёт использования существующего запаса.

## Baseline

- inventory snapshot by SKU;
- stock value and quantity;
- age;
- purpose;
- reservation;
- expected use date;
- purchase request history;
- new purchases where analogue existed;
- WIP by order;
- B2B open documents.

## KPI

- inventory >365 days;
- inventory without decision;
- avoided purchase value;
- inventory cash release;
- WIP days;
- B2B overdue amount;
- stock accuracy;
- supplier lead-time variance.

## Правило признания эффекта

### Cash release

Признаётся только при фактическом поступлении денег либо сокращении подтверждённого платежа.

### Cost avoidance

Признаётся, если:

- существовал утверждённый план закупки;
- найден и использован подходящий старый материал;
- новая закупка действительно отменена;
- сумма рассчитана по сопоставимой landed cost.

## Риск двойного счёта

Нельзя одновременно считать одну и ту же отменённую закупку:

- высвобождением старого запаса;
- cash release;
- cost saving;
- и inventory reduction.

Корректно: один primary effect и дополнительные operational metrics.

---

# 5. Value stream 3. Ликвидность и owner flows

## Диагностический exposure

- существует 4 933 банковских операций в базовом регистре;
- полный transaction-level owner net flow не рассчитан;
- подтверждены встречные движения собственника;
- часть наличных остаётся unresolved;
- 13-недельный forecast не работает как регулярный контур;
- внутренние переводы и FX требуют исключения.

## Механизмы эффекта

1. account master and deduplication;
2. operation classification;
3. owner-flow normalization;
4. cash waterfall;
5. minimum cash buffer;
6. 13-week rolling forecast;
7. reserve for open orders;
8. cash exception governance.

## Как возникает эффект

### Cash preservation

- предотвращение несвоевременных распределений;
- снижение emergency funding;
- снижение пеней и срочных платежей;
- более раннее выявление дефицита.

### Financing cost avoidance

- снижение потребности в краткосрочном личном/заёмном финансировании;
- уменьшение хаотичного перераспределения между счетами.

### Risk reduction

- прозрачность наличных;
- отделение личного и хозяйственного контура;
- исключение двойного учёта FX и переводов.

## Baseline

- account list;
- beginning/ending balances;
- operation register;
- owner withdrawals;
- owner injections;
- loans;
- interaccount transfers;
- FX conversion legs;
- emergency funding events;
- forecast errors.

## KPI

- net owner cash flow;
- owner funding dependency;
- forecast accuracy;
- minimum cash coverage;
- unclassified bank share;
- cash exceptions;
- emergency funding events;
- reserve coverage of open orders.

## Правило признания эффекта

Не допускается заявлять «экономию» только потому, что owner funding снизился. Необходимо доказать, что снижение достигнуто через улучшение operating cash conversion, а не через перенос обязательств или отказ от необходимых расходов.

## Риск двойного счёта

Cash preservation от отменённой закупки относится к inventory stream, а не повторно к treasury stream. Treasury фиксирует улучшение liquidity profile, но не создаёт второй денежный эффект.

---

# 6. Value stream 4. Производительность и failure cost

## Диагностический exposure

- ФОТ — крупнейший видимый операционный блок;
- штатный, договорной и платёжный контуры расходятся;
- rework, ожидание, поиск информации и ручная сверка не выделены отдельно;
- высокая зависимость от персонального знания;
- отсутствует единая capacity model.

## Механизмы эффекта

1. time and activity pilot;
2. value/complexity/failure labor classification;
3. rework analytics;
4. stage gates;
5. standard work for repeatable operations;
6. clear RACI;
7. master data and single source;
8. capacity planning;
9. targeted role redesign.

## Как возникает эффект

### Capacity release

- сокращение переделок;
- сокращение ожидания;
- сокращение ручной сверки;
- увеличение productive hours.

### P&L

- снижение overtime и срочного подряда;
- снижение потерь материалов;
- увеличение contribution на существующем ФОТ.

### Risk reduction

- снижение key-person dependency;
- повышение воспроизводимости процесса.

## Baseline

- total hours by selected roles;
- productive hours;
- rework hours;
- waiting time;
- coordination time;
- order throughput;
- overtime;
- external contractor spend;
- schedule variance.

## KPI

- failure labor share;
- productive utilization;
- rework hours;
- throughput;
- overtime;
- contribution per FTE / bottleneck-hour;
- process cycle time;
- repeat exception rate.

## Правило признания эффекта

Высвобождённые часы не являются денежной экономией, пока не произошло одно из событий:

- реально сокращён оплачиваемый overtime/подряд;
- предотвращён найм;
- высвобождённая мощность конвертирована в дополнительный profitable contribution;
- сокращена штатная стоимость без снижения качества и сроков.

## Риск двойного счёта

Нельзя одновременно учитывать:

- сокращение rework как P&L saving;
- те же часы как capacity release;
- и дополнительный contribution,

если не доказана отдельная коммерческая монетизация высвобождённой мощности.

---

# 7. Value stream 5. Каналы и товарный портфель

## Диагностический exposure

- товарная выручка с подтверждённой себестоимостью за 2025 год — около 72,9 млн ₽;
- каналы имеют различную cash and commission mechanics;
- ЦУМ требует reported и product view;
- gross margin не отражает stock investment и capital charge;
- единый channel contribution отсутствует.

## Механизмы эффекта

1. channel contribution model;
2. return and markdown analytics;
3. sell-through by batch;
4. investment limit by collection;
5. stop-loss rules;
6. assortment simplification;
7. commission and logistics review;
8. repeat-order gate.

## Как возникает эффект

### P&L

- снижение комиссии и прямых расходов;
- снижение markdown;
- сокращение слабых SKU;
- улучшение mix.

### Cash

- ускорение sell-through;
- снижение stock investment;
- сокращение возвратов;
- сокращение дебиторской задержки.

### Capital allocation

- перенос инвестиций из слабых каналов/партий в сильные.

## Baseline

- net sales by channel;
- COGS;
- commission;
- logistics;
- acquiring;
- returns;
- marketing;
- stock by batch;
- sell-through;
- markdown;
- payment lag.

## KPI

- capital-adjusted contribution;
- sell-through;
- stock days;
- return rate;
- markdown rate;
- channel cash conversion;
- collection payback;
- repeat-order success rate.

## Правило признания эффекта

Экономический эффект от закрытия слабого SKU/канала признаётся по фактическому снижению direct and avoidable cost, а не по всей сумме выручки или распределённых shared costs.

## Риск двойного счёта

Сокращение stock investment учитывается как working-capital effect, а улучшение contribution — как P&L effect. Одна и та же отменённая партия не может полностью попасть в оба эффекта.

---

# 8. Value stream 6. Налоговый и кадровый контур

## Диагностический exposure

- налоговый cash значителен;
- начисления, декларации, ЕНС и платежи не сведены в единый bridge;
- существуют несколько юридических контуров;
- отдельные документы 2026-Q2 требуют подтверждения;
- roster и выплаты расходятся;
- часть получателей и статусов требует formalization.

## Механизмы эффекта

1. tax passport;
2. accrual-to-payment bridge;
3. ENS reconciliation;
4. VAT scenario model;
5. import tax bridge;
6. intercompany logic;
7. unified roster;
8. payment basis verification;
9. external legal review where required.

## Как возникает эффект

### Cash/P&L

- предотвращение пеней и штрафов;
- устранение технических переплат при подтверждении;
- корректное использование вычетов/режима при наличии оснований;
- устранение дублей выплат;
- более точное начисление обязательств.

### Risk avoidance

- снижение риска некорректной квалификации операций;
- снижение кадровой и налоговой неопределённости;
- повышение готовности к проверке.

## Baseline

- declarations;
- accruals;
- payments;
- ENS;
- VAT input/output;
- import transactions;
- payroll recipients;
- contract status;
- legal entity allocation;
- overdue filings/issues.

## KPI

- tax accrual-to-payment reconciliation;
- ENS unreconciled amount;
- missing filings;
- payroll recipients matched to roster;
- payments without basis;
- penalties/late payments;
- scenario effective tax rate.

## Правило признания эффекта

Налоговый эффект признаётся только после:

- подтверждённого расчёта;
- проверки применимости законодательства;
- при необходимости — внешнего налогового/юридического заключения;
- фактического уменьшения платежа или возврата.

## Риск двойного счёта

Нельзя учитывать снижение налогового платежа, если оно вызвано только переносом срока. Timing effect должен отражаться отдельно от permanent benefit.

---

# 9. Приоритизация value streams

| Приоритет | Направление | Скорость первого эффекта | Потенциальный масштаб | Доказательность на старте | Ключевая зависимость |
|---:|---|---|---|---|---|
| 1 | B2B collection и bank/owner normalization | высокая | средний | высокая/средняя | document closure |
| 2 | Cash forecast и capital policy | высокая | высокий по устойчивости | средняя | bank register |
| 3 | Inventory decisions and purchase avoidance | средняя | высокий | средняя | item-level review |
| 4 | Unit economics and complexity pricing | средняя | высокий | средняя | order pilot |
| 5 | WIP and capacity control | средняя | высокий | низкая/средняя | WIP register |
| 6 | Channel contribution | средняя | средний/высокий | средняя | unified definitions |
| 7 | Failure-cost reduction | средняя/долгая | высокий | низкая на старте | time/activity baseline |
| 8 | Tax and HR formalization | средняя | средний + risk | средняя | complete source pack |

Приоритет не означает, что низший поток менее важен. Он отражает последовательность получения достоверного эффекта.

---

# 10. Benefit register

Для каждой инициативы необходимо вести единый register.

| Поле | Содержание |
|---|---|
| Benefit ID | уникальный номер |
| Diagnostic finding | исходный вывод Этапа 1 |
| Value stream | направление |
| Benefit type | cash / P&L / avoidance / risk / capacity |
| Baseline | исходное значение и период |
| Action | конкретное изменение |
| Owner | один accountable |
| Start date | дата старта |
| Expected timing | когда эффект должен появиться |
| Gross effect | расчётный валовый эффект |
| Implementation cost | стоимость реализации |
| Net effect | gross less implementation cost |
| Evidence | документы/данные подтверждения |
| Confidence | high / medium / low |
| Double-count link | связанный benefit ID |
| Finance validation | подтверждение финансовой функции |
| Status | hypothesis / approved / in progress / realized / rejected |

---

# 11. Governance экономического эффекта

## Еженедельно

- статус инициатив;
- blockers;
- cash actions;
- owner decisions;
- data completeness.

## Ежемесячно

- baseline vs actual;
- realized vs forecast benefit;
- P&L and cash bridge;
- no-double-count review;
- implementation cost;
- corrective actions.

## Ежеквартально

- стратегическая переоценка портфеля;
- закрытие слабых инициатив;
- перераспределение ресурсов;
- подтверждение устойчивости эффекта;
- обновление target values.

## Роли

- business owner — реализует изменение;
- finance — подтверждает расчёт;
- data owner — подтверждает источник;
- PMO/transformation lead — контролирует сроки и зависимости;
- собственник/board — утверждает крупные trade-offs.

---

# 12. Что нельзя включать в benefit case

Не следует признавать эффектом:

- всю стоимость старого запаса без реализации или отмены закупки;
- всю сумму B2B open без подтверждённого взыскания;
- сокращение планового расхода, который никогда не был утверждён;
- перенос платежа на следующий период;
- снижение затрат из-за уменьшения объёма продаж;
- высвобождённые часы без финансовой монетизации;
- уменьшение owner funding при одновременном росте просроченных обязательств;
- налоговый эффект без проверки правового основания;
- одновременно cash и P&L эффект одной операции без bridge.

---

# 13. Итоговый вывод

У YANINA существует значительный потенциал улучшения, но профессиональная ценность программы определяется не количеством заявленных резервов, а качеством доказательства.

Главные направления:

- повышение contribution индивидуального заказа;
- ускорение возврата капитала из запасов и WIP;
- нормализация ликвидности и owner flows;
- снижение failure cost;
- улучшение channel capital efficiency;
- снижение налоговой и кадровой неопределённости.

> **Эффект должен признаваться только тогда, когда изменение подтверждено данными, имеет одного владельца, не посчитано дважды и проявилось в cash, P&L либо доказанном снижении риска.**
