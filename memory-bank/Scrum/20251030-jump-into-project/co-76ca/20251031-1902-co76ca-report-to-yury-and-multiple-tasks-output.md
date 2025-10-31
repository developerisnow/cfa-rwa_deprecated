 # Prompt
@memory-bank/Scrum/20251030-jump-into-project/20251031-1230-thoughts-what-next-what-important-how-to-fix-stuck.md
 
 # Output
 
 Worked for 48s ──────────────────────────────────────────────────────────────────────────────────────────────────────────────

• TL;DR

  - Предлагаю отчётность в 3 слоя: TimeLog (сырые записи) → DoD/Acceptance (трассировка к результатам) → Weekly Report
    (агрегаты для Юрия). Все записи — с привязкой к артефактам/коммитам/UID.
  - Улучшаем твою модель (CSV 2023‑09) до “операционно‑юридической”: добавляем DoD_ID, Evidence, Acceptance_Status, Scope/Epic,
    Decision/Risk, Client_Visible, AgentID.
  - Оценил текущие доки по критериям (Coverage/Clarity/Actionability/Traceability/Evidence) и дал план роста до “industry
    standard”.

  Steps

  1. Утвердить схему TimeLog v2 (ниже) и DoD‑маппинг (DoD_ID ↔ артефакт/критерии).
  2. Вести ежедневный TimeLog → раз в неделю строить Weekly Report (сводные, эскалации, инвойс).
  3. Привязать TimeLog к DoD/Acceptance и к артефактам (путь к файлу/коммит SHA).
  4. Сразу применить к текущей неделе: заполнить TimeLog v2 за фактическое время; собрать Weekly Report для Юрия.

  Table — Твоя старая модель vs Улучшенная

  - Pros старого CSV:
      - Быстрый ввод, учёт “Duration/Costs”, понятные “Type Activity/Status/Week”.
  - Cons старого:
      - Нет связки с DoD/Acceptance, артефактами, коммитами.
      - Смешанные языки/категории, неоднозначные “Tags”.
      - Нет статуса “Client_Visible/Confidentiality”, нет Decision/Risk, нет Scope/Epic.
  - Улучшения (TimeLog v2 колонки):
      - Date (ISO), Start, End, TZ
      - Scope/Epic, Task_ID (ссылка на задачу)
      - DoD_ID (из master‑checklist/requirements‑trace)
      - Activity_Type (analysis/research/architecture/impl/review/call/admin)
      - Description_Short, Description_Ref (путь к md/номер строки)
      - Evidence_Refs (коммиты, пути, страницы отчётов)
      - Acceptance_Status (pending/accepted/rejected), Acceptance_Refs (критерии)
      - Hours, Rate, Cost
      - Decision_ID, Risk_ID (если возникли)
      - Client_Visible (Y/N), Confidentiality (internal/client)
      - Agent (prefix‑partAgentID, e.g., co‑76ca), Tags
  - Минимально‑достаточные сводки (pivot/views):
      - По Date/Summary: SUM(Hours), SUM(Cost)
      - По Scope/Epic/DoD_ID: часов и статус Acceptance
      - По Activity_Type: доли времени (аналитика vs проделиверённый результат)
      - По Acceptance_Status: прогресс к DoD (burn‑up)
      - Инвойс: SUM(Cost) + деталь по блокам предоплаты

  Пример — CSV заголовок (TimeLog v2)
  Date,Start,End,TZ,Scope,Epic,Task_ID,DoD_ID,Activity_Type,Description_Short,Description_Ref,Evidence_Refs,Acceptance_Status,A
  cceptance_Refs,Hours,Rate,Cost,Decision_ID,Risk_ID,Client_Visible,Confidentiality,Agent,Tags
  2025‑10‑31,07:30,10:45,MSK,CFA‑RU,Competitors,B1‑NRD,DoD‑CFA‑COMP‑NRD‑DVP,analysis,"NRD DvP
  подтверждения","co‑76ca/20251031‑1100‑batch1‑competitors‑sources.md:1","commit:fa3471c; co‑76ca/
  competitors.jsonl:2",accepted,"≥2 источника по DvP",3.25,50,162.5,DEC‑12,RISK‑03,Y,client,co‑76ca,"deepresearch,aggregation"

  JSON (опционально) для тех же данных
  { "date":"2025‑10‑31","start":"07:30+03:00","end":"10:45+03:00","scope":"CFA‑RU","epic":"Competitors","taskId":"B1‑NRD","dodI
  d":"DoD‑CFA‑COMP‑NRD‑DVP","activity":"analysis","desc":"NRD DvP
  подтверждения","descRef":"co‑76ca/20251031‑1100‑batch1‑competitors‑sources.md:1","evidence":
  ["commit:fa3471c","co‑76ca/competitors.jsonl:2"],"acceptance":"accepted","acceptanceRefs":["≥2 источника по
  DvP"],"hours":3.25,"rate":50,"cost":162.5,"decisionId":"DEC‑12","riskId":"RISK‑03","clientVisible":true,"confidentiality":"cl
  ient","agent":"co‑76ca","tags":["deepresearch","aggregation"] }

  What “DoD” means здесь (конкретика)

  - DoD — измеримый результат, мапящийся на чек‑лист/requirements‑trace:
      - Примеры: DoD‑CFA‑COMP‑ATOM‑DLT (DLT подтверждён ≥2 источниками); DoD‑CFA‑COMP‑SBER‑SECONDARY (RFQ/Orderbook
        подтверждены); DoD‑MVP‑ARCH‑C4 (C4 Context/Containers принят); DoD‑SOW‑DISCOVERY (Scope/Deliverables согласованы).
  - Acceptance Criteria:
      - Формализуем в master‑checklist: сюжет + критерии проверки + ссылка на артефакт.
      - В таймлог пишем “accepted/pending/rejected” и ссылку на проверку.

  Еженедельный отчёт Юрию (структура)

  - TL;DR (3 bullets): что достигли/что изменилось/какие блокеры сняты
  - Outcomes vs Plan: список DoD, принятые критерии и артефакты (кликабельные пути)
  - Deltas: отклонения, причины, компенсация
  - Next Week Plan: 3–5 DoD с критериями и артефактами
  - Risks/Decisions: RISK/DEC журналы (кратко + ссылка)
  - Financials: Hours, Rate, Cost, баланс предоплаты
  - One‑pager диаграммы: burn‑up по DoD, pie по Activity_Type

  Оценка документов (1–10 по критериям)

  - Критерии: Coverage (охват), Clarity (ясность), Actionability (готовность к действию), Traceability (связность/ссылки),
    Evidence (доказательность).
  - Моя оценка “как есть”:
      - 20251031‑1125‑client‑kickoff‑pack.md — 9/8/9/8/7 (высоко; добавить примеры acceptance для Discovery)
      - 20251031‑1129‑deliverables‑roadmap.md — 8/8/8/7/6 (добить метрики и даты; отметить зависимости на банк/УКЭП)
      - 20251031‑1127‑glossary‑cfa‑rwa.md — 7/8/7/6/6 (расширить “где применимо в проекте”, привязать к DoD)
      - competitors_all.md/jsonl — 9/7/7/7/7 (полный охват; добавить покрытие по крит. полям и unknown‑обоснование)
      - batch1‑qa.md — 6/8/8/8/6 (хорошие QA‑срезы; добавить путь закрытия unknown)
      - requirements‑trace.md (co‑76ca) — 7/7/7/8/6 (добавить больше ссылок на строки, “accepted by …”)
      - estimation_from_outsource_company.md — 8/9/6/6/5 (лаконично и понятно; мало evidence/trace, но как ориентир — отлично)
      - cc‑171f артефакты (C4/roadmap) — 8/8/8/7/6 (хорошо, но надо привести к DoD/Acceptance и к общей матрице)
  - Куда расти:
      - Везде довести Traceability: DoD_ID ↔ acceptance ↔ артефакт/коммит/номер строки.
      - В Summary‑таблицах показывать покрытие полей и unknown c причинами.
      - Добавить регулярные Weekly Reports с инвойсом и балансом предоплаты.

  “Юрий‑фактор” (психология/досье) — как оформить отчётность

  - Коротко, предметно, “что у меня на столе сейчас” + “что мешает” + “что мне нужно от тебя”.
  - Всегда сумма/часы/остаток блока; демонстрация инкрементов (скрин/ссылка).
  - Scope freeze на спринт; CR — отдельным блоком (видна стоимость/дедлайн).
  - Публичные DoD из конкурентной оценки (чтобы не было ощущения “анализ ради анализа”).

  Нужны ли ещё deepresearch?

  - Широких — нет. Точечных — да (для финализации):
      - Lighthouse DvP: вторичное подтверждение/опровержение (скорее всего unknown — так и зафиксируем).
      - KEP/УКЭП провайдеры + HSM (РФ; SLAs/стоимость/SDK) — для Discovery.
      - Банк‑rails (1–2 банка) — требования к интеграции и SLA/ISO20022.
      - AML/CFT минимальный набор (правила, провайдеры, интеграция).
  - Могу запустить точечные промпты (по merged‑шаблонам) и сразу приложить в Weekly Report.

  Next actions

  - Хочешь — подготовлю шаблон TimeLog v2 (CSV + Google Sheet) и Weekly Report (md + pivot), заполню за текущую неделю и
    сформирую “Юрий‑отчёт” с инвойсом (по твоим часам/ставке).
  - Проведу “acceptance‑проход” по текущим DoD (Discovery/Competitors) — проставлю “accepted/pending” и подготовлю список
    “needs from Yury”.
  - Сверстаю слайды/письмо Юрию из client‑kickoff‑pack (SOW/Discovery/роль/финансы), чтобы ты мог отправить.
