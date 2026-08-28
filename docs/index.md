---
layout: home

hero:
  name: SuperBasic™ Research
  text: A program you run instead of improvising
  tagline: Research with every claim tied to a checkable source. Eight phases, gates that can fail, and a legitimate way to report finding nothing.
  actions:
    - theme: brand
      text: Quick Start
      link: /guide/quick-start
    - theme: alt
      text: View on GitHub
      link: https://github.com/iamstefanp/superbasic-research

features:
  - icon: 🔒
    title: Fabrication caught, not just discouraged
    details: A real tool-calling harness cross-checks every cited source against what an actual search returned this run. Verified across 6 model families, including one live-caught fabrication attempt.
  - icon: 🧪
    title: Tested, not just claimed
    details: An 11-card adversarial method battery, plus a formal, pre-registered red-team evaluation of the harness itself — hypotheses frozen before results, raw evidence for every claim.
  - icon: 📖
    title: The standards stay complete
    details: 14 standards files carry the depth behind every phase — source scoring, independence testing, anomaly investigation. Nothing trimmed for convenience.
  - icon: ⚖️
    title: Calibrated confidence, always
    details: CONFIRMED, LIKELY, ESTIMATED, or UNKNOWN — never a bare assertion, never TBD. Not finding something is a finding, not a failure.
---

## One thing to know before you use this

Left alone, a model asked to research something searches a little, decides that
is enough, and writes something confident. Where it found nothing it produces
a plausible sentence, because it has no permitted way to say *"I could not find
this."* Both failures look identical to good work until someone acts on the
output.

**Bare-paste mode can fabricate.** Cross-model testing found that pasting the
method with no real search tool wired into the request makes some models
invent entire source tables — fake outlets, fake dates, fake quotes — and
stamp them CONFIRMED using the method's own scoring apparatus. Do not use
bare-paste mode for any claim where being wrong carries real cost.

**The [harness](/harness/setup) closes this** — real tool-calling, verified
across Claude, Gemini, ChatGPT, Mistral, DeepSeek, and Llama, with a
[formal red-team evaluation](/testing/red-team) proving the enforcement
mechanism catches fabrication when it happens, not just when a model behaves.
