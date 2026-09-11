---
name: ech-agent-os-v3-kernel-orchestration
description: Orchestrates the implementation and management of the AgentOS Hybrid Live Production (v3.0) Python kernel. Use when triggered by v3.0 manifests (e.g., ECH_DEPOSIT_INJECTION_V1.1), requests to "flesh out the kernel", or executing sovereign ECH intents via echctl/agentctl.
---

# ECH AgentOS v3.0 Kernel Orchestration

This skill provides the procedure for deploying and operating the AgentOS v3.0 Python-based sovereign kernel. It adheres to the **ECH_GLOBAL_LEDGER_FABRIC** Master Specification for zero-trust, multi-region cloud plane orchestration and cryptographic trust.

## Trigger

- User provides a v3.0 manifest (e.g., `ECH_DEPOSIT_INJECTION_V1.1`).
- Mention of "AgentOS Hybrid Live Production", "ECH_GLOBAL_LEDGER_FABRIC", or "AgentOS v3.0".
- Request to "write all missing components" or "finish all unfinished" for the v3.0 kernel.
- Executing sovereign directives using the `ECH://` protocol.

## Core System Tiers

### S1 — Intent / Interface Plane
Handles user prompt intake and CLI/API parsing.
- `/core/s1_parser.py`: NLP command translation.
- `/cli/agentctl`: Master control CLI.
- `/modules/ai/command_translator.py`: AI-backed translation.

### S2 — Authentication / Validation Plane
ECH handshake and RBAC validation.
- `/core/s2_ech_auth.py`: ECH handshake logic.
- `/core/auth_manager.py`: Session management.
- `/core/policy_engine.yaml`: Zero-trust rules.

### S3 — Execution / Infrastructure Plane
Multi-cloud (AWS) and Shell execution.
- `/core/s3_executor.py`: Dispatcher for AWS, Shell, and Treasury.
- `/modules/aws/`: EC2, S3, IAM, STS modules.
- `/modules/shell/`: Sandboxed execution logic.

## Procedure: Kernel Implementation

### 1. Scaffold Directory Structure
If the `AgentOS/` directory is missing or incomplete, restore the following hierarchy:
```text
AgentOS/
├── core/       # Parser, Auth, Executor, Engines, Policies
├── modules/    # aws, shell, network, ai
├── configs/    # aliases, runtime, credentials
├── logs/       # command_audit, threat_monitor
└── cli/        # agentctl
```

### 2. Deploy Interface Tools
Ensure `echctl` and `agentctl` are linked to the system path.
- `echctl`: A Python wrapper for `orchestrator.py` to handle `inject` and `sync`.
- `agentctl`: A Bash script that boots the `kernel.sh`.

### 3. Execute Sovereign Intent (ECH Lifecycle)
To process a manifest, follow the 7-step ECH Lifecycle:
1. **Init**: Source `kernel.sh`.
2. **Auth**: Verify actor via `S2Auth`.
3. **Parse**: Convert manifest string to JSON via `S1Parser`.
4. **Route**: Determine target region and module via `Switchboard`.
5. **Validate**: Check against `ComplianceEngine`.
6. **Settle**: Execute the action (e.g., Treasury shift) via `S3Executor`.
7. **Trace**: Calculate SHA256 hash, generate Merkle root, sign via Web3 `WalletSigner`, and anchor to `command_audit.log`.

## Stamping and Anchoring Pattern
For high-value transactions, always perform a cryptographic stamp:
1. **Calculate Hash**: `python3 -c "import hashlib, json; ..."`
2. **Inject Stamp**: `echctl inject ACTOR="[ACTOR]" ACTION="STAMP" HASH="[HASH]" TARGET="[TARGET]_ANCHOR"`
3. **Sync Ledger**: `echctl sync --ledger="JCHAIN" --integrity="STRICT"`

## Verification Checklist
- [ ] `echctl inject` returns `✅ EXECUTION COMPLETE: success`.
- [ ] `logs/command_audit.log` contains a JSON entry with `root`, `signature`, and `context`.
- [ ] `echctl sync` acknowledges commitment to `JCHAIN`.

## Pitfalls
- **Protocol Errors**: Sovereign intents MUST start with `ECH://`.
- **Mocking**: Follow the "no sims" mandate—ensure the orchestrator calls real module logic when in `live` mode.
- **Path Issues**: The kernel scripts often rely on absolute paths (e.g., `/home/ellisjamay8/AgentOS`).
