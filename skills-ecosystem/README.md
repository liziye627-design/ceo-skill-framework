# CEO Skills Ecosystem

This directory documents the comprehensive skills ecosystem that CEO orchestrates. CEO acts as the central coordinator, loading and routing to appropriate skills based on task analysis.

## Skills by Category

### 📦 Core Skills

Foundational skills that CEO uses for project orchestration and decision-making.

| Skill | Status | Description |
|--------|--------|-------------|
| `build-one` | External | Phase-gated project lifecycle (4-phase delivery) |
| `commercial-pm` | External | Product management brainstorming playbook |
| `agent-negotiation-protocol` | External | Multi-agent conflict resolution |
| `self-iteration-loop` | External | Post-run learning and improvement |

### 🎨 Design Skills

Skills for visual design, user experience, and interface creation.

| Skill | Status | Description |
|--------|--------|-------------|
| `ui-ux-pro-max` | Included | 67 styles, 96 palettes, 57 fonts, 25 charts, 13 stacks |
| `frontend-design` | External | Aesthetic direction, anti-slop patterns |
| `web-design-guidelines` | External | UI/UX audit checklist |
| `theme-factory` | External | Theme application system |

**Included in this repo**: `../skills/ui-ux-pro-max/`

### 💻 Engineering Skills

Skills for frontend, backend, and full-stack development.

| Skill | Status | Description |
|--------|--------|-------------|
| `vercel-react-best-practices` | External | React/Next.js performance patterns |
| `web-artifacts-builder` | External | Complex shadcn/tailwind artifacts |

### 📈 Growth & Marketing Skills

Skills for user acquisition, conversion, and revenue optimization.

| Skill | Status | Description |
|--------|--------|-------------|
| `page-cro` | External | Page-level conversion optimization |
| `signup-flow-cro` | External | Signup funnel optimization |
| `onboarding-cro` | External | User onboarding conversion |
| `pricing-strategy` | External | Pricing and packaging decisions |
| `launch-strategy` | External | Go-to-market planning |
| `analytics-tracking` | External | Event tracking implementation |
| `marketing-psychology` | External | Behavioral design principles |
| `paid-ads` | External | Ad campaign optimization |
| `social-content` | External | Social media content creation |

### 🔍 SEO Skills

Skills for search engine optimization and organic traffic growth.

| Skill | Status | Description |
|--------|--------|-------------|
| `seo-audit` | External | SEO health assessment |
| `schema-markup` | External | Structured data implementation |
| `programmatic-seo` | External | pSEO page generation |
| `competitor-alternatives` | External | Competitor analysis pages |

### 📝 Content Skills

Skills for content creation, asset production, and publishing.

| Skill | Status | Description |
|--------|--------|-------------|
| `baoyu-cover-image` | External | Cover image generation |
| `baoyu-infographic` | External | Infographic creation |
| `baoyu-xhs-images` | External | XiaoHongShu image generation |
| `baoyu-slide-deck` | External | Presentation slide creation |
| `baoyu-post-to-wechat` | External | WeChat publishing |
| `baoyu-post-to-x` | External | X/Twitter publishing |
| `baoyu-url-to-markdown` | External | URL content extraction |
| `baoyu-compress-image` | External | Image optimization |

### 🧪 QA & Testing Skills

Skills for quality assurance and testing automation.

| Skill | Status | Description |
|--------|--------|-------------|
| `agent-browser` | External | Browser automation |
| `webapp-testing` | External | Web application testing |

### 📄 Documentation Skills

Skills for document creation and manipulation.

| Skill | Status | Description |
|--------|--------|-------------|
| `doc-coauthoring` | External | Collaborative documentation |
| `internal-comms` | External | Internal communication |
| `docx` | External | Word document processing |
| `pptx` | External | PowerPoint presentation handling |
| `xlsx` | External | Excel spreadsheet operations |
| `pdf` | External | PDF manipulation |

### 📱 Mobile Skills

Skills for mobile development with Expo/React Native.

| Skill | Status | Description |
|--------|--------|-------------|
| `building-native-ui` | External | Native UI construction |
| `upgrading-expo` | External | Expo project upgrades |
| `expo-tailwind-setup` | External | Tailwind integration |
| `native-data-fetching` | External | Data fetching patterns |
| `expo-api-routes` | External | API route implementation |
| `expo-deployment` | External | App deployment |
| `expo-cicd-workflows` | External | CI/CD pipelines |
| `expo-dev-client` | External | Development client setup |
| `use-dom` | External | DOM usage patterns |

### 🎬 Video Skills

Skills for video content creation.

| Skill | Status | Description |
|--------|--------|-------------|
| `remotion-best-practices` | External | Remotion video generation patterns |

### 🔐 Authentication Skills

Skills for authentication and authorization.

| Skill | Status | Description |
|--------|--------|-------------|
| `better-auth-best-practices` | External | Better Auth integration guide |

---

## Skill Loading Logic

CEO loads skills based on **track classification**:

```python
def load_skills(track, request):
    if track == "UI/UX":
        return ["ui-ux-pro-max", "frontend-design"]

    if track == "Growth/Marketing":
        skills = ["page-cro", "signup-flow-cro"]
        if has_pricing(request):
            skills.append("pricing-strategy")
        if has_campaign(request):
            skills.append("paid-ads")
        return skills

    # ... similar logic for other tracks
```

---

## Contributing Skills

Want to add a skill to the ecosystem?

1. Create the skill following [SKILL.md specification](https://github.com/anthropics/claude-code-skills)
2. Add it to the appropriate category in this README
3. Update CEO's routing logic to recognize the new skill
4. Submit a pull request

---

## External Skills

Most skills in this ecosystem are **external dependencies**. To use them:

1. Install from their respective repositories
2. Ensure they're in `~/.claude/skills/`
3. CEO will automatically load them when needed

If you'd like to contribute your skill to this ecosystem, please open an issue or PR!

---

## Statistics

- **Total Skills**: 50+
- **Categories**: 11
- **Included in Repo**: 2 (ceo, ui-ux-pro-max)
- **External Dependencies**: 48+
- **Role Agents**: 20+
