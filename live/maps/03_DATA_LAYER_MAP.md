# 03 — Карта данных L0→L5 (архитектура)

Updated: 2026-07-27  
Источник: `live/architecture/` (93→107 файлов, 15 регистров, 199 edges as-is)

---

## 1. Слои

```
L0  Сырые файлы (Downloads)          — не в git
L1  Каталог / inventory              — 00_SOURCE_CATALOG_107
L2  Masters (Legal, SKU, Counterparty) — частично
L3  Registers W1–W6                  — staging таблицы
L4  Marts (~75 CSV)                  — margin, recon, gate, MD…
L5  Controls / Gate / Client pack    — решения и качество
```

As-is связность файлов: острова (крупнейший компонент 43/93).  
To-be через регистры (≤3 hops): **93/93 в одном компоненте** (architecture verdict).

---

## 2. Регистры (15) и волны

| Волна | Регистры | Бизнес-смысл | Статус исполнения |
|-------|----------|--------------|-------------------|
| W1 | BANK, CASH, LEGAL | Платежи, ДДС, юрлица | Done → 4933 payments |
| W2 | PAYROLL, EMP | ЗП, сотрудники | Done → multi 100% |
| W3 | SKU, COST, PROD | Номенклатура, себестоимость | Done → dual TSUM later |
| W4 | SALES, SETTLE | Продажи, взаиморасчёты | Done → 2826 lines |
| W5 | SUP, EXP, MAT | Поставщики, opex, ткани | Done → ~30M stock |
| W6 | TAX, BUD | Налоги, бюджет | Done → tax cash 97% |

Hardenings H1–H36 = улучшение поверх регистров (spine, DQ, gate, MD, consulting).

CSV: `register_wave_map.csv`

---

## 3. Marts (семейства)

| Семейство | ≈ файлов | Назначение |
|-----------|----------|------------|
| recon_* | много | Сверки контуров |
| margin_* | | Маржа каналов / dual TSUM |
| release_gate_* | | Ворота месяца |
| operating_bridge_* | | Goods-only bridge (антипример KPI) |
| owner_*/data_request_* | | Запросы owners |
| md_* / forensic_* | | МД и forensic |
| other | | Прочее |

Инвентарь: `marts_inventory.csv`

---

## 4. Spine (ключевые связи)

Типовые рёбра:
- SUP.inn ↔ bank.counterparty  
- SETTLE ↔ bank (doc/amount)  
- SALES ↔ COST (sku)  
- PAYROLL/EXPENSE ↔ DDS ↔ bank  
- SALES DDS ↔ MD payments  
- TAX cash ↔ bank УФК  

Без spine нельзя собрать gate и dual views.

---

## 5. ± слоя данных

| + | − |
|---|---|
| Полный контур W1–W6 построен | Masters (SKU alias) не все ACCEPT |
| Marts + gate дают операционное качество | Unified income mart не собран (by design) |
| Evidence по каждой волне | Сырьё вне репо — воспроизведение нужно с Downloads |
