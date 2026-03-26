# Installation Guide

## Prerequisites

- Claude Code installed and configured
- Git for cloning the repository
- (Optional) OpenCode role agents installed

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ceo-skill-framework.git
cd ceo-skill-framework
```

### 2. Install the CEO Skill

```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy CEO skill
cp skills/ceo/SKILL.md ~/.claude/skills/ceo/SKILL.md
```

### 3. Verify Installation

Start Claude Code and verify the CEO skill is available:

```
/help
```

You should see `ceo` listed in the available skills.

### 4. (Optional) Install Role Agents

For full team output with colored frames, install OpenCode role agents:

```bash
# Create agent directory
mkdir -p ~/.opencode/agent

# Copy role agent definitions
cp agents/* ~/.opencode/agent/
```

## Quick Start

Once installed, you can invoke CEO:

```
/CEO Build a landing page for my SaaS product
```

CEO will respond with:
1. A brief asking for clarification if needed
2. A plan with work orders
3. A request for confirmation

To proceed with execution:

```
/CEO exec
```

## Troubleshooting

### Skill Not Loading

If CEO doesn't appear in `/help`:
1. Verify the file is at `~/.claude/skills/ceo/SKILL.md`
2. Check the YAML frontmatter is valid
3. Restart Claude Code

### Role Agents Not Working

If role agents don't show colored output:
1. Verify agents are in `~/.opencode/agent/`
2. Check each agent has a `.md` file with a valid color definition
3. Ensure CEO skill is loaded

## Next Steps

- Read [USAGE.md](./USAGE.md) for detailed usage examples
- Explore [ROLE_AGENTS.md](./ROLE_AGENTS.md) for role details
- Check [EXAMPLES.md](../examples/) for sample workflows
