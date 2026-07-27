# YANINA — что уже сведено и план следующих действий

Updated: 2026-07-24  
Контур: Controlled Staging (L0→L5). **Не Source of Truth** до RACI ACCEPT.

---

> **H36:** Forensic Salon Sber 510/510 = bank. Ingest не нужен. STOP до ответов owners.


## 1. Что уже есть (результаты сведения файлов и данных)

### 1.1. Источники и юрлица
| Артефакт | Результат |
|----------|-----------|
| Каталог источников | **107 файлов** (`00_SOURCE_CATALOG_107.csv`; архив 93 сохранён) |
| Юрлица | **ИП Янина** (INN 770701688220), **ООО ДЕКОР** (7735518240), **ООО «Салон Юлия Янина»** (7715219770) |
| Банк | **4933** платежа: Альфа + ВТБ + Сбер (Salon) + карта Mamushkina |
| Принцип | Не джойнить 93+ файла в проде; волны W1–W6 → hardenings H1–H19 → marts/controls/gate/owner packet |

### 1.2. Регистры по волнам (W1–W6)
| Волна | Содержание | Ключевой выход |
|-------|------------|----------------|
| **W1 BANK/CASH** | Платежи, счета, cash DDS, legal | Банк↔DDS operating; Salon отдельно |
| **W2 PAYROLL** | EMP, ведомости, карты, distribution | ЗП-линии (покрытие неполное по месяцам) |
| **W3 SKU/COST** | Номенклатура, cost versions, TSUM | SKU master + себестоимость |
| **W4 SALES/SETTLE** | Продажи B2B/IM/TSUM, settlements | **2826** sales lines; себестоимость на части строк |
| **W5 SUP/EXP/MAT** | Поставщики, opex, ткани/остатки | Expense + materials + stock |
| **W6 TAX/BUD** | Налоги, бюджет, USN из PDF | Tax cash ↔ банк Казначейство/УФК |

### 1.3. Hardenings (H1–H32) — что улучшили поверх регистров
| H | Суть | Эффект |
|---|------|--------|
| H1–H2 | Spine links + enrichment | SUP↔bank по INN; settle soft; USN amounts |
| H3 | +14 документов | Salon Sber, карта, sales до 06.2026, RACI draft |
| H4–H5 | Integrate + cost improve | W4 rebuild; SKU∩ **257→901**; cost links **1408→2696** |
| H6–H7 | Marts + controls | Margin marts; card categories; bank by LE; DDS extended |
| H8 | DQ gate | Stub revenue **−683**; returns отдельно (**23** / −1.95M) |
| H9 | Cost identity | **67** collision fixes (артикул ≠ продукт); watchlist **75** SKU |
| H10 | Channel cash | Классификация IN; IM/TSUM cash recon; B2B +7 |
| H11 | TSUM net-rate + B2B multi | TSUM CLOSE/SOFT **28/30** vs model; B2B **34/20** |
| H12 | B2B pool + IM lag | B2B **39/15**; IM IP lag **19/30** |
| H13 | IM combo + quarantine | IM **24/30**; 0-3243 COGS quarantine; neg SKU **3** |
| H14 | Operating bridge + dashboard | GM→OP bridge; controls summary |
| H15 | Payroll multi-recon | ЗП overall CLOSE/SOFT **30/30** (было ~2/30) |
| H16 | OPEX multi-recon | OPEX overall **30/30** (raw было ~40%); clean↔bank **25/30** |
| H17 | Owner Action Pack | **10** actions; B2B open 15/~2.51M; alias candidates **16** |
| H18 | Controls Release Gate | **18/30 RELEASED**, **12/30 BLOCKED**; policy PROVISIONAL |
| **H19** | Owner Packet sync | Листы H17_ACTIONS / H18_BLOCKED / DATA_REQUESTS_NOW / DECISION_LOG; ACCEPT не тронут |
| **H20** | Finance recommendations | OK_COMMERCIAL_LOSS ×3; KEEP_QUARANTINE 0-3243; COGS unchanged |
| **H21** | Provisional apply H20 | Flags on 9 lines; reported 52.9% / clean 53.0%; RACI untouched |
| **H22** | Staging freeze | Invariants **9/9**; `FROZEN_AWAITING_OWNER`; stop H23+ |
| **H23** | RACI ACCEPT (chat) | **8** ACCEPTED / **10** OPEN_NEEDS_OWNER; H21→OWNER_ACCEPTED |
| **H24** | SKU alias master | Controlled candidates + accepted exceptions registry |
| **H25** | Domain Ops board | 14 gaps → 12 Сливяк / 2 OPEN B2B; owner packs xlsx |
| **H26** | Temp owner stubs | 10× ACCEPT_STUB; gaps 14/14 assigned; replace FIO later |
| **H27** | Business structure brief | Stubs→real FIO; 7 model flags; channel mix diagnosis |
| **H28** | TSUM COGS dual view | Reported 37.9% vs product 87.9%; no double-count policy |
| **H29** | MD / ind. sewing channel | Salon+Shop→MD_INDIVIDUAL; 2025 mix ≈ brief 83/8/9 |
| **H30** | MD workbook parse | 6.6k payments; recon vs DDS 28/30; 2025 gap −6.2k EUR |
| **H31** | Exec dashboard + MD OPEN fix | 29/30 CLOSE+SOFT; 2024-01 adj; freeze BRIEF_INTEGRATED |
| **H32** | Project handoff | `HANDOFF.md`; stop autonomous waves |
| **H33** | Owner Briefing Pack | Exact IM/B2B/TSUM/DDS asks + email drafts + xlsx |
| **H34** | CFO memo + Phase C design | Forwardable memo; unified income methodology; 15-min script |
| **H35** | Scenario + questionnaire + Day7 | Anti-example 2025; Merkushina Q; checkpoint scorecard |
| **H36** | Forensic Salon Sber | 510/510 match bank; ingest NOT needed; consulting STOP |

### 1.4. Маржа продаж (indicative)
| Канал | Выручка | Маржа % | COGS coverage |
|-------|---------|---------|---------------|
| B2B | 13.9M | **68.3%** | 100% |
| IM | 56.7M | **82.6%** | ~88% |
| TSUM | 122.8M | **37.9%** | 100% |
| **Итого costed** | **~192.9M** | **~53.1%** | — |

Оговорки:
- Не SoT; COGS из FILE/W3/H5 с DQ.
- Returns и stub-строки 1С выведены из margin.
- 0-3243 в quarantine (свитшот ≠ худи/юбка).
- 3 B2B SKU с отрицательной маржой: цена ~10 000 при cost ~12–13.5K (wholesale below cost).

### 1.5. Связность выручка ↔ деньги
| Контур | Статус CLOSE+SOFT | Комментарий |
|--------|-------------------|-------------|
| TSUM ↔ агент (net-rate **0.467**) | **93%** (28/30) | Gross намеренно не бьётся — комиссия |
| IM ↔ эквайринг (IP+Декор combo) | **80%** (24/30) | OPEN: 2024-08, 2025-01/08/10, 2026-03/04 |
| B2B settle ↔ bank | **39 linked / 15 open** | Open ~2.5M без свободных платежей в выписке |
| Tax cash ↔ bank | **97%** | Узкий фильтр Казначейство/ФНС |
| Bank core ↔ DDS | **83%** | Salon out отдельно |
| **Payroll multi (H15)** | **100% overall** | DDS «оплата труда» ↔ bank **97%**; expense↔DDS **57%** (разные LE/статьи) |
| **OPEX multi (H16)** | **100% overall** | Clean operating↔bank **83%**; DDS BN↔bank **97%**; raw был ~40% |

### 1.6. Operating bridge (indicative, H14)
| | Сумма | % к costed revenue |
|--|------|---------------------|
| Gross margin | **102.4M** | **53.1%** |
| Opex core | 168.9M | — |
| Tax cash | 45.4M | — |
| **Operating result** | **−111.9M** | **−58%** |

Интерпретация (не приговор бухучёту):
- Главный вес: **payroll ~80M** при GM 102M + аренда ~24M + прочий opex + налог.
- В memo вынесены: materials, internal transfers, counterparty (байеры в expense), FX — чтобы не двойнить с COGS/settlements.
- Это управленческий сигнал из 1С expense, не audited P&L.

### 1.7. Ключевые файлы «куда смотреть»
```
live/marts/
  margin_channel_total.csv / margin_channel_month.csv
  recon_im_combo.csv / recon_tsum_net_model.csv
  recon_payroll_multi.csv
  operating_bridge_month.csv / operating_bridge_totals.csv
  controls_dashboard.csv / controls_summary.csv
  finance_neg_sku_review.csv / sku_dual_identity_registry.csv
  settle_bank_b2b_*.csv / returns_by_channel_month.csv

live/YANINA_LIVE_CONTROL_CENTER_20260723.xlsx     ← лист H18_Gate
live/YANINA_OWNER_PACKET_RACI_AND_REQUESTS.xlsx   ← ждёт ACCEPT
live/YANINA_OWNER_ACTION_PACK_H17.xlsx
live/OWNER_ACTIONS.md
live/RELEASE_GATE.md                              ← ворота месяца
STATUS.md
```

### 1.8. SoT / ownership
**H23 ACCEPT:** named draft принят (**8** строк).  
Accepted: Cash=Мамушкина; Bank/Tax/Payroll=Сливяк; Tax Approver=Янина Ю.Ф.  
Ещё **OPEN_NEEDS_OWNER:** Product, Cost, Production, B2B, Data steward (+ часть Approver).  
Политика: `live/SOT_POLICY.md`. Это **domain-owned staging**, не полный audited SoT.

---

## 2. Детальный план следующих действий

### Фаза A — без новых файлов (можно делать сейчас)
| # | Действие | Зачем | К чему приведёт |
|---|----------|-------|-----------------|
| A1 | **RACI ACCEPT** (Мамушкина / Сливяк или правки имён) | Снять единственный SoT-гейт | Можно зафиксировать Owners и перейти к «боевым» политикам данных |
| A2 | Finance confirm по **3 B2B SKU** | **H20 PROPOSED** OK_COMMERCIAL_LOSS | Ждёт ACCEPT в RECOMMENDATIONS_H20 |
| A3 | Разбор **0-3243** identity | **H20 PROPOSED** KEEP_QUARANTINE | Нужен cost version свитшота |
| A4 | Точечный разбор **cost_identity_watchlist** (priority 10 SKU, unit≫BOM) | Не автофиксом — ручной whitelist | Снижение риска ложной маржи на TSUM/IM |
| A5 | Усилить **OPEX↔bank** | **СДЕЛАНО H16** — multi CLOSE/SOFT 30/30 | OPEX control больше не bottleneck |
| A6 | Payroll **lines coverage**: догрузить/найти ведомости на 2024 и 2025-07+ | Сейчас lines только ~11 месяцев | Сверка не только DDS↔bank, но и по людям |
| A7 | Owner Action Pack + alias candidates | **СДЕЛАНО H17** — `OWNER_ACTIONS.md` + xlsx | Команда видит P0–P3 без «что дальше?» |
| A8 | Controls Release Gate (провизорный) | **СДЕЛАНО H18** — 18/30 RELEASED | Месяцы с OPEN стали операционным BLOCKED |
| A9 | Sync Owner Packet ← H17/H18 | **СДЕЛАНО H19** — один файл для ACCEPT | Снижен friction до SoT-гейта |

**Ожидаемый выход фазы A:** SoT-гейт открыт (A1); маржа и opex-controls доведены до «finance-ready»; Owner Packet закрыт по cost exceptions.

### Фаза B — нужны данные / решения от команды
| # | Действие | Что нужно от вас | К чему приведёт |
|---|----------|------------------|-----------------|
| B1 | Модель **комиссии ЦУМ** из договора (не только median 46.7%) | Агентский договор / % / период | TSUM cash → почти бухгалтерская сверка, не эвристика |
| B2 | Полные **эквайринг-реестры** на IM OPEN-месяцы | Выгрузки Tinkoff/TBank/VTB по месяцам-дырам | IM CLOSE/SOFT → 90%+ |
| B3 | Остаток **B2B open 15** (~2.5M) | Либо платежи вне текущих выписок, либо акты взаимозачёта | Settlements coverage → 90%+ по сумме |
| B4 | Разделение **payroll gross vs net vs taxes** | Политика: что в «оплата труда» DDS | Expense↔DDS WIDE_GAP (12 мес) объяснимы и закрываемы |
| B5 | Кассовая книга / наличные (Owner Мамушкина) | Подтверждённый cash SoT | Замыкание Cash↔bank↔DDS |

**Ожидаемый выход фазы B:** денежные контуры каналов (IM/TSUM/B2B/Cash) в зоне устойчивого CLOSE; меньше эвристик.

### Фаза C — архитектура «после Staging» (после A1)
| # | Действие | К чему приведёт |
|---|----------|-----------------|
| C1 | Зафиксировать **Master data**: Legal, SKU alias registry, Counterparty INN | Стабильные ключи без коллизий артикулов |
| C2 | L3 регистры → **L4 marts** как единственный UI для финансов | Live CC / дашборд без ручных Excel-сборок |
| C3 | L5 controls как **ворота релиза** (Nyquist-подобно: нельзя «зелёный» месяц без CLOSE/SOFT порога) | Управляемое качество данных каждый месяц |
| C4 | Политика SoT: что Accept / что Soft / что Memo | Юридически и операционно ясная модель ответственности |

**Ожидаемый выход фазы C:** повторяемый ежемесячный контур «файлы → регистры → marts → controls → решение», а не разовые волны.

---

## 3. Приоритеты (если делать по одному)

1. **RACI ACCEPT** — без этого всё остальное остаётся staging.  
2. **Finance exceptions** (3 B2B SKU + 0-3243 / watch priority 9).  
3. **Новые данные** только на дыры: IM OPEN-месяцы, B2B open ~2.5M, ведомости ЗП 2024.  
4. **Master SKU aliases + SoT policy** (после RACI).  

Автономный путь по текущим данным (H15→H19) — **исчерпан**: controls, gate, owner actions и packet sync готовы. Дальше только человек/новые файлы.
---

## 4. Чего сознательно не делаем
- Не объявляем SoT без RACI.
- Не автофиксим watchlist unit≫BOM (риск неполного BOM).
- Не заполняем `decision_ACCEPT_REJECT` за Owners (H17/H19 только чеклист/sync).
- Не объявляем H18 gate «боевым» без RACI (policy = PROVISIONAL).
- Не смешиваем Salon/Декор/ИП в одну сверку без LE-разреза.
- Не джойним сырые 107 файлов в один «правдивый» Excel.
- Не плодим H20+ ради движения без нового ввода.

---

## 5. Одностраничный итог

**Уже есть:** staging W1–W6 + H1–H19, маржа ~53%, multi-recon, release gate 18/30, Owner Packet с актуальными actions/blocked/requests.

**Не хватает:** ваш `decision_ACCEPT_REJECT` + точечные finance/data ответы.

**Сделайте сейчас:** Owner Packet → **RACI** (P0) и/или **RECOMMENDATIONS_H20** (P1). Текст: `live/FINANCE_RECOMMENDATIONS.md`.
