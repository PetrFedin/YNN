# Map 45 — Цех ЗП ↔ collections / stock warehouses (H74)

```
ЗП_ЦЕХ 0N.26.xlsx (×5)
        │
        ├── портн ──► 7 tailor blocks ──► article × pay («К выплате»)
        │                                    │
        └── сметка ──► hours × rate         │
                                             ▼
                              shop_collection_stock_bridge
                                             │
              ┌──────────────────────────────┼──────────────────────────────┐
              ▼                              ▼                              ▼
     collection sales                  person-cost                   stock_cost
        (H62/H64)                        (H65)                    warehouses
                                                                   (IM/опт/ДЕМИ/…)
```

## Bridge flags (combinable)
`COLLECTION` · `PERSON_COST` · `STOCK_WH` · `ORPHAN` · `NO_ART`

## Rules
- Portn `Итого` = authoritative pay total (col 15), не сумма сырых строк вслепую.
- Stock rarity expected (collection ≠ goods SKU).
- `do_not_auto_accept=YES` · never SoT.
