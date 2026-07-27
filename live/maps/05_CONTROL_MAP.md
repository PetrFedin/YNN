# 05 — Карта контролей качества

Updated: 2026-07-27

---

## 1. Controls CLOSE+SOFT % (30 мес)

| Control | % | Смысл |
|---------|--:|-------|
| PAYROLL_MULTI | 100 | ФОТ контуры сходятся |
| OPEX_MULTI | 100 | Opex контуры сходятся |
| TAX_CASH_BANK | 96.7 | Налоги в банке |
| TSUM_NET_MODEL | 93.3 | Агентский net-rate |
| BANK_DDS_CORE | 83.3 | Ядро банк↔ДДС |
| IM_ACQ_COMBO | 80.0 | ИМ↔эквайринг |

## 2. Release Gate

- **18 RELEASED / 12 BLOCKED**
- Fail frequency: IM×6, BANK_DDS×5, TSUM_NET×2, TAX×1

BLOCKED ≠ «убыток»; = «месяц нельзя читать без оговорки».

## 3. Контурные сверки сверх gate

| Сверка | Статус | Процесс |
|--------|--------|---------|
| MD↔DDS ≥2024 | 29/30 (+1 LAG) | P01 |
| B2B settle | 39 linked / 15 open (2.51M) | P04 |
| Salon Sber forensic | 510/510 | P11 (казначейство / LE Салон) |
| TSUM dual | 37.9 / 87.9 | P03 |
| BANK_DDS core | 83.3%; fail ×5 | P11 |
| IM acquiring | 80%; gate×6 OPEN | P02 |

## 4. DQ / finance exceptions

- Stub revenue / returns выведены из margin (H8)
- 0-3243 quarantine; wholesale OK loss ×3 OWNER_ACCEPTED
- SKU aliases — candidates, не auto-applied

## 5. ±

| + | − |
|---|---|
| Честный gate красит дыры | 40% месяцев BLOCKED |
| Payroll/OPEX/Tax сильны | IM и bank core тянут вниз |
| Exceptions приняты | Watchlist unit≫BOM без ревью Product |
