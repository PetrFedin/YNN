# Owner Action Pack — актуально H48/H49

Updated: 2026-07-28

**Источник правды по исполнению:** `live/marts/master_execution_board.csv` (H48)  
**Handoff:** `live/client_pack/36_STAGE1_HANDOFF_H49.md`  
**Decision log:** `live/marts/handoff_decision_log_blank.csv`

Не SoT. Чеклист решений.

---

## Wave A — сделать на этой неделе (параллельно)

### [P0] E01 — CONFIRM DOM-B2B
- Owner: **Янина**
- Кандидат: Коптева Марина
- Artifact: `raci_yanina_signoff_sheet.csv`
- Status: `WAITING_CONFIRM`
- Unlock: B2B collect 2.51M (E04)

### [P0] E02 — IM POS soft-slices
- Owner: **Сливяк** / Approver Мамушкина·Янина
- 2026-04: **509 351 ₽** · 2025-08: **37 328 ₽** (доля платежа)
- Artifact: `im_pos_slice_payments.csv`
- Status: `WAITING_ACCEPT`
- Unlock: Gate 18→20

### [P0] E03 — CONFIRM PRODUCT / COST / DATA
- Owner: **Янина**
- Кандидаты: Коновалова / Мокеева / Сливяк
- Status: `WAITING_CONFIRM`
- Unlock: alias (E05) + MD pilot (E09)

### [P0] E06 — ЗП янв–фев `#REF!`
- Owner: **Сливяк** · Release: Мамушкина
- Artifact: `payroll_quarantine_fix_checklist.csv`
- Status: `WAITING_FILE_FIX`
- Note: касса DDS↔bank уже CLOSE

---

## Wave B — после RACI / параллельно где можно

| ID | Что | Owner | Status |
|----|-----|-------|--------|
| E04 | B2B collect топ-3 | Коптева | BLOCKED_RACI ← E01 |
| E05 | Alias top-5 | Коновалова | BLOCKED_RACI ← E03 |
| E07 | IM overbank реестры ×4 | Сливяк | WAITING_FILES |
| E09 | MD salon 26 cost gaps 2026 | Мокеева | WAITING_OPS |
| E11 | RACI остаток SRC-CTRL | Янина | WAITING_CONFIRM |

---

## Wave C — gate → 30

| ID | Что | Unlock |
|----|-----|--------|
| E08 | BANK core−card + DDS June | →28 |
| E10 | TSUM Mercury May/Jun cash | →30 |
| E12 | Policy: no MD unit-econ 2024–25 | Stage-1 honesty |

---

## Историческое (H17) — закрыто

- A-RACI draft partial → H23/H27 (ещё 10 OPEN = E01/E03/E11)
- WHOLESALE_OK_LOSS / 0-3243 quarantine → H23 DONE
- Старый текст H17: см. git history; не использовать как актуальный чеклист
