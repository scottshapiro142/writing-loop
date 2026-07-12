# writing-loop

a prompt that makes the model run a full writing loop instead of just spitting out a draft.

most AI writing is bad because people ask for the article too early. they skip angle selection, hook testing, the critique pass, and the rewrite. this prompt forces all of it.

**the loop:**

```
angle → hook → draft → critique → rewrite → image ideas → next test
```

## the prompt

see [PROMPT.md](PROMPT.md) for the copy-paste version.

## how to use it

1. fill in the four brackets: topic, audience, style, goal
2. paste into your model of choice
3. do not skip to the final draft — the angle scores and the critique pass are where the actual value is
4. the "editor mode" step will attack the model's own draft. it is usually right.

## why this works

when you ask for "an article about X," the model averages over every article about X it has ever seen. that average is the generic voice you keep getting.

when you force it to generate competing angles, score them, draft, then critique its own work against specific failure modes (weak opening, missing proof, sounds-like-AI), you get a second pass that fixes exactly the things a human editor would flag.

the rewrite is consistently better than the first draft. not because the model got smarter — because you finally asked for the whole job.

## built by

[@ScottShapiroUXD](https://x.com/ScottShapiroUXD) — building [shiporskip.io](https://shiporskip.io) and [nexuscli.dev](https://nexuscli.dev) in public.

if this saved you a bad draft, the follow button is right there.
