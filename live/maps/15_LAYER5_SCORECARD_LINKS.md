# 15 — Layer 5: scorecard системы + POS по LE + invoice↔МД

Updated: 2026-07-27  
Статус: **сводка исполнения + точечные связи** · не SoT · не Layer-обзор-близнец  
Артефакты: `system_scorecard.csv`, `pos_candidate_by_le_month.csv`, `md_invoice_surname_links.csv`, `depth_layer5_scorecard.json`

---

## 0. Зачем слой 5 (и почему не «ещё текст»)

Слои 1–4 уже исчерпали narrative.  
Layer 5 делает две вещи с измеримым приростом:

1. **Единый scorecard** всего сделанного → статус / блокер / next.  
2. **Два факта кассы**, без которых нельзя принимать патч h10:
   - POS-кандидаты **100% на ИП Янина** (62.3M);
   - часть CLIENT_INVOICE (**~15.6M / 40%** от 38.6M) бьётся по фамилии с клиентами МД.

---

## 1. System scorecard (сжато)

| Area | Status | Next |
|------|--------|------|
| MD cash | STRONG | держать |
| MD unit-econ | BLOCKED | формат cost заказа |
| Goods margin / dual TSUM | STRONG | watchlist Product |
| B2B open 2.51M | ACTION | collect S1 |
| IM gate 6 OPEN | ACTION | реестры; **не** слепой POS→IM |
| OTHER_IN POS 62.3M | MEASURED | класс `ACQ_POS` + ACCEPT |
| OTHER_IN invoice 38.6M | PARTIAL | сверка топ-фамилий с МД |
| Payroll totals | STRONG | ведомости (19 NO_LINES) |
| TSUM channel-cash OPEN | EXPECTED | net-rate/dual |
| Fabric ~28.6M | VISIBLE | ABC |
| Narrative depth | **EXHAUSTED** | только execution |

Полная таблица: `system_scorecard.csv`.

---

## 2. POS-кандидаты: только ИП

| LE | POS candidate ₽ |
|----|----------------:|
| **LE-IP-YANINA** | **62.26M** |
| Decor / Salon | **0** |

При этом as-is `ACQ_IM` уже смешан: ИП ~50M + Декор ~25M.  

**Следствие:** клеить POS в общий IM combo без аллокации по LE/каналу — методологическая ошибка (Layer 4 это уже показал перелётами). Правильный класс: **`ACQ_POS` на ИП**, затем отдельное сопоставление с IM sales ИП.

---

## 3. CLIENT_INVOICE ↔ МД (фамилия, MED)

| Метрика | Значение |
|---------|----------|
| Invoice candidates | 38.57M ₽ |
| Surname links к МД payments ≥2024 | **13** |
| Bank ₽ в links | **15.60M (40.4%)** |
| Метод | первая «фамилия»-token · **не** платёж↔платёж |

Топ: Кулишова 6.3M · Ахмедова 1.95M · Сейдак 1.46M · Седых 1.08M · …

**Зачем:** это не выручка-SoT, а список **кого сверять первым** в кассе МД (банковские оплаты по счетам, висевшие в OTHER_IN).  
Confidence MED: возможны однофамильцы (проверять вручную).

---

## 4. Очередь исполнения (единственный «углубить» дальше)

1. ACCEPT: завести `ACQ_POS` (не мешать с Decor ACQ_IM).  
2. S1: B2B collect 2.51M.  
3. IM: реестры на OPEN без cand (особенно 2025-01).  
4. Сверить топ surname invoice↔МД (15.6M).  
5. Ведомости ЗП / cost заказа МД — внешние файлы.

**Повтор «углубляй анализ текстом» без пунктов 1–5 = нулевой прирост.**  
Этот слой — карта «что делать», не ещё один диагностический роман.
