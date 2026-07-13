# agentic-loop

your prompt one-shots. an agent loops. that's the entire difference.

this repo is one prompt that turns a normal request into an agentic loop — no framework, no orchestration layer, just a prompt shaped like a loop.

## the anatomy

every agentic loop prompt has six parts:

1. **role** — a job, not a persona ("you are my writing loop")
2. **state** — the variables the loop runs on (topic, audience, style, goal)
3. **ordered steps with a gate** — "do not produce the final output immediately" blocks the one-shot reflex
4. **a critic with a named checklist** — vague critics rubber-stamp; named failure modes catch things
5. **a rewrite rule** — every flagged issue gets fixed or defended, no silent skips
6. **a stopping condition + handoff** — end with the deliverable, the weakest remaining part, and what to test next run

## the prompts

- [GENERATOR.md](GENERATOR.md) — a meta-prompt that builds a new loop for any job you describe. the generator is itself a loop.
- [`.claude/skills/loopgen`](.claude/skills/loopgen/SKILL.md) — the generator packaged as a Claude Code skill. type `/loopgen <your task>` and it runs the five steps and hands back a ready-to-paste loop.

swap the steps and the critic's checklist to loop anything — code review, landing page copy, cold emails. or let the generator do the swapping.

## the skill

if you use Claude Code, you don't have to paste the meta-prompt by hand:

```
/loopgen reviewing pull requests on a typescript codebase
```

it derives the domain-specific failure modes, designs the divergence step, builds the six-part loop, stress-tests it, and delivers the loop plus an example fill plus the one failure mode most likely to slip through.

## the shiporskip marketplace

this repo is also the **shiporskip** Claude Code plugin marketplace — a single home for the tools i ship. add it once:

```
/plugin marketplace add scottshapiro142/writing-loop
```

(you add the *repo* `writing-loop`, but install from the *marketplace* named `shiporskip`.) then install any of the tools:

| tool | what it does | install |
|------|--------------|---------|
| **loopgen** | turn a task description into a ready-to-paste agentic loop | `/plugin install loopgen@shiporskip` |
| **roast** | adversarial council that stress-tests an idea → GREEN LIGHT / RESHAPE / KILL + the cheapest 48-hour test | `/plugin install roast@shiporskip` |
| **flip-check** | should you buy this secondhand item to resell? BUY / WALK + max price (ships an eBay comps script) | `/plugin install flip-check@shiporskip` |

once installed, each tool's slash command (`/loopgen`, `/roast`, `/flip-check`) works in every project.

**or clone and use loopgen here** — it also lives at `.claude/skills/loopgen/`, so running Claude Code inside a clone of this repo exposes `/loopgen` with no install step.

> maintainer notes:
> - each tool is a plugin under `plugins/<name>/`. edit the copy there, then bump `version` in its `plugins/<name>/.claude-plugin/plugin.json` so installed users pull the change on `/plugin marketplace update`.
> - `loopgen` also has a project-skill copy at `.claude/skills/loopgen/` (for clone-and-run). keep it identical to `plugins/loopgen/skills/loopgen/SKILL.md` when editing.

## how to use it

1. fill in the four state variables
2. paste into your model of choice
3. don't skip to the final output — the option-scoring and the critique pass are where the value is
4. the critic will attack the model's own work. it is usually right.

## why this works

a one-shot prompt gives you the average of everything the model has seen on that topic. the loop forces divergence (multiple options), judgment (scoring), and revision (critique → rewrite) — the three things a competent human does instinctively and a one-shot prompt skips entirely.

## built by

[@ScottShapiroUXD](https://x.com/ScottShapiroUXD) — building [shiporskip.io](https://shiporskip.io) and [nexuscli.dev](https://nexuscli.dev) in public.

if this saved you a bad draft, the follow button is right there.
