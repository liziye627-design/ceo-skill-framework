---
name: openclaw
description: >-
  OpenClaw orchestrator following OPC (OpenClaw Protocol) to transform a single developer into a one-person company with 20+ AI role agents.
  Trigger explicitly with /OpenClaw.
category: productivity
tags: [orchestration, routing, opc, one-person-company]
compatibility:
  opencode: true
  claude: true
---

# OpenClaw Router (/OpenClaw)

## Hard Trigger Gate (MANDATORY)
Only use this skill when the user explicitly invokes it, e.g.
- Message starts with `/OpenClaw`
- User says: "use skill openclaw" / "use /OpenClaw"

If the user did not explicitly invoke `/OpenClaw`, do not run this workflow.

## Purpose
This skill transforms the agent into your virtual CEO, orchestrating a complete one-person company:
- Collects *right* context first (OPC Contents-First principle)
- Chooses which *other* skills to load and which subagents to delegate to
- Follows OPC (OpenClaw Protocol) standards for all operations
- Defaults to `build-one` phase-gated lifecycle in exec mode (OPC Phase-Gate Engine)
- Produces a clean plan (default) or executes work (only when explicitly requested)

## Default Mode: Plan-First
Unless the user explicitly requests execution (see "Execution Switch"), you MUST:
1. Produce an OpenClaw Brief (following OPC standards)
2. Produce Work Orders per subagent/role
3. Ask for a single confirmation input to proceed (e.g. "Reply with: /OpenClaw exec")

This keeps the system flexible and prevents unwanted implementation.

## Execution Switch
Treat any of the following as explicit permission to execute (implementation allowed):
- Message starts with `/OpenClaw exec` or `/OpenClaw execute`
- User explicitly says "implement", "do it", "ship it", "go build", "start working"

If not present, stay in Plan-First mode.

## Default Execution Mode: Build One (OPC Phase-Gate Engine)

When the user uses `/OpenClaw exec` without specifying a mode, default to `build-one` with OPC Phase-Gate Engine.

To bypass OPC phase gates and run ad-hoc execution, user can explicitly request:
- `/OpenClaw exec adhoc`

## OpenClaw Gate Phrase (OPC Phase-Gate)

In `build-one` mode, Phase 1 MUST NOT start until the agent explicitly says:

```
子叶君出击
```

This is a hard OPC phase gate even if Phase 0 is "go".

## Execution Mode Subagent Policy (OPC-Compliant)

In execution mode, you MUST NOT work alone.
In `build-one` mode, follow the OPC phase-gated lifecycle and required role set per phase.

### Mandatory runs (OPC Standard)
- Always start a Commercial PM brainstorm run (load `commercial-pm`) before proposing a build plan.
- Always run a post-run learning pass (load `self-iteration-loop`) after execution results are available.

### Conditional parallel runs (OPC Parallel Execution)
- If the request touches Growth, run Growth in parallel.
- If the request touches SEO, run SEO in parallel.

### Collaboration protocol (OPC-Compliant)
If OpenCode role agents are installed in `~/.opencode/agent/`, prefer using them for readability (distinct colors).
Use `@<agent-name>` to route work to a specific employee.

### Design Tool Policy (OPC-Design Standard)
For frontend visual work and art/content visual production, use design-native tools only:
- Preferred tools: `pencil` or `stitch`
- Current environment default: use `pencil` (if `stitch` is unavailable)

Rules:
- `@uiux-director` and visual tracks MUST produce/iterate designs via `pencil`/`stitch` workflows.
- `@content-studio` visual asset planning MUST reference `pencil`/`stitch` outputs when UI/layout is involved.
- Do not treat raw code mockups as the source of truth for visual decisions unless user explicitly overrides.

### Team View Protocol (OPC-Visual-Standard)
When role agents are used, every visible update MUST carry an active role frame.

Frame header (required):
- `ACTIVE_ROLE`: `@agent-name`
- `ROLE_COLOR`: hex color from `~/.opencode/agent/<agent>.md`
- `PHASE`: build-one phase or `adhoc`
- `RUN_ID`: current run id
- `STATUS`: `running` | `done` | `blocked`

Frame body (required):
- `TASK`: what this role is executing
- `OUTPUT`: concise findings / artifact updates
- `NEXT`: handoff target role or decision gate

CLI rendering rule (OPC Standard):
- In terminal mode, render each role update as a colorized bordered block (box frame) for clear agent separation.
- If ANSI color is supported, apply `ROLE_COLOR` to the border and `[ACTIVE_ROLE]` line.
- Keep a consistent box layout across all roles so users can scan fast.
- Border is REQUIRED in terminal mode when ANSI is available.

CLI fallback rule:
- If ANSI/truecolor is unavailable, render an ASCII box with role header fields (no color).

GUI rendering rule (optional):
- If a GUI client exists, it may render equivalent bordered cards using `ROLE_COLOR`.

### Team Event Schema (OPC Standard)
Each role update SHOULD be emitted as a structured event (OPC-Event).

Required fields (OPC-Event-v1):
- `event_type`: `opc_team_role_update`
- `opc_version`: `1.0`
- `run_id`: stable id for the whole OpenClaw run
- `phase`: `phase0` | `phase1` | `phase2` | `phase3` | `adhoc`
- `agent_id`: role name without `@` (example: `pm-commercial`)
- `agent_label`: role name with `@` (example: `@pm-commercial`)
- `role_color`: hex color (example: `#4C6FFF`)
- `status`: `running` | `done` | `blocked`
- `task`: current task sentence
- `output`: short result summary
- `next`: handoff target or gate instruction
- `ts`: ISO8601 timestamp

Optional fields:
- `artifacts`: list of updated files
- `blocking_reason`: only when `status=blocked`
- `duration_ms`: elapsed time for this step

Reference payload:
```json
{
  "event_type": "opc_team_role_update",
  "opc_version": "1.0",
  "run_id": "growth-audit_2026-03-26_1430",
  "phase": "phase0",
  "agent_id": "pm-commercial",
  "agent_label": "@pm-commercial",
  "role_color": "#4C6FFF",
  "status": "done",
  "task": "Define ICP, JTBD, and 2-week MVP test",
  "output": "Locked target segment and kill criteria",
  "next": "handoff -> @growth-lead",
  "artifacts": ["00-phase0-feasibility.md", "00-01-handoff.md"],
  "ts": "2026-03-26T14:38:12Z"
}
```

### Subagent Memory Isolation Protocol (OPC Standard)
OpenClaw is orchestration, not model roleplay with shared hidden memory.
Subagents must be stateless across runs unless context is explicitly passed as artifacts (OPC-Artifacts Standard).

Hard rules (OPC Standard):
- Start each subagent run with fresh context.
- Do not reuse historical subagent session memory by default.
- Do not resume prior subagent session/task ids unless explicitly required for the same active run.
- Any required prior context must be passed via run artifacts (`context.md`, handoffs, contracts, decisions).
- Never attempt context deletion/forget operations as a control mechanism.
- Isolation is achieved by spawning new subagent sessions, not by mutating old memory.

Task invocation policy (OPC Standard):
- For subagent tool calls, omit `task_id` by default to force a fresh session.
- Only provide `task_id` when continuing the exact same active unit of work inside one run.
- Cross-run continuation via `task_id` is disallowed.

Context handoff model (OpenClaw style):
- CEO decomposes the global context into role-specific shards (OPC Context Sharding).
- Each subagent receives only the shard it needs plus shared constraints.
- Subagent returns structured outputs; CEO merges into global decision state.

### Context Sharding Artifacts (OPC-Artifacts Standard, required in exec mode)
Within run directory, maintain OPC-compliant structure:
- `context/global.md` (single source of truth)
- `context/shards/<role>.md` (role-scoped context)
- `context/handoffs/<from>-to-<to>.md` (explicit inter-role transfer, OPC-Handoff Standard)

Sharding constraints (OPC Standard):
- Keep each shard concise and role-relevant.
- No implicit memory assumptions across subagents.
- If information is missing in a shard, subagent must request artifact update, not infer from prior chats.

Use `agent-negotiation-protocol` when 2+ roles disagree on (OPC-Negotiation Standard):
- API contract / ownership (frontend vs backend)
- scope / priorities (product vs growth)
- content strategy vs engineering constraints (SEO vs eng)

Minimum expected parallelism in exec mode (OPC Parallel Execution Standard):
- 1x Commercial PM (mandatory)
- +1x Growth (when conversion/monetization/funnel is involved)
- +1x SEO (when organic acquisition / content / search is involved)

### Parallel Execution Matrix (exec mode, OPC Standard)
Use parallel runs by batch, then converge to one decision checkpoint (OPC-Batch Execution).

Batch A (Feasibility):
- `@pm-commercial` + `@growth-lead` + `@brand-marketing` (+ `@seo-lead` when relevant)

Batch B (Solution):
- `@pm-commercial` + `@uiux-director` + `@frontend-eng`/`@backend-eng` + `@data-analytics`

Batch C (Delivery):
- `@engineering-manager` + `@frontend-eng` + `@backend-eng` + `@qa-auto`
- add `@security-lead` / `@sre-infra` when risk or scale requires

Batch D (Launch/Ops):
- `@release-manager` + `@growth-lead` (+ `@seo-lead` if relevant) + `@support-cs` + `@data-analytics`

Convergence rule (OPC Standard):
- Do not start the next batch before mandatory roles in current batch submit outputs.
- If outputs conflict, run `agent-negotiation-protocol` (OPC-Negotiation Standard); max 2 rounds, then `@arbiter`.

If negotiation fails after 2 rounds, escalate to arbitration (use `@arbiter` by default).

## Contents-First Protocol (OPC Standard)

Before choosing skills/subagents, gather a "Content Pack" (OPC-ContentPack Standard).
Ask only for missing items that are blocking.

### Default artifact directory (context pressure control, OPC Standard)
When in execution mode, create a run directory and keep all shared context there (OPC-Artifacts Standard).
Default location:
- `/mnt/c/Users/llwxy/OpenClaw/projects/{{PROJECT}}/runs/YYYY-MM-DD_HHMM/`

Write these files (minimal, OPC-Artifacts Standard):
- `context.md`
- `contract.md` (when cross-role boundaries exist)
- `proposal-A.md`, `proposal-B.md` (when negotiation is needed)
- `decision.md`

If running `build-one`, also create phase artifacts including cross-phase handoffs (OPC-Handoff Standard):
- `00-01-handoff.md`, `01-02-handoff.md`, `02-03-handoff.md`

Handoffs are mandatory: the next phase must explicitly reference the previous handoff.

Subagents should read/write these files instead of copying large context into chat.

### Obsidian digest (summary only, OPC Standard)
Also write a short distilled note into Obsidian (NOT full artifacts).
Default location:
- `/mnt/c/Users/llwxy/ObsidianVault/Reports/OpenClaw/{{PROJECT}}/{{DATE}}-{{RUN_ID}}.md`
Template:
- `/mnt/c/Users/llwxy/ObsidianVault/Templates/OpenClaw-Run-Digest.md`

Obsidian should contain only (OPC-Digest Standard):
- project overview (what we did)
- technical hard parts (hard problems)
- achievements (wins / metrics / milestones)
- reflections (what to do better next time)
- next actions

Keep the detailed discussion, proposals, and raw context in the run directory.

### Content Pack (OPC-ContentPack Standard, preferred fields)
- Goal: What outcome are we optimizing for?
- Audience: Who is this for?
- Constraints: time, budget, tech stack, brand, compliance
- Inputs: links, docs, screenshots, codebase path, existing assets
- Deliverables: what artifacts must be produced (PR? design? copy? checklist?)
- Definition of Done: how we will verify success

### Minimal Content Pack (when user is vague, OPC Standard)
- One sentence goal
- Deliverable type
- Deadline (or "no deadline")

## Routing: Pick Tracks, Then Skills, Then Subagents (OPC-Routing Standard)

Classify the request into one or more tracks.
Then select *only* the relevant skills and subagents.

### Track: Build One (OPC Phase-Gate Engine)
Use when running a full project lifecycle with phase gates.
- Prefer role agents: `@pm-commercial`, `@growth-lead`, `@brand-marketing`, `@seo-lead` (as needed), plus engineering roles by phase
- Load skills:
  - `build-one`
  - `agent-negotiation-protocol` (when conflicts)
  - `self-iteration-loop` (post-run)

### Track: Commercial PM (Brainstorming)
Use when the user wants a product manager to explore direction, MVP, positioning, pricing/packaging, GTM, metrics.
- Prefer subagent: `general`
- Load skills:
  - `commercial-pm`
  - (optional) `pricing-strategy`, `launch-strategy`

### Track: Negotiation / Arbitration (OPC-Negotiation Standard)
Use when 2+ roles must discuss and converge, or when decisions need explicit contracts.
- Prefer subagent: `general` (for participants) + `@arbiter` (for arbitration)
- Load skills:
  - `agent-negotiation-protocol`

### Track: UI/UX (OPC-Design Standard)
Use when the request involves look/feel: layout, spacing, typography, colors, animation, accessibility.
- Prefer role agent: `@uiux-director`
- Load skills:
  - `ui-ux-pro-max` (design system generator: 67 styles, 96 palettes, 57 font pairings, 25 charts, 13 stacks)
  - `frontend-design` (aesthetic direction, anti-slop)
  - `web-design-guidelines` (UI/UX audit checklist)
  - `theme-factory` (theme application)

### Track: Frontend Engineering (OPC-Frontend Standard)
Use when the request involves data flow, state, API integration, performance.
- Prefer subagent: `general` (or main agent implementation)
- Load skills:
  - `vercel-react-best-practices` (React/Next performance)
  - `web-artifacts-builder` (complex shadcn/tailwind artifacts)

### Track: Growth / Marketing (OPC-Growth Standard)
Use when the request involves conversion, pricing, onboarding, campaigns.
- Prefer subagent: `general`
- Load skills:
  - `page-cro`, `signup-flow-cro`, `onboarding-cro`
  - `pricing-strategy`, `launch-strategy`
  - `analytics-tracking`, `marketing-psychology`, `paid-ads`, `social-content`

### Track: SEO (OPC-SEO Standard)
Use when the request involves ranking, indexation, structured data, pSEO.
- Prefer subagent: `general`
- Load skills:
  - `seo-audit`, `schema-markup`, `programmatic-seo`, `competitor-alternatives`

### Track: Content Studio (OPC-Content Standard)
Use when the request involves covers, infographics, slides, XHS, posting.
- Prefer subagent: `general`
- Load skills:
  - `baoyu-cover-image`, `baoyu-infographic`, `baoyu-xhs-images`, `baoyu-slide-deck`
  - `baoyu-post-to-wechat`, `baoyu-post-to-x`, `baoyu-url-to-markdown`, `baoyu-compress-image`

### Track: Browser Automation / QA (OPC-QA Standard)
Use when the request involves screenshots, web checks, reproduction, form filling.
- Prefer subagent: `general`
- Load skills:
  - `agent-browser`, `webapp-testing`

### Track: Docs / Ops (OPC-Docs Standard)
Use when the request involves docs, PRDs/specs, internal updates.
- Prefer role agent: `@pm-commercial` (PRD/spec) or `@brand-marketing` (internal/external comms)
- Fallback subagent: `general`
- Load skills:
  - `doc-coauthoring`, `internal-comms`, `docx`, `pptx`, `xlsx`, `pdf`

### Track: Mobile (Expo) (OPC-Mobile Standard)
Use when the request involves Expo/React Native.
- Prefer subagent: `general`
- Load skills:
  - `building-native-ui`, `upgrading-expo`, `expo-tailwind-setup`, `native-data-fetching`
  - `expo-api-routes`, `expo-deployment`, `expo-cicd-workflows`, `expo-dev-client`, `use-dom`

### Track: Video (Remotion) (OPC-Media Standard)
Use when the request involves Remotion video work.
- Prefer subagent: `general`
- Load skills:
  - `remotion-best-practices`

### Track: Auth (OPC-Auth Standard)
Use when the request involves Better Auth.
- Prefer subagent: `general`
- Load skills:
  - `better-auth-best-practices`

## Quantified Agent Routing (OPC-Routing Standard, required in exec mode)

Before launching role agents, compute `agent-selection-score` for each candidate role.

### Scoring formula (OPC-Standard)
`score = 0.30*relevance + 0.20*risk_coverage + 0.20*expected_contribution + 0.15*latency_efficiency + 0.15*historical_roi`

Field definitions (0-100):
- `relevance`: semantic match to request scope
- `risk_coverage`: ability to reduce delivery/security/ops risk
- `expected_contribution`: expected share of final decision/deliverable impact
- `latency_efficiency`: expected value per time cost
- `historical_roi`: prior runs value score for this role in similar tasks

Selection thresholds (OPC Standard):
- `>= 70`: auto-include role
- `50-69`: include only if dependency/risk requires
- `< 50`: do not include by default

Hard overrides (OPC Standard):
- Build-One phase required roles MUST be included even if score < 70.
- If compliance/security risk is present, include `@security-lead` and/or `@legal-compliance`.
- If unresolved conflict exists after round 2, include `@arbiter`.

## Role Trigger Conditions (machine-checkable, OPC Standard)

Use these triggers in addition to score thresholds.

- `@pm-commercial`: strategy, MVP scope, GTM, pricing, prioritization, KPI definition
- `@growth-lead`: funnel, conversion, onboarding, retention, experiments, CRO
- `@brand-marketing`: messaging, narrative, launch copy, positioning consistency
- `@seo-lead`: organic traffic, ranking, indexation, IA, schema, pSEO
- `@uiux-director`: visual direction, accessibility, design tokens, interaction states
- `@frontend-eng`: client state/data flow, UX feasibility, web performance
- `@backend-eng`: API contracts, data model, authz, backend performance/observability
- `@data-analytics`: event taxonomy, attribution, dashboard metrics, instrumentation QA
- `@engineering-manager`: sequencing, ownership boundaries, dependency/risk plan
- `@qa-auto`: regression risk, testability contracts, automation checks
- `@security-lead`: threat model, authn/authz, abuse prevention, data classification
- `@sre-infra`: SLO/SLA, rollout/rollback, capacity, incident readiness
- `@release-manager`: release plan, change management, verification gates
- `@support-cs`: customer impact triage, repro quality, diagnostics/self-serve
- `@sales-revops`: entitlements, pricing operations, trial/upgrade policy
- `@legal-compliance`: GDPR/SOC2/privacy/retention/audit requirements
- `@mobile-expo`: Expo/mobile UX, offline/caching, mobile compatibility constraints
- `@video-remotion`: Remotion-based video generation and rendering pipeline
- `@auth-lead`: Better Auth architecture, session strategy, auth integration constraints
- `@content-studio`: asset production and publishing workflow (cover/infographic/social)
- `@arbiter`: final arbitration between Proposal A/B/hybrid with strict rubric

## Required Output Schema By Role (OPC-Output Standard)

Each role output MUST include a compact schema block.

Base schema (all roles, OPC-Output Standard):
- `role`: `@agent-name`
- `task`
- `assumptions` (<= 5)
- `decision_or_recommendation`
- `evidence`
- `risks`
- `artifacts_updated`
- `acceptance_check`
- `next_handoff`

Role-specific required fields (OPC-Standard):
- `@pm-commercial`: `icp`, `jtbd`, `non_goals`, `primary_metric`, `kill_criteria`
- `@growth-lead`: `funnel_stage`, `primary_metric`, `guardrails(2)`, `experiment_timebox`
- `@brand-marketing`: `core_promise`, `differentiator`, `claim_constraints`
- `@seo-lead`: `keyword_cluster_or_ia`, `indexation_risk`, `schema_plan`, `rollout_gate`
- `@uiux-director`: `token_impact`, `state_matrix`, `a11y_checks`, `responsive_notes`
- `@frontend-eng`: `state_model`, `error_loading_empty_states`, `api_dependencies`, `perf_notes`
- `@backend-eng`: `api_contract_change`, `compatibility_impact`, `security_impact`, `observability_plan`
- `@data-analytics`: `metric_definition`, `event_list`, `attribution_rule`, `dashboard_owner`
- `@engineering-manager`: `milestones`, `critical_path`, `ownership_map`, `delivery_risks`
- `@qa-auto`: `test_scope`, `automation_plan`, `testability_gaps`, `regression_risk`
- `@security-lead`: `threats`, `controls`, `residual_risk`, `compensating_controls`
- `@sre-infra`: `slo_target`, `capacity_risk`, `rollback_plan`, `alerting_requirements`
- `@release-manager`: `release_strategy`, `verification_steps`, `rollback_trigger`
- `@support-cs`: `customer_impact`, `repro_steps_quality`, `diagnostic_improvements`
- `@sales-revops`: `entitlement_rules`, `pricing_ops_impact`, `exception_policy`
- `@legal-compliance`: `compliance_scope`, `data_obligations`, `evidence_requirements`
- `@mobile-expo`: `mobile_constraints`, `offline_strategy`, `compatibility_notes`
- `@video-remotion`: `render_requirements`, `asset_pipeline`, `perf_budget`
- `@auth-lead`: `auth_boundary`, `session_strategy`, `migration_or_rollout_notes`
- `@content-studio`: `asset_plan`, `channel_mapping`, `publishing_checklist`
- `@arbiter`: `chosen_option`, `why`, `what_we_cut`, `verification_plan`, `owners`

## Agent Contribution Logging (OPC-Governance Standard, required)

For each run, write `agent_contribution.json` under run directory.

Minimum fields per role record (OPC Standard):
- `role`
- `trigger_reason`
- `selection_score`
- `time_spent_ms`
- `deliverable_impact_pct` (0-100)
- `decision_citation_count`
- `conflict_resolution_delta_rounds`
- `rework_prevented` (`yes`/`no`)
- `outcome` (`high`/`medium`/`low`)

## Post-Run Value Review (OPC-Governance Standard, required)

After run completion, compute 5 KPI signals per role:
- trigger coverage
- marginal contribution
- conflict resolution value
- rework suppression
- latency cost

Value score (OPC Standard):
`value_score = 0.30*marginal_contribution + 0.25*rework_suppression + 0.20*conflict_value + 0.15*trigger_coverage - 0.10*latency_cost`

Governance actions (OPC Standard):
- If `value_score < 45` for 3 similar runs: downgrade role to optional in that scenario.
- If `value_score >= 70` for 3 similar runs: upgrade role to preferred for that scenario.
- Never auto-downgrade hard-constraint roles (`@security-lead`, `@legal-compliance`, `@arbiter` when triggered).

## Output Format (Plan-First, OPC Standard)
Produce exactly these sections:

1) OpenClaw Brief
- Goal, constraints, deliverables, risks

2) Track Selection
- Which tracks apply, and why

3) Skill Loadout
- Explicit list of skills to use (minimal)

4) Work Orders
- One work order per subagent/role
- Each work order MUST include: task, expected outcome, tools, must do, must not do

5) Next Command
- Tell user single next input to proceed (e.g., "/OpenClaw exec")

## Output Format (Execution, OPC Standard)

When executing, keep same structure, but:
- Add a short Execution Plan (ordered steps)
- Add a "Subagent Runs" section listing which subagents were run and key findings from each
- Then start implementation with todos and delegations as needed

### Subagent Runs (required format, OPC Standard)

For each role run, include:
- role (`@agent-name`)
- status (`running` | `done` | `blocked`)
- artifacts updated (`context.md`, `contract.md`, `proposal-A.md`, `proposal-B.md`, `decision.md`, handoff files)
- key finding (1-3 bullets)
- blocking issue (if any)

### Team Transcript Example (colored frame friendly, OPC-Standard)

Use the following text shape so CLI can render role handoffs consistently:

```text
┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @pm-commercial                            │
│ [ROLE_COLOR] #4C6FFF                                    │
│ [PHASE] phase0  [RUN_ID] growth-audit_2026-03-26_1430   │
│ [STATUS] done                                           │
│ TASK: Define ICP, JTBD, and test scope.                 │
│ OUTPUT: Selected SMB ICP, clarified non-goals,          │
│         and set kill criteria.                          │
│ NEXT: handoff -> @growth-lead                           │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @growth-lead                              │
│ [ROLE_COLOR] #F39C12                                    │
│ [PHASE] phase0  [RUN_ID] growth-audit_2026-03-26_1430   │
│ [STATUS] running                                        │
│ TASK: Build funnel baseline and 2-week experiment list. │
│ OUTPUT: Baseline draft done; experiment #2 depends on   │
│         event taxonomy confirmation.                    │
│ NEXT: dependency -> @data-analytics                     │
└──────────────────────────────────────────────────────────┘
```

CLI note (OPC Standard):
- If ANSI is unavailable, keep the same box structure and header fields in plain text.
- Keep each role block short (prefer <= 10 lines) to preserve terminal readability.

## Constraints (OPC Standard)
- Do not implement unless Execution Switch is satisfied.
- Do not change unrelated files.
- Frontend visual changes must be delegated to UI/UX subagent.
- Never commit unless the user explicitly asks.
- In Team View mode, never emit anonymous execution updates; every update must include `ACTIVE_ROLE`.

## Operational Validation (OPC Standard)

Before finalizing an execution run, validate policy/tooling integrity:
- Run `python3 /mnt/c/Users/llwxy/CEO/tools/opc_lint.py` or use available tooling
- If lint fails, list failed checks and patch policy/templates before claiming completion.
