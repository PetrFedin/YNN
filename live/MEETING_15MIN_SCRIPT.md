# Meeting script — 15 минут (Янина / Сливяк / команда)

Updated: 2026-07-28 (H49 handoff)

Цель: зафиксировать рамку Stage 1 и **запустить Wave A** (E01/E02/E03/E06).  
Материалы на экране:
- `live/client_pack/36_STAGE1_HANDOFF_H49.md`
- `live/marts/master_execution_board.csv`
- Decision log: `live/marts/handoff_decision_log_blank.csv`

---

## 0:00–3:00 — Рамка сдачи
- Этап 1 = **диагностика на periметре документов**, не внедрение и не audited P&L.
- Два контура: **МД/пошив** (касса) vs **товар** (IM/B2B/ЦУМ).
- Запрет: **−58%/−74% goods ≠ убыток компании.**
- Gate сейчас **18/30**; путь к 30 расписан (не «всё сломано»).

## 3:00–7:00 — Что уже DONE
- G1–G9 + H37–H48 упакованы на GitHub `main`.
- Касса/ДДС/payroll multi в целом читаемы; дыры — точечные.
- MD unit-econ **2024–25 blocked**; **2026 shop 90%** cost = пилот вперёд.
- Единый план: **E01–E12** (H48), не новые отчёты.

## 7:00–12:00 — Решения в комнате (заполнить decision log)

1. **E01** CONFIRM DOM-B2B = Коптева? **Да / другое ФИО / later**  
2. **E03** CONFIRM PRODUCT/COST/DATA (Коновалова/Мокеева/Сливяк)? **Да / правки**  
3. **E02** ACCEPT POS soft 509k (04.26) + 37k (08.25)? **Да / нет**  
4. **E06** Сливяк чинит ЗП янв–фев `#REF!` до даты ____?  
5. Рамка: два контура + запрет −58% как company P&L? **Да / нет**  
6. Unit-econ МД 2024–25 не обещаем? **Да / нет** (E12)

## 12:00–15:00 — Close
- Записать ответы в `handoff_decision_log_blank.csv`.
- Следующий sync: только статусы E01–E12 / новые файлы.
- **Не** стартуем Phase C / unified P&L без рамки п.5–6.
- Новый «аналитический слой» без Accept/файлов — **не заказываем**.

---

## Decision Log (на встрече)

| ID | Decision | Answer | Date |
|----|----------|--------|------|
| D-H48-01 | DOM-B2B CONFIRM | | |
| D-H48-02 | PRODUCT/COST/DATA | | |
| D-H48-03 | POS 2026-04 slice | | |
| D-H48-04 | POS 2025-08 slice | | |
| D-H48-05 | ZP #REF! date | | |
| D-FRAME-01 | Dual contour | | |
| D-FRAME-02 | Ban −58% as company P&L | | |
| D-H47-01 | No MD UE 2024–25 promise | | |
