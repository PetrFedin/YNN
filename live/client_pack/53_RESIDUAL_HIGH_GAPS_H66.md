# H66 — Residual HIGH gaps after H65 (stem / MD / quarantine)

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (приоритет)
H65 закрыл **157/190** HIGH через person-cost. Остались **33** артикула (~**304,141 €**).  
Этот слой **разбирает остаток по действиям**, а не плодит новый forensic.

## Разбор 33 остатков
| Resolution | N | Sale € | Действие |
|------------|--:|-------:|----------|
| STEM_PERSON_COST | 8 | 74,358 | Confirm variant→PC proxy (0-3167/2→0-3167) |
| MD_STRONG_ONLY | 5 | ~71k | Confirm MD STRONG как cost evidence; нужна карточка |
| MD_WEAK_ONLY | 8 | ~54k | Alias / workshop — не Accept |
| QUARANTINE_LABEL | 3 | 26,792 | ICONIC / АКЦИЯ / КЛ-2024 — не SKU |
| TRUE_BLANK | 9 | 77,761 | Запросить файл / workshop card |

**P0 owner actions:** 22 строк в `23_residual_p0_owner_actions.csv`.

## Что усиливает проект
1. **8 stem-хитов** возвращают ~74k€ в уже посчитанный person-cost контур без нового Accept.
2. **5 MD STRONG** (44-09, 44-04, 43-10…) — конкретные salon lines для confirm.
3. **3 ярлыка** убирают шум из HIGH (не артикулы).
4. **9 true blank** — единственный честный «нужен файл», а не пустой анализ.

## Артефакты
- Marts: `residual_high_gap_pack.csv`, `residual_p0_owner_actions.csv`, `residual_true_blanks.csv`
- Wave B: `22–25_*`
- Map: `live/maps/37_RESIDUAL_HIGH_GAPS_MAP.md`
- Builder: `live/registers/h66_residual_high_gaps/build_h66.py`

## Gate
**18/30** без изменения. Следующий рычаг метрик — только owners (подпись / DDS / Mercury) + confirm по P0.
