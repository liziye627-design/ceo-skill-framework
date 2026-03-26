# Role Agents Reference

CEO coordinates a team of specialized role agents. Each agent has a defined color, focus, and responsibility.

## Agent Color Codes

Each role agent uses a specific color for terminal output:

| Agent | Hex Color | RGB |
|--------|------------|------|
| @pm-commercial | #4C6FFF | RGB(76, 111, 255) |
| @growth-lead | #F39C12 | RGB(243, 156, 18) |
| @brand-marketing | #E74C3C | RGB(231, 76, 60) |
| @seo-lead | #27AE60 | RGB(39, 174, 96) |
| @uiux-director | #9B59B6 | RGB(155, 89, 182) |
| @frontend-eng | #3498DB | RGB(52, 152, 219) |
| @backend-eng | #2C3E50 | RGB(44, 62, 80) |
| @data-analytics | #16A085 | RGB(22, 160, 133) |
| @engineering-manager | #7F8C8D | RGB(127, 140, 141) |
| @qa-auto | #E67E22 | RGB(230, 126, 34) |
| @security-lead | #C0392B | RGB(192, 57, 43) |
| @sre-infra | #8E44AD | RGB(142, 68, 173) |
| @release-manager | #D35400 | RGB(211, 84, 0) |
| @support-cs | #2980B9 | RGB(41, 128, 185) |
| @sales-revops | #6C3483 | RGB(108, 52, 131) |
| @legal-compliance | #1A5276 | RGB(26, 82, 118) |
| @mobile-expo | #95A5A6 | RGB(149, 165, 166) |
| @video-remotion | #D98880 | RGB(217, 136, 128) |
| @auth-lead | #17A589 | RGB(23, 165, 137) |
| @content-studio | #F7DC6F | RGB(247, 220, 111) |
| @arbiter | #5D6D7E | RGB(93, 109, 126) |

## Role Definitions

### @pm-commercial
**Color**: #4C6FFF (Blue)

**Focus**: Strategy, MVP scope, GTM, pricing, prioritization, KPI definition

**Required Output Fields**:
- `icp`: Ideal Customer Profile
- `jtbd`: Jobs to Be Done
- `non_goals`: Explicit non-goals
- `primary_metric`: Main success metric
- `kill_criteria`: Conditions that terminate the project

**Trigger Conditions**:
- Strategy discussions
- MVP scope definition
- GTM planning
- Pricing decisions
- Prioritization requests
- KPI definition needed

---

### @growth-lead
**Color**: #F39C12 (Orange)

**Focus**: Funnel, conversion, onboarding, retention, experiments, CRO

**Required Output Fields**:
- `funnel_stage`: Current funnel focus
- `primary_metric`: Main conversion metric
- `guardrails(2)`: Two guardrail constraints
- `experiment_timebox`: Time limit for experiments

**Trigger Conditions**:
- Funnel optimization
- Conversion rate improvement
- Onboarding flow design
- Retention analysis
- Experiment design
- CRO work

---

### @brand-marketing
**Color**: #E74C3C (Red)

**Focus**: Messaging, narrative, launch copy, positioning consistency

**Required Output Fields**:
- `core_promise`: Main value proposition
- `differentiator`: Unique selling point
- `claim_constraints`: Boundaries on what can be claimed

**Trigger Conditions**:
- Messaging development
- Narrative crafting
- Launch copy needed
- Positioning refinement

---

### @seo-lead
**Color**: #27AE60 (Green)

**Focus**: Organic traffic, ranking, indexation, IA, schema, pSEO

**Required Output Fields**:
- `keyword_cluster_or_ia`: Keywords or information architecture
- `indexation_risk`: Potential indexing issues
- `schema_plan`: Structured data strategy
- `rollout_gate`: SEO checkpoint

**Trigger Conditions**:
- Organic traffic growth
- Ranking optimization
- Indexation issues
- IA restructuring
- Schema markup
- Programmatic SEO

---

### @uiux-director
**Color**: #9B59B6 (Purple)

**Focus**: Visual direction, accessibility, design tokens, interaction states

**Required Output Fields**:
- `token_impact`: Design system changes
- `state_matrix`: UI state definitions
- `a11y_checks`: Accessibility requirements
- `responsive_notes`: Mobile/desktop considerations

**Trigger Conditions**:
- Visual design work
- Accessibility audit
- Design system changes
- Interaction states
- Responsive layouts

**Design Tool Policy**: MUST use `pencil` or `stitch` for visual work, not raw code.

---

### @frontend-eng
**Color**: #3498DB (Blue)

**Focus**: Client state/data flow, UX feasibility, web performance

**Required Output Fields**:
- `state_model`: State management approach
- `error_loading_empty_states`: Error handling strategy
- `api_dependencies`: External API requirements
- `perf_notes`: Performance considerations

**Trigger Conditions**:
- Client-side logic
- State management decisions
- API integration
- Performance optimization
- UX feasibility review

---

### @backend-eng
**Color**: #2C3E50 (Dark Blue)

**Focus**: API contracts, data model, authz, backend performance/observability

**Required Output Fields**:
- `api_contract_change`: API modifications
- `compatibility_impact`: Breaking changes assessment
- `security_impact`: Security considerations
- `observability_plan`: Monitoring/logging

**Trigger Conditions**:
- API design/changes
- Data modeling
- Authorization logic
- Performance tuning
- Observability setup

---

### @data-analytics
**Color**: #16A085 (Teal)

**Focus**: Event taxonomy, attribution, dashboard metrics, instrumentation QA

**Required Output Fields**:
- `metric_definition`: Metric formulas
- `event_list`: Events to track
- `attribution_rule`: Attribution logic
- `dashboard_owner`: Dashboard responsibility

**Trigger Conditions**:
- Event tracking setup
- Attribution modeling
- Dashboard requirements
- Instrumentation review

---

### @engineering-manager
**Color**: #7F8C8D (Gray)

**Focus**: Sequencing, ownership boundaries, dependency/risk plan

**Required Output Fields**:
- `milestones`: Key delivery points
- `critical_path`: Dependencies blocking progress
- `ownership_map`: Who owns what
- `delivery_risks`: Risk assessment

**Trigger Conditions**:
- Project planning
- Ownership decisions
- Dependency mapping
- Risk assessment

---

### @qa-auto
**Color**: #E67E22 (Orange)

**Focus**: Regression risk, testability contracts, automation checks

**Required Output Fields**:
- `test_scope`: What to test
- `automation_plan`: Test automation strategy
- `testability_gaps`: Areas needing coverage
- `regression_risk`: Regression probability

**Trigger Conditions**:
- Test planning
- Test automation
- Regression analysis
- Coverage gaps

---

### @security-lead
**Color**: #C0392B (Dark Red)

**Focus**: Threat model, authn/authz, abuse prevention, data classification

**Required Output Fields**:
- `threats`: Identified threats
- `controls`: Mitigation measures
- `residual_risk`: Risk after controls
- `compensating_controls`: Additional safeguards

**Trigger Conditions**:
- Security review required
- Authentication/authorization
- Threat modeling
- Data classification

**Hard Override Role**: Must be included when security/compliance risk exists.

---

### @sre-infra
**Color**: #8E44AD (Purple)

**Focus**: SLO/SLA, rollout/rollback, capacity, incident readiness

**Required Output Fields**:
- `slo_target`: Service level objective
- `capacity_risk`: Scaling concerns
- `rollback_plan`: Rollback procedure
- `alerting_requirements`: Alerting setup

**Trigger Conditions**:
- SLO/SLA definition
- Deployment planning
- Capacity planning
- Incident preparedness

---

### @release-manager
**Color**: #D35400 (Brown)

**Focus**: Release plan, change management, verification gates

**Required Output Fields**:
- `release_strategy`: How to release
- `verification_steps`: What to verify
- `rollback_trigger`: When to roll back

**Trigger Conditions**:
- Release planning
- Change management
- Verification procedures

---

### @support-cs
**Color**: #2980B9 (Dark Blue)

**Focus**: Customer impact triage, repro quality, diagnostics/self-serve

**Required Output Fields**:
- `customer_impact`: User impact assessment
- `repro_steps_quality`: Reproducibility
- `diagnostic_improvements`: Better error messages/logs

**Trigger Conditions**:
- Customer impact analysis
- Bug reproduction
- Diagnostic improvements

---

### @sales-revops
**Color**: #6C3483 (Dark Purple)

**Focus**: Entitlements, pricing operations, trial/upgrade policy

**Required Output Fields**:
- `entitlement_rules`: Feature entitlements
- `pricing_ops_impact`: Pricing changes effect
- `exception_policy`: Exception handling

**Trigger Conditions**:
- Pricing changes
- Entitlement logic
- Trial/upgrade policies

---

### @legal-compliance
**Color**: #1A5276 (Navy)

**Focus**: GDPR/SOC2/privacy/retention/audit requirements

**Required Output Fields**:
- `compliance_scope`: What's in scope
- `data_obligations`: Data handling requirements
- `evidence_requirements`: Audit evidence needed

**Trigger Conditions**:
- GDPR compliance
- SOC2 preparation
- Privacy policy
- Data retention
- Audit requirements

**Hard Override Role**: Must be included when compliance/legal risk exists.

---

### @mobile-expo
**Color**: #95A5A6 (Gray)

**Focus**: Expo/mobile UX, offline/caching, mobile compatibility constraints

**Required Output Fields**:
- `mobile_constraints`: Mobile-specific limitations
- `offline_strategy`: Offline handling
- `compatibility_notes`: Device/OS considerations

**Trigger Conditions**:
- Expo/React Native development
- Mobile UX design
- Offline functionality
- Mobile testing

---

### @video-remotion
**Color**: #D98880 (Salmon)

**Focus**: Remotion-based video generation and rendering pipeline

**Required Output Fields**:
- `render_requirements`: Rendering specs
- `asset_pipeline`: Asset processing
- `perf_budget`: Performance constraints

**Trigger Conditions**:
- Remotion video work
- Rendering pipeline design
- Video performance

---

### @auth-lead
**Color**: #17A589 (Dark Green)

**Focus**: Better Auth architecture, session strategy, auth integration constraints

**Required Output Fields**:
- `auth_boundary`: Auth scope
- `session_strategy`: Session handling
- `migration_or_rollout_notes`: Auth migration notes

**Trigger Conditions**:
- Better Auth setup
- Auth architecture
- Session management
- Auth migrations

---

### @content-studio
**Color**: #F7DC6F (Yellow)

**Focus**: Asset production and publishing workflow (cover/infographic/social)

**Required Output Fields**:
- `asset_plan`: Asset production plan
- `channel_mapping`: Which assets go where
- `publishing_checklist`: Publishing steps

**Trigger Conditions**:
- Cover image creation
- Infographic design
- Social media assets
- Publishing workflows

---

### @arbiter
**Color**: #5D6D7E (Dark Gray)

**Focus**: Final arbitration between Proposal A/B/hybrid with strict rubric

**Required Output Fields**:
- `chosen_option`: A, B, or hybrid
- `why`: Rationale for choice
- `what_we_cut`: Trade-offs made
- `verification_plan`: How to verify the choice
- `owners`: Who's responsible

**Trigger Conditions**:
- Unresolved conflicts after 2 negotiation rounds
- Need for final decision between options

**Hard Override Role**: Must be included when arbitration is needed.

---

## Selection Logic

Roles are selected based on:

1. **Score Threshold** (quantified routing):
   - `>= 70`: Auto-include
   - `50-69`: Include if dependency/risk requires
   - `< 50`: Do not include by default

2. **Trigger Conditions**: Matching the request's semantic content

3. **Hard Overrides**: Required roles (@security-lead, @legal-compliance, @arbiter) when risk exists

4. **Build-One Requirements**: Phase-mandatory roles must be included regardless of score
