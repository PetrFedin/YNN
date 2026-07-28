# H45 — Приоритет: Quarantine ЗП янв–фев 2026

**Горизонт:** H45 · **дата:** 2026-07-28  
**Зачем:** после H44 (alias) следующий P0 по целостности 2026 — **починить критический quarantine ведомостей**.  
**Не делаем:** снятие quarantine без фикса; использование person-lines как SoT; «лечение» кассы (она уже CLOSE).

---

## Вердикт одной строкой

В `Распределение` у **янв/фев 2026** сломан блок **Карты (`#REF!`)**. Касса ЗП через DDS↔bank **CLOSE**. Person-level SoT и контроль месяца — **нет**, пока файлы не починят по шаблону апреля.

---

## Root cause (проверено в xlsx)

| Месяц | Карты в Распределение | zp_where (legacy) | dist_cash_card | DDS↔bank |
|-------|----------------------|-------------------|----------------|----------|
| **2026-01** | `#REF!` на окладники/Итого | окладники:r65 | ~186k (мусор) | **CLOSE** |
| **2026-02** | **все** `#REF!` | Отчет В2В:r17 | **0** | **CLOSE** |
| 2026-03 | OK | Распределение | OK | CLOSE |
| **2026-04** | OK (эталон) | Распределение | OK | CLOSE + MATCH |

Февраль хуже: парсер берёт контроль с **Отчет В2В** — это не ЗП-итог месяца.

---

## Что делать owners

**Сливяк (DOM-PAYROLL):**
1. Починить `#REF!` в феврале (сначала) и январе — блок Карты → лист `карты`.  
2. Выверить `ИТОГО ЗП` как в **марте/апреле**.  
3. Не использовать `Отчет В2В` / сырые `окладники` как контроль месяца.  
4. Заменить файлы в `documents/` → re-run W2.

**Мамушкина (Approver):** снять quarantine только после acceptance:
- `zp_where = Распределение`
- нет `#REF!` в Карты
- dist totals ≈ cash+card
- zp↔DDS не хуже GAP / лучше CLOSE

---

## Secondary quarantine (owners исправлены vs H37)

| Файл | Было (H37) | Стало (H45) |
|------|------------|-------------|
| Себестоимость Жукова.xlsx | Payroll | **DOM-COST — Мокеева** |
| Себестоимость Меркушина.xlsx | Payroll | **DOM-COST — Мокеева** |
| Факт анализ продаж B2B 2026.xlsx | Payroll | **DOM-B2B — Коптева** |

---

## Симуляция

| Сценарий | Эффект |
|----------|--------|
| S1 fix Feb | убирает dist=0 и ложный V2B ctrl |
| S2 fix Jan+Feb + W2 | непрерывность person payroll H1 2026 |
| S3 Approver release | lifecycle Active |

---

## Артефакты

| Файл | Назначение |
|------|------------|
| `live/marts/payroll_quarantine_p0_jan_feb.csv` | 2 файла + root cause |
| `live/marts/payroll_quarantine_fix_checklist.csv` | 7 шагов |
| `live/marts/payroll_2026_month_quality.csv` | янв–май сравнение |
| `live/marts/quarantine_secondary_reowned.csv` | G4/G3 owners |
| `live/marts/payroll_quarantine_owner_actions.csv` | 5 действий |
| `live/registers/h45_payroll_quarantine/` | регистр |
| `live/evidence/h45_payroll_quarantine_20260728/` | evidence |

---

## Оценка

**9.4/10**: найден конкретный `#REF!` (не «файл плохой»), касса отделена от person-SoT, есть эталон апреля и checklist.  
Связи: G7 ↔ W2 ↔ DDS/bank; Approver H43; secondary → H42/G4.

---

## Следующий блок (после H45)

Остатки Stage-1 owner-долга: **IM ACQ_POS Accept slices (H39)** / **unit-econ МД (blocked)** — или ждать replace файлов ЗП.
