# SoT Policy (после RACI ACCEPT) — H23

Updated: 2026-07-24 19:21

## Статус

**RACI draft ACCEPTED** для строк с ФИО.
Это **domain-owned staging**, не полный Source of Truth всего контура.

### Accepted owners

| Domain / control | Owner |
|------------------|-------|
| Cash / Treasury (DOM-CASH) | Мамушкина Елена |
| Bank perimeter (SRC-CTRL-04 Owner) | Сливяк Галина |
| Bank Approver | Мамушкина Елена |
| Tax (DOM-TAX, SRC-CTRL-05 Owner) | Сливяк Галина |
| Tax Approver | ЯНИНА ЮЛИЯ ФЕДОРОВНА |
| Payroll (DOM-PAYROLL, SRC-CTRL-01 Owner) | Сливяк Галина |

### Ещё OPEN (нужны ФИО)

- `SRC-CTRL-01` / Approver
- `SRC-CTRL-02` / Owner
- `SRC-CTRL-02` / Approver
- `SRC-CTRL-03` / Owner
- `SRC-CTRL-03` / Approver
- `DOM-PRODUCT` / Owner
- `DOM-COST` / Owner
- `DOM-PROD` / Owner
- `DOM-B2B` / Owner
- `DOM-DATA` / Owner

## Политики данных (accepted)

1. **Margin exceptions** `WHOLESALE_OK_LOSS` (0-2493A/2496/2497) — owner-accepted; reported margin включает, clean margin исключает.
2. **0-3243** — quarantine до cost version свитшота; не релинковать на худи/юбку.
3. **Release gate** H18 остаётся PROVISIONAL как operational gate; можно ужесточать пороги с data steward (когда назначен).
4. Регистры W1–W6 + marts — **controlled staging with named owners**, не audited accounting SoT.

## Следующие шаги (фаза C)

1. Назначить Owners на Product / Cost / Production / B2B / Data steward
2. Зафиксировать SKU alias registry (кандидаты H17) под Product Owner
3. Ужесточить release gate (запрет SOFT) после data steward
4. Закрывать BLOCKED months данными из DATA_REQUESTS_NOW

Evidence: `chat ACCEPT 2026-07-24 (user confirmed RACI draft)`


---

## H26 — временные заглушки (2026-07-24 19:26)

На OPEN-доменах поставлены **TEMPORARY STUBS** (не реальные ФИО):

| Domain | Stub |
|--------|------|
| PRODUCT | ВРЕМЯНКА Product Owner (stub) |
| COST | ВРЕМЯНКА Cost Owner (stub) |
| PRODUCTION | ВРЕМЯНКА Production Owner (stub) |
| B2B | ВРЕМЯНКА B2B Owner (stub) |
| DATA_STEWARD | ВРЕМЯНКА Data Steward (stub) |

`decision = ACCEPT_STUB`. Заменить на реальные ФИО → обычный `ACCEPT`.
Пока stubs: domain ops может назначать задачи, **полный SoT person-level не заявлен**.


---

## H27 — структура бизнеса и реальные owners (2026-07-24 19:29)

Stubs **сняты**. Owners из брифа:

| Domain | Owner |
|--------|-------|
| CASH | Мамушкина Елена |
| BANK / TAX / PAYROLL / DATA | Сливяк Галина |
| TAX Approver | Янина Ю.Ф. |
| PRODUCT | Коновалова Анна |
| COST / PRODUCTION | Мокеева Анна |
| B2B | Коптева Марина |

Полный текст: `live/BUSINESS_STRUCTURE.md`  
Model flags: `live/marts/model_flags_h27.csv` (особенно **комиссия ЦУМ в COGS**).
