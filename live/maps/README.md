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
| `deep_synthesis_snapshot.json` | Агрегаты для воспроизводимости |

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
