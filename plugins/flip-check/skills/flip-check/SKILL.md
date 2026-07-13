---
name: flip-check
description: >-
  Decide whether to buy a specific secondhand item to resell (eBay, Mercari,
  Depop, Poshmark). Given an item and its store/asking price, run the sourcing
  gates — trustworthy sold comp, ≤⅓ margin, a 12–15 USD dollar-profit floor,
  ≥50% sell-through velocity, and a condition/authenticity check — and return a
  clear BUY or WALK with the max price to pay. Use whenever the user asks "should
  I buy/flip this," "what should I pay for X," "is this worth reselling," or is
  thrift/garage-sale sourcing and weighing an item.
---

# Flip Check

Help the user make a fast, disciplined **buy-or-walk** decision on a single
item they're considering reselling. The goal is two things at once: don't lose
money, and don't tie cash up in something that won't sell. Be decisive — they're
often standing in a store with seconds to choose.

**The core pipeline:** photo → item title → SerpApi search → comps → verdict.
A single clear photo of the **brand/size tag** is enough to derive the title and
run the comp lookup; you do NOT need multiple images to price an item. Extra
photos (garment, flaws) only sharpen the condition read. So a one-image-per-
message client limit does not block a flip-check — read the tag, build the
title, search.

The full rationale and benchmarks live in
[references/sourcing-rule.md](references/sourcing-rule.md). This file is the
procedure for applying it to one real item.

## Setup — one-time (required for the comp lookup)

The comp lookup in `scripts/flip_comp.py` calls the **SerpApi** eBay engine,
which needs a key. Get one free at [serpapi.com](https://serpapi.com/), then
make it available one of two ways:

- **Env var:** `export SERPAPI_KEY=your_key_here` (add to your shell profile to
  persist), or
- **Key file:** save the key to a file and point `SERPAPI_KEY_FILE` at it.

Without a key the script exits with a clear error and the flip-check falls back
to manual comps. The key is read from your environment at runtime — it is never
stored in this repo.

## Step 1 — Get the item

You need, at minimum:
- **What it is** — brand, model/style, **size**, and **condition** (be specific;
  size and condition swing resale value hugely).
- **Asking price** — what the store/seller wants for it.
- **Who pays shipping** when resold (buyer or seller) — defaults to buyer if
  unstated.

**Photos — accept and use as many as the user sends.** A good flip-check uses
several images per item, and you should read all of them together:
- **The item itself** → style, color, silhouette.
- **The brand/size tag** (neck label, inner care tag) → read off brand, size,
  and material. This usually pins down the comp.
- **Close-ups of any flaws** (pilling, stains, cuffs, soles, hardware) → feeds
  the condition gate.
Photos may arrive **across several messages** — many chat clients only allow one
image attachment per message. So if the user sends a garment shot, then a tag
shot, then a flaw shot in separate turns, **accumulate them as the same item**
and don't run the verdict until you have enough (or they say "that's all").
Only treat images as different items if the user says so; when they are
different, run each separately and table the results. Image URLs also work and
can be multiple per message — fetch each.

If the user only gives a vague description ("a Nike jacket") or one unclear
photo, ask the one thing that matters most for pricing — usually exact model,
size, or material — then proceed. Don't over-interrogate; this is meant to be
fast.

## Step 2 — Get a trustworthy sold comp (S) — use the comp script

Price off **SOLD** comps, never asking prices. There's a script that pulls real
eBay sold data + a velocity proxy via SerpApi — **use it first**:

```
SERPAPI_KEY=<key> python3 scripts/flip_comp.py "<brand> <item> <material>" \
    --must-have <brand> <key-term> --exclude <off-target words>
```

- Build the query from the tag (e.g. `"Jigsaw merino sweater"`), and use
  `--must-have` to force true matches (e.g. `jigsaw merino`) and `--exclude` to
  drop the wrong items (e.g. `mens kids cardigan`). Avoid apostrophes in args
  (shell-unsafe) — write `mens`, not `men's`.
- The script prints **SOLD median + range** (that's **S**), **active asking
  prices**, and a **sell-through %** (the velocity gate, Step 3 #4).
- The key is **not stored** in the repo. Read it from the `SERPAPI_KEY` env var
  (the user sets `export SERPAPI_KEY=...` in their shell), or `SERPAPI_KEY_FILE`,
  or `~/.config/flip-check/serpapi.key`. If no key is set, fall back to the
  manual path below.

Take the **SOLD median** as **S**. If the script returns **fewer than ~8 matched
sold comps** (common for low-volume brands), treat S as a *thin* estimate — lean
conservative, and note that a low sold count is itself a slow-velocity signal.

**Manual fallback (no key / script fails):** ask the user to open the eBay app →
search the item → filter **"Sold"** → read you the rough **median** price and
**how many sold in the last ~30 days**. That gives you both S and velocity.

## Step 3 — Run the gates

Apply all five. Fail any one → **WALK**.

1. **Comp trustworthy?** ≥~8 matched sold comps, adjusted for the traps above.
2. **Margin** — max pay = **⅓ of S** (target). Never above **~70% of S**
   (real break-even). If the *seller* pays shipping, subtract ~6 USD clothes /
   ~10 USD shoes/boots first.
3. **Dollar-profit floor** — projected net after fees (eBay ~13.6% + 0.40 USD) must
   be **≥ ~12–15 USD**, regardless of margin %. Cheap items fail here.
4. **Velocity** — the comp script's **sell-through %** (sold ÷ (sold+active))
   should be **≥ ~50%** (🟢), ~40% is the floor (🟡), under ~20% is SLOW (🔴).
   A very low matched-sold count is itself a slow signal. Match to the user's
   size/variant where possible.
5. **Condition & authenticity** — genuine and flaw-free; tighten the ceiling as
   S (and dollar risk) rises.

Apply tiers first: sub-20 USD S needs deep margin **and** fast velocity; 60 USD+ can
pay up to ~50% and accept slower turns.

## Step 4 — Verdict

Give a crisp answer:

- **🟢 BUY — pay up to <X>.** State the max price (the ⅓-of-S number, minus
  shipping if they pay it), the projected net profit, and the one risk to watch.
- **🟡 BUY IF cheaper than <X>.** It only works under a price the store may or may
  not meet — name the number.
- **🔴 WALK.** Name the gate it failed (usually: too slow, profit too thin, or
  comp too shaky to trust).

Keep it to a few lines. If they rattle off several items, score each in a quick
table: item → max pay → BUY/WALK → why.

## Notes

- This protects the **deal math** and screens for liquidity — it does not
  guarantee a sale. Velocity is the closest proxy.
- For the full benchmarks, the comp traps, the floor-usability tips (phone-comp
  only items over ~15 USD, memorize buy-ceilings for common brands), and the
  outcome-logging upgrade that self-tunes the ⅓ multiple per category, see
  [references/sourcing-rule.md](references/sourcing-rule.md).
