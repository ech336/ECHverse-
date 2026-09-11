---
name: ech-monolith-majick-integration
description: Architectural mapping and operational protocols for ECH Monolith System integrated with MaJick Framework. Use for ECH algebraic string (A⊗S⊗α⊗T) operations, system mutations, and intent lineage management.
---

# ECH Monolith / MaJick Integration

## Overview
This skill provides the procedural knowledge required to operate within the ECH Monolith System, specifically its mapping to the MaJick Framework's quantum-fintech primitives.

## Operational Protocol
To execute the ECH string within the Monolith environment, follow this flow:

1. **Intent Initiation:** Interact with `chat.sh` CLI to define the Actor (A) intent.
2. **State Encoding:** Utilize `ech_response` to construct the formal JSON envelope, binding Actor, State, Action, and Target.
3. **Execution and Mutation:** The Telnet server's `handle(msg)` function processes the Action (α), interacting with the Rust-based State (S).
4. **Trace Purge:** Adhere to `data_policy.json`. Block "meta" or "omni" data and execute `purge_traces.sh` to ensure intent lineage integrity.

## Reference Mapping
For detailed technical mappings (Actor, State, Action, Target) and functional alignment (Payload Transformer, Continuous Execution, Shift, Release), see [references/mapping.md](references/mapping.md).

## System Limitations
- **Deployment:** Kubernetes components (`infra/k8s/go-deployment.yaml`) are non-operational due to sandbox restrictions.
- **Interaction:** Rely on direct execution of binaries (`ech-gateway`, `ech-state-engine`) and scripts.

## Core Primitives
- **A⊗S⊗α⊗T:** The fundamental algebraic string for sovereign intent.
- **Φp:** The Payload Transformer logic layer.
- **σ (Shift):** Physical state mutation tracking.
