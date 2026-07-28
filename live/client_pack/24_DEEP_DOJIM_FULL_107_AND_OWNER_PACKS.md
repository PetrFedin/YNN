# 24 — Deep Dojim: полный разбор 107 файлов + пакеты дожима

Updated: 2026-07-28  
Код: **H37** · evidence: `live/evidence/h37_deep_dojim_20260728/`  
Статус: indicative · **не SoT** · **без auto-ACCEPT**

---

## 0. Вердикт

Все **107** файлов каталога **открыты и структуро-просканированы** (страницы PDF / листы Excel / docx).  
Суммы налогов дожаты там, где PDF даёт устойчивые коды строк (**14 HIGH**).  
Операционный дожим (collect B2B, Accept alias, ФИО RACI) **подготовлен пакетами** — исполнение только owners.

Честно: «прочитать глазами каждую букву 1300+ налоговых страниц как аудитор» ≠ то же, что **индекс всех страниц + extract ключевых полей**. Сделано второе end-to-end + точечный HIGH extract. Где коды форм конфликтуют (РСВ) — **LOW**, не выдаём за факт.

---

## 1. Что сделано технически (можно без owners)

| Блок | Результат |
|------|-----------|
| Deep scan 107 | `file_deep_scan_107.csv` — 0 FAIL |
| PDF index | **1326** страниц · 17 emptyish · `pdf_pages_index.csv` |
| Excel sheets | **293** листа xlsx (+ xls/misnamed) · `xlsx_sheets_inventory.csv` |
| Crosswalk файл→группа→marts | `file_crosswalk_marts.csv` |
| Tax extract confident | `tax_pdf_extract_confident.csv` → obligations обновлены |
| Дожим-пакеты | B2B / IM / Alias / RACI / Quarantine CSV |

### 1.1. Статус скана

| scan_status | n | Смысл |
|-------------|--:|-------|
| XLSX_OK | 68 | Все листы прочитаны |
| PDF_OK | 29 | Все страницы проиндексированы (chars/page) |
| DOCX_OK | 5 | Zip/document.xml |
| XLS_AS_XLSX_OK | 3 | StatementFull: OOXML с расширением .xls |
| XLS_OK | 1 | Справочник номенклатуры |
| DOC_LEGACY | 1 | Положение об ОТ (.doc) — бинарный legacy |

**StatementFull (3):** файл открывается, но лист `Report` фактически пустой (max_row=1) — банк уже в W1 из других выписок VTB/Sber; эти три — оболочка/выгрузка без табличных строк.

### 1.2. Глубина анализа по файлам

| analysis_depth | n |
|----------------|--:|
| FULL_STRUCT | 82 |
| FULL_STRUCT+AMOUNTS_HIGH | **14** |
| FULL_STRUCT+AMOUNTS_LOW | 5 (РСВ) |
| FULL_STRUCT_NO_AMOUNTS | 5 (ЕНС/списки/справки) |
| PARTIAL_LEGACY | 1 |

### 1.3. По группам G1–G9 (единицы = страницы или листы)

| Group | Файлов | Pages/sheets |
|-------|-------:|-------------:|
| G1 Банк | 12 | 200 |
| G2 ДДС/opex | 9 | 66 |
| G3 Каналы | 8 | 12 |
| G4 Cost/МД | 6 | 22 |
| G5 Номенклатура | 13 | 28 |
| G6 Ткани/склады | 5 | 5 |
| G7 ЗП | 25 | 156 |
| G8 Налоги | 25 | **1134** |
| G9 Договоры/RACI | 4 | docx |

Все 107 входят в G1–G9 (сумма групп = 107; `Движение товаров с себестоимостью` учтён в G6, связан с G4).

---

## 2. Tax dojim — суммы

### 2.1. HIGH confidence (использовать как якорь periметра)

#### 6-НДФЛ — стр.020 «к перечислению с начала периода»
| LE / год | ₽ |
|----------|--:|
| Декор 2024 | 1 445 469 |
| ИП 2024 | 1 426 959 |
| Декор 2025 | 1 863 059 |
| ИП 2025 | **2 202 651** (дубль файла (1) совпадает) |

#### УСН — налог к доплате за год (код 100)
| LE / год | Доход (113) | К доплате (100) |
|----------|------------:|----------------:|
| Декор 2024 | 15.3M | 117 389 |
| ИП 2024 | 134.5M | 993 121 |
| Декор 2025 | 20.6M | 191 261 |
| ИП 2025 | 125.1M | 1 390 632 |

#### НДС — код 040 (часто «к возмещению»; не путать с 030 «к уплате»)
| Период | ₽ (040) |
|--------|--------:|
| 2025 Q1 | 998 748 |
| 2025 Q2 | 1 602 606 |
| 2025 Q3 | 1 334 790 |
| 2025 Q4 | 2 163 237 |
| 2026 Q1 | 1 443 002 |

**Важно:** по ИП в выборке primary = **040**, не 030. Для налоговых решений сверять с бухгалтером; для Stage 1 — фиксируем extract, не консультацию.

### 2.2. LOW / без сумм
- РСВ: коды конфликтуют между разделами → **LOW**, только lead.  
- ЕНС / списки отчётности / справки: текст есть, устойчивых line-codes нет.

Касса налогов по-прежнему: recon CLOSE (~15.5M/18.5M/11.4M по годам) — это сильнее, чем PDF-парсинг для контроля платежей.

---

## 3. Пакеты дожима для owners (не сделает скрипт)

| Пакет | CSV | n | Кто | Что нужно |
|-------|-----|--:|-----|-----------|
| **B2B collect** | `dojim_B2B_collect_pack.csv` | 15 / **2.51M** | DOM-B2B (**OPEN**) | Collect / списание / решение |
| **IM OPEN** | `dojim_IM_open_pack.csv` | 6 мес. | Сливяк / Мамушкина | Реестры эквайринга или ACCEPT ACQ_POS |
| **Alias review** | `dojim_ALIAS_review_pack.csv` | 20 SKU | DOM-PRODUCT (**OPEN**) | Accept/Reject · `applied_to_sales` пока N |
| **RACI OPEN** | `dojim_RACI_open_pack.csv` | 10 ролей | Янина | Назначить ФИО |
| **Quarantine** | `dojim_QUARANTINE_files_pack.csv` | 5 | Сливяк / учёт | Исправить до использования |

### 3.1. Чего нельзя «дожать» кодом (и не обещаем)

| Тема | Почему BLOCKED |
|------|----------------|
| Unit-econ МД 2024–25 | cost_amount = 0% |
| Фурнитура / WIP МД | нет в учёте |
| Audited company P&L | методологический запрет Stage 1 |
| Договорной % ЦУМ | нет ставки в periметре |
| ABC тканей SoT | leaf units ambiguous |
| Auto-ACCEPT alias/RACI | только человек |

---

## 4. Сопоставление (как сгруппировано)

```text
107 файлов
  ├─ G1…G9 detail MD (уже на GitHub)
  ├─ file_deep_scan_107          ← структура каждого файла
  ├─ pdf_pages_index / xlsx_sheets_inventory
  ├─ file_crosswalk_marts        ← файл → marts/recon
  ├─ tax_pdf_extract_confident   ← суммы HIGH/LOW
  └─ dojim_*_pack                ← очередь owners
         ↓
   marts + controls + gate (18/30)
```

Горизонтальные связи (без ломки):
- G8 tax amounts ↔ G1 bank tax-like ↔ recon_tax_cash  
- G7 quarantine ↔ G7 recon CLOSE через DDS/bank  
- G5 alias pack ↔ G4 cost identity (не auto-apply)  
- G3 B2B/IM packs ↔ G1 касса / gate  

---

## 5. Файлы артефактов

**Client pack / maps**
- `24_DEEP_DOJIM_FULL_107_AND_OWNER_PACKS.md` (этот файл)
- `file_deep_scan_107.csv`
- `file_crosswalk_marts.csv`
- `tax_pdf_extract_confident.csv`
- `xlsx_sheets_inventory.csv` · `pdf_pages_index.csv`
- `dojim_B2B_collect_pack.csv` · `dojim_IM_open_pack.csv`
- `dojim_ALIAS_review_pack.csv` · `dojim_RACI_open_pack.csv`
- `dojim_QUARANTINE_files_pack.csv`

**Registers:** `live/registers/h37_deep_dojim/`  
**Evidence:** `live/evidence/h37_deep_dojim_20260728/`

---

## 6. Оценка дожима (честная)

| Функция | Оценка | Почему |
|---------|-------:|--------|
| Полный structural scan 107 | **9.5/10** | Все файлы, pages/sheets, 0 FAIL |
| Tax HIGH extract | **9/10** | 6-НДФЛ/УСН/НДС-040 устойчивы; не «весь PDF-аудит» |
| Owner dojim packs | **9/10** | Конкретные списки; ждут ФИО/файлы |
| Закрытие кассовых дыр кодом | **3/10** | Нужны люди/деньги/Accept — пакет готов |

---

## 7. Следующий шаг (один)

1. Янина назначает **10 OPEN RACI** (особенно B2B / Product / Cost / Data).  
2. Параллельно: collect B2B по `dojim_B2B_collect_pack.csv` + реестры на 6 IM OPEN.  
3. Product Accept по `dojim_ALIAS_review_pack.csv`.  

Без п.1–3 новый «анализ текста» снова упрётся в тот же потолок — данные уже разложены.
