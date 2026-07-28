# H47 — Приоритет: Unit-econ МД (blocker map + пилот 2026)

**Горизонт:** H47 · **дата:** 2026-07-28  
**Зачем:** последний крупный **аналитический** пробел Stage 1 — маржа заказа пошива.  
**Не делаем:** GM 2024–25 из пустого cost; экстраполяцию pilot GM на год; «чинить» историю без ACCEPT.

---

## Вердикт одной строкой

**2024–25 unit-econ МД = BLOCKED** (salon cost fill **0%**). **Вперёд уже есть база:** shop 2026 **90.5%** cost fill, salon 2026 **78.2%**. Касса ядра при этом **работает** (payments↔DDS).

---

## Cost fill (по `period_month`)

| Канал | 2024 | 2025 | 2026 | Статус |
|-------|------|------|------|--------|
| Salon | **0%** (0/277) | **0%** (0/283) | **78.2%** (93/119) | 24–25 BLOCKED · 26 PILOT |
| Shop | 1.0% | 6.6% | **90.5%** (256/283) | 26 PILOT_OK |

Indicative GM **только на строках cost+price** (не SoT, валюта смешанная):
- Salon 2026 both-only ≈ **63.9%**
- Shop 2026 both-only ≈ **75.3%**  
**Нельзя** ставить в P&L / S2 как факт.

Salon 2026 без cost: **26 строк** → `md_salon_2026_missing_cost_top40.csv`.

---

## Что можно / нельзя говорить

| Утверждение | В модель? |
|-------------|-----------|
| Касса МД видна (payments↔DDS) | **ДА** |
| GM заказа 2024–25 | **НЕТ** |
| Pilot GM shop/salon 2026 (both-only) | только с лейблом PILOT |
| Goods −74% = убыток компании | **НЕТ** (артефакт periметра) |
| S2 «рост маржи МД в ₽» | только процессные KPI |

---

## Blockers

1. **MD-UE-01** — нет cost 2024–25 → permanent без нового контура  
2. **MD-UE-02** — нет stock/WIP МД  
3. **MD-UE-03** — price workbook ≠ DDS scale  
4. **MD-UE-04** — 2026-06 DDS=0 (связь H40)  
5. **MD-UE-05** — person-cost quarantine ≠ order cost (H45)

---

## Forward pilots (единственный путь)

| Пилот | Действие | Owner |
|-------|----------|-------|
| Shop 2026 | Закрепить cost обязателен до close месяца | Мокеева + Коновалова |
| Salon 2026 | Довести fill **≥80%** (сейчас 78%, 26 дыр) | Мокеева + мастера |
| Cash KPI | payments↔DDS + fittings/redo — без ложной маржи | Мамушкина / Мокеева |

---

## Owner actions

1. Policy: **no unit-econ 2024–25** в обещаниях Stage 1  
2. Shop process standard  
3. Заполнить 26 salon 2026 missing cost  
4. DDS June upload  
5. Не elevать indicative GM в SoT  

---

## Артефакты

`live/marts/md_cost_fill_by_year.csv` · `md_cost_fill_2026_monthly.csv` · `md_unit_econ_blockers.csv` · `md_unit_econ_forward_pilots.csv` · `md_salon_2026_missing_cost_top40.csv` · `md_unit_econ_can_cannot_say.csv`  
Регистр: `live/registers/h47_md_unit_econ/`

---

## Оценка

**9.2/10**: честно закрывает «почему нет маржи ядра», даёт **реальный** forward path на 2026 (не фантазию по 2024–25), стыкуется с H40/H45.  
Связи: G4 · H30 workbook · H29 cash · H43 DOM-COST.

---

## Статус серии приоритетов

Аналитические блоки H39–H47 покрыли gate → cash collect → RACI → alias → ЗП → IM Accept → MD unit-econ.  
**Дальше ROI почти только у owners** (`owner_execution_backlog_h46.csv`). Новый «слой ради слоя» без файлов/Accept — не рекомендую.
