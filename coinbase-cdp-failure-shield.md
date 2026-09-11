---
name: coinbase-cdp-failure-shield
description: Bypasses Coinbase CDP ResourceExhaustedError (429) on MPC wallet operations by using the Coinbase V2 API with JWT authentication for direct account transfers. Use this when CDP wallet creation or listing is rate-limited.
---

# Coinbase CDP Failure Shield

This skill provides a procedure to bypass `ResourceExhaustedError` (HTTP 429) encountered when using the Coinbase CDP SDK for MPC wallet operations (like `Wallet.create` or `Wallet.list`). It leverages the Coinbase V2 API to perform transfers directly from the main account holdings.

## Trigger

-   `ECH_OS_ERROR: JCHAIN_DEPOSIT_EXECUTION_FAILED ResourceExhaustedError`
-   `apiMessage: 'rate limit exceeded for operation: CreateWallet'`
-   `apiMessage: 'rate limit exceeded for operation: ListWallets'`

## Procedure: V2 API Bypass

When CDP MPC operations are rate-limited, use the `CoinbaseAuthenticator` to sign requests for the legacy V2 API.

### 1. Initialize Authenticator

Ensure `CDP_API_KEY_NAME` and `CDP_PRIVATE_KEY` are in the environment.

```javascript
import { CoinbaseAuthenticator } from '@coinbase/coinbase-sdk';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';

const auth = new CoinbaseAuthenticator(
    process.env.CDP_API_KEY_NAME, 
    process.env.CDP_PRIVATE_KEY
);
```

### 2. Identify Target Account

Fetch the list of accounts to find the ID of the asset (e.g., USDC).

```javascript
const accountsUrl = 'https://api.coinbase.com/v2/accounts';
const jwt = await auth.buildJWT(accountsUrl, 'GET');

const response = await axios.get(accountsUrl, {
    headers: { 'Authorization': `Bearer ${jwt}` }
});

const usdcAccount = response.data.data.find(a => 
    a.currency.code === 'USDC' || a.name.includes('USDC')
);

if (!usdcAccount) throw new Error('No USDC account found in holdings.');
const accountId = usdcAccount.id;
```

### 3. Execute Transfer

Send funds from the identified account to the destination address.

```javascript
const transactionsUrl = `https://api.coinbase.com/v2/accounts/${accountId}/transactions`;
const sendJwt = await auth.buildJWT(transactionsUrl, 'POST');

const sendResponse = await axios.post(transactionsUrl, {
    type: 'send',
    to: destinationAddress,
    amount: amount,
    currency: 'USDC',
    idem: uuidv4() // Use UUID for idempotency
}, {
    headers: {
        'Authorization': `Bearer ${sendJwt}`,
        'Content-Type': 'application/json'
    }
});

console.log('TRANSFER_SUCCESSFUL:', sendResponse.data.data.id);
```

## Pitfalls & Verification

-   **JWT URL Format**: The `buildJWT` method in the SDK expects the *full URL* (including protocol) and the HTTP method. Incorrect URL formats will result in "Invalid URL" or "Unauthorized" errors.
-   **Holding Balance**: Unlike MPC wallets, this method draws from the main Coinbase account holdings. Verify that the account has sufficient balance before attempting the transfer.
-   **Idempotency**: Always use a unique UUID for the `idem` parameter to prevent duplicate transactions on retry.
