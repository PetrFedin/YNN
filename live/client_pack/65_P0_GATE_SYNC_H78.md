# H78 — P0 gate sync (после H73–H77)

Updated: 2026-07-29 · **не SoT** · без auto-Accept

## Зачем (сейчас #1)
Data-ops P2 (H73–H77) закрыт. Узкое место — **owners**.  
Today Top5 / critical path / TAX tail ещё смотрели на старый «только 36k», без H76 perimeter.

## Что усилили
| Артефакт | Изменение |
|----------|-----------|
| `08_TODAY_TOP5_P0` | MEET → E02 → E08 → **TAX perimeter** → FILES |
| `13_GATE_CRITICAL_PATH` | шаг 26→27 = `14_TAX_SOFT` + `11_TAX_36K` |
| `12_GATE_TAIL` | первой строкой TAX perimeter |
| `15_GATE_UNLOCK_SIMULATION` | лестница 18→30 по сценариям |
| handoff / coverage | H73–H78 DONE; Tax = READY_FOR_SIGN |

## Симуляция (indicative)
```
18 →20 E02 →24 E07 →26 E08 →27 TAX →28 Feb →29 Mercury →30 June
```

## Gate
**18/30**. H78 score не двигает — снижает трение подписи.

## Артефакты
- `live/client_pack/65_P0_GATE_SYNC_H78.md` (этот файл)
- Sign: `15_GATE_UNLOCK_SIMULATION_H78.csv`
- Map: `live/maps/49_P0_GATE_SYNC_MAP.md`
- Builder: `live/registers/h78_p0_gate_sync/build_h78.py`
