---
created: 2025-10-31 11:46
updated: 2025-10-31 11:46
type: research-prompt
sphere: [validation]
topic: [lighthouse, dvp]
author: codex
agentID: 019a362f-76ca-7272-909e-362716cf233d
partAgentID: [co-76ca]
version: 1.0.0
tags: [prompt, mece]
---

Goal: проверить DvP у «Лайтхаус» — подтвердить/опровергнуть наличие T+0/T+1, банки/ISO 20022/СБП.
Output:
- Card: dvp.model | banks | iso20022 | sbp | sources[] | confidence
- Итог: confirmed/likely/unknown, причины unknown (если данных нет)
Constraints: 2024–2025, ≥2 источника для confirmed.

