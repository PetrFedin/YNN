# H84 — Mat movement ↔ fabric aging (P2)

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (последний крупный data-мост)

H67 дал ABC остатков и procurement↔bank, но **без дат документов**.  
В `Движение тканей.xlsx` есть 7.7k документных строк с датами — это aging WC.

## Метод

| Слой | Правило |
|------|---------|
| Aging | days since **last doc date** → as_of 2026-07-29 |
| Money | только **Остатки 31.05.2026**, match `warehouse + article\|name` |
| Leaf qty/₽ в движении | **AMBIGUOUS** — не используем как деньги |
| SoT | **N** |

## Результаты

| Метрика | Значение |
|--------:|----------|
| SKU в движении | **2 227** |
| Doc-строк | **7 736** |
| С датами | **2 226** |
| Match к остаткам | **1 339** |
| Σ matched inventory | **~29.9M ₽** (≈ snapshot) |
| **DEAD_STOCK** (>365д + остаток) | **668 SKU / ~12.87M ₽** |

### Bands (matched ₽)

| Band | SKU | Inventory ₽ |
|------|----:|------------:|
| 0–90 HOT | 523 | ~5.19M |
| 91–180 WARM | 532 | ~5.60M |
| 181–365 COOL | 449 | ~6.23M |
| **365+ STALE** | **722** | **~12.87M** |

### Склады

| Склад | Inventory ₽ | STALE ₽ | DEAD n |
|-------|------------:|--------:|-------:|
| Основной | ~22.6M | ~12.8M | 657 |
| Мокеева | ~3.20M | 0 | 0 |
| Жукова | ~2.88M | ~0.06M | 9 |
| Меркушина | ~1.20M | ~0.00M | 2 |

**Вывод:** заморозка WC почти вся на **Основном складе**.

### ABC-A × STALE (дорогое без свежего движения)

См. `fabric_aging_abc_cross.csv` — приоритет write-off/перекрой не с дешёвого хвоста.

## Что даёт проекту

1. Первый **aging** тканей с датами документов (не snapshot-only ABC).
2. P1 pack для Мокеева/Дендерина: **~12.9M ₽** dead stock.
3. Горизонталь к H67 cash/ABC и RACI Prod/склад без fake Accept.
4. Не двигает gate 18/30.

## Артефакты

- Register: `live/registers/h84_fabric_aging/` (+ `build_h84.py`)
- Marts: `fabric_aging_*.csv` · `fabric_dead_stock_top.csv` · `h84_meta.json`
- Map: `live/maps/55_FABRIC_AGING_MAP.md`
- Ops list: `sign_session_pack/23_FABRIC_DEAD_STOCK_H84.csv`

## Gate

**18/30** — P2 WC. Score = owners / intake only.
