# 21 — IM Overbank work orders

Источник: H53.  
CSV: `im_overbank_work_orders.csv` · `im_overbank_register_template.csv`

## Правило
OVERBANKED → **реестр**, не POS-slice.  
UNDERBANKED → soft-slice (H46/H51), отдельно.

## 4 WO
См. work orders CSV. Шаблон — одна строка-схема колонок для xlsx владельца.
