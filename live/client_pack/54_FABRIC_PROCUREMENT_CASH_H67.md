# H67 — Fabric / procurement cash ABC (G6 WC)

Updated: 2026-07-29 · indicative · **не SoT** · без company P&L

## Зачем (приоритет после H66)
Контур коллекций/SKU дожат до owners. Следующий капитал — **ткани**:  
остатки ~**29,837,656** ₽ (H64) должны стыковаться с **оплатами поставщикам** и статьёй расходов «ткани», иначе WC неуправляем.

## Результаты
| Метрика | Значение |
|---------|----------|
| Список закупок | **63** |
| С bank edge | **30** |
| List-only (нет в банке) | **15** |
| Foreign / без ИНН | **18** |
| Bank fabric-like | **9,233,486** ₽ / 22 поставщиков |
| Expense «ткани*» | **14,194,396** ₽ |
| Inventory A-band | **23,869,121** ₽ |

### Важно
- Delta expense vs bank **не ошибка** — разные контуры (класс Расходов ≠ purpose выписки).
- Foreign (Errepi, Maritex…) **ожидаемо** без РФ bank edge.
- Не смешивать с goods stock / company P&L.

## Артефакты
- Wave B: `26–30_*`
- Marts: `fabric_supplier_bank_abc.csv`, `procurement_bank_coverage.csv`, `fabric_cash_bridge_metrics.csv`
- Map: `live/maps/38_FABRIC_PROCUREMENT_CASH_MAP.md`
- Builder: `live/registers/h67_fabric_procurement_cash/build_h67.py`

## Gate
**18/30**. H67 усиливает ops/WC, не gate score.
