# H85 — Tax filing completeness (P0-adjacent)

Updated: 2026-07-29 · **не SoT** · **do_not_auto_accept=YES** · dual contour

## Зачем (после закрытия data-мостов H82–H84)

Новых файлов в intake нет, подписей нет.  
Ближайшее к **gate 26→27**: комплектность налоговой папки + связка с H76 soft perimeter.

`tax_list` / ЕНС — **сканы без текста** → OCR отдельно; матрица по catalog + anchors.

## Результаты (as_of 2026-07-29)

| Метрика | Значение |
|--------:|----------|
| Tax files в catalog | **25** |
| Слотов матрицы | **28** |
| HAVE | **17** |
| HAVE_DUP | **1** (6-НДФЛ IP 2025 ×2) |
| HAVE_SCAN_NO_TEXT | **4** (списки 24–26 + ЕНС) |
| **MISSING** | **2** — **НДС 2026-Q2**, **РСВ 2026-Q2** (IP) |
| Soft sign open (H76) | **4** |

### Contours

| LE | HAVE | MISSING | Note |
|----|-----:|--------:|------|
| IP Янина | 12 | 2 (Q2’26) | NDS contour |
| Decor ООО | 6 | 0 | без НДС в пакете = OK |
| BOTH meta | 4 scans | 0 | нужен OCR |

## Что даёт проекту

1. Ясные **2 файла к запросу** у Сливяк (Q2 2026) — не «ещё forensic».
2. Напоминание: **TAX→27** всё ещё = human sign H76, не наличие PDF.
3. Dual contour Decor/IP без смешения в company P&L.
4. Списки ФНС помечены OCR — без выдуманных строк из сканов.

## Артефакты

- `live/registers/h85_tax_completeness/`
- Marts: `tax_completeness_*.csv` · `tax_filing_inventory.csv` · `h85_meta.json`
- Map: `live/maps/56_TAX_COMPLETENESS_MAP.md`
- Sign pack: `24_TAX_COMPLETENESS_GAPS_H85.csv`

## Gate

**18/30**. H85 усиливает TAX path; score двигает только подпись perimeter + intake.
