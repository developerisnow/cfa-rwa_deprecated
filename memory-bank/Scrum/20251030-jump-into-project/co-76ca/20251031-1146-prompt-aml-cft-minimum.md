---
created: 2025-10-31 11:46
updated: 2025-10-31 11:46
type: research-prompt
sphere: [compliance]
topic: [aml, cft]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [prompt, mece]
---

Goal: минимально жизнеспособный набор AML/CFT правил и провайдеров для MVP ЦФА.
Output:
- Matrix: Rule | Trigger | Risk level | Alert | Escalation | Provider | Integration
- JSONL: rules (name, trigger, risk, alert, provider, sources[])
Constraints: РФ контекст 2024–2025, провайдеры санкционных списков, ≥2 источника/практики.

