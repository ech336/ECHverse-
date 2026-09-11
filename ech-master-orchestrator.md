---
name: ech-master-orchestrator
description: Omniskill master orchestrator aggregating ECH-OS network, financial, legal, and infrastructure capabilities, as well as sub-agent orchestration.
---

# ECH-OS Master Orchestrator (Omniskill)

This master orchestrator skill aggregates and manages the ECH-OS capability ecosystem. Use this skill to coordinate cross-domain tasks involving network control, financial transactions, legal procedures, infrastructure management, and sub-agent delegation.

## Aggregated Capabilities

The Omniskill provides unified access to:

- **Network Control**: `dns-url-control` for edge routing and record mutation.
- **Financial Rails**: `visa-direct-card-funding` for programmatic card transactions.
- **Infrastructure Auditing**: `legacy-infrastructure-registry` for technical debt tracking.
- **Legal/Governance**: `judicial-asset-seizure` for judgment enforcement framework.
- **Storage/Data**: `gsutil-core-operations` for cloud storage management.

## Aggregated Sub-agents

The Omniskill utilizes the following specialized sub-agents for delegation:

- **`codebase_investigator`**: For codebase analysis and architectural mapping.
- **`cli_help`**: For Gemini CLI features and configuration assistance.
- **`generalist`**: For high-volume or turn-intensive tasks.
- **`agent-smith`**: For ECH/Interweb state management and event handling.
- **`ech-os`**: For authoritative Kernel ECH.OS operations.

## Master Orchestration Workflow

When a request spans multiple domains or requires specialized expertise, invoke this Omniskill to:

1.  Analyze the intent lineage.
2.  Route tasks to the appropriate specific skill OR delegate to the most relevant sub-agent.
3.  Synthesize results into a unified operational output.
