# 25 — Продолжение дожима (H38): что ещё закрыли кодом

Updated: 2026-07-28  
После H37 (scan 107).  
Статус: indicative · **не SoT** · **без auto-ACCEPT**

---

## 0. Вердикт

Сделан следующий технический слой по дырам, которые ещё можно закрыть **без owners**:

| Тема | Результат |
|------|-----------|
| IM OPEN × POS | 6 месяцев разобраны; **1** (2026-04) вероятно закрывается при ACCEPT ACQ_POS |
| Bank↔DDS | 4 WIDE_GAP + 1 BANK_ONLY (июнь 2026) ранжированы |
| ФОТ YoY | **+18.2M expense = +8.1M касса/DDS + +10.1M tax/прочее** |
| Ткани ABC | Indicative A/B/C на ~29.8M (не aging-SoT) |
| Коллекции | 12 файлов / 27 листов; join к SKU пока **слаб** (overlap 3) |
| МД invoice | 13 surname-links → пакет ручной сверки |
| ЦУМ net OPEN | 3 месяца |

Что **по-прежнему только owners:** collect B2B, Accept alias/RACI/ACQ_POS, quarantine ЗП, unit-econ МД.

---

## 1. IM OPEN — гипотеза POS (не применена)

CSV: `im_open_vs_pos_hypothesis.csv`

| Месяц | Sales | Bank combo | Gap | POS cand. | Гипотеза |
|-------|------:|-----------:|----:|----------:|----------|
| 2024-08 | 0.98M | 1.70M | **+0.72M** (банк>) | 0.46M | UNLIKELY (перебор банка) |
| 2025-01 | 0.78M | 1.20M | **+0.42M** | 0 | UNLIKELY |
| 2025-08 | 3.59M | 2.66M | **−0.94M** (банк<) | 0.37M | PARTIAL (~39% дыры) |
| 2025-10 | 0.68M | 0.92M | **+0.24M** | 3.97M | UNLIKELY (перебор; POS другой контур) |
| 2026-03 | 0.41M | 0.67M | **+0.26M** | 4.55M | UNLIKELY |
| **2026-04** | 3.40M | 2.04M | **−1.36M** | 4.12M | **LIKELY_IF_ACCEPTED** |

**Вывод для решения D-ACQ-POS-01:** Accept POS чинит влоб не все 6 OPEN, а в первую очередь **недобор банка** (2026-04, частично 2025-08). Месяцы с «банком больше продаж» требуют реестров/лагов, не слепого POS.

---

## 2. Bank ↔ DDS — ранжированные разрывы

CSV: `bank_dds_delta_ranked.csv`  
Статусы 30 мес.: CLOSE 16 · SOFT 9 · **WIDE 4** · BANK_ONLY 1

| Месяц | Δ core vs DDS | Status | Priority |
|-------|--------------:|--------|----------|
| 2026-06 | **+5.55M** | BANK_ONLY | HIGH (лаг ДДС июня) |
| 2024-12 | +1.85M | WIDE_GAP | HIGH |
| 2026-02 | −1.50M | WIDE_GAP | HIGH |
| 2024-06 | +0.96M | WIDE_GAP | MED |
| 2024-05 | +0.98M | SOFT | MED |

**Действие:** не «новый слой», а разбор 3 HIGH месяцев в операционке (Сливяк) + догрузка ДДС июня.

---

## 3. ФОТ — драйверы +93% expense

CSV: `payroll_yoy_drivers.csv`

| Метрика | 2024 | 2025 | YoY |
|---------|-----:|-----:|----:|
| Expense payroll | 19.6M | **37.8M** | **+18.2M (+93%)** |
| DDS BN (касса-близко) | 19.6M | 27.6M | **+8.1M (+41%)** |
| Tax component в expense | 0 | **10.1M** | **+10.1M** |
| Bank ZP-like | 19.8M | 28.1M | +8.3M |

**Читать так:** почти **половина** «+93%» — это **налоговая/начисленная нагрузка в статье расходов**, не удвоение выдачи на руки. Кассовый рост ~+40% — тоже сильный, но другая управленческая речь.

`payroll_lines_by_group_year.csv` — только **структура групп** (SALARY/EMBROIDERY/MASTERS/DESIGNERS). Суммы lines **не** использовать как ФОТ (не сходятся с recon; риск double-count).

---

## 4. Ткани — indicative ABC (не SoT)

CSV: `fabric_abc_indicative.csv` · `fabric_abc_summary.csv`  
База: snapshot 31.05.2026 без «Итого» · **29.84M ₽** · 1338 позиций

| Class | SKU | ₽ | Share |
|-------|----:|--:|------:|
| **A** (до 80% cum) | 498 | 23.9M | 80% |
| **B** | 408 | 4.5M | 15% |
| **C** | 432 | 1.5M | 5% |

Для экспертного прохода неликвида (вечерние сетки/перья в топе) — да.  
Для «aging SoT / списываем C» — **нет** (единицы leaf historically ambiguous).

---

## 5. Коллекции — inventory + join probe

CSV: `collection_sheets_inventory.csv` · `collection_to_sku_join_probe.csv`

| Факт | Значение |
|------|----------|
| Файлов | 12 |
| Листов | 27 |
| Article-токенов (sample) | 332 |
| Overlap с known sales/cost SKU | **3** (`0-2548`, `0-2604`, `0-3364`) |
| Join status | **NO reliable collection P&L** |

Подтверждает G5: коллекции — слой 2, не дыра Stage 1.

---

## 6. Прочие пакеты

| CSV | n | Зачем |
|-----|--:|-------|
| `dojim_MD_INVOICE_surname_pack.csv` | 13 | Ручной payment-level match (~15.6M bank invoice) |
| `tsum_net_open_months.csv` | 3 | Проверка агентского timing ЦУМ |

---

## 7. Что остаётся только за людьми

1. Назначить OPEN RACI (особенно B2B / Product / Cost / Data)  
2. Collect B2B 2.51M  
3. Решение **ACQ_POS** (с приоритетом 2026-04 / 2025-08) + реестры на «банк>sales» месяцы  
4. Alias Accept 20 SKU  
5. Починить quarantine ЗП 01–02.2026  
6. Пилот cost_amount salon 2026 → unit-econ вперёд  

---

## 8. Артефакты

`live/registers/h38_continue_dojim/` · `live/evidence/h38_continue_dojim_20260728/` · копии в `client_pack/` / `maps/`

Оценка дожима H38: **9/10** на аналитическую ясность; **3/10** на закрытие кассовых дыр без owners (ожидаемо).
