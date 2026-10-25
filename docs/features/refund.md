# Refund — get your SOL back

If a drop is still unclaimed, the original sender can refund it at any time. The funds stay in the vault until someone claims them or the sender chooses to return them.

---

## When you can refund

- the drop is still **unclaimed**
- you connect the **same wallet** that created the drop
- the drop is still tied to the original sender and receiver wallet

There is no automatic expiry in the basic refund flow.

---

## Step by step

### 1. Connect the sender wallet
Open the refund page and connect the wallet that created the drop.

### 2. Review your unclaimed drops
You will see the active drops associated with that wallet, including the amount and status.

### 3. Select a drop and click Refund
Choose the drop or drops you want to return and sign the transaction.

### 4. Confirm the transaction
The funds return to your wallet once the transaction is confirmed. The claim link becomes invalid after refund.

---

## On-chain mechanics

When you refund:

- the program closes the associated **record**
- the vault is emptied and returned to the sender wallet
- the temporary receiver wallet is no longer authorized to claim
- the original sender keeps control of the funds while the drop is active

This keeps the refund flow simple and predictable: if it was never claimed, the sender can always recover it.

---

## Important notes

!!! warning "No partial refund"
    You refund the whole drop, not a portion of it.

!!! info "Only the sender can refund"
    The refund transaction must be signed by the wallet that originally created the drop.

!!! tip "Refund right away if the link was shared carelessly"
    If a claim link was posted publicly or sent to the wrong person, refund it immediately to stop the drop from being claimed.

---

## Troubleshooting

| Issue | Likely cause | Fix |
|-------|--------------|-----|
| Drop not showing | Wrong wallet connected or already claimed | Connect the original sender wallet and check the claim status |
| Transaction failed | RPC issue or network congestion | Retry in a minute and check Solana status |
| "Already claimed" | Someone used the claim link before the refund | The funds were transferred out; if this was unexpected, contact the recipient |

---

## Related

- [Drop](drop.md) — how to create the drop
- [Claim](claim.md) — how the receiver claims it
- [Security Disclaimer](../legal/security-disclaimer.md)