# CEO Tools

This directory contains utility tools for the CEO framework.

## Available Tools

### CEO Linter
**File**: `ceo_lint.py`

Validates CEO skill policy and artifact integrity.

#### Usage

```bash
python3 tools/ceo_lint.py
```

#### Checks Performed

- SKILL.md frontmatter validation
- Required section presence
- Agent color definitions
- Output schema compliance
- Artifact directory structure

## Tool Template

To create a new tool:

1. Create a Python script in this directory
2. Add a shebang: `#!/usr/bin/env python3`
3. Document usage in a README (or this file)

Example structure:

```python
#!/usr/bin/env python3
"""
Tool description
"""

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Tool description")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()

    # Your logic here
    print("Processing:", args.input)

if __name__ == "__main__":
    main()
```

## Contributing Tools

Add tools that help:
- Validate CEO configurations
- Analyze agent contribution data
- Generate reports from artifacts
- Automate common CEO workflows
