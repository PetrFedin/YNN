# Phase C — Unified Income Design (методология, без сборки P&L)

Updated: 2026-07-24 20:05  
Статус: **DESIGN ONLY** · не реализовано · не SoT  
Предусловие старта реализации: ответы P0 из `CFO_EXEC_MEMO.md` (§4 п.1–3) + DDS 2026-06

---

## 1. Зачем фаза C

Сейчас честно существуют **два контура**. Бизнесу нужен третий артефакт — **unified income statement** — но только как *управляемая склейка с явными правилами*, иначе получится красивая ложь.

Цель фазы C: один ежемесячный пакет, где:
- видны **A (МД)**, **B (товар)**, **A+B (группа)**;
- каждый слой подписан источником и качеством (CLOSE/SOFT/OPEN);
- комиссия ЦУМ учитывается **один раз**;
- opex/tax не «съедают» МД-выручку молча.

---

## 2. Рекомендуемая структура отчёта (макет)

```
YANINA Unified Income — YYYY-MM          [PROVISIONAL | RELEASED]
FX policy: EUR@100 (flag)                Gate: PASS/FAIL

1. Revenue
   1.1 MD / Individual sewing (EUR→RUB@policy)     ← SALES DDS Salon+Shop
   1.2 IM retail                                    ← sales lines IM
   1.3 B2B wholesale                                ← sales lines B2B
   1.4 TSUM gross merchandise                       ← sales lines TSUM
   1.5 (−) TSUM agency commission                   ← ONE place only
   = Net revenue (management)

2. Cost of sales
   2.1 MD direct (если появится; сейчас часто N/A)  ← не выдумывать
   2.2 Goods product COGS (W3/FILE clean)           ← без комиссии ЦУМ
   2.3 Quarantine / exceptions memo                 ← 0-3243, wholesale OK loss
   = Gross margin (split A / B / Total)

3. Operating expenses (by LE + nature)
   Payroll | Rent | Marketing | Other               ← expense/DDS maps
   Memo: materials / internal / FX                  ← не в core дважды

4. Tax cash (USN/VAT5/etc.)                         ← tax mart

5. Operating result (management)
   + Quality appendix: control statuses that month
```

### Критическое правило ЦУМ
Выбрать **один** режим и зафиксировать в SoT policy:

| Режим | Revenue | COGS | Cash recon |
|-------|---------|------|------------|
| **C1 (реком.)** | TSUM gross − commission line | Product COGS only | Net-rate сверяет cash, не P&L |
| C2 | TSUM net already | Product COGS | Commission не в P&L |
| C3 (как Excel сейчас) | TSUM gross | FILE COGS **с** комиссией | Net-rate **не** вычитает комиссию снова |

Сейчас staging ближе к **C3 в margin** + **отдельный cash net-rate**. Для unified нужен явный выбор C1/C2/C3 после ответа Меркушиной.

---

## 3. Источники по строкам (mapping)

| Строка | Primary source | Fallback | Quality gate |
|--------|----------------|----------|--------------|
| 1.1 MD revenue | SALES DDS Salon+Shop | МД payments (EUR) | MD↔DDS CLOSE/SOFT |
| 1.2 IM | W4 sales IM | — | lines DQ (no stub/returns) |
| 1.3 B2B | W4 sales B2B | — | settle link % |
| 1.4 TSUM gross | W4 sales TSUM | — | — |
| 1.5 Commission | Договорной % × gross **или** FILE−W3 proxy | agent cash | TSUM_NET CLOSE |
| 2.2 Goods COGS | W3 product preferred | FILE clean | quarantine flags |
| 3 Opex | expense clean + DDS BN | bank | OPEX_MULTI |
| 4 Tax | tax cash | bank УФК | TAX_CASH_BANK |

---

## 4. Чего нельзя делать в v1 unified

1. Подставлять «среднюю маржу 53%» на МД.  
2. Тащить весь opex ИП только против goods GM (текущий bridge).  
3. Аллоцировать payroll на каналы без явной driver-модели (FTE / выручка / ручная) — лучше показать opex **отдельно** в v1.  
4. Скрывать OPEN-месяцы: если gate BLOCKED — unified лист = `PROVISIONAL` с красным appendix.  
5. Смешивать LE Декор 2026+ operating с ИП без wind-down tag.

---

## 5. Аллокация opex (честные варианты)

| Вариант | Плюс | Минус | Рекомендация |
|---------|------|-------|--------------|
| **O0: не аллоцировать** | Честно | Нет «маржи канала после opex» | **v1** |
| O1: % выручки | Просто | МД 83% заберёт почти весь opex | v2 после стабилизации revenue |
| O2: driver (FTE/часы) | Экономически ближе | Нужны данные Мокеевой/кадров | v2–v3 |
| O3: только direct cost по каналу | Чисто | Неполный P&L | параллельно O0 |

**Консалтинговая позиция:** стартовать с **O0**. Иначе первый же unified P&L обвинит МД в «съедении» opex и повторит ошибку goods bridge с другим знаком.

---

## 6. Валюта и FX

- Бриф: отчёты часто EUR@**100**.  
- Unified header обязан нести `fx_policy=100` или `market`.  
- Не смешивать EUR МД и RUB goods без колонки `amount_rub` + `fx_rate_used`.  
- Курсовые с 2026 — отдельная memo-строка, не внутри GM.

---

## 7. Критерии готовности к реализации (go / no-go)

| # | Критерий | Go if |
|---|----------|-------|
| G1 | Правило двух контуров принято | да |
| G2 | Режим ЦУМ C1/C2/C3 выбран письменно | да |
| G3 | MD DDS_LAG 2026-06 закрыт | да |
| G4 | IM CLOSE+SOFT ≥90% **или** OPEN-месяцы явно excluded | да |
| G5 | B2B open < 0.5M или memo по каждой крупной | да |
| G6 | Decor wind-down tag в bank marts | желательно |

Пока G1–G3 = no → **не кодить** unified mart.

---

## 8. Порядок работ (когда go)

1. Зафиксировать `UNIFIED_POLICY.md` (C-режим ЦУМ, FX, O0).  
2. Собрать `marts/unified_income_month.csv` (только строки 1.x + 2.2 + 3 total + 4).  
3. Appendix controls на тот же месяц.  
4. Пилот: 2025-01..2025-12 (12 мес), сверка totals с DDS/sales.  
5. Только потом: UI / Live CC sheet «Unified».

Оценка трудоёмкости после go: **2–4 рабочих дня** аналитика при готовых файлах; не «ещё 10 hardenings».

---

## 9. Связь с текущими артефактами

| Уже есть | Роль в Phase C |
|----------|----------------|
| `margin_channel_*` | Блок 1.2–1.4 / 2.2 |
| `tsum_margin_dual_*` | Выбор C-режима |
| `recon_md_*` | Блок 1.1 quality |
| `operating_bridge_*` | **Антипример** аллокации (goods-only) |
| `release_gate_*` | Header PROVISIONAL/RELEASED |
| `OWNER_BRIEFING_PACK` | Разблокировка G1–G5 |

---

## 10. Итог

Phase C — это **дисциплина склейки**, не новый Excel «на всё».  
Пока owners не закрыли P0 по интерпретации и ЦУМ, правильный профессиональный ход — **держать два контура отдельно** и рассылать `CFO_EXEC_MEMO.md`.
