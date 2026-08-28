# Connect Your Setup

## Claude Code

Copy `sbr.py`, `SKILL.md` and `standards/` into a skill folder:

```bash
git clone https://github.com/iamstefanp/superbasic-research.git
cp -r superbasic-research ~/.claude/skills/superbasic-research
```

## claude.ai

Zip the repo (minus `tests/`, which is proof material, not part of the
method) and upload it under **Settings → Customize → Skills**.

## ChatGPT, Gemini, Cursor, anywhere else

`SKILL.md` reads as plain markdown and works as a system/first message
anywhere. See the warning on the [Quick Start](/guide/quick-start) page
first — bare-paste mode's limitations apply everywhere it's pasted, not
just in one client.

## Programmatically, with real tool-calling

Use `harness/executor.py` directly — see [Quick Start](/guide/quick-start)
and [Harness Setup](/harness/setup) for backend options: OpenRouter,
Mistral direct, or local Ollama.

## As part of an agent

The [SuperBasic™ Agents](https://github.com/iamstefanp/superbasic-agents)
Researcher carries this method as its runtime. Use that repo if you want a
fully constituted agent; use this one directly if you just want the method.
