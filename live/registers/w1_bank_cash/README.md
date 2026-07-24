# W1 BANK / CASH / LEGAL

Generated: 2026-07-23 18:39

## Файлы регистров
- `legal.csv` — 2 юрлица (ИП подтверждён ИНН из выписки; ООО ДЕКОР — INN TBD)
- `bank_accounts.csv` — Alfa parsed + 3 VTB PDF gap
- `bank_payments.csv` — **1715** платежей из 3 Alfa xlsx
- `cash_lines.csv` — **5981** строк ДДС (data B + data D)
- `recon_bank_vs_dds_month.csv` — помесячная сверка
- `soft_matches_pilot.csv` — пилот 2025-08: exact amount same month
- `gaps.csv` — VTB PDF и пр.

## Evidence
`../../evidence/w1_bank_cash_20260723/YANINA_W1_BANK_CASH_EVIDENCE.xlsx`

## Важно
Это Controlled Staging, не Source of Truth.
Match по сумме+месяцу = LOW confidence (в ДДС нет payment_date).

## W1b (VTB PDF)
- +2291 платежей из 3 VTB PDF
- internal transfers flagged → operating recon
- 8 CLOSE + 18 SOFT_GAP; 2026-04 CLOSE
