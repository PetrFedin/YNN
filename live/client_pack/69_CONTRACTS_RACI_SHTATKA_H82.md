# H82 — Contracts / RACI / штатка bridge (P2)

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (следующий приоритет после H81)

P0 (подписи/файлы) без owners не двигается.  
Среди оставшихся документных связок **макс. ROI для встречи**:  
**договор Stage1 + «Финансы и платежи» + штатка ↔ formal RACI / yanina signoff**.

G9 уже описывал группу файлов; H82 делает **машиночитаемый bridge** и evidence-ready лист для OPEN roles.

## Источники (catalog 107)

| Файл | Роль |
|------|------|
| Договор комплексной диагностики + паспорт | Scope IN/OUT Stage1 |
| NDA | режим данных |
| план работы.docx | пилот 3–4 нед / зачёт в бюджет |
| Финансы и платежи.docx | ops RACI draft |
| Штатка ИП.xlsx | 84 чел · roster |

## Результаты

| Метрика | Значение |
|--------:|----------|
| Domain blocks | **10** |
| People×domain rows | **24** |
| Штатка | **84** |
| UNFORMAL в штатке | **38** |
| Из них в finance RACI | **0** (ключевые owners оформлены) |
| RACI-имена найдены в штатке | **11** |
| Signoff candidates evidence YES | **10 / 10** |
| Vacancy | **Кладовщик** (замещают Дендерина + Коновалова) |
| B2B gap | **менеджера нет** (контроль = Коптева) |

### Domains → H23

| Domain ops | → formal | Status | Сигнал |
|------------|----------|--------|--------|
| Cash / безнал | CASH | ACCEPTED | Мамушкина + Сливяк |
| Налоги/1С | TAX | ACCEPTED | Сливяк |
| ФОТ | PAYROLL | ACCEPTED | цеха + Сливяк свод + выдача Мамушкина |
| Закупки | COST | OPEN | Дендерина / Меркушина / Богдашкина |
| Склад | PRODUCT | OPEN | vacancy кладовщик |
| Производство МД | PRODUCTION | OPEN | Мокеева + Богдашкина |
| Себестоимость | COST | OPEN | 4 R без единого Owner |
| B2B | B2B | OPEN | менеджера нет → Коптева A |
| B2C | — | MAP | Лимачева (нет DOM-B2C) |

### Scope Stage1 (договор) — напоминание на встречу

**IN:** диагностика, отчёт, карта ограничений, рекомендации, презентация.  
**OUT:** внедрение, постановка УУ, регламенты, сопровождение изменений, аудит отчётности / налоговая·юрэкспертиза (если не оговорено отдельно).

## Что даёт проекту

1. **Meeting ammo:** все 10 строк `raci_yanina_signoff_sheet` имеют evidence YES (в finance doc + штатке, не UNFORMAL).
2. **Нет расползания scope** на встрече — договор явно режет Stage2-обещания.
3. **Два конкретных org-gap:** кладовщик vacancy; B2B без менеджера — без fake Accept.
4. **HR risk packaged:** 38 UNFORMAL — следующий P2 (HR↔payroll), не gate.

## Артефакты

- Register: `live/registers/h82_contracts_raci_bridge/` (+ `build_h82.py`)
- Marts: `contracts_*.csv` · `h82_meta.json`
- Map: `live/maps/53_CONTRACTS_RACI_SHTATKA_MAP.md`
- Связь: G9 narrative · sign pack `01_*` / `16_*`

## Gate

**18/30** — P2 ops. Score двигают только owners (E02…) / intake файлы.
