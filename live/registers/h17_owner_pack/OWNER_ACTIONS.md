# Owner Action Pack (H17)

Updated: 2026-07-24 17:39

Не SoT. Чеклист решений и запросов данных.

## [P0] A-RACI-01 — ACCEPT или REJECT черновика RACI
- Owner hint: **Юлия / Сливяк / Мамушкина**
- Category: RACI
- В Owner Packet: Мамушкина Елена = Cash Owner; Сливяк Галина = Bank/Tax/Payroll Owner. Заполнить decision_ACCEPT_REJECT. Без этого регистры остаются staging, не SoT.
- Blocks: SoT / эталонные политики данных
- Evidence: `live/YANINA_OWNER_PACKET_RACI_AND_REQUESTS.xlsx`
- Status: `TODO`

## [P1] A-FIN-0-2497 — Подтвердить B2B убыток 0-2497
- Owner hint: **Финансы / коммерция**
- Category: FINANCE_EXCEPTION
- Цена/ед 10000.01 ₽ vs cost/ед 13579.34 ₽ (gap -3579.33 ₽). Выручка 70000.04, маржа -25055.34. Варианты: OK commercial loss / ошибка cost / прайс.
- Blocks: Чистота margin SoT по B2B
- Evidence: `live/marts/finance_b2b_loss_evidence.csv`
- Status: `TODO`

## [P1] A-FIN-0-2496 — Подтвердить B2B убыток 0-2496
- Owner hint: **Финансы / коммерция**
- Category: FINANCE_EXCEPTION
- Цена/ед 10000.01 ₽ vs cost/ед 12359.27 ₽ (gap -2359.26 ₽). Выручка 60000.05, маржа -14155.57. Варианты: OK commercial loss / ошибка cost / прайс.
- Blocks: Чистота margin SoT по B2B
- Evidence: `live/marts/finance_b2b_loss_evidence.csv`
- Status: `TODO`

## [P1] A-FIN-0-2493A — Подтвердить B2B убыток 0-2493A
- Owner hint: **Финансы / коммерция**
- Category: FINANCE_EXCEPTION
- Цена/ед 10000.0 ₽ vs cost/ед 11961.52 ₽ (gap -1961.52 ₽). Выручка 30000.0, маржа -5884.56. Варианты: OK commercial loss / ошибка cost / прайс.
- Blocks: Чистота margin SoT по B2B
- Evidence: `live/marts/finance_b2b_loss_evidence.csv`
- Status: `TODO`

## [P1] A-FIN-0-3243 — Разрешить identity 0-3243
- Owner hint: **Производство / 1С номенклатура**
- Category: SKU_IDENTITY
- Продажа = свитшот «Be a poem»; cost masters = худи/юбка; соседний 0-3244 свитшот с unit≈43160 (ещё хуже). Нужен правильный cost version или alias map.
- Blocks: IM COGS на одной строке
- Evidence: `live/registers/h13_im_finance/cogs_quarantine.csv`
- Status: `TODO`

## [P2] A-DATA-IM-01 — Эквайринг-реестры на IM OPEN-месяцы
- Owner hint: **Сливяк / банк**
- Category: DATA_REQUEST
- Месяцы: 2024-08,2025-01,2025-08,2025-10,2026-03,2026-04. Нужны полные возмещения Tinkoff/TBank/VTB (и Декор, если отдельно). Цель: IM CLOSE/SOFT с 80% → 90%+.
- Blocks: IM cash coverage
- Evidence: `live/marts/recon_im_combo.csv`
- Status: `TODO`

## [P2] A-DATA-B2B-01 — Платежи/взаимозачёты на B2B open (15 шт, ~2,514,023 ₽)
- Owner hint: **Сливяк / продажи B2B**
- Category: DATA_REQUEST
- В текущих выписках нет достаточных свободных платежей тех же контрагентов. Покупатели: БЕЛЬ ВИЗО ООО; ИП Бекеева Асият Багаутдиновна; ИП Джелялова Екатерина Сергеевна; ИП Кондрашкина Жанна Геннадьевна; ИП Нурова Сабигат Зайирбеговна; ИП Раева Елена Валентиновна; ИП Сердюкова Ольга Леонидовна; ИП Смирнова Яна Владимировна….
- Blocks: B2B settle coverage
- Evidence: `live/marts/data_request_b2b_open.csv`
- Status: `TODO`

## [P2] A-DATA-ZP-01 — Ведомости ЗП на месяцы без payroll_lines
- Owner hint: **Сливяк / кадры**
- Category: DATA_REQUEST
- Месяцы без линий: 2024-01, 2024-02, 2024-03, 2024-04, 2024-05, 2024-06, 2024-07, 2024-08, 2024-09, 2024-10, 2024-11, 2024-12, 2025-07, 2025-08, 2025-09, 2025-10, 2025-11, 2025-12, 2026-06. DDS↔bank уже CLOSE; ведомости нужны для сверки по сотрудникам.
- Blocks: Payroll person-level SoT
- Evidence: `live/marts/recon_payroll_multi.csv`
- Status: `TODO`

## [P3] A-FIN-WATCH-01 — Ревью 10 SKU с unit≫BOM (без автофикса)
- Owner hint: **Производство / финансы**
- Category: SKU_IDENTITY
- Высокий ratio при похожем имени — возможен неполный BOM или неверный FILE cost.
- Blocks: Качество маржи TSUM/IM
- Evidence: `live/marts/cost_identity_review_priority.csv`
- Status: `TODO`

## [P3] A-TSUM-RATE-01 — Агентский % ЦУМ из договора
- Owner hint: **Юридический / финансы**
- Category: DATA_REQUEST
- Сейчас net-rate median 0.4668 (эвристика). Договорной % → почти бухгалтерская сверка.
- Blocks: TSUM model SoT
- Evidence: `live/marts/recon_tsum_net_model.csv`
- Status: `TODO`
