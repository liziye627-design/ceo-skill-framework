# CEO Orchestration Framework for Claude Code

> "Contents is all you need" - A CEO-style orchestration router for AI-powered software development teams.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-brightgreen)

## Overview

CEO is a skill-based orchestration framework for Claude Code that transforms the AI agent into a full-stack development team coordinator. It applies the "Contents is all you need" philosophy to intelligently route work to the right skills and subagents at the right time.

### What CEO Does

- **Context-First Approach**: Collects the right context before deciding implementation
- **Intelligent Routing**: Selects appropriate skills and role agents based on task analysis
- **Phase-Gated Execution**: Uses the Build One lifecycle for production-grade delivery
- **Parallel Execution**: Coordinates multiple role agents simultaneously
- **Structured Collaboration**: Enforces clear handoffs and accountability

## Features

### Core Capabilities

| Feature | Description |
|---------|-------------|
| **Plan-First Mode** | Produces clear plans before execution, preventing unwanted changes |
| **Execution Mode** | Implements work with full team coordination |
| **Quantified Agent Routing** | Scores and selects agents based on 5 weighted dimensions |
| **Context Sharding** | Isolates memory between subagents for clean handoffs |
| **Team View Protocol** | Colored, structured output for clear agent separation |
| **Post-Run Review** | Tracks agent contribution for continuous improvement |

### Role Agents

CEO works with a comprehensive set of role agents:

| Role | Color | Focus |
|------|-------|-------|
| `@pm-commercial` | #4C6FFF | Strategy, MVP, GTM, pricing |
| `@growth-lead` | #F39C12 | Funnel, conversion, experiments |
| `@brand-marketing` | #E74C3C | Messaging, narrative, positioning |
| `@seo-lead` | #27AE60 | Organic traffic, ranking, schema |
| `@uiux-director` | #9B59B6 | Visual direction, accessibility, design tokens |
| `@frontend-eng` | #3498DB | Client state, data flow, performance |
| `@backend-eng` | #2C3E50 | API contracts, data model, observability |
| `@data-analytics` | #16A085 | Event taxonomy, attribution, metrics |
| `@engineering-manager` | #7F8C8D | Sequencing, ownership, risk planning |
| `@qa-auto` | #E67E22 | Test scope, automation, regression |
| `@security-lead` | #C0392B | Threat model, authn/authz, data classification |
| `@sre-infra` | #8E44AD | SLO/SLA, rollout, capacity |
| `@release-manager` | #D35400 | Release plan, verification, rollback |
| `@support-cs` | #2980B9 | Customer impact, repro quality |
| `@sales-revops` | #6C3483 | Entitlements, pricing operations |
| `@legal-compliance` | #1A5276 | GDPR/SOC2, privacy, audit |
| `@mobile-expo` | #95A5A6 | Expo/mobile UX, offline, compatibility |
| `@video-remotion` | #D98880 | Video generation, rendering pipeline |
| `@auth-lead` | #17A589 | Auth architecture, session strategy |
| `@content-studio` | #F7DC6F | Asset production, publishing workflow |
| `@arbiter` | #5D6D7E | Final arbitration between proposals |

## Usage

### Triggering CEO

CEO requires explicit invocation:

```
/CEO
```

For immediate execution:

```
/CEO exec
```

For ad-hoc execution (bypassing phase gates):

```
/CEO exec adhoc
```

### Default Behavior

When invoked without `exec`, CEO operates in **Plan-First mode**:
1. Produces a CEO Brief
2. Creates Work Orders for each role
3. Requests confirmation before proceeding

This ensures you have full control over what gets implemented.

### Build One Gate

When using `build-one` execution mode, Phase 1 starts only after CEO explicitly says:

```
子叶君出击
```

This is a hard gate that prevents premature implementation.

## Tracks

CEO classifies requests into tracks for optimal skill loading:

| Track | Use Case | Skills Loaded |
|-------|-----------|---------------|
| **Build One** | Full project lifecycle with phase gates | `build-one`, `agent-negotiation-protocol` |
| **Commercial PM** | Brainstorming direction, MVP, pricing | `commercial-pm` |
| **Negotiation** | Multi-role convergence or contracts | `agent-negotiation-protocol` |
| **UI/UX** | Visual design, layout, typography | `ui-ux-pro-max`, `frontend-design` |
| **Frontend** | Data flow, state, API integration | `vercel-react-best-practices` |
| **Growth/Marketing** | Conversion, pricing, campaigns | `page-cro`, `pricing-strategy`, `analytics-tracking` |
| **SEO** | Ranking, indexation, structured data | `seo-audit`, `schema-markup`, `pSEO` |
| **Content Studio** | Assets, covers, publishing | `baoyu-*` skills |
| **Browser/QA** | Screenshots, web checks | `agent-browser`, `webapp-testing` |
| **Docs/Ops** | PRDs, specs, internal comms | `doc-coauthoring`, `docx`, `pptx` |
| **Mobile (Expo)** | Expo/React Native projects | `building-native-ui`, `expo-*` |
| **Video (Remotion)** | Remotion video work | `remotion-best-practices` |
| **Auth** | Better Auth integration | `better-auth-best-practices` |

## Project Structure

```
CEO/projects/{PROJECT}/runs/YYYY-MM-DD_HHMM/
├── context.md                    # Global context (single source of truth)
├── contract.md                   # Cross-role contracts (when needed)
├── proposal-A.md                 # Option A (when negotiating)
├── proposal-B.md                 # Option B (when negotiating)
├── decision.md                   # Final decision
├── 00-01-handoff.md            # Phase 0 to 1 handoff (build-one)
├── 01-02-handoff.md            # Phase 1 to 2 handoff
├── 02-03-handoff.md            # Phase 2 to 3 handoff
└── agent_contribution.json       # Role contribution tracking
```

## Installation

### For Claude Code Users

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ceo-skill-framework.git
   cd ceo-skill-framework
   ```

2. Copy the skill to your Claude Code skills directory:
   ```bash
   mkdir -p ~/.claude/skills
   cp -r skills/* ~/.claude/skills/
   ```

3. Restart Claude Code

### For Role Agents

Install role agents to `~/.opencode/agent/` for colored, readable team output.

## Output Format

### Plan-First Output

```
1) CEO Brief
   - Goal, constraints, deliverables, risks

2) Track Selection
   - Which tracks apply, and why

3) Skill Loadout
   - Explicit list of skills to use

4) Work Orders
   - One per subagent/role

5) Next Command
   - Single input to proceed (e.g., "/CEO exec")
```

### Execution Output

```text
┌──────────────────────────────────────────────────────────┐
│ [ACTIVE_ROLE] @pm-commercial                            │
│ [ROLE_COLOR] #4C6FFF                                    │
│ [PHASE] phase0  [RUN_ID] growth-audit_2026-02-06_1430   │
│ [STATUS] done                                           │
│ TASK: Define ICP, JTBD, and test scope.                 │
│ OUTPUT: Selected SMB ICP, clarified non-goals,          │
│         and set kill criteria.                          │
│ NEXT: handoff -> @growth-lead                           │
└──────────────────────────────────────────────────────────┘
```

## Design Philosophy

### Contents is All You Need

CEO starts by gathering a "Content Pack" before making decisions:

- **Goal**: What outcome are we optimizing for?
- **Audience**: Who is this for?
- **Constraints**: time, budget, tech stack, brand, compliance
- **Inputs**: links, docs, screenshots, codebase path
- **Deliverables**: what artifacts must be produced
- **Definition of Done**: how we will verify success

### Subagent Memory Isolation

CEO enforces stateless subagent execution:
- Fresh context per run
- No hidden memory assumptions
- Explicit handoffs via artifacts
- Context sharding for role relevance

### Quantified Decision Making

Agent selection uses a weighted scoring formula:

```
score = 0.30*relevance +
        0.20*risk_coverage +
        0.20*expected_contribution +
        0.15*latency_efficiency +
        0.15*historical_roi
```

Thresholds:
- `>= 70`: Auto-include
- `50-69`: Include if dependency/risk requires
- `< 50`: Do not include by default

## Parallel Execution Matrix

CEO coordinates parallel work in batches:

| Batch | Phase | Roles |
|--------|--------|-------|
| **A** | Feasibility | PM, Growth, Brand, (SEO) |
| **B** | Solution | PM, UI/UX, Frontend/Backend, Data |
| **C** | Delivery | Eng Manager, Frontend/Backend, QA, (Security/SRE) |
| **D** | Launch/Ops | Release, Growth (SEO), Support, Data |

## Contributing

Contributions are welcome! Areas of interest:

- Additional role agents
- Skill integrations
- Documentation improvements
- Example workflows
- Tooling (linting, validation)

## License

MIT License - see LICENSE file for details.

## Acknowledgments

Built for Claude Code by the AI development community.

## Links

- [Claude Code](https://claude.ai/claude-code)
- [SKILL.md Specification](https://github.com/anthropics/claude-code-skills)
