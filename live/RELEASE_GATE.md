# Controls Release Gate (H18)

Updated: 2026-07-24 17:42

Провизорные ворота месяца. **Не SoT.**

- Months: **30**
- RELEASED: **18**
- BLOCKED: **12** (40.0%)
- Gate controls: `IM_ACQ_COMBO, TSUM_NET_MODEL, BANK_DDS_CORE, TAX_CASH_BANK, PAYROLL_MULTI, OPEX_MULTI`
- PASS statuses: `CLOSE, SOFT, SOFT_GAP`

## BLOCKED months

| Month | Fail | Soft pass | Owner actions |
|-------|------|-----------|---------------|
| 2024-01 | BANK_DDS_CORE|TAX_CASH_BANK | IM_ACQ_COMBO | — |
| 2024-06 | BANK_DDS_CORE | IM_ACQ_COMBO | — |
| 2024-08 | IM_ACQ_COMBO | BANK_DDS_CORE | A-DATA-IM-01 |
| 2024-12 | BANK_DDS_CORE | IM_ACQ_COMBO|TSUM_NET_MODEL | — |
| 2025-01 | IM_ACQ_COMBO | BANK_DDS_CORE | A-DATA-IM-01 |
| 2025-08 | IM_ACQ_COMBO | TAX_CASH_BANK | A-DATA-IM-01 |
| 2025-10 | IM_ACQ_COMBO | — | A-DATA-IM-01 |
| 2026-02 | BANK_DDS_CORE | IM_ACQ_COMBO | — |
| 2026-03 | IM_ACQ_COMBO | — | A-DATA-IM-01 |
| 2026-04 | IM_ACQ_COMBO | — | A-DATA-IM-01 |
| 2026-05 | TSUM_NET_MODEL | — | A-TSUM-RATE-01 |
| 2026-06 | TSUM_NET_MODEL|BANK_DDS_CORE | IM_ACQ_COMBO|TAX_CASH_BANK | A-TSUM-RATE-01 |

## Как читать

1. `RELEASED` — все gate-controls CLOSE/SOFT (управленчески «можно смотреть месяц»).
2. `BLOCKED` — есть OPEN/WIDE_GAP/…; смотрите `release_gate_blocked.csv` и Owner Actions.
3. После RACI ACCEPT политику можно ужесточить (например, запретить SOFT).

Файлы: `live/marts/release_gate_month.csv`, `release_gate_blocked.csv`, `release_gate_fails.csv`.
