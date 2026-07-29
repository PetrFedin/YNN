# H59 — Alias evidence + TSUM missing + soft-slice/ZP cards

**Дата:** 2026-07-29  
**Зачем:** закрыть оставшиеся data-prep дыры Wave B/C/A — evidence для alias, доказательство отсутствия Mercury, карточки soft-slice и ЗП P0.  
**Не делаем:** fake TSUM allocate / auto-Accept alias.

---

## 1. TSUM — платёж Меркурий за май **MISSING_IN_BANK**

| Sales | Ожидаемый net | В банке за pay-month | Статус |
|-------|---------------|----------------------|--------|
| 2026-05 | ~2.58M (окно 20–30.06) | **0** Mercury в июне | MISSING |
| 2026-06 | ~1.77M (окно 20–30.07) | 0 (окно впереди) | WAIT |

Последний Mercury в выписке: **2026-05-28** (оплата апреля).  
Июньские крупные приходы = POS/TBank — **не** TSUM (`08_tsum_do_not_allocate…`).

## 2. Alias топ-5 evidence

Один лист: sale vs cost names + revenue/COGS/lines + preferred CV.  
Wave B: `11_alias_top5_evidence_sheet.csv`

## 3. Soft-slice sign card

2 строки с payment_id и суммами долей — в `sign_session_pack/06_…` и Wave A `16_…`.

## 4. ZP P0 runbook

Янв/фев: file id, #REF! evidence, acceptance, target 2026-08-04.  
Wave A: `17_zp_p0_fix_runbook.csv`

---

## Оценка

**9.4/10**: TSUM — фактологическая проверка банка; alias/ZP/soft — готовые к подписи/правке листы.
