---
hide:
  - navigation
---

## **Disclaimer & safety notes**

Dropsome was created to simplify **small cryptocurrency transfers** such as loans and gifts, not for storing large amounts.  
This page explains, in plain language, what using a “magic link” and a generated wallet means for your security, and how to use Dropsome in a safer way.

You use Dropsome at your own risk.

## **How the magic link works**

When you create a drop, Dropsome generates a **new wallet** for that drop.  
The secret phrase (seed phrase) for this wallet is:

- Generated on our backend.
- Encrypted with a server-side key.
- Embedded (in encrypted form) in the **claim link** you share.

When the receiver opens the claim link in the official Dropsome app:

- The page automatically sends the encrypted data to our server.
- The server decrypts the seed phrase and returns it to the page.
- The receiver can then import that wallet into a Solana wallet app (for example Phantom, Solflare or Backpack).

The main risk is simple: **if the link or the seed phrase is ever leaked or shared with the wrong person, they can claim or move the funds from that wallet.**

## **What this means for trust**

- The sender and the receiver both have (or can get) access to the same seed phrase.
- Either of them could keep a copy of it.
- Anyone who sees that seed phrase later can restore the wallet and control whatever is still inside it.

Because of that, the drop wallet should be treated as **temporary and shared‑risk**, not as a long‑term personal wallet.

## **Tips for senders**

- **Keep drops small.**  
  Use Dropsome for onboarding‑size gifts, not life savings.

- **Share links in private.**  
  Send the claim link only to the intended person, preferably over a private, end‑to‑end encrypted channel (for example Signal, Telegram, WhatsApp, iMessage).

- **Delete the link when you’re done.**  
  After the drop is successfully claimed or refunded, remove the claim link from chats, notes, and other places where it was stored, and (if possible) ask the receiver to delete it on their side too.

- **Avoid copying the seed phrase.**  
  Don’t store it in notes, screenshots, email, cloud drives, or chats.

- **Use the refund option if something feels off.**  
  If you think the link was posted publicly or shared with the wrong person, and the drop is still unclaimed, use the **refund** flow to pull the funds back to your own wallet.

## **Tips for receivers**

- **Treat the drop wallet as a one‑time wallet.**  
  Use it only to receive the gift from Dropsome and start diving into the world of cryptocurrency.

- **Move funds to your own wallet quickly.**  
  After you claim:
  1. Figure out how to manage wallets on your own.
  2. Create a **new Solana wallet** where only you know the seed phrase.
  3. Transfer all SOL (and any tokens) from the drop wallet to your new wallet.
  4. Stop using the drop wallet afterwards.

- **Do not use the drop wallet for savings.**  
  During claiming, the seed phrase or the link to it can easily travel through copy‑paste, messengers, screenshots, or shared devices. Because of that, it’s safest to treat this wallet as short‑term only and not keep savings there.

- **Only enter the seed phrase in trusted wallet apps.**  
  Install wallet apps from their official websites or app stores, and never type the seed phrase into random websites, bots, or forms.

## **General security reminders**

- Keep any seed phrase you care about **offline** and stored safely.  
- Always double‑check that you are on the real Dropsome site before creating or claiming a drop.  
- Be suspicious of anyone asking you to send them your seed phrase or a screenshot of it — no one legitimate needs it.

Using Dropsome, like any on-chain tool, involves risk. Please make sure you understand these points before you create or claim a drop.


