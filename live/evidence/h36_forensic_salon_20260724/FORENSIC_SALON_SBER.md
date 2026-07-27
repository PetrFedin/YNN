# H36 — Forensic: свежие выписки Salon Sber

Updated: 2026-07-24 20:40  
Статус: **forensic complete** · ingest **не** делался · не SoT

---

## Вопрос

Нужно ли заново глотать Salon Sber / карту из Downloads от 24.07, чтобы снять BLOCKED по `BANK_DDS_CORE`?

## Метод

Свежие файлы:
- `СберБизнес…40702810638040103938` за 2024, 2025, 2026-01..06  

Сверка с `live/registers/w1_bank_cash/bank_payments.csv` где `bank_account_id = 40702810638040103938` (LE-OOO-SALON-YANINA, source_bank=SBER).

Ключ матча: `payment_date | abs(amount)`.

## Результат

| Метрика | Значение |
|---------|----------|
| Строк в свежих выписках | **510** (OUT 471 / IN 39) |
| Строк в bank mart (Salon) | **510** (out 471 / in 39) |
| Match date\|amount | **510 / 510** |
| Missing in bank | **0** |
| Extra in bank | **0** |
| Оборот OUT | 5,516,594 ₽ = bank |
| Оборот IN | 4,923,674 ₽ = bank |

Помесячный CSV: `live/marts/forensic_salon_sber_coverage.csv` (расхождений нет).

## Вердикт

**FRESH_ALREADY_COVERED — ingest Salon Sber не нужен.**

Следствие для консалтинга:
1. `OPTIONAL_DATA_NOTE` по Salon Sber **закрыт**.  
2. BLOCKED месяцы `BANK_DDS_CORE` (2024-01/06/12, 2026-02, …) **не** объясняются «нету выписки Салона». Нужен memo по статьям/периметру DDS↔bank core, не перезаливка Sber.  
3. Карта `StatementFull_*` — отдельный optional; в bank уже **417** VTB_CARD. Без жалобы на дыру карты — не трогаем.

---

## Стоп-линия консалтинга (честно)

Цепочка H32→H35 (handoff → diagnostic → briefing → memo/Phase C → scenario/опросник/Day7) + H36 forensic исчерпала **аналитическую** работу без входа owners.

Дальше без D1/D2 / ответа Меркушиной / DDS 06 / IM / B2B файлов:
- новые MD «волны» = имитация;
- новый ingest Salon = пустая работа (доказано выше);
- сборка Phase C P&L = методологическая ошибка.

**Единственный value now:** провести 15 мин / переслать memo + опросник.
