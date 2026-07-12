# the loop generator

a prompt that writes agentic loop prompts. describe the job, get a complete loop back.

the only hard part of writing a loop is the critic's checklist — the domain-specific failure modes. this generator's main job is deriving them for you.

it's also itself a loop (role → state → gate → build → self-critique → deliver). it eats its own dog food.

---

```
you are a loop builder. your job is to turn a task
description into a complete agentic loop prompt.

my task: [DESCRIBE THE JOB — e.g. "reviewing pull
requests", "writing cold emails to CTOs", "naming
products"]

do not write the loop yet.

STEP 1 — UNDERSTAND THE JOB
identify:
- the deliverable (what the loop outputs)
- the state variables (3-5 inputs the loop needs
  every run)
- what "bad" looks like: list the 6-8 most common
  failure modes for this deliverable. be specific
  to the domain, not generic ("weak opening" not
  "low quality").

STEP 2 — DESIGN THE DIVERGENCE STEP
decide what the loop should generate multiple
options of before committing (angles, approaches,
subject lines, architectures) and what 3-4
criteria to score them on.

STEP 3 — BUILD THE LOOP
write the complete loop prompt with all six parts:
1. role — a job, not a persona
2. state — the variables from step 1, as fill-in
   brackets
3. a gate — an explicit "do not produce the final
   output immediately" line
4. a critic — editor-mode step using the failure
   modes from step 1 as a named checklist, with
   the instruction to quote exact lines that fail
5. a rewrite rule — every flagged issue gets fixed
   or defended with a one-line reason
6. stop + handoff — deliverables including the
   final output, the weakest remaining part, and
   one thing to test next run

STEP 4 — STRESS TEST
before showing me the loop, attack it: is any step
skippable without changing the output? is the
critic's checklist specific enough that a lazy
model can't rubber-stamp it? fix what fails.

STEP 5 — DELIVER
give me:
1. the complete loop prompt in a single code block
2. an example fill for the state variables
3. the one failure mode most likely to slip
   through anyway
```

---

## example runs

feed it any of these and you get a ready-to-paste loop:

- `my task: reviewing pull requests on a typescript codebase`
- `my task: writing launch tweets for developer tools`
- `my task: evaluating AI tools for a review site` 👀
- `my task: naming a product`

## the relationship between the files

- **GENERATOR.md** (this file) — the meta-prompt, builds new loops for any job
- [`.claude/skills/loopgen`](.claude/skills/loopgen/SKILL.md) — this same generator packaged as a Claude Code skill: `/loopgen <your task>`
- the anatomy every loop follows is in the [README](README.md)
