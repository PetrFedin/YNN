# 08 — Единый алгоритм всего, что есть

Updated: 2026-07-27

Это операционный алгоритм чтения и развития системы YANINA / YNN — от сырого файла до решения.

---

## Алгоритм A — Чтение любого вопроса («что происходит?»)

```
1. Классифицируй вопрос
   ├─ Деньги / касса          → P05 + BANK/CASH
   ├─ Выручка канала          → P01–P04 + channel mart
   ├─ Маржа товара            → P02–P04 + margin_* (не MD)
   ├─ ФОТ / налог / opex      → P06/P07/P10
   ├─ Запасы                  → P09
   └─ Качество месяца         → Gate (05)

2. Возьми SoT-контур (не файл)
   документ → регистр волны → mart → control

3. Проверь gate / control % за период
   RELEASED → можно цитировать как факт
   BLOCKED  → только с оговоркой + причина fail

4. Раздели контуры
   МД ≠ goods; TSUM reported ≠ product; Decor ≠ operating 2026+

5. Ответ = число + источник + статус ACCEPT/OPEN
```

---

## Алгоритм B — Добавление / изменение данных

```
1. Файл в L0 (Downloads) → каталог L1 (hash, domain, risk)
2. Определи волну W1–W6 и регистр
3. Extract → register (не в mart напрямую)
4. Spine keys (INN/sku/period/doc)
5. Rebuild затронутые marts
6. Пересчёт controls + gate
7. Если меняет RACI/SoT → только через ACCEPT owner
8. Не ingest повторно то, что forensic закрыл (Salon Sber)
```

---

## Алгоритм C — Решение по оптимизации (S1→S4)

```
S1 Дисциплина (сначала)
   B2B open → collect
   Gate IM/BANK fails → process fix
   FX policy → зафиксировать
   Результат: 1–2.5M one-time + чище месяцы

S2 Рост МД-процесса (после фактов S1)
   WIP / остатки заказов (если появятся)
   Cycle time / предоплата discipline
   Результат: гипотеза 5–12M/год — требует данных

S3 Условия / costs
   TSUM dual → переговоры с фактом product GM
   Ткани ABC → высвобождение капитала
   Результат: гипотеза 10–16M/год

S4 Структура (только после S1–S3)
   Decor / channel mix / LE
   Стресс 5–10M vs upside 15–25M
   Gate: нельзя без board + SoT
```

---

## Алгоритм D — Ежемесячный close (операционный)

```
День 1–3:  bank extract + DDS + sales контуры
День 3–5:  payroll / opex / tax cash
День 5–7:  rebuild marts + controls
День 7:    Release Gate
           ├─ RELEASED → пакет в Live Control / client
           └─ BLOCKED  → ticket owner по fail control
День 7+:   только OPEN_MODEL / data requests, не «дорисовать» SoT
```

---

## Алгоритм E — Карты ↔ артефакты (навигация)

| Нужно | Открыть |
|-------|---------|
| Процесс | `01_PROCESS_MAP` |
| Что в файлах | `02_DOCUMENT_DATA_MAP` |
| Архитектура | `03_DATA_LAYER_MAP` |
| Кто/канал | `04_ENTITY_CHANNEL_MAP` |
| Качество | `05_CONTROL_MAP` |
| Где деньги | `06_VALUE_STREAM_MAP` |
| Связи всё↔всё | `07_CROSSWALK_MATRIX` |
| Проблемы | `09_PROBLEMS_PLUS_MINUS` |
| Клиенту Stage 1 | `live/client_pack/` |
| Сценарии ₽ | `OPTIMIZATION_SCENARIOS` |

---

## Инвариант (нельзя нарушать)

1. Domain-owned staging ≠ audited SoT  
2. Не изобретать ACCEPT  
3. Не джойнить MD services в goods COGS  
4. Не выдавать goods bridge за P&L компании  
5. Dual TSUM всегда рядом с reported GM
