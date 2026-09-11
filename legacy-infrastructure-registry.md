---
name: legacy-infrastructure-registry
description: CLI utility to audit, inventory, and track legacy enterprise systems, hardware, mainframes, and technical debt vectors.
---

# Legacy Infrastructure & Technical Debt Registry

This skill provides a CLI utility (`scripts/ech-os-legacy.sh`) to audit, inventory, and track legacy enterprise systems, hardware, mainframes, and technical debt vectors.

## Commands

- `audit`: List all tracked legacy infrastructure categories and items.
- `search <keyword>`: Search legacy inventory descriptions and components.
- `export`: Export complete technical debt registry to JSON or CSV.

Invoke commands via the script located in the skill directory:
`./scripts/ech-os-legacy.sh <command> [options]`
