# G9 — Группа «Договоры / проект / RACI»

Updated: 2026-07-29 (H82 bridge)  
Серия: …G8 → **G9** (финал серии групп)  
Файлов: **4** (+ штатка как roster evidence в H82)  
CSV: `group_G9_contracts_raci_files.csv` · bridge: `69_CONTRACTS_RACI_SHTATKA_H82.md`  
Статус: governance · задаёт **границы этапа и owners**, не финансовый SoT

---

## 1. Зачем эта группа

Это не «ещё Excel с цифрами», а **рамка работы**:

- что заказано (договор диагностики);  
- конфиденциальность (NDA);  
- план работ;  
- кто за какой домен отвечает (RACI / «Финансы и платежи»).

**Главный вопрос:** можно ли принимать решения по G1–G8 с понятными owners и без обещаний вне scope.

---

## 2. Карта группы — что лежит

| Файл | Роль |
|------|------|
| Договор комплексной диагностики ИП Янина + паспорт | Scope Stage 1 |
| NDA ИП Янина + паспорт | Конфиденциальность |
| план работы.docx | Календарь/этапы |
| Финансы и платежи.docx | RACI-контур финансов |

### Поток

```text
 Договор + план ──► границы Stage 1 / что НЕ обещаем
 NDA ─────────────► режим данных
 RACI ────────────► ACCEPT owners (H23) + OPEN роли
        │
        └─► политики SoT (exceptions, quarantine, staging)
```

---

## 3. Детализация — что зафиксировано

### 3.1. RACI ACCEPT (H23, 2026-07-24)

| Domain / control | Owner | Статус |
|------------------|-------|--------|
| Cash / Treasury | Мамушкина Елена | ACCEPT |
| Bank perimeter | Сливяк Галина | ACCEPT |
| Bank Approver | Мамушкина Елена | ACCEPT |
| Tax | Сливяк Галина | ACCEPT |
| Tax Approver | Янина Ю.Ф. | ACCEPT |
| Payroll | Сливяк Галина | ACCEPT |

**Ещё OPEN (нужны ФИО):** Product, Cost, Production, B2B, Data steward + ряд Approver/Owner SRC-CTRL-01…03.

Итог H23: **8 named ACCEPT · 10 OPEN_NEEDS_OWNER** — domain-owned staging, не audited SoT.

### 3.2. Политики данных (accepted)

1. B2B below-cost `WHOLESALE_OK_LOSS` (0-2493A/2496/2497) — в reported margin; clean исключает.  
2. SKU `0-3243` — quarantine identity.  
3. Release gate — operational PROVISIONAL.  
4. W1–W6 + marts — controlled staging с named owners.

### 3.3. Связь с серией G1–G8

| Группа | Owner-якорь из RACI / практики |
|--------|--------------------------------|
| G1 Банк | Сливяк / Мамушкина |
| G2 ДДС | Сливяк |
| G3 Каналы / B2B | B2B Owner — **OPEN** |
| G4 Cost / МД | Cost/Prod Owner — **OPEN** |
| G5 Product / alias | Product Owner — **OPEN** (кандидат Коновалова в H27) |
| G6 Ткани | Prod/закупки — OPEN |
| G7 ЗП | Сливяк |
| G8 Налоги | Сливяк / Approver Янина |

---

## 4. Анализ ведения бизнеса (по G9)

### 4.1. Сильное
1. Есть юридическая и RACI-рамка этапа.  
2. Критичные money-домены (cash/bank/tax/payroll) уже с ФИО.  
3. Политики exceptions зафиксированы — меньше споров «чья цифра».

### 4.2. Слабое
1. Product/Cost/B2B/Data без ACCEPT → тормозит alias, cost versions, collect B2B.  
2. Путаница «staging = SoT» у стейкхолдеров.  
3. План работы нужно сверять с фактическим execution pack (не перечитывать как новый scope).

---

## 5. DONE / TODO / BLOCKED

| Статус | Пункт |
|--------|-------|
| **DONE** | Inventory 4 файла |
| **DONE** | RACI ACCEPT map + OPEN list |
| **DONE** | SoT policy exceptions |
| **TODO** | Назначить 10 OPEN owners |
| **TODO** | Product Accept alias (G5) после назначения |
| **НЕ ДЕЛАТЬ** | Расширять Stage 1 за договор; объявлять marts аудированным SoT |

---

## 6. Выводы по G9

1. Серия G1–G8 **управляема**, потому что money-домены имеют owners.  
2. Главный governance-долг — **OPEN Product/Cost/B2B/Data**.  
3. G9 закрывает вопрос «кто отвечает», не «какая прибыль компании».

---

## 7. Мини-план (G9)

| # | Действие | Owner | Эффект |
|---|----------|-------|--------|
| 1 | Закрыть 10 OPEN RACI строк ФИО | Янина | Разблокировка Accept |
| 2 | Явно держать: staging ≠ SoT | Все | Честные решения |
| 3 | Product Owner → alias Accept (G5) | Янина | Чистый cost |
| 4 | B2B Owner → collect 2.51M (G3) | Янина | Касса опта |
| 5 | Сверить план работы с execution pack | Сливяк | Один roadmap |

---

## 8. Серия групп — итог

| Код | Группа | Статус |
|-----|--------|--------|
| G1 | Банк | DONE |
| G2 | ДДС / opex / SALES | DONE |
| G3 | Продажи IM/B2B/ЦУМ | DONE |
| G4 | Себестоимость + МД | DONE |
| G5 | Номенклатура / коллекции | DONE |
| G6 | Ткани / склады / закупки | DONE |
| G7 | Персонал / ЗП | DONE |
| G8 | Налоги PDF | DONE |
| **G9** | Договоры / RACI | **DONE** |

**Серия детальных групп G1–G9 завершена.** Дальше — точечный дожим (collect, alias Accept, tax extract, OPEN RACI), не новые «слои ради слоёв».
