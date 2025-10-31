---
created: 2025-10-31 10:40
updated: 2025-10-31 10:40
type: research-run
sphere: [market, cfa]
topic: [batch1, competitors]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [thread-mode, runbook]
---

TL;DR
- Batch‑1: 4 платформы (Атомайз, НРД, Сбер, Лайтхаус). 5 провайдеров × по 1 прогону. Выход: JSONL карточки + сводка MD + Mermaid.
- Расположение результатов: `memory-bank/Scrum/20251030-jump-into-project/deepresearches/01-CFA-platforms-RU-2024-2025/…`

Targets
- Атомайз; НРД; Сбер; Лайтхаус

Providers
- OpenAI GPT‑5 Pro; Anthropic Opus/Sonnet; Perplexity; Gemini 2.5p; Parallel

Naming
- `01-CFA-platforms-RU-2024-2025/{yyyymmdd-hhmm}-{provider}-{model}-CFA-platforms-RU-2024-2025.deepresearch.{md|json|jsonl}`

Prompt
- Использовать: `…/co-76ca/deepresearch-pipelines/01-CFA-platforms-RU-2024-2025/20251031-1026-prompts-cfa-platforms-ru-2024-2025.md`

Deliverables
- `competitors.jsonl` — одна JSON карточка на платформу (строка)
- `competitors.md` — сводная таблица и ссылки на источники
- `competitors-sources.md` — список источников с датами/цитатами (Perplexity first)

Done Criteria
- По полям dlt/ukep/dvp ≥2 независимых источника; остальное — хотя бы 1 или `unknown` с пометкой

