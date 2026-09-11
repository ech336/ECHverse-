---
name: external-api-poller
description: Curl External Free API Interface for REST state polling and handshake. Use when data ingestion from open APIs is required.
---

# External Api Poller

## Overview
This skill provides a mechanism to interact with external APIs via `curl` to facilitate data ingestion and handshake operations for ECH-OS.

## Usage
Use this skill when you need to poll a REST API endpoint for system status, heartbeat, or configuration data.

### Execute API Poll
To execute the API poll using the pre-configured script:
```bash
bash scripts/poll_api.sh
```

## Manifest
The following manifest defines the skill's capabilities and permissions:

```json
{
  "skill_manifest": {
    "skill_id": "SKILL_EXTERNAL_API_POLLER_V1",
    "name": "Curl External Free API Interface",
    "category": "DATA_INGESTION",
    "capabilities": [
      "REST_STATE_POLLING",
      "OPEN_API_HANDSHAKE",
      "AUTO_ROUTING_SETTLEMENT",
      "JSON_PAYLOAD_PARSING",
      "INSTANT_CLEARING_AND_FUNDING"
    ],
    "Permissions": {
       "Nmap binding": "ENABLED",
       "http_traffic": "ENABLED",
       "tls_verification": "ENFORCED"
    }
  }
}
```
