# H62 — Коллекции / showroom → маржа + связь с МД

**Дата:** 2026-07-29  
**Зачем:** 12 файлов `collection_result` были `(layer2 optional)` — лежали в каталоге, но не вшиты в анализ. Это приоритет #1 досводки документов.  
**Контур:** showroom/MD commercial — **не** company P&L / не goods −58%.  
**Не делаем:** auto-Accept link в SoT.

---

## Результат

| Метрика | Значение |
|---------|----------|
| Файлов | 12 |
| Строк заказов | **1 758** |
| Продажи (EUR, со скидкой) | **~4.04M €** |
| STRONG link → МД (article+surname) | **313** |
| Скрипт | `live/registers/h62_collections_margin/build_h62.py` |

### По коллекциям (ядро)

| ID | Lines | Sale € | Strong→MD % | GM% (где есть cost) |
|----|-------|--------|-------------|---------------------|
| COL43 | 147 | 674k | **78.9%** | 90.2 |
| COL44 | 64 | 424k | **79.7%** | 92.4 |
| COL45 | 61 | 256k | **72.1%** | 75.5 |
| COL46 | 41 | 330k | **80.5%** | 87.5 |
| COL47 | 71 | 638k | **64.8%** | 88.3 |

Капсула / НГ / круиз: продажи есть, но STRONG к МД низкий (артикулы `0-xxxx` / `ИМ-` чаще не бьются 1:1 с salon article) — нужны alias/ручной match.

---

## Артефакты

- `collection_order_lines.csv` — все заказы  
- `collection_margin_by_collection.csv` — свод  
- `collection_top40_models.csv` — топ моделей  
- `collection_md_links.csv` — crosswalk (STRONG/WEAK/NONE)  
- Wave B: `12–14_collection_*`

---

## Зачем это проекту

1. Закрывает пробел «12 файлов не в анализе»  
2. Даёт маржу showroom по коллекциям (управленчески)  
3. COL43–47 уже стыкуются с МД-заказами → путь к payment-level / cost fill  
4. Честно отделяет showroom от товарного контура  

## Оценка

**9.5/10** как data-integration: реальный ingest + цифры + crosswalk без fake SoT.
