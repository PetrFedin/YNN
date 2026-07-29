# Пакет на стол — one-pager встречи (H79)

**Цель:** gate **18→30** · **не SoT** · без auto-Accept  
**Держать открытыми:** `01_SIGN_CHECKBOXES` · `07_E02` · `10_E08` · `14_TAX_SOFT` · `15_SIM`

---

## 15–20 минут

| Мин | Кто | Что подписать / сказать |
|-----|-----|-------------------------|
| 0–2 | ведущий | Data закрыты (H73–H77). Сегодня только подписи. Запреты: не весь POS; не goods как P&L; не FORCE_CLOSE TAX/Feb |
| 2–7 | **Янина** | E01, E03a–c, E12, FRAME1–2, **E08 Path A** |
| 7–12 | **Сливяк + Мамушкина** | **E02a/b** soft 509 351 + 37 328 · E06 дата · по возможности **TAX perimeter** |
| 12–15 | все | Фото листа · пинги `02_*` · async хвост |
| 15–20 | буфер | Если успели — `TAX_PERIMETER` + `TAX36k` (= **26→27**) |

CSV-скрипт: [`16_MEETING_MINUTE_SCRIPT.csv`](16_MEETING_MINUTE_SCRIPT.csv)

---

## После встречи (без нового совещания)

1. E07 overbank confirm  
2. TAX perimeter (если не на встрече) — SLA **2026-08-06**  
3. Feb dump · Mercury · DDS June  

Путь: [`13_GATE_CRITICAL_PATH.csv`](13_GATE_CRITICAL_PATH.csv) · симуляция: [`15_GATE_UNLOCK_SIMULATION_H78.csv`](15_GATE_UNLOCK_SIMULATION_H78.csv)

---

## Запреты (повторить вслух)

- Не принимать **весь** POS как IM  
- Не June POS/TBank → TSUM_NET  
- Не FORCE_CLOSE TAX без perimeter / Feb без dump  
- Не путать «доходы−расходы» SALES с P&L компании

---

После подписи: [`17_POST_SIGN_ACTIVATION.csv`](17_POST_SIGN_ACTIVATION.csv) · отправить: [`18_TELEGRAM_BLAST_READY.csv`](18_TELEGRAM_BLAST_READY.csv)
