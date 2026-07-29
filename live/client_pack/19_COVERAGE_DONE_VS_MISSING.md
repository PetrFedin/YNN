# 19 — Полный перечень: что сделано и чего нет

Updated: 2026-07-29 (H52/H53 gap-fill отмечен)  
Статус: **инвентарь покрытия** · не новый «обзорный слой» · не SoT  
Собрано с проверкой каталога 107, marts, maps, client_pack, freeze/SOT, scorecard  
Агенты: inventory + TOR gap matrix  
CSV: `../maps/coverage_done_vs_missing.csv`  
Дополнено: H52 карты 16–19 · H53 WO/unlock/queue (`40_PRIORITY_OPS_H53.md`)

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
- Gate **18/30**; controls payroll/opex 100%, tax cash **READY_FOR_SIGN** (H76 Salon UFK)
- H73–H78 data/P0 packaging closed — see `65_P0_GATE_SYNC_H78.md`  
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
| IM acquiring | **PARTIAL** | control 80%; H52 map; H53 4 WO + template | 6 OPEN; заполненные реестры | D-IM-REG-01 + файлы |
| Ops close calendar | **DONE (map)** | H52 `ops_close_calendar` | ☐ done_flag owners | исполнение Wave A |
| Unlock / intake | **DONE (ops)** | H53 dependency + file_intake | подписи/файлы | U09→U01–U05 |
| MD payment queue | **PARTIAL+** | H53 queue+rules поверх surname 40% | line-by-line match | D-MD-INV-01 |
| B2B settle | **PARTIAL+** | open 2.51M; **H54 Wave B call pack топ-3** | Collect после E01 | D-B2B-01 |
| Alias Accept | **PARTIAL+** | H44 sheet; **H54 top-5 в Wave B** | ACCEPT/REJECT Коновалова | D-ALIAS-01 |
| BANK↔DDS | **PARTIAL+** | H40 matrix; **H54 3 WO** | DDS June + policy | D-BANK-DDS |
| Gate path | **MAPPED** | **H54 ladder 18→30** | исполнение E02/E07/E08/E10 | owners |
| OTHER_IN / POS | **PARTIAL** | 62.3M измерено | ACCEPT ACQ_POS | D-ACQ-POS-01 |
| Invoice↔МД | **PARTIAL** | 40% surname MED | Платёж↔платёж | D-MD-INV-01 |
| Payroll totals | **PARTIAL** | multi CLOSE | 19 NO_LINES; split | D-PAY-LINES-01 |
| Tax cash | **PARTIAL→лучше** | ~97% bank + **H37 HIGH extract 14 PDF** | RSV LOW; ЕНС без сумм | Бухгалтер verify НДС 030/040 |
| Ткани WC | **PARTIAL** | ~28.6M видно | ABC-aging | Этап 2 I11 |
| **Коллекции/showroom** | **PARTIAL→DONE ingest** | **H62:** 1758 lines / ~4.04M€; COL43–47 strong→MD 65–80% | capsule/cruise alias; Accept links | D-COL-01 |
| **Бюджет↔факт** | **PARTIAL→DONE ingest** | **H63:** 497 plan/fact; top variances; opex bridge | unit EUR_LIKE vs opex RUB; June fact income empty | D-BUD-01 |
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

- [x] H52 gap maps (calendar / IM acq / MD cost to-be / RACI)  
- [x] H53 priority ops (overbank WO / MD payment queue / unlock)  
- [x] H54 Wave B ready pack  
- [x] H55 exec enablement (sign 15мин / pings / SLA / Stage2 entry / Wave C)  
- [x] H56 Command Center (`NOW.md` / weekly ops / stop-doing)  

### Не сделано (нужны owners / файлы / этапы 2+)
- [ ] **Подпись H51 / sign session 15 мин** *(пакет `sign_session_pack/` готов)*  
- [ ] ACCEPT soft-slice IM / класса `ACQ_POS` (политика)  
- [ ] Collect B2B 2.51M  *(Wave B call pack готов)*  
- [ ] Эквайринг-реестры на IM OPEN / OVERBANK *(WO+шаблон готовы)*  
- [ ] Alias Accept топ-5/20 SKU  *(Wave B sheet готов)*  
- [ ] Закрыть OPEN RACI ФИО  *(sign checkboxes готовы)*  
- [ ] Ведомости ЗП (NO_LINES) + quarantine 01–02.2026  
- [ ] Формат cost/WIP МД + пилот contribution *(26 WO готов)*  
- [ ] Договорной % ЦУМ / Mercury cash  
- [ ] ABC тканей; учёт фурнитуры  
- [ ] Unified income / audited P&L  
- [ ] KPI-система и дашборды «в бою»  
- [ ] Утверждённые SOP + обучение  
- [ ] Stage 2–4 внедрение и сопровождение  *(entry criteria H55)*

~~- [ ] Полный extract tax PDF~~ → **частично закрыто H37** (HIGH 14; RSV LOW; списки без сумм)
---

## 5. Очередь разблокировки (единственный полезный next)

1. **Sign session 15 мин** — `sign_session_pack/00_SIGN_SESSION_15MIN.md`  
2. **Разослать пинги** — `owner_ping_messages.csv`  
3. **D-ACQ-POS / soft-slice** — ACCEPT долей  
4. **D-B2B-01** — collect Wave B  
5. **D-IM-REG-01** — файлы overbank  
6. **DDS June + TSUM** — Wave C  
7. **D-MD-INV / PAY / COST / TSUM-RATE** — по SLA  

Без подписей/файлов новый «углублённый анализ» = пересказ этого перечня.  
Пакеты исполнения: `execution_wave_a|b|c/` + `sign_session_pack/`.

---

## 6. Связанные пути

- Scorecard: `live/maps/system_scorecard.csv`  
- Decisions: `live/maps/execution_pack/OWNER_DECISIONS_PENDING.csv`  
- Схема: `18_MASTER_SCHEME_CLIENT.md`  
- Freeze: `live/STAGING_FREEZE.md` · SoT: `live/SOT_POLICY.md`  
- Каталог: `live/registers/00_SOURCE_CATALOG_107.csv`
