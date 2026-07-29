# Map 46 — Stock end-qty ↔ IM/TSUM sell-through (H75)

```
stock_by_warehouse_full (qty_end)
        │
        ├── Склад ИМ ─────────────► channel_map=IM
        ├── Остатки ЦУМ ──────────► channel_map=TSUM
        └── Склад оптовых ────────► channel_map=B2B
                │
                ▼
        stock_channel_bridge  ◄──── sales_lines (IM/TSUM/B2B)
                │
                ├── STOCK_AND_SALES
                ├── STOCK_NO_SALES      ← dead-stock candidates
                └── SALES_NO_STOCK      ← sold-through / no snapshot
```

## Rules
- Snapshot vs multi-period sales → proxy only.
- TSUM warehouse↔sales identity may not join — flag, don’t conclude.
- `do_not_auto_accept=YES` · never SoT.
