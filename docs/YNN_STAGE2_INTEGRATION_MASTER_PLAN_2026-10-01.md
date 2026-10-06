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

## Additional wave — management-data lineage and reproducible close snapshots

### OpenLineage event model — ADOPT/CONDITIONAL

Reference: https://github.com/OpenLineage/OpenLineage

When Stage 2 pipelines move from a handful of manually managed files to recurring ingestion/transformation jobs, emit lineage events for:

`source extract -> immutable landing -> validated staging -> management table -> close snapshot -> dashboard/report`

Each lineage event should identify:

- source dataset/version/hash;
- job/run;
- output dataset;
- period/as-of date;
- code/config version;
- success/failure.

OpenLineage is metadata about the pipeline, not the financial source of truth.

### Marquez lineage UI — DEFER/ADAPT

Reference: https://github.com/MarquezProject/marquez

Use only when visual lineage becomes operationally useful to finance/analytics engineering.

Marquez can display OpenLineage runs/datasets, but it must not become the place where business users edit classifications, order economics or cash commitments.

For the first Stage 2 pilot, a simpler lineage ledger may be enough.

### Apache Arrow / Parquet close snapshots — ADOPT

Reference: https://github.com/apache/arrow

Create immutable columnar snapshot packs for major management-close datasets:

- classified cash transactions;
- AR/AP aging;
- open WIP;
- inventory/working capital;
- order economics;
- dual P&L bridge;
- benefit register.

Each snapshot pack includes:

- period/as-of;
- schema version;
- source hashes;
- row counts/totals;
- code/version;
- generated_at;
- manifest checksum.

This makes D+10 close and later re-performance reproducible without depending on a mutable BI dashboard.

### Management evidence pack

For every completed close, produce a manifest linking:

`input source hashes -> validated snapshot IDs -> reconciliation results -> management outputs -> sign-off status`

The manifest is evidence and reproducibility metadata. It must not replace the underlying source tables/files.

### Acceptance extension

- a prior close can be reproduced from retained inputs + code/schema version;
- lineage explains exactly which source contributed to each management dataset;
- changing a source after close creates a new version rather than silently altering history;
- Arrow/Parquet exports reconcile to authoritative management totals.

**Sequencing:** snapshot packs can start with the first stable close; OpenLineage is added once recurring jobs exist; Marquez only when the lineage graph is large enough to justify a dedicated UI.

## Additional wave — receivables control, variance bridge and management action register

This wave turns the Stage 2 management model into a weekly decision cadence around cash collection, forecast variance and accountable actions.

### Receivables Collection Authority — ADOPT

Create an operational AR collection register linked to invoices/orders/customers:

- debtor/customer;
- invoice/order;
- original amount;
- outstanding amount;
- contractual due date;
- expected receipt date;
- collection status;
- dispute/hold reason;
- owner;
- last contact;
- next action/date;
- promise-to-pay amount/date;
- evidence/reference.

The 13-week Cash Authority consumes the approved expected receipt, not a generic accounting due date.

A promise-to-pay is a forecast input with its own confidence/status; it is not cash until received.

### Payables Commitment Queue — ADOPT

Strengthen purchase/AP control by separating:

- unavoidable/contractual;
- production-critical;
- tax/payroll;
- supplier relationship;
- discretionary/postponable.

Each commitment stores due date, amount, vendor, linked purchase/WIP/order, criticality, deferability, consequence and approval.

13-week cash scenarios can then answer which payments are movable and which are not.

### Forecast-vs-Actual Variance Bridge — ADOPT

For each closed week/month, produce a deterministic bridge:

forecast closing cash -> timing variance -> volume/revenue variance -> margin/cost variance -> unplanned purchase -> collection slippage -> owner/tax/financing flows -> actual closing cash

Each material variance gets:

- amount;
- driver taxonomy;
- source rows;
- owner;
- controllable/uncontrollable flag;
- corrective action link.

Do not use a catch-all other bucket beyond a defined materiality threshold without review.

### Management Action Register — ADOPT

Create one owner-facing action register linked to diagnostics and management outputs:

- action;
- problem/opportunity;
- owner;
- due date;
- expected cash/P&L/WC effect;
- dependencies;
- status;
- evidence;
- realised effect link;
- decision/close note.

Flow:

variance/working-capital/order-economics insight -> management decision -> action -> evidence -> Benefit Realisation Register

This closes the current loop from analytics to execution.

### Stress / Downside Scenario Pack — ADOPT

Maintain explicit scenario assumptions rather than editing the base forecast:

- delayed receipts;
- lower sales;
- margin erosion;
- production delay/rework;
- FX/supplier-cost shock;
- tax/one-off payments;
- inventory liquidation/recovery.

Each scenario derives from the same authoritative base snapshot and stores assumption deltas + resulting liquidity runway/lowest cash point.

Do not blend downside assumptions into the base case without an approved scenario change.

### Additional acceptance

- AR expected receipts reconcile to open receivables and actual receipts;
- payment queue identifies source commitment and deferability;
- every material cash/P&L variance resolves to source rows and a driver;
- management actions have one owner and evidence of closure;
- realised benefits cannot be claimed without an action/evidence link;
- base/downside/upside scenarios remain separately versioned.

**Sequencing:** stable 13-week cash + AR/AP ingestion -> collection/payables registers -> variance bridge -> action register -> stress pack -> Benefit Realisation feedback loop.

## Additional wave — finite-capacity production planning and promise-date simulation

This wave turns the WIP Digital Twin into a decision tool for couture/atelier delivery commitments.

### Finite-capacity scheduling engine — ADAPT

Reference: https://github.com/google/or-tools

Use OR-Tools as a **scenario solver**, not the production authority.

Inputs come from YNN authoritative tables:

- open orders;
- operation/stage sequence;
- estimated remaining effort;
- required skill/resource;
- staff/resource calendars;
- fitting/customer dependencies;
- material readiness;
- fixed deadlines;
- urgency/priority;
- rework;
- external-work lead times.

Output proposals:

- feasible start/finish per operation;
- bottleneck load;
- lateness risk;
- idle/waiting time;
- alternative resource assignment;
- impact of a rush order/new order;
- next feasible promise date.

Planner/production manager approves the selected scenario before it becomes the operating plan.

### Capacity Calendar Authority — ADOPT

Build a native weekly capacity table:

- resource/person/team;
- skill;
- available hours;
- leave/absence;
- non-order work;
- fitting/sample time;
- committed production time;
- remaining capacity.

Do not infer 100% productive capacity from payroll hours.

### Promise-date Simulator — ADOPT

When a new couture order or deadline change is considered:

current committed plan + new demand -> solver scenario -> earliest feasible completion + affected orders + bottleneck/cash impact

Display at least:

- feasible/at-risk;
- earliest realistic date;
- orders displaced;
- incremental overtime/external-work assumption;
- WIP/cash-to-complete consequence.

The simulator proposes a commercial promise; the final customer commitment remains a human decision.

### Schedule-vs-Actual Learning Loop — ADOPT

After each week/order:

- planned operation duration;
- actual duration;
- waiting/material delay;
- rework;
- fitting/customer delay;
- external supplier delay.

Use this history to update planning assumptions deliberately.

Do not allow automatic model adjustment to rewrite historical plans or approved customer commitments.

### Additional acceptance

- solver inputs reconcile to WIP/capacity authoritative records;
- every proposed schedule stores input snapshot + solver config/version;
- manual override is explicit and reasoned;
- promise-date output shows displaced work/bottleneck consequences;
- actual-vs-plan feedback updates future assumptions without rewriting history.

**Sequencing:** WIP Digital Twin + capacity data first -> OR-Tools scenario engine -> promise-date simulator -> weekly actual-learning loop.

**Dependency note:** OR-Tools is a solver component; it must remain replaceable and cannot write YNN authoritative schedules directly.

## Additional wave — process mining of couture flow and delay causes

This wave uses the Stage 2 event history to diagnose where real orders spend time, wait or rework rather than relying on anecdotal impressions.

### Process Event Log Authority — ADOPT

Create a normalized event-log projection from existing operational facts.

Event examples:

- order created;
- design/spec approved;
- material ordered/received;
- work stage started/completed;
- fitting scheduled/held;
- rework opened/closed;
- external work sent/returned;
- customer change;
- final acceptance;
- payment milestone;
- order completed.

Every event stores:

- order/case ID;
- activity;
- timestamp;
- actor/resource where appropriate;
- source table/record;
- stage/version;
- event provenance.

The projection is derived from authoritative Stage 2 tables; it is not a second operational workflow database.

### PM4Py offline analysis — CONDITIONAL / ANALYTICAL SIDECAR

Reference:

https://github.com/process-intelligence-solutions/pm4py

Use PM4Py for bounded analytical studies such as:

- discovered process variants;
- throughput time;
- waiting time;
- rework loops;
- bottleneck transitions;
- conformance against the agreed couture process;
- comparison by complexity/urgency/order type.

Because the verified upstream repository is AGPL-3.0, treat PM4Py as a separate analysis environment/tool unless licensing review approves another mode.

### Planned-vs-Actual Process Conformance — ADOPT

Compare actual event sequences with the intended operating model.

Flag examples:

- stage skipped;
- fitting added unexpectedly;
- material ordered after work should have started;
- repeated rework loop;
- long waiting state;
- customer change after design freeze.

A conformance deviation is a diagnostic signal, not automatically an employee/process failure.

### Delay Cause Taxonomy — ADOPT

Link waiting/rework segments to explicit causes:

- material;
- customer;
- internal capacity;
- quality/rework;
- external contractor;
- approval;
- unclear specification;
- scheduling;
- other reviewed reason.

This allows the process-mining output to feed the existing Management Action Register.

### Process Improvement Evidence — ADOPT

For a change initiative, compare before/after cohorts using:

- median/percentile throughput;
- waiting share;
- rework count;
- schedule adherence;
- contribution per bottleneck hour.

Do not claim causal effect without considering mix/season/complexity changes.

### Additional acceptance

- every process event resolves to an authoritative source row;
- process mining can be reproduced from an exact event-log snapshot;
- AGPL tool remains operationally isolated unless explicitly approved;
- discovered variants never overwrite process/status authority;
- improvement claims link to period/cohort/methodology;
- findings can create Management Actions but not silently reconfigure operations.

**Sequencing:** stable order/WIP event capture -> normalized process log -> descriptive throughput analysis -> conformance/rework studies -> management actions.



## Additional wave — Transformation Evidence and Value Realization Operating System

This wave keeps YNN in its correct role: not a generic SaaS marketplace, but the evidence and governance layer that proves whether Stage 2 changes actually improved economics and operating performance.

### Intervention Registry — ADOPT

Every approved transformation action should carry:

- intervention ID;
- problem/hypothesis;
- owner;
- baseline period;
- target metric(s);
- expected mechanism;
- required operational change;
- start/end dates;
- evidence sources;
- confounders/assumptions;
- decision state.

### Baseline Freeze — ADOPT

Before an intervention starts, freeze a reproducible baseline snapshot over the agreed period.

The baseline contains:

- exact source references;
- data cut-off;
- formulas;
- exclusions;
- metric definitions;
- known data-quality limitations.

No later data cleanup may silently rewrite the original baseline.

### Value Realization Ledger — ADOPT

Track:

`diagnosed leakage -> approved intervention -> executed change -> measured operating effect -> financial bridge -> realized / not realized / uncertain`

Value states:

- proposed;
- modelled;
- approved;
- in execution;
- observed operational effect;
- financially realized;
- rejected / not proven.

### Counterfactual / Comparison Discipline — ADOPT

Where feasible, compare:

- before vs after;
- comparable cohorts;
- plan vs actual;
- untreated/less-affected group;
- normalized season/mix view.

Do not claim causality from simple before/after movement when mix, seasonality or pricing changed materially.

### Evidence Pack per Initiative — ADOPT

Generate a durable pack containing:

- baseline;
- intervention;
- implementation evidence;
- post-period metrics;
- methodology;
- financial bridge;
- unresolved caveats;
- management decision;
- next action.

### Transformation Portfolio — ADOPT

Owner/board view:

- initiatives by domain;
- capital/time invested;
- realized benefit;
- forecast benefit;
- blocked initiatives;
- confidence/evidence level;
- payback;
- responsible owner.

### Stage 2 Acceptance Gate — ADOPT

An initiative is not "done" because a process or dashboard was implemented.

Closure requires explicit state:

- operationally implemented;
- evidence complete;
- effect measured;
- financial impact classified;
- owner accepted;
- sustainment control assigned.

### Reusable Diagnostic-to-Execution Method — ADOPT

Formalize the YNN method itself as a versioned internal standard:

`diagnose -> quantify -> design -> implement -> measure -> reconcile -> sustain`

This is process IP and can be reused in future transformation engagements without turning YNN into an unrelated software platform.

### Controlled Export to Operating Systems — ADOPT

YNN may consume or receive approved evidence from operating systems such as yanina-management, but:

- YNN does not become production authority;
- source record identity is preserved;
- imported metrics are versioned;
- reconciliation exceptions remain visible.

### Additional acceptance

- realized value always resolves to source evidence;
- baseline snapshots are immutable;
- forecast savings never equal realized savings automatically;
- intervention closure requires measured outcome or explicit "not proven";
- methodology changes are versioned;
- source operational systems remain authoritative.

**Sequencing:** stable Stage 2 operational data -> intervention registry -> baseline freeze -> value ledger -> evidence packs -> portfolio view -> reusable method.

**Moat:** YNN's defensibility is the accumulated transformation evidence linking management decisions to verified operational and financial outcomes.
