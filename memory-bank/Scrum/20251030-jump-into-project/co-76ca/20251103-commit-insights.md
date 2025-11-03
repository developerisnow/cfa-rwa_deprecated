---
created: 2025-11-03 12:00
updated: 2025-11-03 12:00
type: commit-insights
sphere: [governance, delivery]
topic: [git, iterations]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [insights, changelog]
---

TL;DR
- Коммиты показывают поступательное наращивание ценности: от правил/структуры → требований/чеклистов → ресерча/инструментов → конкурентной витрины → клиентских артефактов и отчётности.
- Сильные стороны: итеративность, следование AGENTS.md, frontmatter, трассировка, клиентские deliverables. Улучшить: доведение evidence/acceptance до 100% и фиксация решений (ledger, банк, УКЭП).

Основные вехи (по коммитам)
- Governance & правила
  - 0892bd2 chore(co, governance): update AGENTS.md with repo addendum — зафиксированы локальные правила (префиксы, manifest, чеклисты/trace, cadence).
  - 3ef94ba docs(agents): cadence/guardrails/commit style — 10–15m чанки, предоплата/объём, evaluator.
- Требования и чеклисты
  - 99b2323 co: docs(requirements): add requirements trace and update master-checklist — введён requirements‑trace и master‑чеклист с ссылками на источники.
- Deepresearch/промпты/инструменты
  - 7f516c4 feat(research-prompts): comprehensive competitors RU prompt — структура JSON/таблица/источники.
  - 498d0be docs(research): добавлены 8 deepresearch доков по Ledger и CFA‑RU (pipeline/prompts/orchestration/evaluation).
  - 92e1076 feat(tools): claims_indexer.py — консолидация claims JSONL; 76ae77b chore(run): выполнение и сводка 40 claims.
- Конкуренты РФ
  - fa3471c feat(batch1): competitors.jsonl + summary + sources (4 платформы). f06184a docs(qa): Batch‑1 QA (DvP unknown у Лайтхауса честно помечен).
  - 9186a18 feat(competitors): расширение до 20 платформ (competitors_all.md/jsonl) из structured sources.
- Клиентские артефакты/отчётность
  - fd14b74 docs(client): kickoff pack, glossary, roadmap/budget.
  - 74450fd docs(reporting): timelog v1 CSV, weekly report template, deliverables list, outsourced vs ours evaluation.
  - 8f1facf docs(client-report): weekly report + draft invoice + client deliverables list; 2025w44 инвойс (draft).
- Cross‑agent вклад
  - e17e2d3/f847886/e3253c5/... (cc‑e4ee, cc‑03‑0f8f): упорядочили структуру, project.manifest.json (index‑mode), добавили синтез и критические действия; усилили “industry standard” упаковку.

Инсайты
- Итеративная дисциплина: каждое значимое добавление — отдельный коммит с префиксом и frontmatter; видна траектория от «как работать» → «что делать» → «что показали клиенту».
- Трассировка: requirements‑trace/master‑checklist + QA по конкурентам позволяют прозрачно показать покрытие и unknown‑поля.
- Client‑first упаковка: есть weekly report, kickoff, roadmap, email‑драфт и инвойс — готово для коммуникации с Юрием.
- Объективные unknown: Lighthouse DvP оставлен как unknown (нет достоверных источников) — хороший тон для доверия.
- Manifest как index: решения пока не «зашиты», что снижает риск преждевременной фиксации стека до Discovery.

Зоны роста (по истории)
- Evidence/Acceptance: довести ссылки и acceptance‑критерии по всем deliverables до 100% (особенно там, где сейчас Draft/Unknown).
- Decisions: зафиксировать в decision‑log итог выбора ledger (Fabric/Besu vs immudb audit‑core), банк‑rails, УКЭП/ГОСТ провайдеров.
- Reporting: включить TimeLog v2 и burn‑up по DoD_ID в weekly report (client‑view останется компактным).

Next (по следам коммитов)
- Добавить decision‑log.md (решение/дата/вариант/основание/ссылки/владелец) и acceptance‑matrix.md (deliverable → DoD_ID → status → evidence).
- Закрыть unknown по Лайтхаусу повторной проверкой уже имеющихся MD‑отчётов; если нет — оставить как «нет подтверждений».

