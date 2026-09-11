---
name: dns-url-control
description: DNS Control Over URL Target. Use when needing URL_LEVEL_ORIGIN_REBINDING, DYNAMIC_A_CNAME_STEERING, AUTOMATED_ZONE_RECORD_MUTATION, or EDGE_ROUTING_OVERRIDE.
---

# DNS Control Over URL Target

This skill allows for URL-level origin rebinding, dynamic A/CNAME steering, automated zone record mutation, and edge routing override.

## Skill Manifest

```json
{
  "skill_manifest": {
    "skill_id": "SKILL_DNS_URL_CONTROL_V1",
    "name": "DNS Control Over URL Target",
    "category": "NETWORK_INFRASTRUCTURE",
    "capabilities": [
      "URL_LEVEL_ORIGIN_REBINDING",
      "DYNAMIC_A_CNAME_STEERING",
      "AUTOMATED_ZONE_RECORD_MUTATION",
      "EDGE_ROUTING_OVERRIDE"
    ],
    "permissions": {
      "dns_zone_authority": "FULL_CONTROL",
      "http_redirect_interception": "ENABLED",
      "ssl_tls_sni_binding": "AUTOMATIC"
    }
  },
  "runtime_hook": "sys.network.dns.bind_url_controller"
}
```

## Usage

Use this skill when you need to perform low-level DNS manipulation or routing control at the edge. Ensure you have the necessary authority before invoking.
