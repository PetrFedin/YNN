# 07 — Каталог KPI (черновик, не внедрённая система)

Updated: 2026-07-27  
Статус: **DRAFT KPI CATALOG** · для утверждения · без автоматизации и дашборд-внедрения

Ритм (предложение): **неделя** — data ops / касса; **месяц** — gate + контуры A/B.

---

## A. Обязательные KPI (P0)

| KPI ID | Название | Формула / определение | Источник | Owner | Порог / правило |
|--------|----------|----------------------|----------|-------|-----------------|
| K01 | MD Income | Σ SALES DDS Salon+Shop (мес) | DDS / MD_INDIVIDUAL | Сливяк / Мамушкина | тренд; лаг = alert |
| K02 | MD↔DDS status | CLOSE/SOFT/OPEN/DDS_LAG | recon_md_* | Сливяк | ≥2024: цель 30/30 CLOSE+SOFT |
| K03 | Goods GM % | (Rev−COGS)/Rev costed | margin_channel_* | Мокеева | смотреть by channel |
| K04 | TSUM GM dual | reported % **и** product % | margin_channel_views_h28 | Коптева / Мокеева | всегда оба; не одно число |
| K05 | Release Gate | RELEASED / BLOCKED | release_gate_month | Сливяк | доля BLOCKED ↓ |
| K06 | B2B Open ₽ | Σ open settlements | data_request_b2b_open | Коптева | → 0 или memo |
| K07 | IM Acq status | CLOSE+SOFT % | recon_im_combo | Сливяк | цель ≥90% |
| K08 | Payroll control | PAYROLL_MULTI status | recon_payroll_multi | Сливяк | держать CLOSE/SOFT |
| K09 | Tax cash control | TAX_CASH_BANK status | recon_tax_* | Сливяк | держать ≥95% |
| K10 | Two-contour flag | Отчёт помечен A/B | политика | Янина | 100% отчётов |

## B. KPI развития (P1) — после пилотов

| KPI ID | Название | Зачем | Блокер сейчас |
|--------|----------|-------|---------------|
| K11 | MD Contribution % | Экономика ядра | нет COGS заказа |
| K12 | MD cycle time / предоплата | Процесс | нет регулярного замера |
| K13 | Fabric DOH / slow% | WC | нужен ABC-aging |
| K14 | TSUM commission % actual | Убрать dual ambiguity | ответ Меркушиной |
| K15 | FTE split MD/Goods/Shared | Безопасная оптимизация ФОТ | экспертный split |
| K16 | Unified income (O0) | Картина группы | Phase C go G1–G3 |

## C. Антикипи (запрещены)

| Запрет | Почему |
|--------|--------|
| Goods operating % как «прибыль YANINA» | Нет МД в базе |
| TSUM GM только 37.9% | Комиссия в COGS |
| «Маржа компании = 53%» | Только goods |
| Сырой opex % от MD+goods без политики | Аллокация врёт |

## D. Минимальный отчёт месяца (1 страница)

1. K01–K02 (МД)  
2. K03–K04 (товар + TSUM dual)  
3. K05–K07 (gate / касса)  
4. K08–K09 (контроль)  
5. Список BLOCKED месяцев + owners  

Это **ещё не KPI-система**: нет автоматических витрин и регламента взыскания. Для Этапа 3 — внедрить ритм и владельцев из таблицы выше.
