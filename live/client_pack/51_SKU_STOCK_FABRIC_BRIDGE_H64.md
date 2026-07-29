# H64 — SKU ↔ stock ↔ fabric ABC + collection bridge

Updated: 2026-07-29 · indicative · **не SoT** · без auto-Accept

## Зачем
После H62/H63 нужен слой «что продали ↔ что в номенклатуре/складе ↔ что в тканях».  
Без него B2B/alias и MD-cost висят без доказательной базы.

## Результаты
| Слой | Факт |
|------|------|
| SKU master | **1863** строк / **1854** с артикулом |
| Stock cost | **2957** линий / **1081** арт. |
| Fabric ABC | **1338** / **29,837,656** ₽ · A=498 (23,869,121 ₽) · без Итого/Склад |
| Bridge | **538** арт. · stock 16 · sku 38 · **NONE 500** · HIGH 190 |

### Семейства артикулов (критично)
- **GOODS_STYLE**: n=432, sale=1,680,477€, stock=15, sku=37, NONE=395
- **COLLECTION_STYLE**: n=98, sale=2,322,496€, stock=0, sku=0, NONE=98 — COL43-47 = MD-showroom; goods stock = `0-xxxx` → дожим H65
- **OTHER**: n=8, sale=34,802€, stock=1, sku=1, NONE=7

## Почему match низкий — не баг
- `43-xx` / `47-xx` = MD showroom → **0** прямых попаданий в goods stock (`0-xxxx`).
- Goods-style даёт почти весь stock/sku match.
- Дожим: **H65 person-cost** (Мокеева/Жукова/вышивка).

## Артефакты
- Marts/maps/registers: `h64_sku_stock_fabric/`
- Wave B: `15–18_*`
- Map: `live/maps/35_SKU_STOCK_FABRIC_BRIDGE_MAP.md`
- Builder: `live/registers/h64_sku_stock_fabric/build_h64.py`

## Gate
**18/30 без изменения** — data/intel слой.
