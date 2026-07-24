# Unified Data Architecture

Updated: 2026-07-24 16:10

Главный файл: `YANINA_UNIFIED_DATA_ARCHITECTURE.xlsx`

## Принцип
As-is 199 file edges = диагностика островов.
To-be = L0..L5 через Masters/Registers/Marts — **единый контур 93/93**.

## Ключевой вывод (max connectivity)
| Контур | Файлов в крупнейшем компоненте | Компонент |
|--------|--------------------------------:|----------:|
| As-is (прямые рёбра) | 43 / 93 | 50 |
| To-be spine (≤3 hops) | **93 / 93** | **1** |

Пар файл↔файл через регистры: hop0=1884, hop1=1774, hop2=547, hop3=73.
Семейных схем с путём: **276 / 276**.

## Состав workbook
- 00–12: слои, регистры, spine, families, files→regs, marts, paths, contracts
- **13_Max_Connectivity** — цифры as-is vs to-be
- **14_Family_Max_Schemes** — все пары семейств + spine path
- **15_Reg_Reachability** — матрица достижимости регистров
- **16_Reg_Pair_Potential** — потенциал пар файлов между регистрами
- **17_Path_File_Examples** — 12 path с примерами FILE-xxx
- **18_Register_DDL** — колонки/ключи/волны W0–W6
- **19_Architecture_Verdict** — ответы «можно ли соединить всё»

## Рядом
- `architecture.json`, `max_connectivity.json`
- `family_max_schemes.csv`, `register_reachability.csv`, `register_pair_potential.csv`
- W1 stubs: `../registers/w1_bank_cash/` (BANK, CASH, LEGAL)

## Порядок
W0 LEGAL/RACI → **W1 BANK/CASH** → W2 PAYROLL/EMP → W3 SKU/COST → W4 SALES/SETTLE → W5 SUP/EXP/MAT/PROD → W6 TAX/BUD

## W1 execution (2026-07-23)
Staging загружен: `../registers/w1_bank_cash/`
- 4006 bank payments (Alfa+VTB), 5981 cash lines
- operating recon: 8 CLOSE + 18 SOFT; 2026-04 CLOSE
- evidence: `../evidence/w1_bank_cash_20260723/`

## W2 execution (2026-07-24)
Staging: `../registers/w2_payroll/`
- 151 EMP, 991 payroll lines, 481 card rows
- **2026-04 dual CLOSE**: ZP↔DDS и cards↔bank
- evidence: `../evidence/w2_payroll_20260724/`

## W3 execution (2026-07-24)
Staging: `../registers/w3_sku_cost/`
- TSUM 800 lines / 220 SKU; cost 2043 versions; intersection **100**
- 2026 coverage ~77% SKU / ~82% amount; matched margin ~74% (indicative)
- evidence: `../evidence/w3_sku_cost_20260724/`

## W4 execution (2026-07-24)
Staging: `../registers/w4_sales_settle/`
- 2082 1C sales + 800 TSUM; 755 settlements; 31 settle↔bank soft matches
- 1159 1C lines linked to W3 cost
- evidence: `../evidence/w4_sales_settle_20260724/`

## W5 execution (2026-07-24)
Staging: `../registers/w5_sup_exp_mat/`
- 63 SUP / 1568 opex / 1339 fabric SKU (~22.6M warehouse)
- ИТОГО↔DDS Б/Нал: 24 CLOSE; hub↔bank: 8 CLOSE+7 SOFT
- evidence: `../evidence/w5_sup_exp_mat_20260724/`

## W6 execution (2026-07-24)
Staging: `../registers/w6_tax_bud/`
- 25 tax obligations; DEKOR INN **7735518240**
- tax_cash↔bank (ФНС/УФК/ОСФР): **26 CLOSE + 3 SOFT**; **2026-04 CLOSE**
- budget 475 lines; bud_exp↔DDS: 2 CLOSE + 1 SOFT (2026-01..03)
- evidence: `../evidence/w6_tax_bud_20260724/`
- **W1–W6 Controlled Staging complete** → next gate: RACI/SoT

## H1 spine links (2026-07-24)
Staging: `../registers/h1_spine_links/`
- SUP.inn↔bank: **28/44**, 304 OUT edges (~54.7M ₽)
- SETTLE↔bank: doc_num + amount/name → **14** matches (8 amount_name, 6 doc)
- evidence: `../evidence/h1_spine_links_20260724/`
- Owner Packet: листы FILL_CHECKLIST + GAP_MITIGATION (без выдуманных ФИО)

## H2 enrichment (2026-07-24)
Staging: `../registers/h2_enrichment/`
- settle backfill 8 links into W4 settlements
- USN PDF amounts 4/4 → W6 obligations
- signer candidates for Owner Packet (confirm manually)
- evidence: `../evidence/h2_enrichment_20260724/`

## H3 new documents (2026-07-24)
- +14 files → catalog **107** (`../registers/00_SOURCE_CATALOG_107.csv`)
- NEW LE: ООО Салон Юлия Янина (7715219770) + Sber 510 payments
- VTB card StatementFull 417 (Мамушкина Е.А.)
- SKU master 1863; sales B2B/IM/TSUM extended to 2026-06
- RACI draft from «Финансы и платежи.docx»
- evidence: `../evidence/h3_new_docs_20260724/`

## H4 integrate (2026-07-24)
- W4 refresh from H3 sales_extended: 2826 lines / 806 settlements / to 2026-06
- SKU master coverage: ∩ cost∩sales = 257
- Fabric movements staging in W5 (`material_movements_fabric.csv`)
- evidence: `../evidence/h4_integrate_20260724/`

## H5 improve (2026-07-24)
- Stock cost FILE-099 → 2957 lines; +720 derived unit costs into W3
- Alias relink (lat/cyr + strip): W4 cost links 1408→2696; SKU∩ 257→901
- Sber Salon tax-like: 10 pays ~520k RUB
- evidence: `../evidence/h5_improve_20260724/`

## H7 controls (2026-07-24)
- Card spend categories (Mamushkina)
- Bank by legal entity + extended core↔DDS recon (Salon separated)
- Margin anomaly controls → `../marts/margin_anomalies.csv`
- evidence: `../evidence/h7_controls_20260724/`

## H8 DQ (2026-07-24)
- COGS quality gate: drop inflated W3/H5 unit costs; restore FILE cogs when sane
- Exclude junk revenue lines from margin marts
- Neg SKUs reduced; margin marts refreshed in `../marts/`
- evidence: `../evidence/h8_dq_20260724/`
