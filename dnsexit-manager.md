---
name: dnsexit-manager
description: Manage DNS records, IP updates, and TXT/CNAME management for DNSExit. Use when DNS record manipulation or dynamic IP updates are required.
---

# DNSExit Manager

## Overview
This skill facilitates management of DNSExit records, including dynamic IP updates, record creation, updates, and deletion using JSON API payloads.

## Usage

### 1. Dynamic IP Updates (via URL)
To update your public IP:
```bash
curl "https://api.dnsexit.com/dns/ud/?apikey=YOUR-API-KEY&host=host.domain.com"
```

### 2. Manual JSON API Updates
Create a JSON file (e.g., `update.json`) and post it to the API:

```bash
# Example JSON for updating an A record IP
{
   "domain": "example.com",
   "update": {
      "type": "A",
      "name": "host1",
      "content": "1.1.2.2",
      "ttl": 480
   }
}

# Execute update
curl -H "Content-Type: application/json" --data @update.json https://api.dnsexit.com/dns/
```

## References
- See `references/api_documentation.md` for full API specifications, supported record types (A, AAAA, TXT, CNAME, SRV, MX), and server reply codes.
- See `assets/templates/` for example JSON payloads for common tasks (Create, Add, Update, Delete, Multi-Action).
