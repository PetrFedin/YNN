# 09 — Карта данных (one-pager)

Updated: 2026-07-27 · для заказчика

```
ИСТОЧНИКИ (~107 файлов)
  Банк · ДДС · SALES · МД workbook · Продажи IM/B2B/TSUM
  Расходы · Ткани/склады · Налоги PDF · ЗП · Бриф/RACI
        ↓
РЕГИСТРЫ W1–W6 (staging)
  bank_payments · sales_lines · MD · expense · materials · tax
        ↓
MARTS / CONTROLS (~75)
  margin_* · recon_* · release_gate_* · executive_dashboard
        ↓
УПР. АРТЕФАКТЫ
  client_pack (диагностика) · Owner Briefing · Scenarios S1–S4
  KPI catalog draft · Fin model skeleton · Policy drafts
```

| Вопрос заказчика | Куда смотреть |
|------------------|---------------|
| Сходится ли касса | release_gate, recon_*, OWNER_BRIEFING |
| Маржа товара | margin_channel_*, TSUM dual |
| Доход МД | MD_CHANNEL / recon_md_* |
| Что делать | client_pack 02–05, OPTIMIZATION_SCENARIOS |
| Что мерить | 07_KPI_CATALOG_DRAFT |

Подробнее: `HANDOFF.md`, `live/architecture/`.
