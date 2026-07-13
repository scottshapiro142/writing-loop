# Reselling Sourcing Rule — In-Store Cheat Card

A concrete operating rule for **thrift/resale flipping** (eBay, Mercari, Depop,
Poshmark). Use this when a roast verdict greenlights or reshapes a reselling
idea and the user is ready to source inventory. It answers the in-store
question: *"Should I buy this item?"*

This rule was itself pressure-tested by the council. The core "pay ⅓ / sell 3x"
instinct is the dominant real-world reseller heuristic and is confirmed sound —
but it only works with **four guardrails** the naive version misses: a real
comp, a dollar-profit floor, price tiers, and a condition check. They're baked
in below.

A buy is a YES only when **all** gates pass: comp is trustworthy, margin is
safe, the dollars clear a floor, it actually sells, and it's real/clean. One
gate without the others is a trap.

---

## Gate 0 — Get a trustworthy comp (most people skip this and it burns them)

Price off **SOLD** comps, never asking prices — but not off *one* sold comp.
→ eBay app: search → filter **"Sold"** → take the **median of 8–15 listings**
that match your item's **exact size, color, and condition**. Use the middle
cluster; ignore high/low outliers. Call that median **S**.

Three documented traps that inflate S — adjust for them:
- **Hidden Best-Offer prices.** eBay shows the *listed* price, not the
  accepted-offer price (often much lower). Assume real prices run below the
  sticker; check 130Point/Terapeak for high-dollar items.
- **Cancelled/returned orders still show as "sold."** A reversed sale stays in
  the comps forever — don't trust a lone high comp.
- **Condition/variant mismatch.** A NWT comp doesn't price your pilled, stained
  copy. Match condition or discount S.

If you can't find ~8 matched comps, treat S as a guess and be conservative.

## Gate 1 — Margin: "Will I make money?"

Work backward from S to the most you can pay:

| | Buyer pays shipping | Seller pays shipping |
|---|---|---|
| 🟩 **Target (~50% net margin)** | pay ≤ **⅓ of S** | pay ≤ **(⅓ of S) − shipping** |
| 🟥 **Never-cross (real break-even)** | pay ≤ **~70% of S** | pay ≤ **(~70% of S) − shipping** |

Fast mental version: **pay no more than ~⅓ of the median sold price.**
> Sold for 45 USD → pay under ~15 USD.

> ⚠️ The break-even line is **~70%, not 85%.** "Keep 85%" is eBay's fees-only
> figure; once *you* pay shipping and any promoted-listing fee, real take-home
> is ~65–80%. Paying ⅓ nets you **~2.3–2.6x your money after fees** — not a
> clean 3x. Shipping estimate when you pay it: ~6 USD clothes / ~10 USD shoes/boots.
> Fee assumption: eBay ~13.6% + 0.40 USD/order, charged on shipping too.

## Gate 2 — Dollar-profit floor: "Is it worth my labor?"

A percentage alone green-lights labor-negative buys. Sourcing + listing + pack +
ship is ~15–25 min **per item regardless of price**, so cheap flips lose money
even at a "great" margin.

> 🚫 **Skip anything that won't net ≥ ~12–15 USD after fees**, no matter how good
> the margin % looks. (Casual floor ~8–10 USD; part-time ~12–15 USD; full-time
> 15–25 USD.) A 9 USD item bought at ⅓ nets ~2 USD for 20 min of work — that's a loss.

## Gate 3 — Velocity: "Will it sell *fast enough*?"

Great margin on an item that sits for months freezes a small bankroll. Check
from the "Sold" screen, **matched to your size/variant** (category velocity ≠
your item's velocity):

- **Sell-through rate (STR)** = sold ÷ (sold + active). 🟢 **≥ ~50%** = strong;
  🟡 ~40% = minimum worth buying; 🔴 under ~20% = skip.
  *(Don't require "more sold than active" / STR > 100% — that's the rare elite
  tier, not a normal buy bar.)*
- **Recent dates:** several sold in the **last ~30 days** = it moves. Only 1–2,
  months old → skip unless it's a home-run flip.

## Gate 4 — Condition & authenticity (no gate here = funding fakes)

The margin gate authorizes *more dollars* exactly where fakes and flaws live
(sneakers, designer, denim, electronics). So:

- **Verify it's real** before a high-dollar buy. One fake = the whole sale
  reverses plus return shipping.
- **Inspect for flaws** the comp didn't have (stains, odor, pilling, missing
  parts, dead battery).
- **Tighten the buy ceiling as S rises** — more dollars at risk = more caution.

---

## The decision

> **Trustworthy comp + pay ≤ ⅓ of S + nets ≥ 12–15 USD + STR ≥ ~50% + real/clean
> = BUY.** Fail any gate → walk.

- Good margin + 🔴 velocity → **leave it.** Frozen cash is the #1 killer of a
  small bankroll.
- On a tight bankroll, **fast-and-decent beats slow-and-amazing** — the money
  has to recycle to compound.

## Make it usable on the floor (or the rule slows you to a crawl)

A picker can't comp 50 items at 60–90 sec each with bad signal. So:
- **Phone-comp only items over ~15 USD** (or anything you can't price from memory).
- **Memorize buy-ceilings** for the brands you see often — 80% of the rack is
  repeats; most items should need zero lookup.
- **Check velocity per category trend**, not per individual item.
- Skip the rest in under 30 seconds. Indecision is a cost.

## Tiers (apply before the gates)

- **Sub-20 USD sold price:** require deep margin **and** high velocity — cheap
  items only earn their keep as fast churn.
- **20–60 USD:** the classic ⅓ rule as written.
- **60 USD+:** can pay up to ~50% and accept slower turns — the absolute dollars
  justify your time and the wait.

## Compounding upgrade (turn the rule into a flywheel)

Log one row per buy at listing time — `date | category | comp S | paid | actual
sold price | days-to-sell | fees`. After ~50–100 sales, compute realized price ÷
comp (usually 0.7–0.9, not 1.0) and real days-to-sell per category, then **retune
the ⅓ multiple per category from your own data** instead of dogma. Track the
*skips* too if you can — that's how you find the gold you're leaving behind.

## What this rule does and doesn't promise
- It protects the **deal math** and screens for liquidity. It does **not**
  guarantee a sale — Gate 3 is the closest proxy; the only real proof is listing
  and watching what moves.
- **Validate it on your own data first:** backtest against listings you've
  already made — do the buys it would *approve* line up with your actual
  sellers/watchers, and the *rejects* with your dead stock? If yes, adopt it.
