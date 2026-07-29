# H54 — Wave B ready-pack (усиление исполнения)

**Дата:** 2026-07-29  
**Зачем:** Wave A уже упакован; следующий по важности слой — **готовые к работе пакеты Wave B/C** (cash / margin / gate), иначе после подписи H51 owners снова «не знают с чего начать».  
**Не делаем:** fake ACCEPT; новый forensic; BPMN/audited P&L.

---

## Приоритет сейчас

| Ранг | Что | Wave | Impact |
|------|-----|------|--------|
| 1 | Подпись H51 (разблок B) | A | CRITICAL |
| 2 | Soft-slice → gate 18→20 | A | HIGH |
| 3 | B2B топ-3 звонки (~2.07M) | B | HIGH cash |
| 4 | Overbank реестры ×4 | B | HIGH gate |
| 5 | Alias топ-5 | B | HIGH margin |
| 6 | DDS June + card policy | C | HIGH gate +3…+4 |
| 7 | 26 salon cost | B | MED pilot |
| 8 | TSUM Mercury / TIMING | C | MED →30/30 |

Папка: `live/client_pack/execution_wave_b/`

---

## Что внутри Wave B

| Файл | Содержание |
|------|------------|
| `00_WAVE_B_CHECKLIST.csv` | E01→E10 статусы и done_when |
| `01_b2b_call_top3.csv` | Скрипты + outcome fields |
| `02_b2b_docs_top3.csv` | 6 документов по топ-3 |
| `03_alias_top5.csv` | Лист Коноваловой |
| `04_md_salon_cost_wo.csv` | 26 строк FILL cost |
| `05_bank_dds_work_orders.csv` | June / card policy / 2026-02 |
| `06_tsum_wait_calendar.csv` | Окна оплаты Меркурий |
| `07_gate_score_ladder.csv` | 18→20→24→28→30 |
| `08_person_action_cards.csv` | Карточки по людям |
| `09_file_intake_priority_v2.csv` | Intake v2 (A+B+C) |

Карты: `23_WAVE_B_READY.md` · `24_GATE_SCORE_LADDER.md` · `25_PERSON_ACTION_CARDS.md`

---

## Лестница gate (зачем это важно)

```
18 ──E02──► 20 ──E07──► 24 ──E08──► 28 ──E10──► 30
     soft      overbank    BANK/DDS     TSUM
```

Без подписей/файлов score **застрял на 18**.

---

## Карточки людей (сегодня)

- **Янина (15 мин):** E01 + E03 + dual contour  
- **Сливяк (30):** soft-slice + overbank 2024-08 + DDS June ask  
- **Коптева (после E01):** 3 звонка  
- **Коновалова (после E03):** 5 SKU  
- **Мокеева:** 26 cost lines  

---

## Оценка

**9.5/10** как усиление приоритета: превращает «Wave B существует в board» в **открываемые CSV с outcome-полями**, без изобретения Accept.
