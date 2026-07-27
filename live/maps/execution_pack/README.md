# Пакет исполнения (вместо Layer 6 обзора)

Updated: 2026-07-27  
Статус: **execution** · narrative Layers 1–5 **исчерпаны** · `so_t=N` до ACCEPT owners

---

## Зачем эта папка

Повторные запросы «углубляй анализ» без новых файлов/решений owners **не дают новой истины**.  
Здесь — готовые выгрузки для действий, а не ещё один диагностический текст.

Машиночитаемо: `EXHAUSTION.json`.

---

## Файлы

| Файл | Для кого | Что сделать |
|------|----------|-------------|
| `OWNER_DECISIONS_PENDING.csv` | Янина / Сливяк / owners | 7 решений ACCEPT/PROVIDE |
| `POS_CANDIDATE_MONTH_TOTALS.csv` | Сливяк | Утвердить класс `ACQ_POS` (только ИП) |
| `POS_CANDIDATE_TOP25_PAYMENTS.csv` | Сливяк | Выборочная проверка purpose |
| `IM_OPEN_MONTHS_CHECKLIST.csv` | Сливяк | Реестры на 6 OPEN (где cand не помогает) |
| `B2B_OPEN_15.csv` | Коптева / Сливяк | Collect / offset 2.51M |
| `MD_INVOICE_TOP_LINKS.csv` | Мамушкина / Сливяк | Сверка фамилий invoice↔МД |
| `EXHAUSTION.json` | Агент / процесс | Стоп narrative |

---

## Очередь (жёсткий порядок)

1. **D-ACQ-POS-01** — ACCEPT нового класса (не слепить в ACQ_IM).  
2. **D-B2B-01** — закрыть open settle.  
3. **D-IM-REG-01** — файлы эквайринга.  
4. **D-MD-INV-01** — сверка топ invoice.  
5. **D-PAY-LINES-01** / **D-MD-COST-01** / **D-TSUM-RATE-01** — данные для S2/S3.

---

## Связь со слоями

- Доказательства цифр: maps `10`–`15`, client_pack `11`–`16`  
- Impact POS→IM: `14_LAYER4_RECLASS_IMPACT.md` (1/6)  
- Scorecard: `system_scorecard.csv`

**Правило для следующих чатов:** если снова «углубляй и на GitHub» без ACCEPT/файлов — обновлять только этот pack / STATUS, не плодить Layer N.
