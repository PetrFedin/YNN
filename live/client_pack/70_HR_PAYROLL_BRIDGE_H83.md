# H83 — HR policy ↔ штатка ↔ payroll streams (P2)

Updated: 2026-07-29 · indicative · **не SoT** · **do_not_auto_accept=YES**

## Зачем (приоритет после H82)

H82 показал **38 UNFORMAL** в штатке. Следующий вопрос по важности:  
**кто из них реально получает деньги в 2026** и как это стыкуется с Положением об оплате.

Без этого Wave B (ФОТ / 6‑НДФЛ / owners) спотыкается о roster drift.

## Источники

| Слой | Файл / mart |
|------|-------------|
| Policy | Положение об оплате…doc + Приложение 1 |
| Roster | Штатка (H82 `contracts_shtatka_coverage`) |
| Monthly ZP | w2 `payroll_lines` 2026 (479 строк) |
| Designers | H73 `designer_kpi_monthly` |
| Цех | H74 `shop_pay_totals` |

Янв/фев 2026 ZP остаются в **quarantine** (#REF!) — суммы person-level indicative.

## Результаты

| Метрика | Значение |
|--------:|----------|
| Штатка | **84** |
| UNFORMAL | **38** |
| **UNFORMAL + paid 2026** | **36** |
| Σ выплат UNFORMAL (indicative) | **~11.56M ₽** |
| Уникальных в payroll streams 2026 | **109** |
| Есть выплата, нет в штатке | **27** |
| В штатке, нет выплаты 2026 | **2** |
| Policy↔group MISMATCH | **6** |

### Топ UNFORMAL+paid (для разбора)

| ФИО | Роль | Группа | Σ 2026 ≈ |
|-----|------|--------|--------:|
| Янина Дарья | директор по межд. проектам | SALARY | 1.60M |
| Скитева Татьяна | Конструктор | DESIGNERS | 1.39M |
| Галецкий Антон | дизайнер ИМ | SALARY | 0.82M |
| Корнеева Юля | дизайнер-художник | SALARY | 0.73M |
| Ходина Анна | художник по тканям | SALARY | 0.65M |
| Прудникова Л. | Вышивальщица | EMBROIDERY | 0.50M |

Полный список: `hr_unformal_paid_2026.csv`.

### Policy streams

| Система (Положение) | People | Paid | UNFORMAL paid | Артефакт выплат |
|---------------------|-------:|-----:|--------------:|-----------------|
| TIME_SALARY (повременная) | 44 | 43 | 10 | окладники |
| SALARY_BONUS (окладно‑прем.) | 44 | 44 | 18 | вышивка + конструкторы |
| PIECE_BONUS (сдельно‑прем.) | 22 | 21 | 7 | ЗП_ЦЕХ + Прил.1 |

### Дыры в Положении (не цифры)

- наставничество — **НА ОБСУЖДЕНИЕ**
- совмещение / доплата — **НА ОБСУЖДЕНИЕ**
- лимиты командировок — пусто  
Зафиксировано: проезд **3500 ₽**, график **40%/60%** (20-е / 5-е), выплата на карту.

## Что даёт проекту

1. **P1 compliance pack** для Сливяк/Мамушкина: 36 имён с деньгами без оформления — не «ещё forensic».
2. Связка **policy → sheet group → H73/H74** без смешения с company P&L.
3. Roster gap **27** payroll-only — чинить штатку до owner-проверок.
4. Не трогает gate score; усиливает исполнение после sign session.

## Артефакты

- Register: `live/registers/h83_hr_payroll_bridge/` (+ `build_h83.py`)
- Marts: `hr_*.csv` · `h83_meta.json`
- Map: `live/maps/54_HR_PAYROLL_BRIDGE_MAP.md`
- Meeting/ops: `live/client_pack/70_HR_PAYROLL_BRIDGE_H83.md`

## Gate

**18/30** — P2. Score двигают только owners / intake файлы.
