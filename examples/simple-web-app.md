# Simple Web Application Example

## Request

```
/CEO Build a landing page for a developer tool SaaS
```

## Expected Track

**Track**: UI/UX + Frontend Engineering

## Expected Roles

1. **@pm-commercial** (if in exec mode)
   - Define core value proposition
   - Set success metrics

2. **@uiux-director**
   - Create visual design using Pencil
   - Define design tokens
   - Plan responsive layout

3. **@frontend-eng**
   - Implement React components
   - Set up Tailwind CSS
   - Ensure performance

## Expected Plan-First Output

```
1) CEO Brief
   Goal: Build a landing page for developer tool SaaS
   Constraints: Web stack, performance-focused
   Deliverables: Landing page with 3 sections
   Risks: None identified

2) Track Selection
   - UI/UX: Visual design required
   - Frontend: Implementation needed

3) Skill Loadout
   - ui-ux-pro-max (design system)
   - frontend-design (aesthetic direction)
   - vercel-react-best-practices (performance)

4) Work Orders
   - @uiux-director: Create hero section, features, pricing cards
   - @frontend-eng: Implement responsive React components

5) Next Command
   Reply with: /CEO exec
```

## Expected Execution Output (Simplified)

```
┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @pm-commercial                            │
│ [ROLE_COLOR] #4C6FFF                                    │
│ [PHASE] adhoc  [RUN_ID] landing_2026-03-26_1430        │
│ [STATUS] done                                           │
│ TASK: Define value prop and success metrics.               │
│ OUTPUT: "Ship faster with AI-powered code review"          │
│         Success: 20% signup conversion                    │
│ NEXT: handoff -> @uiux-director                         │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @uiux-director                           │
│ [ROLE_COLOR] #9B59B6                                    │
│ [PHASE] adhoc  [RUN_ID] landing_2026-03-26_1430        │
│ [STATUS] done                                           │
│ TASK: Create hero + features + pricing design.             │
│ OUTPUT: Dark theme, glassmorphism, 3 sections            │
│         Design tokens exported to .pen file                │
│ NEXT: handoff -> @frontend-eng                         │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @frontend-eng                             │
│ [ROLE_COLOR] #3498DB                                    │
│ [PHASE] adhoc  [RUN_ID] landing_2026-03-26_1430        │
│ [STATUS] done                                           │
│ TASK: Implement React + Tailwind components.              │
│ OUTPUT: 4 components (Hero, Features, Pricing, CTA)     │
│         Performance: Lighthouse 95+                       │
│ NEXT: Complete                                          │
└──────────────────────────────────────────────────────────┘
```

## Artifacts Created

```
CEO/projects/landing-page/runs/2026-03-26_1430/
├── context.md
├── context/shards/pm-commercial.md
├── context/shards/uiux-director.md
├── context/shards/frontend-eng.md
├── context/handoffs/pm-to-uiux.md
├── context/handoffs/uiux-to-frontend.md
└── agent_contribution.json
```
