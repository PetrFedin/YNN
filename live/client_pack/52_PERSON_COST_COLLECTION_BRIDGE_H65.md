# H65 — Person-cost / embroidery → collection bridge

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (приоритет после H64)
H64 показал: **COLLECTION_STYLE** (98 арт / ~2.3M €) имеет **0** stock/sku match.  
Workshop-карточки Мокеевой / Жуковой / Меркушиной / вышивки несут **те же** model codes (`43-25`, `44-22`…) — это рабочий proxy для MD cost, пока нет alias Accept.

## Результаты
| Метрика | Значение |
|---------|----------|
| Линий person/emb | **7096** |
| Уник. артикулов | **1030** |
| Закрывает NONE gap | **327** арт / **3,407,253 €** продаж |
| HIGH gaps с hit | **157 / 190** |
| COLLECTION_STYLE linked | **88** |
| По источникам | embroidery 4873 · mokeeva 941 · zhukova 998 · merkushina 284 |

### Топ закрытых HIGH (пример)
| Артикул | Sale € | Источники |
|---------|-------:|-----------|
| 43-25 | 111 556 | mokeeva + zhukova |
| 44-22 | 102 330 | embroidery + mokeeva |
| 47-20 | 96 740 | embroidery + mokeeva |
| 46-21 | 79 176 | embroidery + mokeeva + zhukova |

## Что это даёт проекту
1. **G4/G5 связка**: showroom-код → workshop cost card без выдуманного Accept.
2. Owner worksheet: `21_high_gap_owner_worksheet.csv` — confirm proxy **или** нужен alias/MD line.
3. Не путать с company P&L / goods COGS: суммы **indicative**.

## Артефакты
- `live/marts/person_cost_*.csv` · `high_gap_owner_worksheet.csv`
- Wave B: `19–21_*`
- Map: `live/maps/36_PERSON_COST_COLLECTION_BRIDGE_MAP.md`
- Builder: `live/registers/h65_person_cost_bridge/build_h65.py`

## Gate
**18/30** — intel усиливает Wave B; метрики двигают только owners (подпись / soft-slice / файлы).
