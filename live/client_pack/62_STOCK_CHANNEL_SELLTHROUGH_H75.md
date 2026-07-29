# H75 — Goods stock end-qty ↔ IM/TSUM sell-through

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (P2 после H74)
H74 показал: цех почти не пересекается с goods stock.  
Следующий вопрос владельца: **что лежит на Склад ИМ / ЦУМ и продаётся ли в канале**.

## Источники
| Слой | Файл |
|------|------|
| Остатки | `h6_marts/stock_by_warehouse_full.csv` (`qty_end`) |
| Продажи | `w4_sales_settle/sales_lines.csv` (IM / TSUM / B2B) |

`sellthrough_proxy = sales_qty / (sales_qty + qty_end)` — **грубый**, snapshot vs multi-period sales.

## Результаты
| Класс | SKU | qty_end | sales qty | revenue ₽ |
|-------|----:|--------:|----------:|----------:|
| STOCK_AND_SALES | **214** | 579 | 1 508 | ~105.8M |
| STOCK_NO_SALES | **226** | 388 | 0 | 0 |
| SALES_NO_STOCK | **322** | 0 | 951 | ~87.5M |

### Канальный фокус складов
| Склад→канал | Rows | Aligned | Stock без sales канала | qty_end без sales |
|-------------|-----:|--------:|-----------------------:|------------------:|
| ИМ → IM | 552 | 107 | **191** | **312** |
| ЦУМ → TSUM | 52 | 0* | 0 | 0 |
| Опт → B2B | 126 | 11 | 17 | 25 |

\*TSUM: identity join склада «Остатки ЦУМ» ↔ sales `canonical_sku` слабый — не читать как «всё продано».

### Owner actions
- **235** кандидатов (36 HIGH): остаток без продаж / IM stock без IM sales  
- Примеры HIGH: `0-2359`, `T-3069C`, `0-3221D`, `0-1729`  
- Ask: markdown / перемещение / списание / нет файла продаж

## Что даёт проекту
1. Рабочий dead-stock / sell-through контур на goods identity (не коллекция).
2. Усиливает Wave B: конкретный список SKU для коммерции/склада.
3. Не путать с company P&L; не auto-Accept.

## Артефакты
- Register: `live/registers/h75_stock_channel_sellthrough/` (+ `build_h75.py`)
- Wave B: `43–46_stock_channel_*`
- Map: `live/maps/46_STOCK_CHANNEL_SELLTHROUGH_MAP.md`

## Gate
**18/30** — data/ops P2.
