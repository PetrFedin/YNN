# YNN — YANINA Analytics Workspace

Репозиторий управленческой аналитики и диагностики бизнеса **YANINA** (ИП Янина / Салон / Декор) на основе предоставленных документов.

## Важно

- Это **controlled staging / диагностика**, не audited Source of Truth и не бухгалтерский P&L.
- Сырые исходники (`documents/`, `sources/`, `processed/` → Downloads) **не публикуются**.
- Секреты и `.venv` в git не входят.

## С чего начать

| Путь | Содержание |
|------|------------|
| **[`NOW.md`](NOW.md)** | **Command Center — что делать прямо сейчас (H56)** |
| [`live/client_pack/sign_session_pack/`](live/client_pack/sign_session_pack/) | Подпись 15 мин + пинги + SLA |
| [`STATUS.md`](STATUS.md) | Текущий статус git-пакета |
| [`live/client_pack/`](live/client_pack/) | **Этап 1 для заказчика** (отчёт + waves A/B/C) |
| [`live/OPTIMIZATION_SCENARIOS.md`](live/OPTIMIZATION_SCENARIOS.md) | Сценарии оптимизации S1–S4 |
| [`HANDOFF.md`](HANDOFF.md) | Навигация по артефактам |
| [`live/marts/`](live/marts/) | Расчётные витрины |
| [`live/registers/`](live/registers/) | Регистры W1–W6 и hardenings |

## Граница Этапа 1

Входит: диагностика, карты ограничений/резервов, приоритеты, сценарии, черновики KPI/политик.  
Не входит как внедрение: боевые дашборды, утверждённые регламенты, сопровождение изменений.

## Контакты контура

Локальный путь разработки: `yanina-docs` → remote **YNN**.

- **H64**: SKU↔stock↔fabric ABC + collection bridge — `live/docs/51_SKU_STOCK_FABRIC_BRIDGE_H64.md`
- **H65**: person-cost/embroidery → collection gaps — `live/client_pack/52_PERSON_COST_COLLECTION_BRIDGE_H65.md`
- **H66**: residual HIGH gaps stem/MD/quarantine — `live/client_pack/53_RESIDUAL_HIGH_GAPS_H66.md`
- **H67**: fabric/procurement cash ABC — `live/client_pack/54_FABRIC_PROCUREMENT_CASH_H67.md`
- **H68**: master P0 board + E02 evidence — `live/client_pack/55_MASTER_P0_BOARD_H68.md`
- **H69**: overbank channel hypotheses — `live/client_pack/56_OVERBANK_HYPOTHESIS_H69.md`
- **H70**: card→DDS hypotheses + E08 dual-path — `live/client_pack/57_CARD_DDS_HYPOTHESIS_H70.md`
- **H71**: gate tail TAX/Feb/Mercury — `live/client_pack/58_GATE_TAIL_H71.md`
- **H72**: sign pack sync to gate path — `live/client_pack/59_SIGN_PACK_SYNC_H72.md`
- **H73**: designers KPI/smetka ↔ collections/person-cost — `live/client_pack/60_DESIGNERS_COLLECTION_BRIDGE_H73.md`
- **H74**: цех ЗП ↔ collections/person-cost/warehouses — `live/client_pack/61_SHOP_WAREHOUSE_BRIDGE_H74.md`
- **H75**: stock end-qty ↔ IM/TSUM sell-through — `live/client_pack/62_STOCK_CHANNEL_SELLTHROUGH_H75.md`
- **H76**: tax SOFT/GAP ↔ Salon UFK perimeter — `live/client_pack/63_TAX_SOFT_PERIMETER_H76.md`
- **H77**: SALES ДДС-доход ↔ budget sanity — `live/client_pack/64_SALES_BUDGET_SANITY_H77.md`
- **H78**: P0 gate sync (today/path/TAX/simulation) — `live/client_pack/65_P0_GATE_SYNC_H78.md`
- **H79**: meeting exec kit (checkboxes+TAX/pings/runcard) — `live/client_pack/66_MEETING_EXEC_KIT_H79.md`
- **H80**: post-sign activation + telegram blast — `live/client_pack/67_POST_SIGN_ACTIVATION_H80.md`
- **H81**: waiting-on-owners checkpoint + print index — `live/client_pack/68_WAITING_ON_OWNERS_H81.md`
- **H82**: contracts ↔ RACI ↔ штатка (meeting evidence) — `live/client_pack/69_CONTRACTS_RACI_SHTATKA_H82.md`
