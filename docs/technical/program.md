# Solana Program — on-chain mechanics

The Dropsome program handles the escrow, claim, and refund logic for each drop. This page summarizes the core account model and transaction flow used by the app.

---

## Program ID

**Mainnet**: `DSdHwC1vGPL4KzNAhgxMYggZnBBaY8upKx6uo655kVYZ`

---

## Accounts

### AppState (global config)
A single PDA at `["app_state"]` stores global config for the app.

```rust
pub struct AppState {
    pub is_initialized: bool,
    pub authority: Pubkey,
    pub is_active: bool,
    pub network_fee_reserve: u64,
    pub treasury: Pubkey,
    pub fee_basis_points: u16,
    pub min_drop_amount: u64,
}
```

### Record (per drop)
A PDA at `["record", sender, receiver]` tracks each active drop.

```rust
pub struct Record {
    pub sender: Pubkey,
    pub receiver: Pubkey,
    pub vault: Pubkey,
    pub amount: u64,
}
```

### Vault (per drop)
A PDA at `["vault", sender, receiver]` holds the SOL while the drop is active.

---

## Instructions

### 1. `drop` — create a drop
**Accounts**: sender, temporary receiver keypair, vault, record, app state, treasury, system program

**Flow**:
1. validate the amount against the minimum and app state
2. calculate the service fee and reserve requirements
3. initialize the `Record` account with sender, receiver, vault, and amount
4. transfer the network fee reserve to the receiver wallet
5. transfer the drop amount and rent exemption into the vault
6. transfer the service fee to the treasury

The receiver is a freshly generated wallet keypair, not a PDA. The frontend provides its public key to the program as the claim target.

---

### 2. `claim` — receiver claims funds
**Accounts**: claimer signer, vault, record, system program

**Flow**:
1. verify the signer matches the `record.receiver`
2. transfer the vault balance to the receiver wallet
3. close the `Record` account so rent goes back to the sender
4. let the runtime close the empty vault account

Only the wallet generated for the drop can claim it.

---

### 3. `refund` — sender reclaims unclaimed funds
**Accounts**: sender signer, vault, record, system program

**Flow**:
1. verify the signer matches the original `record.sender`
2. transfer the vault balance back to the sender wallet
3. close the `Record` account

Only the original sender can refund. There is no third-party refund path.

---

### 4. `update` — admin config update
**Accounts**: authority signer, app state

This updates the global state such as fee settings, min amount, active status, and treasury destination.

---

## Fees

| Fee | Paid by | Destination | Typical behavior |
|-----|---------|-------------|------------------|
| Service fee | Sender | Treasury | Small app fee |
| Network fee reserve | Sender | Receiver wallet | Covers claim transaction gas |
| Vault rent exemption | Sender | Returned on claim/refund | Temporarily locked in the vault |

The UI should show the total before confirmation so the sender sees the full cost.

---

## Security properties

- **single claimer** — only the generated temporary wallet can claim
- **single refunder** — only the original sender can refund
- **no partial refunds** — each drop is refunded in full or not at all
- **rent is returned** — the accounts are closed cleanly on claim or refund
- **funds stay in escrow** until a valid claim or refund occurs

---

## Frontend integration

| Action | Frontend behavior | Program call |
|--------|-------------------|--------------|
| Drop | generates receiver keypair, encrypts recovery phrase, builds link | `drop` |
| Claim | decrypts recovery phrase, user imports wallet, connects it | `claim` |
| Refund | lists sender-owned unclaimed records and builds tx | `refund` |

---

## Deploy and upgrade

- **Framework**: Anchor (Rust)
- **Program authority**: app state authority
- **IDL**: generated at build and used by the frontend for transaction construction

---

## Related

- [Encryption](encryption.md) — claim link security model
- [Security Disclaimer](../legal/security-disclaimer.md) — plain-language risk summary