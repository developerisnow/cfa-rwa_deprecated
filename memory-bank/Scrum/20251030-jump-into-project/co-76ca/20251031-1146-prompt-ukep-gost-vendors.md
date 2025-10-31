---
created: 2025-10-31 11:46
updated: 2025-10-31 11:46
type: research-prompt
sphere: [compliance]
topic: [ukep, gost, vendors]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [prompt, mece]
---

Goal: shortlist УКЭП/ГОСТ провайдеров в РФ для ЦФА‑платформы (SDK, SLAs, цены, интеграции, HSM/СКЗИ).
Output:
- Table: Vendor | SDK/API | ГОСТ/HSM | SLAs | Pricing | Cases | Risks
- JSONL cards per vendor (name, sdk, gost, hsm, slas, pricing, cases, sources[])
Sources priority: оф. сайты, регуляторы, reputable медиа, вакансии (confidence mid/low).
Constraints: период 2024–2025, ≥2 источника для ключевых полей.

