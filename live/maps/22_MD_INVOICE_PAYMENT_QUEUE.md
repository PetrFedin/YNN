# 22 — MD invoice payment-level queue

Источник: H53 (надстройка над Layer 5 surname links).  
CSV: `md_invoice_payment_match_queue.csv` · `md_invoice_payment_match_rules.csv`

## Зачем
Surname MED ≈40% / 15.6M — недостаточно для reconcile.  
Очередь ранжирует 13 фамилий; правила R1–R6 задают, когда link сильный.

## Политика
Авто-Accept запрещён. STRONG_LINK → human batch confirm (D-MD-INV-01).
