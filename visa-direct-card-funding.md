---
name: visa-direct-card-funding
description: Programmatic card-based transactions, AFT (Account Funding), and OCT (Original Credit Transactions) via Visa Direct CLI/MCP.
---

# Visa Direct & Card Funding CLI

This skill provides programmatic control for Visa Direct transactions, including Account Funding Transactions (AFT) and Original Credit Transactions (OCT).

## Usage

This skill includes an executable script: `scripts/ech-os-visa.sh`.

### Commands
- `init`: Initialize credentials.
- `aft`: Pull funds (AFT).
- `oct`: Push funds/payout (OCT).
- `balance`: Check balances.
- `verify`: Perform card eligibility checks.

Invoke these commands via the script located in the skill directory:
`./scripts/ech-os-visa.sh <command> [options]`
