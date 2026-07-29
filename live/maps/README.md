# YANINA / YNN — карты системы

Updated: 2026-07-27

## С чего начать

1. **`00_MAPS_INDEX.md`** — навигация по всем картам 01–09  
2. **`08_UNIFIED_ALGORITHM.md`** — единый алгоритм чтения / данных / оптимизации / close  
3. **`09_PROBLEMS_PLUS_MINUS.md`** — честный ± и приоритеты P0–P2  

## Набор карт (консалтинг + архитектура)

| Файл | Содержание |
|------|------------|
| `01_PROCESS_MAP.md` | Бизнес-процессы P01–P12, два контура |
| `02_DOCUMENT_DATA_MAP.md` | 107 документов и данные в них |
| `03_DATA_LAYER_MAP.md` | L0→L5, волны W1–W6, marts |
| `04_ENTITY_CHANNEL_MAP.md` | Юрлица, каналы, RACI |
| `05_CONTROL_MAP.md` | Gate, controls, сверки |
| `06_VALUE_STREAM_MAP.md` | Где ценность и утечки |
| `07_CROSSWALK_MATRIX.md` | Сопоставление всё↔всё |
| `08_UNIFIED_ALGORITHM.md` | Алгоритмы A–E |
| `09_PROBLEMS_PLUS_MINUS.md` | Проблемы и зрелость |
| `10_DEEP_SYNTHESIS.md` | Углублённый синтез всех контуров |
| `11_MONTHLY_QUALITY_MAP.md` | Gate/gaps по месяцам |
| `12_LAYER2_MD_OPEX_SKU.md` | Forensic МД + opex + SKU ABC |
| `13_LAYER3_CASH_CLASSIFICATION.md` | OTHER_IN / bank DDS / payroll lines |
| `14_LAYER4_RECLASS_IMPACT.md` | Impact переклассификации на IM |
| `15_LAYER5_SCORECARD_LINKS.md` | Scorecard + POS LE + MD invoice links |
| `build_layer4_reclass_impact.py` | Кандидаты OTHER_IN |
| `build_layer5_scorecard.py` | Scorecard / links |
| `system_scorecard.csv` | Единый статус областей |
| `md_invoice_surname_links.csv` | Invoice↔МД (фамилия, MED) |
| `pos_candidate_by_le_month.csv` | POS по LE/месяц |

## Машиночитаемое

CSV в этой папке: каталог документов, crosswalk процессов, волны, marts, edges_199, field_lineage_644.

## Старый детальный xlsx-контур

`YANINA_DETAILED_ECONOMIC_DATA_MAP_*.xlsx` + листы 00–13 — см. ниже исторический README-блок.

---

## Исторически: детальная карта данных (xlsx)

### Главный файл
`YANINA_DETAILED_ECONOMIC_DATA_MAP_20260723.xlsx`

### Листы
1. `00_Обзор` — метрики  
2. `01_Цепочки` — 6 экономических контуров  
3. `02_Связи_199` — межфайловые связи  
4. `03_Документы` — degree, поля, ключи  
5. `04_Сущности` — 30 канонических сущностей  
6. `05_Поля_топ` / `05b_Entity_freq`  
7. `06_Lineage_поля` — 644 field-lineage  
8. `07_Анализы` — готовность 30 анализов  
9. `08_Пробелы`  
10. `09_Ключи` — 491 key candidates  
11. `10_Матрица_файл_цепочка`  
12. `11_Join_rules` / `12_Data_contracts`  
13. `13_Пути_экономики`

### CSV рядом
- `edges_199.csv`
- `field_lineage_644.csv`
- `economic_map_summary.json`
- `35_SKU_STOCK_FABRIC_BRIDGE_MAP.md` (H64)
- `36_PERSON_COST_COLLECTION_BRIDGE_MAP.md` (H65)
- `37_RESIDUAL_HIGH_GAPS_MAP.md` (H66)
- `38_FABRIC_PROCUREMENT_CASH_MAP.md` (H67)
- `39_MASTER_P0_BOARD_MAP.md` (H68)
- `40_OVERBANK_HYPOTHESIS_MAP.md` (H69)
- `41_CARD_DDS_E08_MAP.md` (H70)
- `42_GATE_TAIL_MAP.md` (H71)
- `43_SIGN_PACK_SYNC_MAP.md` (H72)
- `44_DESIGNERS_COLLECTION_BRIDGE_MAP.md` (H73)
- `45_SHOP_WAREHOUSE_BRIDGE_MAP.md` (H74)
- `46_STOCK_CHANNEL_SELLTHROUGH_MAP.md` (H75)
- `47_TAX_SOFT_PERIMETER_MAP.md` (H76)
- `48_SALES_BUDGET_SANITY_MAP.md` (H77)
- `49_P0_GATE_SYNC_MAP.md` (H78)
- `50_MEETING_EXEC_KIT_MAP.md` (H79)
- `51_POST_SIGN_ACTIVATION_MAP.md` (H80)
- `52_WAITING_OWNERS_CHECKPOINT_MAP.md` (H81)
