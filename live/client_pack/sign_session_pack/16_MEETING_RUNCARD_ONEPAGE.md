# Пакет на стол — one-pager встречи (H79)

**Цель:** gate **18→30** · **не SoT** · без auto-Accept  
**Держать открытыми:** `01_SIGN_CHECKBOXES` · `07_E02` · `10_E08` · `14_TAX_SOFT` · `15_SIM`

---

## 15–20 минут

| Мин | Кто | Что подписать / сказать |
|-----|-----|-------------------------|
| 0–2 | ведущий | Data закрыты (H73–H77). Сегодня только подписи. Scope: Stage1 = диагностика (**не** UE/регламенты) — H82/договор. Запреты: не весь POS; не goods как P&L; не FORCE_CLOSE TAX/Feb |
| 2–7 | **Янина** | E01, E03a–c, E12, FRAME1–2, **E08 Path A** · OPEN RACI: evidence [`21_RACI_SIGNOFF_EVIDENCE_H82.csv`](21_RACI_SIGNOFF_EVIDENCE_H82.csv) (10/10) |
| 7–12 | **Сливяк + Мамушкина** | **E02a/b** soft 509 351 + 37 328 · E06 дата · по возможности **TAX perimeter** |
| 12–15 | все | Фото листа · пинги `02_*` · async хвост |
| 15–20 | буфер | Если успели — `TAX_PERIMETER` + `TAX36k` (= **26→27**) |

CSV-скрипт: [`16_MEETING_MINUTE_SCRIPT.csv`](16_MEETING_MINUTE_SCRIPT.csv)

---

## После встречи (без нового совещания)

1. E07 overbank confirm  
2. TAX perimeter (если не на встрече) — SLA **2026-08-06**  
3. Feb dump · Mercury · DDS June
4. HR UNFORMAL+paid (H83) — [`22_HR_UNFORMAL_PAID_H83.csv`](22_HR_UNFORMAL_PAID_H83.csv) → Сливяк/Мамушкина
5. Fabric DEAD_STOCK (H84) — [`23_FABRIC_DEAD_STOCK_H84.csv`](23_FABRIC_DEAD_STOCK_H84.csv) → Мокеева/Дендерина
6. Tax gaps (H85) — [`24_TAX_COMPLETENESS_GAPS_H85.csv`](24_TAX_COMPLETENESS_GAPS_H85.csv) → Сливяк (Q2’26 + OCR)  

Путь: [`13_GATE_CRITICAL_PATH.csv`](13_GATE_CRITICAL_PATH.csv) · симуляция: [`15_GATE_UNLOCK_SIMULATION_H78.csv`](15_GATE_UNLOCK_SIMULATION_H78.csv)

---

## Запреты (повторить вслух)

- Не принимать **весь** POS как IM  
- Не June POS/TBank → TSUM_NET  
- Не FORCE_CLOSE TAX без perimeter / Feb без dump  
- Не путать «доходы−расходы» SALES с P&L компании

---

После подписи: [`17_POST_SIGN_ACTIVATION.csv`](17_POST_SIGN_ACTIVATION.csv) · отправить: [`18_TELEGRAM_BLAST_READY.csv`](18_TELEGRAM_BLAST_READY.csv)
