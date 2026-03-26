# SaaS Launch Example (Full Build-One)

## Request

```
/CEO Launch a new SaaS product: AI-powered task manager for remote teams
```

## Expected Track

**Track**: Build One (Full 4-phase lifecycle)

## Expected Roles by Phase

### Phase 0: Feasibility
- **@pm-commercial**: Define ICP, JTBD, MVP scope, kill criteria
- **@growth-lead**: Funnel baseline, 2-week experiment list
- **@brand-marketing**: Core promise, differentiator, claim constraints
- **@seo-lead** (if organic growth needed): Keyword cluster, schema plan

### Phase 1: Solution
- **@pm-commercial**: Validate Phase 0, refine requirements
- **@uiux-director**: Create full UI design via Pencil
- **@frontend-eng**: Define state model, API dependencies
- **@backend-eng**: Design API contracts, data model
- **@data-analytics**: Define metrics, events, attribution

### Phase 2: Delivery
- **@engineering-manager**: Define milestones, critical path, ownership
- **@frontend-eng**: Implement features
- **@backend-eng**: Build APIs
- **@qa-auto**: Test scope, automation plan
- **@security-lead** (if auth/data sensitive): Threat model, controls

### Phase 3: Launch/Ops
- **@release-manager**: Release strategy, verification steps
- **@growth-lead**: Launch campaigns, post-launch experiments
- **@seo-lead** (if relevant): SEO rollout gate
- **@support-cs**: Customer impact triage, diagnostics

## Expected Gate Phrases

```
After Phase 0:
CEO: "Phase 0 complete. Waiting for: 子叶君出击"

After gate phrase:
CEO: "子叶君出击 - Phase 1 starting"
```

## Artifacts Created

```
CEO/projects/ai-task-manager/runs/2026-03-26_1430/
├── context/
│   ├── global.md
│   ├── shards/
│   │   ├── pm-commercial.md
│   │   ├── growth-lead.md
│   │   ├── brand-marketing.md
│   │   ├── uiux-director.md
│   │   ├── frontend-eng.md
│   │   ├── backend-eng.md
│   │   ├── data-analytics.md
│   │   ├── engineering-manager.md
│   │   ├── qa-auto.md
│   │   ├── release-manager.md
│   │   └── support-cs.md
│   └── handoffs/
│       ├── 00-01-handoff.md
│       ├── 01-02-handoff.md
│       └── 02-03-handoff.md
├── artifacts/
│   ├── context.md
│   ├── 00-phase0-feasibility.md
│   ├── 01-phase1-solution.md
│   ├── 02-phase2-delivery.md
│   ├── 03-phase3-launch.md
│   ├── contract.md
│   └── decision.md
└── agent_contribution.json
```

## Obsidian Digest (Summary)

CEO writes a condensed summary to Obsidian:

```
ObsidianVault/Reports/CEO/ai-task-manager/2026-03-26-ai-task-manager.md

# AI Task Manager - Launch Summary

## What We Did
- Launched AI-powered task manager for remote teams
- Completed full 4-phase Build-One lifecycle
- MVP includes: AI prioritization, team collaboration, analytics

## Technical Hard Parts
- AI scoring algorithm integration
- Real-time collaboration via WebSocket
- Responsive design with complex state

## Achievements
- First 100 users in 2 weeks
- Lighthouse score: 96
- Zero critical bugs in first week

## Reflections
- QA automation should have started earlier
- Handoffs between frontend/backend were smooth

## Next Actions
- A/B test AI weighting
- Add mobile app
```
