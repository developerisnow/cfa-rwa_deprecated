---
created: 2025-10-31 07:30
updated: 2025-10-31 07:30
type: research-prompts
sphere: [ledger, compliance, market]
topic: [merged-deepresearch]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [prompts, consolidation]
---

TL;DR
- Объединённый набор deepresearch‑промптов без дублирования: синтез `co-76ca` и `cc-171f`.
- Приоритет: РФ ЦФА (2024–2025), permissioned Ethereum (Besu/Quorum), KEP/УКЭП, AML, DvP, конкуренты РФ.
- Дополнение: проверка выводов 20251004 исследования по гос‑блокчейнам.

Ledger (Permissioned Ethereum vs Fabric vs Audit‑core)
- Goal: принять решение для MVP РФ ЦФА.
- Inputs: 20251004-2245-thread-profession-government-blockchain-architecture.md; Estimation‑doc (DLT/immudb);
- Ask: прод‑кейсы 2023–2025, ops‑сложность, privacy patterns (Tessera), latency, tooling.
- Deliverable: таблица 8×8 + PoC‑план (поднять Besu/RAFT/IBFT, тест Emission/DvP/Anchoring).

KEP/УКЭП Integration
- Goal: связка аккаунтов и подписей (63‑ФЗ) + mTLS.
- Ask: провайдеры в РФ, SDK/API, SLAs, кейсы; требования к хранению ключей (ГОСТ), HSM отечественные.
- Deliverable: чеклист внедрения + runbook инцидентов.

AML/CFT
- Goal: минимальный рабочий набор правил для ЦФА на старте.
- Ask: санкционные списки/провайдеры (2024–2025), risk‑скоринг, алерты, Travel Rule применимость.
- Deliverable: матрица правил (низк/сред/высок) + интеграции.

DvP Rails
- Goal: атомарный обмен ЦФА↔рубль с 1 банком.
- Ask: escrow‑модели, ISO 20022 форматы, reconciliation, SLA.
- Deliverable: sequence + risk‑лог + PoC тест‑набор.

Secondary (RFQ/OTC)
- Goal: RFQ до ордербуков.
- Ask: допуски, авторизация заявок, комплаенс, аудит.
- Deliverable: RFQ API + события, миграция к orderbook.

Competitors РФ (per‑platform)
- Goal: 12 работающих + 6 неработающих + 3 в пути.
- Ask: по шаблону research‑template, на фактах 2024–2025; избегать «слухов».
- Deliverable: таблица + сводная карта.

Sanctions/BRICS Stack
- Goal: вендор/стек без санкционных рисков.
- Ask: HSM/MPC отечественные, регуляторные ограничения, SBoM требований.
- Deliverable: shortlist + риски.

