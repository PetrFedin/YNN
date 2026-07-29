# NOW — Command Center YANINA / YNN

**Обновлено:** 2026-07-29 (H56)  
**Вердикт:** Stage 1 диагностика и пакеты исполнения **готовы**. Сдвиг метрик = только owners (подписи / файлы / звонки).

---

## Сделать сегодня (P0)

1. Открыть и провести **15 мин подписи** → [`live/client_pack/sign_session_pack/00_SIGN_SESSION_15MIN.md`](live/client_pack/sign_session_pack/00_SIGN_SESSION_15MIN.md)  
2. Разослать пинги → [`…/02_OWNER_PING_MESSAGES.csv`](live/client_pack/sign_session_pack/02_OWNER_PING_MESSAGES.csv)  
3. Держать запреты: не весь POS→IM · не POS в OVERBANK · не goods −58/−74% как P&L компании  

Недельная карта: [`live/marts/weekly_ops_card.csv`](live/marts/weekly_ops_card.csv)

---

## Gate path

```
18 ──soft-slice──► 20 ──overbank regs──► 24 ──BANK/DDS──► 28 ──TSUM──► 30
```

Сейчас: **18/30**. Без E02 остаёмся здесь.

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
