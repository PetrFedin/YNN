# H53 — Приоритетное усиление (что двигает метрики)

**Дата:** 2026-07-29  
**Зачем:** после H52 (карты) закрыть следующий слой «не хватает» — **шаблоны запроса файлов / очередь match / граф разблокировок**. Без этого owners не знают *что именно* принести.  
**Не делаем:** fake ACCEPT; forensic ради слоя; BPMN/audited P&L (Stage 2+).

---

## Приоритет (что важнее сейчас)

| Ранг | Действие | Тип | Разблокирует | Impact |
|------|----------|-----|--------------|--------|
| 1 | Подпись H51 draft (15 мин) | DECISION | весь Wave A | CRITICAL |
| 2 | Soft-slice IM POS Accept | DECISION | gate 18→20 | HIGH |
| 3–4 | Реестры overbank 2024-08, 2025-01 | FILE | 2× IM OPEN explain | HIGH |
| 5 | ЗП #REF! янв–фев | FILE | person payroll SoT | MED |
| 6 | Реестры 2026-03, 2025-10 | FILE | остальные OVERBANK | HIGH |
| 7 | Top-5 surname → payment match | EXTRACT | invoice↔МД usable | MED |
| 8 | 26 salon cost 2026 | DATA | pilot GM | MED |

CSV: `file_intake_priority.csv` · `unlock_dependency_graph.csv`

---

## 1. Overbank — work orders (4 месяца)

POS **запрещён**. Нужен реестр возмещений.

| WO | Месяц | Surplus | Особенность |
|----|-------|---------|-------------|
| WO-ACQ-2024-08 | 2024-08 | ~725k | POS+TBank+Dekor |
| WO-ACQ-2025-01 | 2025-01 | ~421k | **POS=0** — только TBank |
| WO-ACQ-2026-03 | 2026-03 | ~264k | POS pool огромный vs sales |
| WO-ACQ-2025-10 | 2025-10 | ~245k | POS >> IM |

Шаблон колонок: `im_overbank_register_template.csv`  
Заказы: `im_overbank_work_orders.csv`

---

## 2. MD↔invoice — очередь payment-level

Surname MED (~15.6M / 40%) уже есть. Следующий шаг — **не новый анализ**, а ручной match по правилам R1–R6.

Топ очереди (по bank ₽): Кулишова → Ахмедова → Сейдак → Седых → Коган.  
`md_invoice_payment_match_queue.csv` · `md_invoice_payment_match_rules.csv`

Правило политики: **нет Accept автоматом** даже на STRONG_LINK — только батч + human.

---

## 3. Граф разблокировок

Критический узел **U09** (подпись H51) → U01–U03.  
Параллельно файловый контур U05 (4 реестра) и U04 (ЗП).  
U10 (BPMN/P&L) = out of scope сейчас.

Карта: `20_UNLOCK_DEPENDENCY.md` · `21_IM_OVERBANK_WORK_ORDERS.md` · `22_MD_INVOICE_PAYMENT_QUEUE.md`

---

## Оценка

**9.4/10** как ops-усиление: превращает «нужны файлы» в конкретные WO + шаблон + очередь match + порядок подписей. Метрики gate/cash двигаются только после исполнения owners.
