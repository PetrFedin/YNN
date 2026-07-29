# Карты YANINA / YNN — индекс

Updated: 2026-07-29  
Назначение: полный комплект карт поверх уже сделанной аналитики + сопоставление + единый алгоритм + проблемы ± + gap-fill H52.

| # | Карта | Файл | Зачем |
|---|-------|------|-------|
| 00 | Индекс | этот файл | Навигация |
| 01 | Карта процессов | `01_PROCESS_MAP.md` | Как работает бизнес end-to-end |
| 02 | Карта документов и данных в них | `02_DOCUMENT_DATA_MAP.md` | 107 источников → что внутри |
| 03 | Карта данных (L0–L5) | `03_DATA_LAYER_MAP.md` | Архитектура staging |
| 04 | Карта сущностей и каналов | `04_ENTITY_CHANNEL_MAP.md` | LE / каналы / owners |
| 05 | Карта контролей качества | `05_CONTROL_MAP.md` | Gate / recon / DQ |
| 06 | Карта ценности (value stream) | `06_VALUE_STREAM_MAP.md` | Где создаётся/теряется ценность |
| 07 | Матрица сопоставлений | `07_CROSSWALK_MATRIX.md` | Процесс↔док↔регистр↔mart↔KPI↔проблема |
| 08 | Единый алгоритм | `08_UNIFIED_ALGORITHM.md` | Как всё связано и в каком порядке читать/считать |
| 09 | Проблемы ± (углублённый разбор) | `09_PROBLEMS_PLUS_MINUS.md` | Плюсы/минусы по каждому контуру |
| 10 | Углублённый синтез | `10_DEEP_SYNTHESIS.md` | Причинность + цифры по всем контурам |
| 11 | Помесячное качество | `11_MONTHLY_QUALITY_MAP.md` | 18/12 gate, fails, gap board |
| 12 | Layer 2: МД/opex/SKU | `12_LAYER2_MD_OPEX_SKU.md` | Forensic cost МД + ФОТ +93% + SKU ABC |
| 13 | Layer 3: касса/классы | `13_LAYER3_CASH_CLASSIFICATION.md` | OTHER_IN 62M POS-like, payroll lines, TSUM≠IM |
| 14 | Layer 4: impact reclass | `14_LAYER4_RECLASS_IMPACT.md` | Кандидаты + эффект на IM OPEN (1/6) |
| 15 | Layer 5: scorecard + links | `15_LAYER5_SCORECARD_LINKS.md` | Статус системы; POS=IP; invoice↔МД 40% |
| **16** | **Ops close calendar** | `16_OPS_CLOSE_CALENDAR.md` | **H52:** даты E01–E12 до 05.09 |
| **17** | **IM acquiring map** | `17_IM_ACQUIRING_MAP.md` | **H52:** POS/TBank/Dekor × месяцы |
| **18** | **MD cost to-be** | `18_MD_COST_PROCESS_TOBE.md` | **H52:** процесс unit-econ 2026+ |
| **19** | **RACI formal vs candidate** | `19_RACI_FORMAL_VS_CANDIDATE.md` | **H52:** H23↔H27↔H51 |
| **20** | **Unlock dependency** | `20_UNLOCK_DEPENDENCY.md` | **H53:** что разблокирует gate/cash |
| **21** | **IM overbank WO** | `21_IM_OVERBANK_WORK_ORDERS.md` | **H53:** 4 реестра + шаблон |
| **22** | **MD invoice payment queue** | `22_MD_INVOICE_PAYMENT_QUEUE.md` | **H53:** payment-level поверх surname |
| **23** | **Wave B ready** | `23_WAVE_B_READY.md` | **H54:** B2B/alias/cost/BANK/TSUM pack |
| **24** | **Gate score ladder** | `24_GATE_SCORE_LADDER.md` | **H54:** 18→20→24→28→30 |
| **25** | **Person action cards** | `25_PERSON_ACTION_CARDS.md` | **H54:** что делать сегодня по ФИО |
| **26** | **Sign + pings** | `26_SIGN_SESSION_AND_PINGS.md` | **H55:** 15 мин + тексты owners |
| **27** | **Stage 2 entry** | `27_STAGE2_ENTRY_CRITERIA.md` | **H55:** must / not-must |
| **28** | **Wave C BANK/TSUM** | `28_WAVE_C_BANK_TSUM.md` | **H55:** path 24→30 |
| **NOW** | **Command Center** | `../../NOW.md` | **H56:** что делать прямо сейчас |
| **29** | **Overbank prefill** | `29_OVERBANK_REGISTER_PREFILL.md` | **H57:** 48 bank lines ready to fill |
| **30** | **BANK/B2B prefill** | `30_BANK_B2B_PREFILL.md` | **H58:** 89 card lines + B2B confirm + dekor fix |
| **31** | **Alias/TSUM/ZP** | `31_ALIAS_TSUM_ZP.md` | **H59:** evidence + Mercury missing + P0 ZP |
| **32** | **Gate path + TAX** | `32_GATE_PATH_TAX.md` | **H60:** 18→30 + TAX 36k prefill + board sync |
| **33** | **Collections margin** | `33_COLLECTIONS_MARGIN.md` | **H62:** 12 showroom files → 1.7k lines / 4.0M€ |
| EXEC | Пакет исполнения | `wave_a` + `wave_b` + `wave_c` + `sign_session_pack` | Решения owners |
| JSON | Снимки слоёв | `deep_synthesis_snapshot.json`, `depth_layer2_*.json` … | Воспроизводимость |
| CSV | Машиночитаемые срезы | `*.csv` в этой папке | + H52 gap maps |

## Как пользоваться (30 секунд)

1. Вопрос про бизнес → `01` + `04`  
2. «Откуда цифра?» → `02` + `03` + lineage в client_pack  
3. «Можно ли верить месяцу?» → `05` + `11`  
4. «Где теряем деньги?» → `06` + `09`  
5. «Как всё связать?» → `07` + **`08`**  
6. «Что уже доказано / что делать?» → **`15`** + `system_scorecard.csv`  
7. «Ещё углубляй текстом?» → **EXHAUSTED** → `execution_pack/` (решения), не Layer 6 обзор  

Канон ID процессов: только P01–P12 из `01_PROCESS_MAP.md`.

Связь с Этапом 1: `live/client_pack/` (отчёт, резервы, сценарии).  
Архитектура-источник: `live/architecture/`.  
Сценарии ₽: `live/OPTIMIZATION_SCENARIOS.md`.
