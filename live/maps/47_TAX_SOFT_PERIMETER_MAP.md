# Map 47 — Tax SOFT ↔ Salon UFK perimeter (H76)

```
tax_cash_lines (opex «налоги»)
        │
        ▼
 recon_tax_cash_bank  ◄──── bank_tax_like (IP/Декор УФК/ФНС/ОСФР)
        │                         ▲
        │                         │ missing
        │                         │
        └── GAP/SOFT deltas ──────┴── Salon Sber → УФК
                                      (sber_salon_tax_payments)

2024-01  36 000 ──► TAX→27 candidate
2024-10 147 180 ──► recon quality
2025-08  77 410 ──► recon quality
2026-06 −30 900 ──► trademark fee noise + residual
```

## Rules
- Perimeter change = **owner sign**, not auto-Accept.
- PDF obligations ≠ monthly cash.
- Trademark/IP fees ≠ tax obligation.
