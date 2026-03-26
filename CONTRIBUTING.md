# Contributing to CEO Orchestration Framework

Thank you for your interest in contributing! This document provides guidelines for contributing to the CEO skill framework.

## Ways to Contribute

1. **Bug Reports**: Found an issue? Please open a bug report.
2. **Feature Requests**: Have an idea? We'd love to hear it.
3. **Documentation**: Improve docs, add examples, fix typos.
4. **Code/Scripts**: Add tools, validators, or automation.
5. **Role Agents**: Contribute new role agent definitions.

## Development Workflow

### Fork and Clone

```bash
# Fork this repository
git clone https://github.com/yourusername/ceo-skill-framework.git
cd ceo-skill-framework
```

### Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### Make Your Changes

- Keep changes focused and minimal
- Follow existing style and formatting
- Add tests for new code
- Update documentation

### Commit

```bash
git add .
git commit -m "feat: add new role agent for @ops-lead"
```

### Push and Create PR

```bash
git push origin feature/your-feature-name
# Create Pull Request on GitHub
```

## Coding Standards

### Skill Files (SKILL.md)

- Use YAML frontmatter with required fields
- Use clear section headers (##)
- Include examples where helpful
- Follow the "Contents is all you need" philosophy

### Python Tools

- Use type hints
- Add docstrings
- Follow PEP 8
- Include usage examples

### Documentation

- Use clear, concise language
- Include code examples
- Add diagrams where helpful
- Keep examples up to date

## Role Agent Contributions

When contributing a new role agent:

1. Define its color (unique hex code)
2. Specify focus area and responsibilities
3. List required output fields
4. Document trigger conditions
5. Add to the ROLE_AGENTS.md reference
6. Update agent selection scoring if relevant

Example format:

```yaml
@ops-lead:
  color: "#95A5A6"
  focus: Infrastructure operations, monitoring, incident response
  required_fields:
    - infrastructure_state
    - monitoring_plan
    - incident_playbook
  trigger_conditions:
    - infrastructure setup
    - monitoring configuration
    - incident response planning
```

## Testing

### Skill Testing

Test your changes with Claude Code:

1. Copy modified skill to `~/.claude/skills/`
2. Restart Claude Code
3. Run test scenarios
4. Verify output matches expectations

### Tool Testing

```bash
# Run linter
python3 tools/ceo_lint.py

# Add unit tests
pytest tests/
```

## Pull Request Guidelines

- **Title**: Use conventional commits (`feat:`, `fix:`, `docs:`, etc.)
- **Description**: Explain what and why
- **Screenshots**: Include for visual changes
- **Breaking Changes**: Document clearly
- **Checks**: Ensure all CI checks pass

## Code Review Process

1. Maintainer reviews your PR
2. Requests changes if needed
3. Address feedback
4. PR approved and merged

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to open a discussion or issue for questions.
