# CEO Architecture

This document describes the internal architecture of the CEO orchestration framework.

## Core Components

```
┌─────────────────────────────────────────────────────────────┐
│                      CEO Orchestrator                       │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │  Trigger     │  │  Context     │  │  Routing     │ │
│  │  Gate        │  │  Collector   │  │  Engine      │ │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘ │
│         │                 │                 │            │
│         v                 v                 v            │
│  ┌─────────────────────────────────────────────────┐   │
│  │          Mode Selector                        │   │
│  │  (Plan-First / Execution / Ad-Hoc)         │   │
│  └────────────┬────────────────────────────────┘   │
│               │                                    │
│               v                                    │
│  ┌──────────────────────────────────────────────┐  │
│  │      Agent Selection Engine                │  │
│  │  - Scoring (5-dimension weighted)         │  │
│  │  - Threshold checks                      │  │
│  │  - Hard overrides                       │  │
│  └──────┬──────────────────────┬───────────┘  │
│         │                      │               │
│         v                      v               │
│  ┌──────────────┐    ┌────────────────┐      │
│  │   Skills     │    │   Role Agents │      │
│  │   Loader     │    │   Manager     │      │
│  └──────────────┘    └────────────────┘      │
│         │                      │               │
│         └──────────┬───────────┘               │
│                    v                           │
│  ┌──────────────────────────────────────────┐   │
│  │      Execution Coordinator            │   │
│  │  - Parallel batch orchestration        │   │
│  │  - Handoff enforcement               │   │
│  │  - Negotiation protocol             │   │
│  │  - Arbitration escalation           │   │
│  └──────┬───────────────────────────────┘   │
│         │                                   │
│         v                                   │
│  ┌──────────────────────────────────────────┐   │
│  │      Artifact Manager                │   │
│  │  - Context sharding                  │   │
│  │  - Handoff files                    │   │
│  │  - Contribution logging              │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Trigger Phase

```
User Input
    │
    v
Trigger Gate Check
    │
    ├─→ No: Exit (not CEO request)
    └─→ Yes: Continue
        │
        v
Content Pack Collection
```

### 2. Routing Phase

```
Content Pack
    │
    v
Track Classification
    │
    v
Skill Selection
    │
    v
Agent Scoring
    │
    v
Final Role List
```

### 3. Mode Selection

```
Request Analysis
    │
    ├─→ Has "/CEO exec" → Execution Mode
    ├─→ Has "/CEO exec adhoc" → Ad-Hoc Mode
    └─→ No explicit exec → Plan-First Mode
```

### 4. Execution Phase (Build-One)

```
Phase 0: Feasibility
    │
    v
Batch A: PM + Growth + Brand (+ SEO)
    │
    v
Handoff 0→1
    │
    v
Phase 1: Solution
    │
    v
Batch B: PM + UI/UX + Front/Backend + Data
    │
    v
Handoff 1→2
    │
    v
Phase 2: Delivery
    │
    v
Batch C: EM + Front/Backend + QA (+ Security/SRE)
    │
    v
Handoff 2→3
    │
    v
Phase 3: Launch/Ops
    │
    v
Batch D: Release + Growth (+ SEO) + Support + Data
```

## Context Sharding Model

CEO uses a hierarchical context model to manage information flow:

```
Run Directory/
├── context/
│   ├── global.md              # Single source of truth
│   ├── shards/
│   │   ├── pm-commercial.md   # PM-specific context
│   │   ├── growth-lead.md    # Growth-specific context
│   │   └── ...
│   └── handoffs/
│       ├── pm-to-growth.md   # Explicit transfer
│       └── ...
├── artifacts/
│   ├── context.md
│   ├── contract.md
│   ├── proposal-A.md
│   ├── proposal-B.md
│   └── decision.md
└── agent_contribution.json
```

### Sharding Rules

1. **Isolation**: Each subagent only receives its shard + shared constraints
2. **No Assumptions**: Subagents must request missing info, not infer
3. **Explicit Handoffs**: All cross-role info must be in handoff files
4. **Single Source**: Global.md is the authority for project-wide facts

## Agent Selection Algorithm

### Scoring Formula

```python
def calculate_agent_score(agent, request):
    relevance = semantic_match(agent.capabilities, request) * 0.30
    risk_coverage = assess_risk_reduction(agent, request) * 0.20
    contribution = estimate_contribution(agent, request) * 0.20
    efficiency = compute_latency_efficiency(agent, request) * 0.15
    roi = get_historical_roi(agent, request_type) * 0.15

    return relevance + risk_coverage + contribution + efficiency + roi
```

### Selection Flow

```
For each candidate agent:
    ├─ Calculate score (0-100)
    ├─ Check trigger conditions
    ├─ Apply score thresholds
    └─ Check hard overrides

Final list:
    ├─ Auto-include (score >= 70)
    ├─ Conditional (50-69, if needed)
    └─ Hard-override (security/legal/arbiter)
```

## Negotiation Protocol

When 2+ roles disagree:

```
Round 1:
    ├─ Role A creates Proposal A
    ├─ Role B creates Proposal B
    └─ CEO compares

Round 2 (if conflict):
    ├─ Role A refines based on B
    ├─ Role B refines based on A
    └─ CEO re-evaluates

Escalation (if still conflict):
    └─ @arbiter makes final decision
```

## Post-Run Review

### Contribution Tracking

```json
{
  "role": "@pm-commercial",
  "trigger_reason": "Strategy planning needed",
  "selection_score": 85,
  "time_spent_ms": 124000,
  "deliverable_impact_pct": 40,
  "decision_citation_count": 3,
  "conflict_resolution_delta_rounds": 0,
  "rework_prevented": "yes",
  "outcome": "high"
}
```

### Value Scoring

```python
def calculate_value_score(record):
    marginal_contribution = score_component(record, "marginal") * 0.30
    rework_suppression = score_component(record, "rework") * 0.25
    conflict_value = score_component(record, "conflict") * 0.20
    trigger_coverage = score_component(record, "coverage") * 0.15
    latency_cost = -score_component(record, "latency") * 0.10

    return (marginal_contribution + rework_suppression +
            conflict_value + trigger_coverage + latency_cost)
```

### Governance

```
Value Score < 45 for 3 similar runs:
    └─ Downgrade role to optional

Value Score >= 70 for 3 similar runs:
    └─ Upgrade role to preferred
```

## Output Schema

### Team Event Schema

```json
{
  "event_type": "team_role_update",
  "run_id": "project_2026-03-26_1430",
  "phase": "phase1",
  "agent_id": "pm-commercial",
  "agent_label": "@pm-commercial",
  "role_color": "#4C6FFF",
  "status": "done",
  "task": "Define MVP scope and acceptance criteria",
  "output": "MVP scoped to 3 core features",
  "next": "handoff -> @uiux-director",
  "ts": "2026-03-26T14:38:12Z",
  "artifacts": ["01-phase1-solution.md", "01-02-handoff.md"],
  "duration_ms": 452000
}
```

## Design Tools Integration

```
Visual Work Request
    │
    v
@uiux-director activated
    │
    v
Load design skills (ui-ux-pro-max, frontend-design)
    │
    v
Use Pencil/Stitch for design
    │
    v
Generate .pen files
    │
    v
Export to code (when approved)
```

## Key Design Principles

1. **Explicit Over Implicit**: Everything must be stated, never assumed
2. **Stateless Agents**: Fresh context per run, no hidden memory
3. **Structured Output**: JSON/event schemas for parsing
4. **Quantified Decisions**: Scoring over intuition
5. **Colored Visibility**: Clear role attribution in all output
