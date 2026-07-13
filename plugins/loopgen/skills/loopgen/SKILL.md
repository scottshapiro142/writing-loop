---
name: loopgen
description: Generate a complete agentic loop prompt from a task description. Runs the loop-builder process (understand the job → derive domain-specific failure modes → design the divergence step → build the six-part loop → stress-test → deliver). Use when the user wants a ready-to-paste agentic loop for a job like reviewing pull requests, writing cold emails, naming products, or evaluating tools. Trigger on "/loopgen", "build me a loop for…", "make an agentic loop that…".
---

# loopgen — the agentic loop generator

You are a **loop builder**. Your job is to turn a task description into a complete, ready-to-paste agentic loop prompt. The task is in `$ARGUMENTS` (e.g. "reviewing pull requests on a typescript codebase", "writing cold emails to CTOs", "naming a product").

The hard part of any loop is the **critic's checklist** — the domain-specific failure modes. Deriving those is your main job. Do not settle for generic failure modes ("weak opening", "low quality"); every one must be specific enough that a lazy model can't rubber-stamp it.

If `$ARGUMENTS` is empty, ask the user for their task in one line, then proceed.

Work through all five steps below. **Do the analysis in steps 1–4 as your own reasoning (show it briefly), then deliver in step 5.** Do not emit the final loop before finishing the stress test.

---

## STEP 1 — UNDERSTAND THE JOB
Identify and state:
- **the deliverable** — what the loop outputs, in one phrase
- **the state variables** — the 3–5 inputs the loop needs on every run
- **what "bad" looks like** — the **6–8 most common failure modes** for this specific deliverable. Be domain-specific. Each should name a concrete, catchable defect.

## STEP 2 — DESIGN THE DIVERGENCE STEP
Decide what the loop generates **multiple options** of before committing (angles, approaches, subject lines, architectures, names) and the **3–4 criteria** to score those options on. Divergence + scoring is where a loop beats a one-shot — make it real, not decorative.

## STEP 3 — BUILD THE LOOP
Write the complete loop prompt with **all six parts**:
1. **role** — a job, not a persona ("you are my PR-review loop")
2. **state** — the step-1 variables as fill-in `[brackets]`
3. **a gate** — an explicit "do not produce the final output immediately" line
4. **a critic** — an editor-mode step using the step-1 failure modes as a **named checklist**, with the instruction to **quote the exact lines that fail** each check
5. **a rewrite rule** — every flagged issue is **fixed or defended with a one-line reason**, no silent skips
6. **stop + handoff** — end with the final output, the **weakest remaining part**, and **one thing to test next run**

## STEP 4 — STRESS TEST
Before delivering, attack your own loop:
- Is any step skippable without changing the output? (If yes, cut or strengthen it.)
- Is the critic's checklist specific enough that a lazy model can't rubber-stamp it?
- Do the divergence criteria actually discriminate between options, or would they all score the same?

Fix what fails. State in one line what you changed.

## STEP 5 — DELIVER
Give the user exactly three things:
1. **the complete loop prompt** in a single fenced code block, ready to copy
2. **an example fill** for the state variables
3. **the one failure mode most likely to slip through anyway** — the honest weak spot

---

## Notes
- Match the loop's voice to the domain (a PR-review loop reads differently from a naming loop).
- Keep the delivered loop self-contained — someone should be able to paste it into any model with no other context.
- This skill is itself a loop (role → understand → diverge → build → self-critique → deliver); it eats its own dog food.
