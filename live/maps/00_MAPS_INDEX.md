# Карты YANINA / YNN — индекс

Updated: 2026-07-27  
Назначение: полный комплект карт поверх уже сделанной аналитики + сопоставление + единый алгоритм + проблемы ±.

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
| EXEC | Пакет исполнения | `execution_pack/` | Решения owners · CSV · стоп narrative |
| JSON | Снимки слоёв | `deep_synthesis_snapshot.json`, `depth_layer2_*.json` … `depth_layer5_*.json` | Воспроизводимость |
| CSV | Машиночитаемые срезы | `*.csv` в этой папке | Каталог, crosswalk, scorecard, links |

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
