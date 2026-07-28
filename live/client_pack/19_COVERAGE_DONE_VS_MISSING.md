# 19 — Полный перечень: что сделано и чего нет

Updated: 2026-07-28  
Статус: **инвентарь покрытия** · не новый «обзорный слой» · не SoT  
Собрано с проверкой каталога 107, marts, maps, client_pack, freeze/SOT, scorecard  
Агенты: inventory + TOR gap matrix  
CSV: `../maps/coverage_done_vs_missing.csv`

---

## 0. Вердикт одной строкой

**Этап 1 (диагностика) — выполнен.**  
**Операционное закрытие дыр и Stage 2+ внедрение — не выполнены** (ждут ACCEPT/файлов owners).  
Текстовое «углубление без данных» — исчерпано; этот документ = карта покрытия, не Layer 6.

---

## 1. Что у нас ЕСТЬ (активы)

### 1.1. Источники
| Метрика | Значение |
|---------|----------|
| Файлов в каталоге | **107** (Active) |
| Домены (топ) | Налоги 25 · ЗП 25 · Финансы 15 · Коллекции 12 |
| Годы | 2024–2026 основной periметр |
| Ext | xlsx 68 · pdf 29 · docx/xls/doc |
| Risk | Низкий 80 · Средний 24 · Критич./Высок. 3 |
| Quarantine | 5 файлов (ЗП 2026, cost, B2B 2026) |
| Точный дубль | 1 пара 6-НДФЛ |

### 1.2. Конвейер данных
| Слой | Статус |
|------|--------|
| L0 сырьё | есть (вне git) |
| L1 каталог | 107 |
| L3 регистры W1–W6 | done |
| L4 marts | **~80 CSV** |
| L5 controls / pack | gate, RACI, freeze, client_pack |

Marts (семейства): margin 10 · md 10 · recon 9 · settle 5 · bank 4 · + gate/finance/sku…

### 1.3. Аналитические артефакты
| Пакет | Файлов | Содержание |
|-------|--------|------------|
| `client_pack/` | 20 MD + snapshot | Stage 1 ТЗ 01–05 + 06–18 |
| `maps/` | 17 MD + CSV/JSON | процессы, layers 2–5, scorecard |
| `execution_pack/` | решения + CSV | 7 PENDING decisions |
| Сценарии | S1–S4 | ₽-ориентиры + go/no-go |
| Freeze H22/H31 | invariants PASS | staging frozen; не audited SoT |

### 1.4. Ключевые факты уже посчитаны
- МД 2025 DDS ≈ **232.6M** @100; сверка 29/30  
- Банк **4933**; Salon Sber **510/510**  
- Goods margin / dual TSUM **37.9 / 87.9**; commission proxy ~61M/30м  
- B2B open **2.51M** / 15  
- Gate **18/30**; controls payroll/opex 100%, tax cash ~97%  
- POS-like в OTHER_IN **62.3M** (только ИП); invoice↔МД surname ~**15.6M**  
- ФОТ classified **+18.2M YoY (+93%)**  
- Ткани end **~28.6M** (money-trusted)

---

## 2. Матрица DONE / PARTIAL / NOT / BLOCKED

| Область | Статус | Что есть | Чего нет | Как разблокировать |
|---------|--------|----------|----------|-------------------|
| Два контура финансов | **DONE** | Диагноз, политики draft, скелет модели | Единый P&L как KPI | Не смешивать; ACCEPT P-A |
| Товарная маржа | **DONE** | IM/B2B/TSUM по годам | Aliases ACCEPT | Product review |
| Dual TSUM | **DONE** | Dual view + proxy комиссии | Договорной % | Меркушина D-TSUM-RATE-01 |
| Сценарии S1–S4 | **DONE** | Диапазоны + условия | Гарантия ₽ | Исполнение, не новый отчёт |
| RACI | **DONE** | 18 ACCEPT, owners | Ритм ЦУМ SME | Регулярный контур |
| Release gate | **DONE** | 18/30, fail map | ≤8–9 BLOCKED | Закрыть IM/BANK fails |
| Карты процессов/данных | **DONE** | P01–P12, L0–L5, crosswalk | BPMN to-be внедрение | Этап 3 |
| Master scheme заказчику | **DONE** | `18_MASTER_SCHEME` + canvas | — | — |
| Bank↔DDS | **PARTIAL** | 83.3%; Salon OK | 5 WIDE_GAP; DDS Jun lag | Разбор + DDS файл |
| IM acquiring | **PARTIAL** | control 80%; impact POS | 6 OPEN; реестры | D-IM-REG-01 |
| B2B settle | **PARTIAL** | open list 2.51M | Collect | D-B2B-01 |
| OTHER_IN / POS | **PARTIAL** | 62.3M измерено | ACCEPT ACQ_POS | D-ACQ-POS-01 |
| Invoice↔МД | **PARTIAL** | 40% surname MED | Платёж↔платёж | D-MD-INV-01 |
| Payroll totals | **PARTIAL** | multi CLOSE | 19 NO_LINES; split | D-PAY-LINES-01 |
| Tax cash | **PARTIAL→лучше** | ~97% bank + **H37 HIGH extract 14 PDF** | RSV LOW; ЕНС без сумм | Бухгалтер verify НДС 030/040 |
| Ткани WC | **PARTIAL** | ~28.6M видно | ABC-aging | Этап 2 I11 |
| Decor wind-down | **PARTIAL** | статус ясен | tags periметра | I06 ACCEPT |
| Дашборд/KPI/SOP | **PARTIAL** | drafts в pack | Внедрение в бою | Этап 3 |
| **МД unit-econ** | **BLOCKED** | payments/DDS | cost/WIP 2024–25 =0% | D-MD-COST-01 + пилот |
| **Фурнитура** | **BLOCKED** | только намёк в DDS | учёт 1С | мини-регистр |
| **Единый audited P&L** | **NOT_DONE** | запрещён методологически на Stage 1 | Phase C | G1–G3 + MD contrib |
| **Stage 2+ внедрение** | **NOT_DONE** | план в 05 | proxy МД, ABC, live KPI/BI | после P0 S1 |

Полная таблица CSV: `live/maps/coverage_done_vs_missing.csv`.

---

## 3. Покрытие блоков ТЗ Этапа 1

| Блок ТЗ | Покрытие | Комментарий |
|---------|----------|-------------|
| 1. Финансы | Высокое / оговорка | 2 контура да; company P&L нет |
| 2. Запасы/НК | Среднее | ткани да; фурнитура/МД WIP нет |
| 3. Ассортимент | Среднее+ | товар да; МД categories нет |
| 4. Процессы | Среднее | диагноз да; исполнение кассы PARTIAL |
| 5. Управление | Высокое | RACI/gate; KPI-система draft |
| 6. Налоги/орг | Среднее+ | cash/структура; PDF amounts нет |

**Итог ТЗ Этапа 1:** достаточен для диагностики и выбора направления.  
**Недостаточен** для audited финвердикта и внедрения.

---

## 4. Что СДЕЛАНО vs что НЕ СДЕЛАНО (чеклист)

### Сделано
- [x] Каталог 107 + волны W1–W6 + ~80 marts  
- [x] Сверки MD/bank/payroll/opex/tax cash  
- [x] Dual TSUM + freeze invariants  
- [x] Gate + domain gap board  
- [x] Client pack Stage 1 (01–05 + приложения)  
- [x] Карты 00–15 + layers 2–5 + scorecard  
- [x] Сценарии S1–S4  
- [x] Execution pack (7 решений)  
- [x] Master scheme для заказчика  
- [x] Измерение POS/invoice в OTHER_IN  

- [x] H37 deep scan 107 + tax HIGH extract + dojim owner packs (`24_…`)  
- [x] H38 continue: IM×POS, bank/DDS gaps, FOT drivers, fabric ABC indicative (`25_…`)  

### Не сделано (нужны owners / файлы / этапы 2+)
- [ ] ACCEPT класса `ACQ_POS`  
- [ ] Collect B2B 2.51M  *(пакет `dojim_B2B_collect_pack.csv` готов)*  
- [ ] Эквайринг-реестры на 6 IM OPEN  *(пакет `dojim_IM_open_pack.csv` готов)*  
- [ ] Alias Accept 20 SKU  *(пакет `dojim_ALIAS_review_pack.csv` готов)*  
- [ ] Закрыть 10 OPEN RACI ФИО  *(пакет `dojim_RACI_open_pack.csv` готов)*  
- [ ] Ведомости ЗП (NO_LINES) + quarantine 01–02.2026  
- [ ] Формат cost/WIP МД + пилот contribution  
- [ ] Договорной % ЦУМ  
- [ ] ABC тканей; учёт фурнитуры  
- [ ] Unified income / audited P&L  
- [ ] KPI-система и дашборды «в бою»  
- [ ] Утверждённые SOP + обучение  
- [ ] Stage 2–4 внедрение и сопровождение  

~~- [ ] Полный extract tax PDF~~ → **частично закрыто H37** (HIGH 14; RSV LOW; списки без сумм)
---

## 5. Очередь разблокировки (единственный полезный next)

1. **D-ACQ-POS-01** — ACCEPT  
2. **D-B2B-01** — collect  
3. **D-IM-REG-01** — файлы  
4. **D-MD-INV-01** — сверка  
5. **D-PAY-LINES-01 / D-MD-COST-01 / D-TSUM-RATE-01** — данные для S2/S3  

Без этого новый «углублённый анализ» = пересказ этого перечня.

---

## 6. Связанные пути

- Scorecard: `live/maps/system_scorecard.csv`  
- Decisions: `live/maps/execution_pack/OWNER_DECISIONS_PENDING.csv`  
- Схема: `18_MASTER_SCHEME_CLIENT.md`  
- Freeze: `live/STAGING_FREEZE.md` · SoT: `live/SOT_POLICY.md`  
- Каталог: `live/registers/00_SOURCE_CATALOG_107.csv`
