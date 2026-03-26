# Skills Directory

This directory contains the core CEO skill and any additional skills that work with the CEO framework.

## CEO Skill

**File**: `ceo/SKILL.md`

The main orchestration router that:
- Accepts requests via `/CEO` trigger
- Routes work to appropriate tracks
- Coordinates role agents
- Manages context and artifacts

## Skill Structure

```markdown
---
name: ceo
description: CEO orchestration router
category: productivity
tags: [orchestration, routing, contents-first]
compatibility:
  opencode: true
  claude: true
---

# Skill Content

## Sections
- Hard Trigger Gate
- Purpose
- Default Mode
- Execution Switch
- Execution Mode Subagent Policy
- ... (see full SKILL.md)
```

## Adding Skills

To add a new skill that integrates with CEO:

1. Create a new directory: `skills/your-skill/`
2. Add `SKILL.md` with proper frontmatter
3. Document in the CEO routing section
4. Update examples if applicable

## Skill Dependencies

CEO integrates with these skills (not included in this repo):

- `build-one`: Phase-gated project lifecycle
- `commercial-pm`: Product management brainstorming
- `agent-negotiation-protocol`: Conflict resolution
- `self-iteration-loop`: Post-run learning
- `ui-ux-pro-max`: Design system generation
- `frontend-design`: Aesthetic direction
- Various engineering and domain-specific skills

## Installing Skills

From this directory:

```bash
# Copy specific skill
cp -r ceo ~/.claude/skills/

# Or copy all
cp -r * ~/.claude/skills/
```
