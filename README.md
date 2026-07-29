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
