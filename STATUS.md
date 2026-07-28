# Статус YANINA / YNN

## GitHub
https://github.com/PetrFedin/YNN · `main`

## Приоритет сейчас: H41 Gate TSUM_NET
Документ: `live/client_pack/28_PRIORITY_GATE_TSUM_NET_H41.md`

### Ключевой find
OPEN 2026-05/06 = **лаг оплаты +1 мес** (29/29), не ошибка ставки. В июньской выписке **нет** платежа Меркурий (~2.58M за май).

### Quick path к gate
1. H39 IM → 24/30  
2. H40 BANK↔DDS → 28/30  
3. H41 платёж май + июль-выписка июнь → **30/30**  
   (alt: Accept TIMING_LAG policy)

Договорный % (A-TSUM-RATE-01) — **вторично**, пока agent_cash=0.

Updated: 2026-07-28
