# YNN / YANINA — Stage 2 Integration Master Plan

**Document:** `docs/YNN_STAGE2_INTEGRATION_MASTER_PLAN_2026-10-01.md`  
**Status:** PLANNED  
**Date:** 2026-10-01  
**Repository:** `PetrFedin/YNN`

## Purpose

This file is the canonical implementation roadmap for turning Stage 2 from diagnostic conclusions into a repeatable management operating system. It complements, and does not replace, the approved Stage 2 scope and acceptance criteria already stored in the client pack.

A future instruction to implement this document means building the data, control and reporting mechanisms below in the stated order.

## Existing business authority to preserve

The Stage 2 scope already defines the business methodology:

- 13-week cash forecast;
- dual P&L / management balance;
- order economics;
- WIP and capacity;
- inventory / working capital;
- purchasing and supplier control;
- D+10 close;
- tax scenarios;
- benefit realisation.

This plan must automate and operationalise that methodology, not invent a new one.

## Integration disposition

| Capability | Source | Decision |
|---|---|---|
| 13-week Cash Authority | native | ADOPT |
| Order Economics Ledger | native | ADOPT |
| WIP Digital Twin | native | ADOPT |
| D+10 Close Cockpit | native | ADOPT |
| Benefit Realisation Register | native | ADOPT |
| Data ingestion | dlt | ADOPT |
| File/schema contracts | Frictionless | ADOPT |
| DataFrame validation | Pandera | ADOPT |
| Transformation methodology | dbt-core patterns | ADAPT |
| Data quality | Great Expectations | ADAPT |
| Workflow orchestration | Dagster patterns | ADAPT/CONDITIONAL |
| Semantic metrics | Cube | ADAPT |
| Management BI | Metabase | SIDECAR/ADAPT |
| Statistical forecasting | StatsForecast | CONDITIONAL |
| Connector platform | Airbyte | DEFER |

## Phase 0 — Methodology freeze

Before automation:

1. freeze metric definitions;
2. freeze source ownership;
3. freeze row/field authority rules;
4. freeze snapshot/version policy;
5. define who can approve corrections;
6. define how actuals, forecasts and scenarios differ.

No dashboard is built before these are explicit.

## Phase 1 — Governed ingestion

### dlt

Use for repeatable loads from:

- bank exports;
- accounting/1C exports;
- orders;
- WIP;
- inventory;
- supplier files;
- channel sales.

Flow:

`source file/API -> immutable landing -> schema contract -> validation -> normalized staging -> authoritative management table`

Every load has:

- source;
- period;
- file hash;
- loaded_at;
- version;
- status;
- rejected rows.

### Frictionless

Define file-level schemas for every recurring Excel/CSV input.

### Pandera

Apply business/dataframe checks after parsing:

- required columns;
- type/range;
- uniqueness;
- non-negative constraints;
- date logic;
- allowed statuses;
- reconciliation totals.

## Phase 2 — 13-week Cash Authority

Create a rolling weekly model based on commitments, not ML guesses.

Entities:

- opening cash;
- committed receipt/payment;
- probable receipt/payment;
- owner financing;
- tax/payment calendar;
- payroll;
- purchase commitments;
- WIP completion reserve;
- minimum liquidity reserve;
- scenario adjustment.

Outputs:

- weekly opening/closing cash;
- minimum cash point;
- committed gap;
- discretionary payment queue;
- explanation of forecast vs actual.

StatsForecast may later provide statistical context for uncertain operating inflows, but it must never override committed obligations.

## Phase 3 — Order Economics Ledger

For each couture/order:

`quoted revenue -> discount -> material -> labour -> external work -> rework -> logistics -> allocated cost -> actual margin -> contribution per bottleneck hour`

Store plan and fact separately.

Required controls:

- design freeze;
- change after freeze;
- urgency premium;
- complexity class;
- reason for variance;
- rework owner.

Order ledger becomes the source for management analysis; no manual dashboard correction outside ledger.

## Phase 4 — WIP Digital Twin

Each open order gets:

- stage;
- planned completion;
- material readiness;
- accumulated cost;
- cost-to-complete;
- bottleneck resource;
- delay/rework reason;
- owner;
- risk flag.

The twin is operational/financial, not a 3D model.

Portfolio views:

- WIP aging;
- value tied up;
- cost-to-complete;
- capacity by week;
- overdue commitments;
- cash requirement to finish.

## Phase 5 — Inventory & Working Capital

Build canonical inventory decisions:

`item -> quantity/value -> age -> reservation/use -> free stock -> class -> decision -> owner -> realised effect`

Decisions:

- use;
- reserve;
- substitute new purchase;
- return;
- sell;
- archive;
- write off.

Prevented purchase is tracked separately from accounting write-off.

## Phase 6 — Dual P&L + Management Balance

Build:

- Couture P&L;
- merchandise/channel P&L;
- common-cost allocation;
- consolidated P&L;
- management balance;
- AR/AP aging;
- WIP/inventory bridge;
- P&L -> cash bridge.

Metric formulas should be documented once and shared between calculations and BI.

## Phase 7 — D+10 Close Cockpit

Create close checklist:

- bank classification;
- sales completeness;
- COGS/WIP;
- payroll;
- tax;
- AP/AR;
- inventory adjustments;
- intercompany/internal transfers;
- owner flows;
- reconciliations;
- management sign-off.

Each task has owner, due date, evidence and status.

The cockpit is successful only after two consecutive closes within D+10.

## Phase 8 — Benefit Realisation Register

For every initiative:

- baseline;
- action;
- owner;
- expected effect;
- actual effect;
- evidence;
- one-off vs recurring;
- cash vs accounting vs avoided-cost effect;
- confidence/approval status.

Do not double-count the same effect across margin, inventory and cash initiatives.

## Phase 9 — BI / Semantic Layer

### Cube

Optional semantic layer for agreed metrics when multiple dashboards/consumers appear.

### Metabase

Use as a management viewing surface only after validated tables are stable.

Never allow manual BI edits to become source data.

## Phase 10 — Quality and orchestration

### Great Expectations

Use for reconciliation/data-quality suites where Pandera row/table validation is insufficient.

### dbt-core patterns

Use for transformation lineage/tests; actual adoption depends on chosen warehouse/database.

### Dagster

Adopt only when ingestion/transformation/close workflows need durable orchestration and retries.

### Airbyte

Defer until the number of live connectors justifies its operational weight.

## Cross-cutting acceptance

- every source load is versioned and hashable;
- every management metric has owner + formula + source;
- all corrections leave audit trail;
- plan/fact/scenario are not mixed;
- month close reproduces from source snapshots;
- benefit claims link to evidence;
- no dashboard bypasses canonical tables.

## Prohibited

Do not:

- automate before methodology freeze;
- use forecast ML for committed cash;
- treat account balance as free cash;
- mix prevented purchase with P&L savings;
- let Metabase/Cube become source of truth;
- silently overwrite historical snapshots;
- double-count realised benefits.

## Suggested issue order

1. YNN-INT-00 Methodology/data-contract freeze.
2. YNN-INT-01 Governed ingestion.
3. YNN-INT-02 13-week Cash Authority.
4. YNN-INT-03 Order Economics Ledger.
5. YNN-INT-04 WIP Digital Twin.
6. YNN-INT-05 Inventory/working-capital authority.
7. YNN-INT-06 Dual P&L/management balance.
8. YNN-INT-07 D+10 cockpit.
9. YNN-INT-08 Benefit Realisation Register.
10. YNN-INT-09 BI/semantic layer.
11. YNN-INT-10 Quality/orchestration scale gate.

**Implementation instruction:** Stage 2 is implementation and proof, not another diagnostic report.
