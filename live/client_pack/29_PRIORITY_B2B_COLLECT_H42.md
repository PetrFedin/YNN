# H42 — Приоритет: B2B collect 2.51M ₽

**Горизонт:** H42 · **дата:** 2026-07-28  
**Зачем:** после H39–H41 (путь gate → 30/30) следующий блок по деньгам — **открытая B2B-дебиторка 15 док. / 2.51M**.  
**Не делаем:** auto-link платежей; ACCEPT списания; назначение DOM-B2B без owners.

---

## Вердикт одной строкой

**82% долга = 3 покупателя**; **95% суммы старше 366 дней**; в банке почти нет «готовых» матчей — нужен **звонок/сбор + решение write-off**, а не новый ETL.

---

## Срез OPEN

| Метрика | Значение |
|---------|----------|
| Документов | 15 |
| Сумма | **2 514 023 ₽** |
| Топ-3 доля | **82.2%** (Бекеева 0.83M · Нурова 0.74M · Чухонцева 0.50M) |
| Age 366+ | **2.40M** (12 док.) |
| Age 0–90 | 10k (Раева — свежий) |
| Bank STRONG hypothesis | **1 док. / 0.22M** (Бекеева накл. 229) |
| Bank WEAK | ~0.66M |
| Без гипотезы в банке | **1.64M** (в т.ч. Нурова 0.74M) |
| RACI | DOM-B2B = **OPEN** (блокер исполнения) |

---

## Aging → политика

| Bucket | Док. | ₽ | Политика |
|--------|------|---|----------|
| 0–90 | 1 | 10k | мягкий collect |
| 91–180 | 0 | 0 | — |
| 181–365 | 2 | 104k | претензия |
| **366+** | **12** | **2.40M** | **collect vs списание — только owner** |

Heuristic recovery (диагностика, не прогноз): ~**0.45M** при возрастных коэффициентах. Реалистичный рычаг — топ-3.

---

## Bank hypotheses (не Accept)

Строгий фильтр: фамилия в counterpart/purpose + дата ≥ sale−7д + band суммы.

| Уровень | Что | Действие |
|---------|-----|----------|
| STRONG (~0.22M) | Бекеева / накл. 229 ↔ платёж ~243k | Owner: confirm link **или** reject |
| WEAK (~0.66M) | частичные / широкие ratio | Сначала звонок, потом сверка |
| NONE (~1.64M) | Нурова и др. | Collect / претензия / write-off |

Автолинк **запрещён** (`do_not_auto_accept=YES`).

---

## Owner actions

1. **H42-A1** — назначить ФИО DOM-B2B (RACI). Без этого pack не исполняется.  
2. **H42-A2** — обзвонить топ-3 (SLA 5 дней) по `b2b_call_script.csv`.  
3. **H42-A3** — подтвердить/отклонить STRONG hypotheses.  
4. **H42-A4** — по 366+ без bank hit — решение collect vs write-off.  
5. **H42-A5** — Раева 10k — мягкий collect (не путать с одноимённым платежом 2025).

---

## Симуляция

| Сценарий | Эффект |
|----------|--------|
| S1 confirm STRONG | ~0.22M «закрытие» без нового платежа (если верно) |
| S2 топ-3 @40% heuristic | ~0.83M recover |
| S3 age heuristic full | ~0.45M |
| S4 write-off residual 366+ | только после Accept владельца |

---

## Артефакты

| Файл | Содержание |
|------|------------|
| `live/marts/b2b_open_enriched_aging.csv` | 15 док. + age/tier/next_step |
| `live/marts/b2b_buyer_concentration.csv` | концентрация |
| `live/marts/b2b_call_script.csv` | скрипты звонка |
| `live/marts/b2b_bank_hypotheses_best.csv` | лучшие гипотезы |
| `live/marts/b2b_bank_hypotheses.csv` | полный пул |
| `live/marts/b2b_aging_summary.csv` | buckets |
| `live/marts/b2b_recovery_simulation.csv` | S0–S4 |
| `live/marts/b2b_collect_owner_actions.csv` | 5 действий |
| `live/registers/h42_b2b_collect/` | регистр |
| `live/evidence/h42_b2b_collect_20260728/` | evidence |

Связь с H37: `dojim_B2B_collect_pack.csv` — этот блок **операционализирует** его (aging + банк + call).

---

## Оценка

**9.3/10** для post-gate приоритета: прямой cash impact, концентрация на 3 звонках, честный разрыв bank vs docs, без фейкового ACCEPT.  
Связи: settle H12 ↔ bank W1; RACI DOM-B2B; горизонтально не трогает gate score (H39–H41).

---

## Следующий блок

**RACI 10 OPEN FIO** (разблокирует DOM-B2B и остальные owners) — или quarantine ЗП янв–фев 2026.
