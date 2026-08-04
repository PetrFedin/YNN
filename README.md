# YNN — YANINA Analytics Workspace

Репозиторий управленческой аналитики и комплексной диагностики бизнеса **YANINA** — ИП Янина / Салон / Декор.

## Главная точка входа

**Финальный клиентский пакет Этапа 1:**  
[`live/client_pack/final_stage1/00_FINAL_PACKAGE_STRUCTURE.md`](live/client_pack/final_stage1/00_FINAL_PACKAGE_STRUCTURE.md)

Пакет включает:

- Executive Summary для собственников;
- полный диагностический отчёт;
- финансовую модель и структуру затрат;
- денежный поток и ликвидность;
- запасы и оборотный капитал;
- налоговую диагностику;
- процессы и управленческую отчётность;
- реестр доказательств;
- матрицу рисков и резервов;
- карту приоритетов Этапа 2;
- повестку управленческих решений;
- методологию и ограничения;
- checklist перед финальным freeze;
- регистр ключевых метрик.

## Важно

- Это **controlled staging / управленческая диагностика**, не audited Source of Truth и не бухгалтерский P&L.
- Налоговый блок не является юридическим налоговым аудитом.
- Потенциальные резервы не равны гарантированному эффекту до отдельного расчёта и реализации.
- Сырые исходники (`documents/`, `sources/`, `processed/` → Downloads) не публикуются.
- Секреты, персональные исходники и `.venv` в git не входят.

## С чего начать

| Путь | Содержание |
|---|---|
| **[`live/client_pack/final_stage1/`](live/client_pack/final_stage1/)** | **Финальная клиентская редакция комплексной диагностики Этапа 1** |
| [`live/client_pack/final_stage1/01_EXECUTIVE_SUMMARY_FOR_OWNERS.md`](live/client_pack/final_stage1/01_EXECUTIVE_SUMMARY_FOR_OWNERS.md) | Краткий итог для собственников |
| [`live/client_pack/final_stage1/02_FULL_BUSINESS_DIAGNOSTIC_REPORT.md`](live/client_pack/final_stage1/02_FULL_BUSINESS_DIAGNOSTIC_REPORT.md) | Основной полный отчёт |
| [`live/client_pack/final_stage1/14_MANAGEMENT_DECISION_AGENDA.md`](live/client_pack/final_stage1/14_MANAGEMENT_DECISION_AGENDA.md) | Решения для итоговой встречи |
| [`live/client_pack/final_stage1/13_OPEN_ITEMS_BEFORE_FINAL_FREEZE.md`](live/client_pack/final_stage1/13_OPEN_ITEMS_BEFORE_FINAL_FREEZE.md) | Что необходимо закрыть перед freeze |
| [`NOW.md`](NOW.md) | Операционный command center |
| [`STATUS.md`](STATUS.md) | Текущий статус рабочей среды |
| [`HANDOFF.md`](HANDOFF.md) | Навигация по техническим артефактам |
| [`live/marts/`](live/marts/) | Расчётные витрины |
| [`live/registers/`](live/registers/) | Регистры и reconciliation layers |

## Главный диагностический вывод

YANINA обладает сильным продуктом, профессиональной экспертизой и реальной способностью формировать значительный денежный поток. Основное ограничение находится в разрыве между сложностью бизнеса и зрелостью системы управления экономикой.

В текущей модели отсутствует единый сквозной механизм:

`заказ → материалы → труд → производство → склад → продажа → деньги → налоги → прибыль`.

Из-за этого денежный поток смешивается с прибылью, два разных бизнес-контура оцениваются одной моделью, а часть капитала и обязательств становится видна слишком поздно.

## Граница Этапа 1

### Входит

- диагностика финансовой модели;
- денежный поток и ликвидность;
- структура затрат;
- запасы и оборотный капитал;
- закупки, производство и планирование;
- управленческая отчётность;
- налоговая нагрузка и риски;
- карта ограничений и резервов;
- рекомендации и приоритеты Этапа 2.

### Не входит как выполненное внедрение

- промышленный управленческий учёт;
- регулярный P&L и баланс;
- unit-экономика всех заказов;
- ERP/PLM;
- налоговая реструктуризация;
- кадровое переоформление;
- полный набор регламентов;
- сопровождение изменений.

## Последние аналитические сессии

- **H64**: SKU ↔ stock ↔ fabric ABC + collection bridge — `live/docs/51_SKU_STOCK_FABRIC_BRIDGE_H64.md`
- **H65**: person-cost/embroidery → collection gaps — `live/client_pack/52_PERSON_COST_COLLECTION_BRIDGE_H65.md`
- **H66**: residual HIGH gaps stem/MD/quarantine — `live/client_pack/53_RESIDUAL_HIGH_GAPS_H66.md`
- **H67**: fabric/procurement cash ABC — `live/client_pack/54_FABRIC_PROCUREMENT_CASH_H67.md`
- **H68**: master P0 board + E02 evidence — `live/client_pack/55_MASTER_P0_BOARD_H68.md`
- **H69**: overbank channel hypotheses — `live/client_pack/56_OVERBANK_HYPOTHESIS_H69.md`
- **H70**: card → DDS hypotheses + E08 dual-path — `live/client_pack/57_CARD_DDS_HYPOTHESIS_H70.md`
- **H71**: gate tail TAX/Feb/Mercury — `live/client_pack/58_GATE_TAIL_H71.md`
- **H72**: sign pack sync to gate path — `live/client_pack/59_SIGN_PACK_SYNC_H72.md`
- **H73**: designers KPI/smetka ↔ collections/person-cost — `live/client_pack/60_DESIGNERS_COLLECTION_BRIDGE_H73.md`
- **H74**: цех ЗП ↔ collections/person-cost/warehouses — `live/client_pack/61_SHOP_WAREHOUSE_BRIDGE_H74.md`
- **H75**: stock end-qty ↔ IM/TSUM sell-through — `live/client_pack/62_STOCK_CHANNEL_SELLTHROUGH_H75.md`
- **H76**: tax SOFT/GAP ↔ Salon UFK perimeter — `live/client_pack/63_TAX_SOFT_PERIMETER_H76.md`
- **H77**: SALES ДДС-доход ↔ budget sanity — `live/client_pack/64_SALES_BUDGET_SANITY_H77.md`
- **H78**: P0 gate sync — `live/client_pack/65_P0_GATE_SYNC_H78.md`
- **H79**: meeting exec kit — `live/client_pack/66_MEETING_EXEC_KIT_H79.md`
- **H80**: post-sign activation — `live/client_pack/67_POST_SIGN_ACTIVATION_H80.md`
- **H81**: waiting-on-owners checkpoint — `live/client_pack/68_WAITING_ON_OWNERS_H81.md`
- **H82**: contracts ↔ RACI ↔ штатка — `live/client_pack/69_CONTRACTS_RACI_SHTATKA_H82.md`
- **H83**: HR policy ↔ payroll ↔ штатка — `live/client_pack/70_HR_PAYROLL_BRIDGE_H83.md`
- **H84**: fabric aging — `live/client_pack/71_FABRIC_AGING_H84.md`
- **H85**: tax filing completeness — `live/client_pack/72_TAX_COMPLETENESS_H85.md`
- **H86**: P0 executive refresh — `live/client_pack/73_P0_EXEC_REFRESH_H86.md`
- **H87**: client meeting brief — `live/client_pack/74_CLIENT_MEETING_BRIEF_H87.md`
- **H88**: new bank statements and owner cash-flow reassessment — `live/client_pack/76_BANK_STATEMENTS_INTAKE_H88.md`
