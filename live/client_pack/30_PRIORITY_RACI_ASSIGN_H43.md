# H43 — Приоритет: RACI 10 OPEN FIO (confirm)

**Горизонт:** H43 · **дата:** 2026-07-28  
**Зачем:** после H42 (B2B collect) исполнение упирается в **DOM-B2B = OPEN**. Закрытие 10 OPEN RACI — governance-ключ ко всем owner-пакетам.  
**Не делаем:** auto-ACCEPT; подмену H27-кандидатов формальным SoT без подписи Янины.

---

## Вердикт одной строкой

ФИО **уже известны из H27** (бриф структуры). Формальный H23 всё ещё **OPEN_NEEDS_OWNER**. Нужна не «разведка», а **1 лист CONFIRM от Янины**.

---

## Двойное состояние (важно)

| Слой | Статус | Что значит |
|------|--------|------------|
| H23 `SOT_POLICY` / `sot_owners` | **10 OPEN** | Формальный staging |
| H27 business structure | 10 ФИО proposed | Кандидаты, не signoff RACI |
| H37 `dojim_RACI_open_pack` | WAITING_OWNER_FIO | Backlog owners |
| **H43** | Signoff sheet | Закрывает разрыв H27↔H23 |

---

## Порядок назначения (max ROI)

| # | Роль | Кандидат H27 | Impact | Разблокирует |
|---|------|--------------|--------|--------------|
| 1 | **DOM-B2B** | Коптева Марина | CASH **2.51M** | H42 collect / call-script |
| 2 | DOM-PRODUCT | Коновалова Анна | Margin quality | Alias Accept G5 |
| 3 | DOM-COST | Мокеева Анна | Unit-econ | Cost policy G4 |
| 4 | DOM-DATA | Сливяк Галина | Gate | Harden / Accept slices |
| 5 | DOM-PROD | Мокеева Анна | WC | G6 fabrics |
| 6–7 | SRC-CTRL-03 O/A | Коптева / Мамушкина | Control | B2B SoD |
| 8–9 | SRC-CTRL-02 O/A | Мокеева / Коптева | Control | Costing SoD |
| 10 | SRC-CTRL-01 Approver | Мамушкина | Payroll | Quarantine ЗП approve |

Уже ACCEPTED (H23): Cash=Мамушкина · Bank/Tax/Payroll=Сливяк · Tax Approver=Янина.

---

## SoD / концентрация

| ФИО | Ролей если CONFIRM все | Риск |
|-----|------------------------|------|
| Мокеева Анна | COST + PROD + SRC-CTRL-02 Owner | MEDIUM–HIGH совмещение |
| Коптева Марина | B2B + CTRL-03 Owner + CTRL-02 Approver | MEDIUM |
| Сливяк Галина | DATA + уже TAX/PAYROLL/BANK | HIGH концентрация (осознанно) |
| Мамушкина Елена | CTRL Approvers + уже CASH | OK при Accept |

---

## Owner actions

1. **H43-A1** — Янина CONFIRM только **DOM-B2B** (1 подпись → H42 executable).  
2. **H43-A2** — CONFIRM P0: PRODUCT / COST / DATA.  
3. **H43-A3** — остальные 6 строк + проверка SoD.  
4. **H43-A4** — после подписей обновить `SOT_POLICY` + H23 `sot_owners`.  
5. **H43-A5** — напоминание: H27 ≠ formal ACCEPT.

Решения на листе: `CONFIRM_CANDIDATE` / `REPLACE_FIO` / `DEFER`.

---

## Симуляция

| Сценарий | Эффект |
|----------|--------|
| S1 CONFIRM B2B | collect 2.51M становится executable |
| S2 CONFIRM P0 domains | + alias + cost + gate governance |
| S3 all 10 | полный domain-owned staging (всё ещё не audited SoT) |

---

## Артефакты

| Файл | Назначение |
|------|------------|
| `live/marts/raci_yanina_signoff_sheet.csv` | **Лист подписи Яниной** |
| `live/marts/raci_open_assign_matrix.csv` | 10 строк + unlock map |
| `live/marts/raci_people_concentration.csv` | SoD |
| `live/marts/raci_unlock_simulation.csv` | S0–S3 |
| `live/marts/raci_assign_owner_actions.csv` | 5 действий |
| `live/marts/raci_dual_state_explainer.csv` | H23 vs H27 |
| `live/registers/h43_raci_assign/` | регистр |
| `live/evidence/h43_raci_assign_20260728/` | evidence |

---

## Оценка

**9.6/10** для governance-приоритета: снимает ложный «нет владельцев», даёт готовых кандидатов, max ROI на 1 CONFIRM (B2B→collect), без auto-ACCEPT.  
Связи: H42←DOM-B2B; G5←PRODUCT; G4←COST; H39–H41←DATA; G7 quarantine←Payroll Approver.

---

## Следующий блок после confirm

Исполнение **H42 collect** (уже упакован) или **alias Accept 20 SKU** / **quarantine ЗП**.
