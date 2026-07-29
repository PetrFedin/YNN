# Map 44 — Designers payroll ↔ collections / person-cost (H73)

```
зп_конструкторы_0N.26.xlsx (×5)
        │
        ├── Лист1 (KPI monthly) ──► pay_net / cut / delivered / score
        │                              │
        │                              ▼
        │                     designer_kpi_monthly
        │                     designer_constructor_summary
        │
        └── сметк 01.25 (dedupe ×1) ──► article × constructor × hours
                                           │
                                           ▼
                              designer_smetka_collection_bridge
                                           │
                    ┌──────────────────────┼──────────────────────┐
                    ▼                      ▼                      ▼
            collection sales          person-cost             HIGH gap
              (H62/H64)                 (H65)                worksheet
```

## Bridge values
| Value | Meaning |
|-------|---------|
| `LINKS_COLLECTION_AND_PC` | арт в продажах коллекции **и** workshop cost |
| `LINKS_COLLECTION_ONLY` | только продажи |
| `LINKS_PERSON_COST_ONLY` | только workshop |
| `ORPHAN_SMETKA` | нет ни там, ни там (сейчас `0-2483`) |

## Rules
- Smetka fingerprint-dedupe — не суммировать 5 копий.
- KPI score: строка «Результат» может быть **без ФИО в col0**.
- `do_not_auto_accept=YES` · никогда не SoT.
