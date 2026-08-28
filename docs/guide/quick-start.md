# Quick Start

## 1. No install — paste it

Open [`SKILL.md`](https://github.com/iamstefanp/superbasic-research/blob/main/SKILL.md)
on GitHub, copy everything in it, and paste it into the start of a
conversation with an AI chat **that has live search or browsing turned on.**

Ask your actual research question. The method should first ask whether it
actually has a usable search tool right now, then what mode to run in
(LIGHT or HEAVY).

::: warning Read this before you rely on step 1 for anything that matters
Bare-paste mode — no real tool wired into the request — can make some models
fabricate entire source tables and stamp them CONFIRMED. See
[Security & Legal](/guide/security-legal) and the
[red-team evaluation](/testing/red-team) for the full picture. Use the
harness below for anything where being wrong carries real cost.
:::

## 2. Programmatic — real tool-calling, verified across 6 model families

```python
import sys
sys.path.insert(0, "harness")
import executor, sbr

card = sbr.RunCard({"question": "your real research question", "mode": "LIGHT"})
ctx  = sbr.RunContext({"destination": None})

result = sbr.run_sbr(
    card, ctx,
    agent_executor=executor.make_executor(
        model="anthropic/claude-sonnet-5", backend="openrouter", max_tokens=12000,
    ),
    writer=lambda dest, name, content: {"id": name, "url": None},
)
print(result.status)      # COMPLETE | PARTIAL | STOPPED
```

## 3. HEAVY mode — more sources, stricter thresholds, same code

```python
card = sbr.RunCard({"question": "your real research question", "mode": "HEAVY"})
# everything else identical — mode is the only thing that changes
```

See [Connect Your Setup](/guide/connect) for Claude Code, claude.ai, ChatGPT,
Gemini, and running it as part of an agent.
