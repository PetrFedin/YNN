# NOW — Command Center YANINA / YNN

**Обновлено:** 2026-07-29 (H56)  
**Вердикт:** Stage 1 диагностика и пакеты исполнения **готовы**. Сдвиг метрик = только owners (подписи / файлы / звонки).

---

## Сделать сегодня (P0)

1. Открыть и провести **15 мин подписи** → [`live/client_pack/sign_session_pack/00_SIGN_SESSION_15MIN.md`](live/client_pack/sign_session_pack/00_SIGN_SESSION_15MIN.md)  
2. Разослать пинги → [`…/02_OWNER_PING_MESSAGES.csv`](live/client_pack/sign_session_pack/02_OWNER_PING_MESSAGES.csv)  
3. Сливяк: заполнить channel shares в **prefill реестре** → [`execution_wave_a/12_im_overbank_register_prefill_all.csv`](live/client_pack/execution_wave_a/12_im_overbank_register_prefill_all.csv)  
4. Сливяк/Янина: card→DDS prefill **или** draft policy core−card → [`execution_wave_c/04_bank_card_dds_map_prefill.csv`](live/client_pack/execution_wave_c/04_bank_card_dds_map_prefill.csv)  
5. Держать запреты: не весь POS→IM · не POS в OVERBANK · не goods −58/−74% как P&L · **не** лить июньский POS в TSUM  

H59: Mercury за май **нет в банке** → [`46_ALIAS_TSUM_ZP_H59.md`](live/client_pack/46_ALIAS_TSUM_ZP_H59.md)  
H58/H57: prefill BANK/overbank · точка входа: этот файл + `weekly_ops_card.csv`

---

## Gate path

```
18 ──E02──► 20 ──E07──► 24 ──E08 card──► 26 ──TAX36k──► 27 ──Feb recon──► 28 ──Mercury──► 30
```

Сейчас: **18/30**. Детали: [`gate_critical_path_unified.csv`](live/marts/gate_critical_path_unified.csv)  
Board (актуальные файлы): [`master_execution_board.csv`](live/marts/master_execution_board.csv) · audit **12/12 READY**

H60: [`47_BOARD_SYNC_TAX_H60.md`](live/client_pack/47_BOARD_SYNC_TAX_H60.md)

---

## Пакеты по волнам

| Wave | Папка | Когда |
|------|-------|-------|
| **Sign** | [`sign_session_pack/`](live/client_pack/sign_session_pack/) | сегодня |
| **A** | [`execution_wave_a/`](live/client_pack/execution_wave_a/) | на подписи |
| **B** | [`execution_wave_b/`](live/client_pack/execution_wave_b/) | после E01/E03 |
| **C** | [`execution_wave_c/`](live/client_pack/execution_wave_c/) | файлы DDS/TSUM |

---

## Люди → первое действие

| Кто | Первое действие |
|-----|-----------------|
| Янина | E01 + E03 + FRAME (15 мин) |
| Сливяк | Soft-slice + реестр 2024-08 + DDS июнь |
| Мамушкина | Approver soft-slice / release ЗП |
| Коптева | 3 звонка B2B (после E01) |
| Коновалова | Alias топ-5 (после E03) |
| Мокеева | 26 salon cost |

Карточки: [`person_action_cards.csv`](live/marts/person_action_cards.csv)

---

## Не делать (анти-размытие)

См. [`stop_doing_list.csv`](live/marts/stop_doing_list.csv): новый forensic без файлов · auto-Accept · company P&L сейчас · UE МД 24–25 · BPMN/BI сейчас.

---

## Навигация

Полный индекс: [`command_center_nav.csv`](live/marts/command_center_nav.csv) · статус git: [`STATUS.md`](STATUS.md) · coverage: [`19_…`](live/client_pack/19_COVERAGE_DONE_VS_MISSING.md)

**H56:** [`live/client_pack/43_COMMAND_CENTER_H56.md`](live/client_pack/43_COMMAND_CENTER_H56.md)
