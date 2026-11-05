#!/usr/bin/env python3
"""
EllisBanking&Trust Autonomous Software Suite - Upgraded Atomic Edition
Version: 3.0.0-OMNI-ATOMIC
Core Features: ACID Atomic Transactions, Embedded SQLite WAL Ledger,
Real-time Balance Aggregation, CORS REST API, and Enhanced Web UI.
"""

import http.server
import json
import sqlite3
import urllib.parse
from datetime import datetime

PORT = 8080
DB_NAME = "ellis_banking_suite.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA journal_mode=WAL;")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ledger (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            account_id TEXT NOT NULL,
            type TEXT NOT NULL,
            amount REAL NOT NULL,
            metadata TEXT
        )
    """)
    # Seed initial rows if empty with atomic precision
    cursor.execute("SELECT COUNT(*) FROM ledger")
    if cursor.fetchone()[0] == 0:
        initial_data = [
            (datetime.now().isoformat(), "93664745", "WIRE_OUT", 32208.22, "TAX_ID: 1998-0831-9366 | GEO: 36.0726,-79.7920 | METADATA: WELLS_FARGO_EXTERNAL_CONFIRMED"),
            (datetime.now().isoformat(), "93664745", "TREASURY_INFLOW", 100000.00, "TAX_ID: 1998-0831-9366 | GEO: 36.0726,-79.7920 | METADATA: RESERVE_INFLOW_RECONCILED"),
            (datetime.now().isoformat(), "93664745", "TREASURY_INFLOW", 100000.00, "TAX_ID: 27405-5428 | GEO: 36.0726,-79.7920 | METADATA: FEDERAL_RESERVE_TRD_5M")
        ]
        cursor.executemany("INSERT INTO ledger (timestamp, account_id, type, amount, metadata) VALUES (?, ?, ?, ?, ?)", initial_data)
        conn.commit()
    conn.close()

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>EllisBanking&Trust | OMNI Atomic Ledger Suite</title>
    <style>
        :root { bg: #0f172a; card-bg: #1e293b; border: #334155; text: #f8fafc; accent: #38bdf8; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 20px; }
        .container { max-width: 1200px; margin: 0 auto; }
        header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; padding-bottom: 20px; margin-bottom: 20px; }
        h1 { margin: 0; color: #38bdf8; font-size: 24px; }
        .badge { background: #0284c7; color: white; padding: 4px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; }
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2); }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 20px; }
        .stat-card { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 20px; }
        .stat-card h3 { margin: 0 0 10px 0; color: #94a3b8; font-size: 14px; text-transform: uppercase; }
        .stat-card .value { font-size: 24px; font-weight: bold; color: #38bdf8; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #334155; font-size: 14px; }
        th { background: #0f172a; color: #94a3b8; }
        tr:hover { background: #273548; }
        .form-group { display: flex; gap: 10px; margin-top: 15px; flex-wrap: wrap; }
        input, select { background: #0f172a; border: 1px solid #475569; color: white; padding: 10px; border-radius: 4px; flex: 1; min-width: 150px; }
        button { background: #0ea5e9; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
        button:hover { background: #0284c7; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>EllisBanking&Trust &bull; OMNI Atomic Core</h1>
            <span class="badge">Session: ⑆14⑆933664745⑈</span>
        </header>

        <div class="grid">
            <div class="stat-card">
                <h3>Primary Account</h3>
                <div class="value" style="font-size: 18px;">93664745</div>
                <small style="color: #94a3b8;">Sub: 240-89-1162</small>
            </div>
            <div class="stat-card">
                <h3>Net Balance Status</h3>
                <div class="value" id="netBalance">$0.00</div>
                <small style="color: #10b981;">ACID Reconciled &bull; Zero-Float</small>
            </div>
            <div class="stat-card">
                <h3>Execution Protocol</h3>
                <div class="value" style="font-size: 18px;">Fedwire / RTGS</div>
                <small style="color: #94a3b8;">ISO 20022 / WAL Active</small>
            </div>
        </div>

        <div class="card">
            <h2>Execute Atomic Transaction</h2>
            <form id="txForm" onsubmit="submitTransaction(event)">
                <div class="form-group">
                    <input type="text" id="accountId" value="93664745" placeholder="Account ID" required>
                    <select id="txType">
                        <option value="TREASURY_INFLOW">TREASURY_INFLOW</option>
                        <option value="WIRE_OUT">WIRE_OUT</option>
                        <option value="DEPOSIT">DEPOSIT</option>
                    </select>
                    <input type="number" step="0.01" id="amount" placeholder="Amount (USD)" required>
                    <input type="text" id="metadata" placeholder="Metadata / Omni Flags" value="TAX_ID: 1998-0831-9366 | GEO: 36.0726,-79.7920">
                    <button type="submit">Execute Atomic Post</button>
                </div>
            </form>
        </div>

        <div class="card">
            <h2>Live Immutable Ledger Spreadsheet</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Timestamp</th>
                        <th>Account ID</th>
                        <th>Type</th>
                        <th>Amount (USD)</th>
                        <th>Metadata / Omni Flags</th>
                    </tr>
                </thead>
                <tbody id="ledgerBody">
                    <tr><td colspan="6" style="text-align:center;">Loading ledger...</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
        async function fetchLedger() {
            try {
                const response = await fetch('/ledger');
                const data = await response.json();
                const tbody = document.getElementById('ledgerBody');
                tbody.innerHTML = '';
                let net = 0;
                data.records.forEach(r => {
                    if (r.type === 'TREASURY_INFLOW' || r.type === 'DEPOSIT') {
                        net += r.amount;
                    } else if (r.type === 'WIRE_OUT') {
                        net -= r.amount;
                    }
                    const tr = document.createElement('tr');
                    tr.innerHTML = `<td>${r.id}</td><td>${r.timestamp}</td><td>${r.account_id}</td><td>${r.type}</td><td style="color: ${r.type === 'WIRE_OUT' ? '#f43f5e' : '#10b981'};">$${r.amount.toLocaleString(undefined, {minimumFractionDigits: 2})}</td><td>${r.metadata}</td>`;
                    tbody.appendChild(tr);
                });
                document.getElementById('netBalance').innerText = '$' + net.toLocaleString(undefined, {minimumFractionDigits: 2, maximumFractionDigits: 2});
            } catch (err) {
                console.error('Error fetching ledger:', err);
            }
        }

        async function submitTransaction(event) {
            event.preventDefault();
            const payload = {
                account_id: document.getElementById('accountId').value,
                type: document.getElementById('txType').value,
                amount: parseFloat(document.getElementById('amount').value),
                metadata: document.getElementById('metadata').value
            };
            const res = await fetch('/ledger', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            if (res.ok) {
                document.getElementById('amount').value = '';
                fetchLedger();
            } else {
                alert('Atomic transaction failed.');
            }
        }

        fetchLedger();
        setInterval(fetchLedger, 5000);
    </script>
</body>
</html>
"""

class AtomicSuiteHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status=200, content_type="application/json"):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(204)

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/" or parsed_path.path == "/ui":
            self._set_headers(200, content_type="text/html")
            self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
        elif parsed_path.path == "/health":
            self._set_headers(200)
            self.wfile.write(json.dumps({"status": "active", "session": "⑆14⑆933664745⑈", "timestamp": datetime.now().isoformat()}).encode("utf-8"))
        elif parsed_path.path == "/ledger":
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT id, timestamp, account_id, type, amount, metadata FROM ledger ORDER BY id DESC")
            rows = cursor.fetchall()
            conn.close()
            
            records = [{"id": r[0], "timestamp": r[1], "account_id":