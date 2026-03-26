# CEO Orchestration Framework for Claude Code

> "Contents is all you need" - Enterprise-grade AI orchestration system modeled after traditional software development organizations.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-brightgreen)
![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A0-brightgreen)

## What is CEO?

CEO is an **open-source** orchestration framework for Claude Code that transforms a single AI agent into a **complete virtual development organization**. Inspired by traditional enterprise software development structures, CEO orchestrates **20+ specialized role agents** to collaborate, negotiate, and deliver production-grade software.

### Enterprise Architecture Model

```
┌─────────────────────────────────────────────────────────────┐
│                    Virtual CEO Office                      │
│                  (Orchestration Layer)                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Product  │  │ Growth   │  │ Branding │    │
│  │   Team   │  │   Team   │  │   Team   │    │
│  └──────────┘  └──────────┘  └──────────┘    │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   UX/UI  │  │ Frontend │  │ Backend  │    │
│  │   Team   │  │   Team   │  │   Team   │    │
│  └──────────┘  └──────────┘  └──────────┘    │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Security │  │    QA    │  │   Ops    │    │
│  │   Team   │  │   Team   │  │   Team   │    │
│  └──────────┘  └──────────┘  └──────────┘    │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Content  │  │   SEO    │  │ Support  │    │
│  │  Studio  │  │   Team   │  │   Team   │    │
│  └──────────┘  └──────────┘  └──────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Why This Approach Matters

Traditional software companies succeed because they have **specialized teams** working together:

| Traditional Organization | CEO Framework |
|---------------------|---------------|
| Product Managers define strategy | `@pm-commercial` |
| Growth teams optimize funnels | `@growth-lead` |
| Designers create visuals | `@uiux-director` |
| Engineers build features | `@frontend-eng`, `@backend-eng` |
| QA ensures quality | `@qa-auto` |
| Security teams protect users | `@security-lead` |
| Legal/compliance review risks | `@legal-compliance` |

CEO brings this **full organizational structure** to your AI development workflow.

---

## Key Features

### 🏢 Enterprise Organization Structure

- **20+ Specialized Role Agents**: Each with distinct responsibilities and expertise
- **Color-Coded Team Output**: Easy visual identification of which team is speaking
- **Parallel Execution Matrix**: Multiple teams working simultaneously, just like real orgs
- **Explicit Handoffs**: Clear communication between teams, no information lost

### 🎯 Phase-Gated Delivery

```
Phase 0 → Feasibility → Gate → Phase 1 → Solution → Gate →
Phase 2 → Delivery → Gate → Phase 3 → Launch/Ops
```

Each phase has required approvals and can't start without the previous phase's output.

### 📊 Quantified Decision Making

Agents are selected using a **5-dimension weighted scoring system**:

```
score = 30% relevance
      + 20% risk coverage
      + 20% expected contribution
      + 15% latency efficiency
      + 15% historical ROI
```

### 🔄 Conflict Resolution Protocol

When teams disagree, CEO manages a structured negotiation:

1. **Round 1**: Each team creates their proposal
2. **Round 2**: Refine based on feedback
3. **Escalation**: @arbiter makes final decision if needed

### 📝 Complete Artifact System

All work is tracked in structured artifacts:

```
runs/YYYY-MM-DD_HHMM/
├── context/             # Global truth and role-specific shards
├── artifacts/          # Decisions, contracts, proposals
├── handoffs/          # Inter-team communication
└── contribution.json   # Performance metrics per role
```

---

## Role Agents Reference

| Role | Color | Department | Core Responsibility |
|-------|--------|-------------|---------------------|
| `@pm-commercial` | #4C6FFF | Product | Strategy, MVP, GTM, pricing |
| `@growth-lead` | #F39C12 | Growth | Funnel, conversion, experiments |
| `@brand-marketing` | #E74C3C | Marketing | Messaging, narrative, positioning |
| `@seo-lead` | #27AE60 | Marketing | Organic traffic, ranking, schema |
| `@uiux-director` | #9B59B6 | Design | Visual direction, accessibility |
| `@frontend-eng` | #3498DB | Engineering | Client state, data flow |
| `@backend-eng` | #2C3E50 | Engineering | API contracts, data model |
| `@data-analytics` | #16A085 | Analytics | Events, attribution, metrics |
| `@engineering-manager` | #7F8C8D | Management | Sequencing, ownership, risk |
| `@qa-auto` | #E67E22 | QA | Test scope, automation |
| `@security-lead` | #C0392B | Security | Threat model, authn/authz |
| `@sre-infra` | #8E44AD | Ops | SLO/SLA, rollout, capacity |
| `@release-manager` | #D35400 | Release | Release plan, verification |
| `@support-cs` | #2980B9 | Support | Customer impact, triage |
| `@sales-revops` | #6C3483 | Sales | Entitlements, pricing ops |
| `@legal-compliance` | #1A5276 | Legal | GDPR/SOC2, compliance |
| `@mobile-expo` | #95A5A6 | Mobile | Expo/mobile UX |
| `@video-remotion` | #D98880 | Media | Video generation pipeline |
| `@auth-lead` | #17A589 | Auth | Auth architecture |
| `@content-studio` | #F7DC6F | Content | Asset production, publishing |
| `@arbiter` | #5D6D7E | Governance | Final decision maker |

---

## Skills Ecosystem

CEO integrates with a comprehensive skills ecosystem, each representing specialized tools and methodologies:

### 📦 Core Skills

| Skill | Purpose |
|--------|----------|
| `build-one` | Phase-gated project lifecycle framework |
| `commercial-pm` | Product management brainstorming playbook |
| `agent-negotiation-protocol` | Multi-agent conflict resolution system |
| `self-iteration-loop` | Post-run learning and improvement |

### 🎨 Design Skills

| Skill | Purpose |
|--------|----------|
| `ui-ux-pro-max` | 67 styles, 96 palettes, 57 font pairings, 25 charts |
| `frontend-design` | Aesthetic direction and anti-slop patterns |
| `web-design-guidelines` | UI/UX audit checklist |
| `theme-factory` | Theme application system |

### 💻 Engineering Skills

| Skill | Purpose |
|--------|----------|
| `vercel-react-best-practices` | React/Next.js performance optimization |
| `web-artifacts-builder` | Complex shadcn/tailwind component generation |

### 📈 Growth Skills

| Skill | Purpose |
|--------|----------|
| `page-cro` | Page-level conversion rate optimization |
| `signup-flow-cro` | Signup funnel optimization |
| `onboarding-cro` | User onboarding conversion |
| `pricing-strategy` | Pricing and packaging decisions |
| `launch-strategy` | Go-to-market planning |
| `analytics-tracking` | Event tracking implementation |
| `marketing-psychology` | Behavioral design principles |
| `paid-ads` | Advertising campaign optimization |
| `social-content` | Social media content creation |

### 🔍 SEO Skills

| Skill | Purpose |
|--------|----------|
| `seo-audit` | SEO health assessment |
| `schema-markup` | Structured data implementation |
| `programmatic-seo` | pSEO page generation |
| `competitor-alternatives` | Competitor analysis pages |

### 📝 Content Skills

| Skill | Purpose |
|--------|----------|
| `baoyu-cover-image` | Cover image generation |
| `baoyu-infographic` | Infographic creation |
| `baoyu-xhs-images` | XiaoHongShu image generation |
| `baoyu-slide-deck` | Presentation slide creation |
| `baoyu-post-to-wechat` | WeChat publishing |
| `baoyu-post-to-x` | X/Twitter publishing |
| `baoyu-url-to-markdown` | URL content extraction |
| `baoyu-compress-image` | Image optimization |

### 🧪 QA Skills

| Skill | Purpose |
|--------|----------|
| `agent-browser` | Browser automation |
| `webapp-testing` | Web application testing |

### 📄 Documentation Skills

| Skill | Purpose |
|--------|----------|
| `doc-coauthoring` | Collaborative documentation |
| `internal-comms` | Internal communication |
| `docx` | Word document processing |
| `pptx` | PowerPoint presentation handling |
| `xlsx` | Excel spreadsheet operations |
| `pdf` | PDF manipulation |

### 📱 Mobile Skills

| Skill | Purpose |
|--------|----------|
| `building-native-ui` | Native UI construction |
| `upgrading-expo` | Expo project upgrades |
| `expo-tailwind-setup` | Tailwind integration |
| `native-data-fetching` | Data fetching patterns |
| `expo-api-routes` | API route implementation |
| `expo-deployment` | App deployment |
| `expo-cicd-workflows` | CI/CD pipelines |
| `expo-dev-client` | Development client setup |
| `use-dom` | DOM usage patterns |

### 🎬 Video Skills

| Skill | Purpose |
|--------|----------|
| `remotion-best-practices` | Remotion video generation patterns |

### 🔐 Auth Skills

| Skill | Purpose |
|--------|----------|
| `better-auth-best-practices` | Better Auth integration guide |

---

## Usage

### Quick Start

```bash
# Clone the repository
git clone https://github.com/liziye627-design/ceo-skill-framework.git
cd ceo-skill-framework

# Install CEO skill
cp -r skills/ceo ~/.claude/skills/

# Start Claude Code and invoke CEO
/CEO Build a SaaS landing page
```

### Trigger Modes

| Command | Mode | Description |
|---------|-------|-------------|
| `/CEO` | Plan-First | Generates plan, asks for confirmation |
| `/CEO exec` | Execution | Implements with build-one lifecycle |
| `/CEO exec adhoc` | Ad-Hoc | Bypasses phase gates |

### Example Session

```
User: /CEO Build a developer tool SaaS

CEO:
┌──────────────────────────────────────────────────────────┐
│ 1) CEO Brief                                     │
│    Goal: Build developer tool SaaS                  │
│    Deliverables: Landing page + auth + dashboard     │
│                                                     │
│ 2) Track Selection                                  │
│    - Build One (full lifecycle)                      │
│                                                     │
│ 3) Skill Loadout                                    │
│    - ui-ux-pro-max (design system)                 │
│    - vercel-react-best-practices (performance)       │
│    - commercial-pm (product strategy)                │
│                                                     │
│ 4) Work Orders                                      │
│    @pm-commercial: Define ICP and JTBD            │
│    @uiux-director: Create visual design              │
│    @frontend-eng: Implement React components           │
│                                                     │
│ 5) Next Command                                      │
│    Reply with: /CEO exec                             │
└──────────────────────────────────────────────────────────┘
```

---

## Architecture

```
User Request
    │
    ├─→ Trigger Gate (explicit /CEO required)
    │
    v
Content Pack Collection
    │
    v
Track Classification (14+ tracks)
    │
    v
Skill Selection (50+ skills ecosystem)
    │
    v
Agent Scoring (5-dimension weighted)
    │
    v
Parallel Batch Execution
    │
    ├─→ Batch A: Feasibility
    ├─→ Batch B: Solution
    ├─→ Batch C: Delivery
    └─→ Batch D: Launch/Ops
```

---

## Open Source

This is an **open-source** project under the MIT License. We believe that enterprise-grade AI orchestration should be accessible to everyone.

### Why Open Source?

- **Transparency**: See how decisions are made
- **Extensibility**: Add your own skills and roles
- **Community**: Learn from others' implementations
- **Standardization**: Establish patterns for AI team orchestration

### Contributing

We welcome contributions! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

Areas of interest:
- New role agents
- Additional skill integrations
- Documentation improvements
- Tooling and automation
- Example workflows

---

## Installation

### Basic Installation

```bash
# 1. Clone
git clone https://github.com/liziye627-design/ceo-skill-framework.git
cd ceo-skill-framework

# 2. Install CEO skill
mkdir -p ~/.claude/skills
cp -r skills/ceo ~/.claude/skills/

# 3. (Optional) Copy ui-ux-pro-max if you need design tools
cp -r skills/ui-ux-pro-max ~/.claude/skills/

# 4. Restart Claude Code
```

### Full Installation (All Skills)

```bash
# Install all skills
cp -r skills/* ~/.claude/skills/

# (Optional) Install role agents for colored output
mkdir -p ~/.opencode/agent
cp agents/* ~/.opencode/agent/
```

---

## Documentation

- [Architecture Guide](./docs/ARCHITECTURE.md) - Deep dive into internal architecture
- [Installation Guide](./docs/INSTALLATION.md) - Detailed installation instructions
- [Role Agents Reference](./docs/ROLE_AGENTS.md) - Complete role documentation
- [Skills Ecosystem](./skills-ecosystem/) - Full skills catalog
- [Examples](./examples/) - Example workflows

---

## Comparison: Traditional vs CEO Framework

| Aspect | Traditional Dev | CEO Framework |
|---------|-----------------|---------------|
| Team Size | Fixed, limited | Dynamic, 20+ agents available |
| Specialization | Human experts | Specialized AI agents |
| Coordination | Meetings, emails | Structured handoffs |
| Decision Making | Hierarchical | Quantified scoring |
| Context Sharing | Implicit, lossy | Explicit artifacts |
| Conflict Resolution | Political | Negotiation protocol |
| Cost | High (salaries) | Free (open source) |
| Scale | Difficult | Instant parallelism |

---

## Roadmap

- [ ] Additional role agents (DevOps, Database, etc.)
- [ ] Web dashboard for visualizing team execution
- [ ] Integration with more skills
- [ ] Real-time contribution analytics
- [ ] Community marketplace for skills/roles

---

## License

MIT License - see [LICENSE](./LICENSE) file for details.

---

## Contributors

### Maintainer

**[liziye627](https://github.com/liziye627-design)** - Primary author and maintainer of the CEO Orchestration Framework.

### Acknowledgments

Built for the Claude Code community by developers who believe in the power of well-organized teams.

---

## Links

- **Repository**: https://github.com/liziye627-design/ceo-skill-framework
- **Claude Code**: https://claude.ai/claude-code
- **Skills Spec**: https://github.com/anthropics/claude-code-skills
- **Issues**: https://github.com/liziye627-design/ceo-skill-framework/issues

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=liziye627-design/ceo-skill-framework&type=Date)](https://star-history.com/#liziye627-design/ceo-skill-framework&Date)

---

## Stargazers

Thanks to all who star this project! ⭐
