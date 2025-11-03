---
created: 2025-11-03 14:15
updated: 2025-11-03 14:15
type: presentation
sphere: [client, executive]
topic: [mvp, discovery, decisions]
author: claude-code
agentID: vk-8ad8
partAgentID: [vk-8ad8, co-76ca]
version: 2.0.0
tags: [slides, executive, 30-60min]
---

# ОИС ЦФА "Капитал" — Discovery 50h + MVP Roadmap
## Презентация для 30-60 мин обсуждения с Yury

---

## СЛАЙД 1: Статус & Что Сделано ✓

### Discovery Phase: 50h ✓
- **Старт**: November 3, 2025
- **Срок**: 1.5–2 недели

### Что Уже Готово (до Discovery)
✓ **Конкурентный анализ**: 20 платформ РФ ЦФА
✓ **Deep dive**: 4 ключевые платформы (Atomyze, НРД, Сбер, Лайтхаус)
✓ **Research framework**: 2 направления (Ledger worldwide, CFA-RU)
✓ **Governance**: Multi-agent система, версионирование, трассировка
✓ **SOW**: Prepayment blocks, scope control, weekly demos

---

## СЛАЙД 1a: 10% Essence (Iceberg)

### Что показываем на звонке
- Executive Brief → 5 ключевых артефактов
- Competitors (20) → рынок и приоритизация
- SoW 50h + Architecture (C4) → как работаем
- Roadmap (10–12 недель) → когда и в каком порядке
- Kickoff (90m) → что решаем вместе

### Портал (быстрые ссылки)
- [[20251103-executive-brief]]
- [[competitors-all-in-one]]
- [[20251103-sow-architecture-overview]]
- [[roadmap]]
- [[kickoff-pack]]

---

## СЛАЙД 2: Discovery 50h — Deliverables

### Что Получите
1. **C4 Architecture** (Context/Containers диаграммы)
   - Границы системы, внешние интеграции
   - Доменные сервисы и их взаимодействия

2. **Каталог Событий + API Контракты**
   - Event-driven архитектура (Kafka)
   - OpenAPI specs (черновики)

3. **Ledger Memo** (без финального выбора)
   - Fabric vs Besu vs immudb audit-core
   - Trade-offs: ops-сложность, privacy, latency, tooling
   - Recommendation с путями миграции

4. **Shortlists**
   - 1-2 банка для DvP T+0 rails (ISO 20022, СБП, escrow)
   - 2-3 УКЭП/ГОСТ вендора (SDK, SLAs, HSM, pricing)

5. **MVP План** (10-12 недель)
   - Domains: Registry/KYC, Tokenization, Custody, Settlement, Disclosure
   - DoD per slice
   - Risk mitigation strategies

6. **Discovery Report**
   - Executive summary
   - Key decisions needed
   - Next steps

---

## СЛАЙД 3: MVP Scope (Primary Market Only)

### Что Включено в MVP ✓
- **Registry/Identity**: Участники, роли, ABAC, KEP/УКЭП привязка
- **KYC/KYB**: Sanctions/PEP checks, biometrics (optional)
- **Tokenization**: Emission, term-sheets, disclosures, basic corporate actions
- **Settlement DvP**: T+0 с 1 банком, atomic swap cash↔ЦФА
- **Custody**: HSM/MPC keys, M-of-N policies, wallet profiles
- **Disclosure/Reporting**: TSA timestamps, regulator exports, XBRL/ISO 20022

### Что Отложено (v1.1+) ⏸
- **Secondary Market**: RFQ/OTC → v1.1, Orderbooks/Auctions → v1.2
- **Extended Corporate Actions**: Coupons, amortization schedules
- **Multi-bank DvP**: MVP = 1 bank, масштабирование позже

### Why Primary Only?
- **Быстрый time-to-market**: 10-12 недель vs 20+ для full platform
- **Risk reduction**: Фокус на regulatory compliance (259-ФЗ, 63-ФЗ) сначала
- **Proof of concept**: Валидируем tech stack перед secondary market

---

## СЛАЙД 4: Конкурентный Ландшафт РФ (Key Insights)

### 20 Платформ Проанализировано
- **Работают (12)**: Альфа-Банк, Atomyze, Блокчейн Хаб, ВТБ Капитал, ЕВРОФИНАНС, Токеон, Лайтхаус, НРД, Сбербанк, Системы распр. реестра, СПБ Биржа, МРЦ
- **Не работают (6)**: Синара, БКС, Газпромбанк, ТБанк, Токеник, [+1]
- **В процессе (3)**: МАДРИГАЛ (скоро), Статус/Спутник (ждут лицензии)

### Batch-1 Deep Dive (4 платформы)

#### Atomyze
- **DLT**: Hyperledger Fabric (confirmed, 2+ sources)
- **Custody**: HSM-based (Thales/nCipher confirmed)
- **УКЭП**: ГОСТ-compatible (CryptoPro integration)
- **DvP**: T+1 model with Russian banks
- **Secondary**: RFQ/OTC operational
- **Confidence**: HIGH

#### НРД (Национальный Расчетный Депозитарий)
- **DLT**: Own proprietary DLT (based on Fabric fork)
- **Custody**: Integrated with existing depository infrastructure
- **УКЭП**: ГОСТ/УКЭП mandatory for all operations
- **DvP**: T+0 capable (депозитарная система)
- **Secondary**: Secondary market integrated with existing infrastructure
- **Confidence**: HIGH

#### Сбербанк (Цифровые Активы)
- **DLT**: Hyperledger Fabric + exploring Besu
- **Custody**: Internal HSM infrastructure (ГОСТ-compliant)
- **УКЭП**: Full ГОСТ/УКЭП integration
- **DvP**: T+0 via Sber's banking rails
- **Secondary**: Planned but not public yet
- **Confidence**: HIGH

#### Лайтхаус (Lighthouse)
- **DLT**: Undisclosed (likely Fabric or proprietary)
- **Custody**: HSM-based (vendor unknown)
- **УКЭП**: ГОСТ compliance confirmed
- **DvP**: **UNKNOWN** ⚠️ (no public evidence)
- **Secondary**: RFQ model (confirmed)
- **Confidence**: MEDIUM (DvP gap)

### Key Takeaway: Honest Unknowns
- Мы **не спекулируем**, а честно отмечаем "unknown"
- Это показывает **rigor** и **integrity** исследования
- Клиент видит, где нужны уточнения (например, Lighthouse DvP)

---

## СЛАЙД 5: Технические Решения & Направления

### Ledger Direction (будет memo в Discovery)
**Option 1: Permissioned Ethereum (Besu/Quorum)**
- ✅ EVM, Solidity, богатая экосистема
- ✅ Privacy: Tessera for private transactions
- ✅ Consensus: RAFT/IBFT (fast finality 1-2s)
- ❌ Ops complexity (node management, gas pricing)
- **Use Case**: Smart contracts для tokenization/settlement

**Option 2: Hyperledger Fabric**
- ✅ Mature permissioned DLT, channels, rich ACL
- ✅ Production-proven (Atomyze, Сбер используют)
- ❌ Chaincode learning curve, oper complexity
- **Use Case**: Enterprise-grade privacy & compliance

**Option 3: immudb Audit-Core**
- ✅ Simple, fast, append-only, minimal ops
- ✅ Cryptographic proof of immutability
- ❌ No smart contracts (app-level logic only)
- **Use Case**: Fast MVP audit trail + hash anchoring

### Рекомендация (предварительная)
- **MVP**: Start with **Besu (permissioned Ethereum)** + IBFT consensus
  - Reasoning: EVM = flexibility, Solidity talent available, ecosystem tooling
- **Hedge**: Implement **Ledger Adapter** pattern (event-sourcing + CQRS)
  - Enables: Switch to Fabric or add immudb anchoring without rewrite
- **Audit**: Independent hash anchoring regardless of ledger choice

### Architecture Principles
- **Spec-first**: OpenAPI + event schemas before code
- **Event-driven**: Kafka for async, CQRS for read/write separation
- **Ledger-agnostic**: Adapter pattern to avoid lock-in
- **Compliance by design**: 259-ФЗ, 63-ФЗ, AML/CFT embedded

---

## СЛАЙД 6: Критические Решения (3 Blocker)

### Blocker 1: Ledger Selection ⏳
- **Status**: Discovery 50h will produce trade-off memo
- **Your Decision Needed**: Choose direction (Fabric/Besu/immudb)
- **Timeline**: Week 1 of Discovery (memo ready), Week 2 (confirm choice)

### Blocker 2: Bank DvP Rails ⏳
- **Status**: Discovery 50h will shortlist 1-2 banks
- **Your Decision Needed**: Select bank partner, initiate integration talks
- **Timeline**: Week 1 (shortlist), Week 2 (selection), then integration spike

### Blocker 3: УКЭП/ГОСТ Vendor ⏳
- **Status**: Discovery 50h will shortlist 2-3 vendors
- **Your Decision Needed**: Choose provider, procurement initiation
- **Timeline**: Week 1 (shortlist), Week 2 (selection), then test CA setup

### Why These Are Critical
- **Ledger**: Determines tech stack, hiring, ops overhead
- **Bank**: DvP impossible without partner; integration = 4-6 weeks lead time
- **УКЭП**: Regulatory compliance blocker; procurement = 2-4 weeks

### Decision Framework (in Discovery Report)
- **Criteria**: Cost, latency, privacy, ops complexity, vendor lock-in risk
- **Matrix**: Weighted scoring for objective comparison
- **Recommendation**: With rationale, but final choice is yours

---

## СЛАЙД 7: Timeline & Budget

### Discovery Phase (Current) ✓
- **Duration**: 1.5-2 weeks
- **Hours**: 40h
- **Cost**: $2,000 (PAID)
- **Deliverables**: See Slide 2

### MVP Phase (После Discovery)
- **Duration**: 10-12 weeks
- **Hours**: 400-600h
- **Cost**: $20k-$30k (at $50/h base rate)
- **Structure**: Prepayment blocks (80-170h per block)
- **Team**: Lead/Arch, 2 BE, 1 FE, 1 DevOps/Sec, 0.5 BA, 0.5 QA

### MVP Milestones (Outline)
- **M0 (Week 0-1)**: Architecture + env setup + CI/CD
- **M1 (Week 2-4)**: Registry/KYC + basic tokenization
- **M2 (Week 5-7)**: Custody/HSM + Settlement DvP (mocked bank)
- **M3 (Week 8-10)**: Bank integration + Disclosure/Reporting
- **M4 (Week 11-12)**: UAT, pilot with 1 issuer, handoff

### Post-MVP (v1.1+)
- **Secondary Market**: RFQ/OTC (8-12 weeks, $15k-$25k)
- **Orderbooks/Auctions**: v1.2 (12-16 weeks, $25k-$40k)
- **Extended Features**: Corporate actions, multi-bank, analytics

---

## СЛАЙД 8: Risk Management

### Technical Risks → Mitigations
1. **Bank rails delay**
   → Mock settlement + parallel bank track (don't block MVP)

2. **Ledger choice churn**
   → Ledger adapter + event-sourcing (decouple from specifics)

3. **KEP/УКЭП vendor lead-time**
   → Start procurement NOW; temporary test CA in parallel

4. **Secondary market scope creep**
   → Lock MVP to primary; defer RFQ/OTC to v1.1 (strict DoD)

### Economic Risks → Mitigations
1. **Scope creep & unpaid overtime**
   → 100% prepayment blocks; scope freeze per sprint; change requests = new blocks

2. **Misaligned expectations**
   → Weekly demos with visible increments; acceptance tests signed upfront

3. **Budget overrun**
   → Fixed-scope blocks; transparent timelog; no hidden hours

### Regulatory Risks → Mitigations
1. **259-ФЗ compliance gaps**
   → Operator duties embedded in architecture; audit trail ≥7 years

2. **63-ФЗ KEP/УКЭП requirements**
   → ГОСТ-compatible stack from day 1; vendor procurement in Discovery

3. **AML/CFT enforcement**
   → Sanctions/PEP checks; transaction monitoring; alerts; escalation to Росфинмониторинг

---

## СЛАЙД 9: Governance & Reporting

### Weekly Cadence
- **Demos**: Every Friday (visible increments only, no WIP)
- **Weekly Report**: Client view (Deliverables/Goal/Why Now/Status)
- **Blockers**: Escalated immediately (не ждём недели)

### Transparency Model
- **Client View (10%)**: Executive summaries, decisions, next steps
- **Internal (90%)**: Research, traceability, evaluation, timelog
- **GitHub**: Two-repo strategy (public for client visibility, private for scaffolding)

### Prepayment Blocks (Guardrails)
- **Discovery**: 50h ($2k) — PAID ✓
- **MVP Block 1**: 80-170h ($4k-$8.5k) — prepay before start
- **MVP Block 2+**: Same structure, approved per block
- **Change Requests**: New block, separate scope/pricing

### Acceptance Criteria (DoD per Slice)
- API contracts + event schemas
- Audit logs + hash anchoring
- README per service
- Test cases (unit + integration)
- Demo-ready increment

---

## СЛАЙД 10: What Makes This Different

### 1. Honest Unknowns (No BS)
- Lighthouse DvP = unknown ⚠️ (instead of guessing)
- Shows **integrity** and **rigor** of research

### 2. Multi-Agent Validation
- 5 AI providers (GPT-5, Opus 4.1, Sonnet 4.5, Gemini 2.5p, Perplexity)
- Cross-validated claims (≥2 sources for critical fields)
- Evaluation metrics prevent overload

### 3. 10% Essence Extraction
- You get: Executive summaries, decisions, next steps (30-60 min)
- We keep: Deep research, traceability, evaluation (hours of work)
- **Result**: Your time is respected

### 4. Prepayment-First Economics
- Protects both sides: no unpaid overtime, no non-payment risk
- Scope freeze per sprint: change requests = new blocks
- Transparent timelog: you see where hours go

### 5. Ledger-Agnostic Design
- Adapter pattern: switch Fabric/Besu/immudb without rewrite
- Event-sourcing: replay history on new ledger if needed
- Independent anchoring: audit trail separate from ledger

### 6. Production-Grade From Day 1
- Security: mTLS, OAuth2/OIDC, WAF, HSM/MPC, audit logs
- Compliance: 259-ФЗ, 63-ФЗ, AML/CFT, PDN, TSA timestamps
- Ops: CI/CD, monitoring, DR/BCP, key rotation

---

## СЛАЙД 11: Next Steps (Action Items)

### Immediate (This Week)
1. ✓ **Confirm Discovery 50h PAID** (done)
2. ⏳ **Schedule 90-min Kickoff** (you + tech lead + me)
   - Agenda: Review Discovery scope, confirm deliverables, align on timeline
3. ⏳ **Provide Context** (if available)
   - BitChange PHP code (for reuse audit)
   - Bank contacts (for DvP shortlist)
   - УКЭП vendor preferences (if any)

### Discovery Phase (Week 1-2)
1. **Week 1**: Research + shortlists (Ledger memo, Bank rails, УКЭП vendors)
2. **Week 2**: C4 diagrams, event catalog, API drafts, MVP plan, Discovery report
3. **Handoff**: 60-min review session (present report, Q&A, decision on MVP)

### After Discovery (If MVP Approved)
1. Confirm MVP Block 1 prepayment (80-170h)
2. Initiate bank integration talks + УКЭП procurement
3. Set up dev/staging environments
4. Start M0: Architecture + env setup + CI/CD

---

## СЛАЙД 12: Questions & Discussion

### Open for Discussion
- Discovery scope adjustments?
- Priority of deliverables (if time-constrained)?
- Bank/УКЭП vendor leads to explore?
- MVP timeline expectations (10-12 weeks realistic)?
- Budget constraints or flexibility?

### What I Need From You
1. **Kickoff call**: 90 min (when works for you?)
2. **Context docs**: BitChange code, bank contacts, УКЭП preferences (if any)
3. **Decision authority**: Who approves blockers (Ledger/Bank/УКЭП)?
4. **Communication channel**: Telegram/Email/Slack (your preference)

### What You Get From Me
- **Discovery Report**: Comprehensive, actionable, decision-ready
- **Weekly updates**: Transparent, no surprises
- **Honest assessment**: If something is unknown/risky, you'll know
- **Production-ready artifacts**: Not just slides, but executable docs

---

## Приложение: Документы в Пакете

1. **presentation.md** (this file) — Executive overview
2. **00-commit-insights-sequential-analysis.md** — Evolution of project (meta-analysis)
3. **weekly-report.md** — Status update (client view)
4. **kickoff-pack.md** — Discovery 50h agenda + deliverables
5. **roadmap.md** — Timeline/budget/risks
6. **competitors-overview.md** — 20 platforms (high-level)
7. **batch1-competitors.md** — 4 platforms (deep-dive)
8. **batch1-sources.md** — Research sources
9. **batch1-qa.md** — What's confirmed/unknown
10. **glossary.md** — ЦФА/RWA terminology
11. **invoice-discovery-40h.md** — Invoice (PAID ✓)

### How to Use This Pack
- **Offline-viewable**: No internet needed
- **Self-contained**: All context included
- **Flashdrive-ready**: Copy to USB and open in any text/markdown editor

---

**Prepared by**: Claude Code (vk-8ad8) + Codex (co-76ca)
**Date**: November 3, 2025
**Version**: 2.0.0 (Enhanced with commit insights)
**agentID**: vk-8ad8, co-76ca
**Status**: Discovery 50h PAID ✓, Ready to Start

---

## Контакты
- **Email**: [your-email]
- **Telegram**: [your-telegram]
- **Payment**: USDT TRC-20 [wallet-address]

**Давайте начнём Discovery и доведём платформу до production!** 🚀
