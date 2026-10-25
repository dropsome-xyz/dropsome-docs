# Drop — send SOL with a link

A drop lets you send SOL without collecting a wallet address in advance. The app creates a temporary wallet, locks the funds in a program vault, and gives you a claim link to share privately.

---

## How it works

### 1. Enter the amount
Choose the amount of SOL you want to send. The app will generate a temporary wallet and a unique claim link.

### 2. Funds are locked on-chain
The SOL, plus a little gas reserve and app fee, is stored in a Dropsome vault on Solana until the receiver claims it or you refund it.

### 3. Share the link privately
Send the claim link through a private channel: text message, encrypted email, DM, or in person. Anyone who holds the link can claim the drop.

---

## What happens on-chain

When you create a drop, the app creates a vault and a record for that drop:

- the **vault** holds the SOL until claim or refund
- the **record** tracks the sender, temporary receiver wallet, amount, and claim state
- the temporary wallet is the only wallet authorized to claim the funds
- the sender can refund at any time while the drop remains unclaimed

This is not a generic airdrop flow. Each drop is tied to one sender and one temporary receiver wallet.

---

## Fees and balances

| Fee | Who pays | Typical behavior |
|-----|----------|------------------|
| Service fee | Sender | Small app fee charged by the protocol |
| Network fee reserve | Sender | Set aside to cover the receiver’s claim transaction |
| Rent exemption | Sender | Temporarily locked and returned on claim or refund |

The app shows the total before you confirm. You need enough SOL to cover the drop amount plus fees.

---

## Prerequisites

- a Solana wallet such as Phantom, Solflare, or Backpack
- enough SOL for the amount plus fees
- an internet connection and a private way to send the claim link

---

## Security reminders

!!! warning "Treat the claim link like cash"
    Anyone who has the link can claim the funds. Share it only through a private, trusted channel.

!!! tip "Start small"
    If you are testing the flow for the first time, use a small amount.

!!! info "Refund is always available"
    As long as the drop remains unclaimed, you can refund the full amount back to your wallet. See [Refund](refund.md).

---

## Troubleshooting

| Issue | Likely cause | Fix |
|-------|--------------|-----|
| "Insufficient balance" | Not enough SOL for the amount and fees | Add more SOL or lower the amount |
| Transaction failed | Network congestion or RPC issue | Retry in a minute and check Solana status |
| Drop not showing in refund flow | Wrong wallet connected or already claimed | Connect the original sender wallet and check the claim status |

---

## Related

- [Claim](claim.md) — how the receiver claims the drop
- [Refund](refund.md) — how the sender gets funds back if unclaimed
- [Security Disclaimer](../legal/security-disclaimer.md)