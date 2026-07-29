# Пакет на подпись — 15–20 минут (H78 sync · H76 TAX perimeter)

**Дата пакета:** 2026-07-29  
**Цель:** один документ на встречу → сдвиг gate **18→30**.  
**Это черновик рекомендаций, не авто-Accept в SoT.**

Карта пути: [`13_GATE_CRITICAL_PATH.csv`](13_GATE_CRITICAL_PATH.csv) · хвост: [`12_GATE_TAIL_CHECKLIST.csv`](12_GATE_TAIL_CHECKLIST.csv) · симуляция: [`15_GATE_UNLOCK_SIMULATION_H78.csv`](15_GATE_UNLOCK_SIMULATION_H78.csv)

---

## Тайминг

| Мин | Кто | Что |
|-----|-----|-----|
| 0–2 | ведущий | Stage 1 DONE; gate 18/30; пакет H68–H71 готов |
| 2–7 | Янина | E01, E03a–c, E12, FRAME1–2 · **E08 Path A core−card** (рекомендуем) |
| 7–14 | Сливяк + Мамушкина | **E02** soft-slice · дата E06 ЗП · next: E07/TAX/Mercury файлы |
| 14–20 | все | фото листа · разослать пинги `02_*` |

Чекбоксы: [`01_SIGN_CHECKBOXES.csv`](01_SIGN_CHECKBOXES.csv) · E02 evidence: [`07_E02_EVIDENCE_BRIEF.md`](07_E02_EVIDENCE_BRIEF.md)

---

## Блок Янина (CONFIRM / YES)

1. ☐ **E01** DOM-B2B = **Коптева** → collect 2.51M  
2. ☐ **E03a** DOM-PRODUCT = **Коновалова**  
3. ☐ **E03b** DOM-COST = **Мокеева**  
4. ☐ **E03c** DOM-DATA = **Сливяк**  
5. ☐ **E12** Не обещать UE МД **2024–25**  
6. ☐ **FRAME1** Два контура в отчётах  
7. ☐ **FRAME2** Запрет goods −58/−74% как P&L компании  
8. ☐ **E08 Path A** core−card policy `D-H58-BANK-01` → gate BANK ([`10_E08_*`](10_E08_DUAL_PATH_CHECKLIST.csv))

Подпись Янина: __________ дата: ______

---

## Блок Сливяк / Мамушкина (на встрече)

9. ☐ **E02a** Soft-slice IM **2026-04 = 509 351.08 ₽** (не весь POS)  
10. ☐ **E02b** Soft-slice IM **2025-08 = 37 327.69 ₽**  
11. ☐ **E06** ЗП `#REF!` янв–фев до **2026-08-04**

Подпись Сливяк: __________  Мамушкина: __________  дата: ______

---

## Сразу после / async (без нового совещания)

| # | Действие | Файл | Gate |
|---|----------|------|------|
| A | Confirm overbank hypotheses (TBANK→IM, POS→HOLD) | `../execution_wave_a/20_im_overbank_hypothesis_prefill.csv` | →24 |
| B | TAX 36k + Salon UFK perimeter (H76) | [`11_TAX_36K_EVIDENCE_BRIEF.md`](11_TAX_36K_EVIDENCE_BRIEF.md) · [`14_TAX_SOFT_PERIMETER_H76.csv`](14_TAX_SOFT_PERIMETER_H76.csv) | →27 |
| C | DDS Feb dump (−1.5M) | `../execution_wave_c/27_feb2026_recon_work_order.csv` | →28 |
| D | Mercury May + July bank | `../execution_wave_c/26_mercury_intake_work_orders.csv` | →29 |
| E | DDS 2026 full June | `../execution_wave_c/01_bank_dds_work_orders.csv` | BANK_ONLY |

Чеклист хвоста: [`12_GATE_TAIL_CHECKLIST.csv`](12_GATE_TAIL_CHECKLIST.csv)

---

## Жёсткие запреты

- Не принимать **весь** POS как IM  
- Не лить POS в **OVERBANK** / не `ADD_POS_TO_IM`  
- Не мапить June POS/TBank в **TSUM_NET**  
- Не FORCE_CLOSE Feb без article dump  
- Не FORCE_CLOSE TAX без подписи Salon UFK perimeter (H76)  
- Не смешивать контур МД и товарный P&L  

---

## После подписи Wave B

1. Коптева — `../execution_wave_b/01_b2b_call_top3.csv`  
2. Коновалова — alias топ-5  
3. Мокеева — salon cost lines  

Пинги: [`02_OWNER_PING_MESSAGES.csv`](02_OWNER_PING_MESSAGES.csv) · Today: [`08_TODAY_TOP5_P0.csv`](08_TODAY_TOP5_P0.csv)
