# YANINA — Project Handoff (H32)

Updated: 2026-07-24 19:40  
Статус freeze: **`BRIEF_INTEGRATED_H31`** · Domain-owned staging · **не** audited SoT

---

## Открыть в этом порядке

| # | Файл | Зачем |
|---|------|--------|
| 1 | `STATUS.md` | Что сейчас важно |
| 1a | `live/CONSULTING_DIAGNOSTIC.md` | Честный консалтинговый вердикт + 14-дневный sprint |
| 1b | `live/OWNER_BRIEFING_PACK.md` + `YANINA_OWNER_BRIEFING_PACK.xlsx` | Готовые asks + черновики писем owners |
| 1c | `live/CFO_EXEC_MEMO.md` + `MEETING_15MIN_SCRIPT.md` | Memo собственнику + сценарий 15 мин |
| 1d | `live/PHASE_C_UNIFIED_INCOME_DESIGN.md` | Как склеивать A+B позже (design only) |
| 1e | `live/ILLUSTRATIVE_SCENARIO_2025.md` + `MERKUSHINA_QUESTIONNAIRE.md` | Антипример 2025 + опросник ЦУМ |
| 1f | `live/DAY7_CHECKPOINT_SCORECARD.md` | Контроль через неделю |
| 1g | `live/OPTIMIZATION_SCENARIOS.md` | Сценарии S1–S4 (мягкий→жёсткий) с эффектами |
| 2 | `live/EXEC_DASHBOARD.md` + `live/marts/executive_dashboard.csv` | Срез MD + goods + TSUM |
| 3 | `live/BUSINESS_STRUCTURE.md` | Юрлица, каналы 83/8/9, RACI |
| 4 | `live/SOT_POLICY.md` | Owners после ACCEPT |
| 5 | `live/YANINA_OWNER_PACKET_RACI_AND_REQUESTS.xlsx` | RACI 18×ACCEPT + model flags |
| 6 | `live/YANINA_LIVE_CONTROL_CENTER_20260723.xlsx` | Листы H17–H31 |
| 7 | `live/RESULTS_AND_NEXT_PLAN.md` | Полная история W1–H31 |

---

## Два контура (не смешивать)

### A. Услуги МД / инд.пошив (~83% выручки)
- Income: SALES DDS `Salon+Shop` → `MD_INDIVIDUAL` (H29)
- Detail: `МД — копия.xlsx` → payments / salon / shop (H30)
- Recon: **29/30 CLOSE+SOFT** + 1× **DDS_LAG** 2026-06 (H31)
- Docs: `live/MD_CHANNEL.md`, `live/MD_WORKBOOK.md`

### B. Товар (B2B / IM / TSUM)
- Sales lines + COGS + margin marts
- TSUM dual (H28): reported **37.9%** vs product **87.9%**
- Doc: `live/TSUM_COGS_SPLIT.md`
- Controls / release gate: `live/RELEASE_GATE.md`, `live/DOMAIN_OPS.md`

---

## Owners (из брифа, H27)

| Домен | ФИО |
|-------|-----|
| Cash | Мамушкина Елена |
| Bank / Tax / Payroll / Data | Сливяк Галина |
| Tax Approver | Янина Ю.Ф. |
| Product | Коновалова Анна |
| Cost / Production | Мокеева Анна |
| B2B | Коптева Марина |

---

## Что ждёт человека / новые файлы

1. **`закоммить`** — зафиксировать H1–H31 в git (скажите явно)
2. SALES DDS за **2026-06** — снимет DDS_LAG
3. Меркушина: формула **% комиссии ЦУМ** в cost cards
4. Опционально: выписки Салон / карта (уже в «расходы», periметр)

---

## Чего больше не делать автономно

- Не плодить H33+ без новых данных или явной команды
- Не объявлять полный SoT / audited P&L
- Не джойнить МД-услуги в goods COGS
- Не вычитать комиссию ЦУМ дважды (cash net-rate + FILE COGS)

---

## Ключевые цифры (indicative)

| Метрика | Значение |
|---------|----------|
| MD 2025 income | 2.33M EUR (~83.9% vs brief 83%) |
| MD↔DDS 2025 gap | −6.2k EUR |
| TSUM reported / product GM | 37.9% / 87.9% |
| Goods B2B / IM margin | ~68% / ~82% |
| RACI | 18 ACCEPT |

Evidence roots: `live/evidence/h27_*` … `h31_*`
