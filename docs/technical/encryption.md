# Encryption — how the claim link works

Dropsome uses an encrypted claim link to deliver a temporary wallet's recovery phrase to the receiver. The recovery phrase is generated on demand, encrypted in the app backend, and decrypted when the receiver opens the link.

---

## The short version

1. The backend generates a temporary wallet for the drop
2. The recovery phrase is encrypted with a server-side key
3. The ciphertext is embedded in the claim URL as a `data` payload
4. The receiver opens the claim page and requests decryption from the API
5. The app returns the recovery phrase so the user can import it into a wallet

This keeps the flow simple for new users while preserving the on-chain authorization model.

---

## Threat model

| What is protected | How |
|-------------------|-----|
| Recovery phrase in the claim link | The link contains encrypted ciphertext, not the phrase in plain text |
| Recovery phrase in the Dropsome backend | Not persisted by the claim endpoint; decrypted only on demand |
| Recovery phrase in the browser | Returned to the claiming browser so the user can import the wallet |
| Server key compromise | Could enable decryption of unclaimed drop payloads |

!!! warning "Trust assumption"
    The server holds the decryption key and the claim flow returns the decrypted recovery phrase to the receiver's browser. Dropsome does not persist the phrase in the backend, but the claim payload is a bearer credential: anyone who obtains the claim link or its encrypted `data` value may be able to claim the drop. Use this flow for small amounts and share links privately.

---

## Technical details

### Encryption
- **Algorithm**: AES-256-CBC
- **Key**: A server-side key kept in environment configuration
- **IV**: Random per encryption so the same recovery phrase does not produce the same ciphertext
- **Output**: encrypted payload is encoded and embedded in the claim URL

AES-256-CBC provides confidentiality for the payload, but it is not an authenticated-encryption mode. The claim endpoint must therefore be treated as part of the trusted application flow; this documentation is not a claim that the payload is tamper-proof.

### Link format

```text
https://dropsome.xyz/claim?data=<encrypted_payload>
```

The encrypted payload:
- is embedded in the URL as data, not shown to the user in plain text
- is sent to the API for decryption over HTTPS when the receiver opens the link
- may be retained in browser history, copied messages, analytics, referrer data, or infrastructure access logs that record full URLs
- is not intended to be used as a public identifier or shared outside the intended claim flow

The current implementation uses a query parameter rather than a URL fragment. Dropsome's own claim endpoint does not persist the payload or log the decrypted phrase, but the app cannot guarantee that every browser, hosting provider, proxy, monitoring service, or messaging platform will omit the URL from its own records.

### Decryption flow

1. The receiver opens the claim link
2. The frontend reads the encrypted payload from the URL
3. The frontend sends it to the API for decryption
4. The server decrypts it and returns the recovery phrase to the browser
5. The receiver imports the phrase into a wallet app

The phrase is not stored in local storage or cookies by the app.

---

## What this means for you

### As a sender
- the claim link is the secret used to retrieve the drop
- share it only through a trusted private channel
- keep the link out of public, shared, or automatically indexed spaces
- if the link is exposed and the drop is still unclaimed, use the refund flow immediately

### As a receiver
- the recovery phrase shown on the claim page is the only copy needed to access the drop wallet
- import it into a wallet immediately
- move the funds to a wallet you control after claiming
- avoid opening claim links on shared devices or in browsers with untrusted extensions

### If you are building on Dropsome
- keep the decryption key in a secure environment variable
- protect the decryption endpoint with the same rate limiting and authentication model as the rest of the app
- treat the server as a trusted component for the claim flow

---

## Related

- [Security Disclaimer](../legal/security-disclaimer.md) — plain-language risks
- [Solana Program](program.md) — on-chain mechanics