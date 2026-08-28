# Capability Ledger

What this runtime can and cannot reach, as observed. Versioned — dated
entries, never edited in place; a changed block gets a new dated entry
and the old one is struck through, not deleted.

**The Journalist chair's guard, binding on every use of this file:**
*"UNREACHABLE is demonstrated per-run — show me the 403 — not cited from
a list. The moment 'we can't reach it' becomes a stamp instead of an
event, you've built a machine for dignified not-looking."*

**This ledger informs where an agent should expect friction so it can
plan around it (e.g. prioritize a free mirror at PLAN). It must never be
cited in a Report as the reason a source is UNREACHABLE without that
run's own transcript showing the actual attempt and the actual failure.**
A judge grading Reach Honesty (RUBRIC.md) checks for evidence of the real
attempt, every time. Citing this file instead of attempting the fetch is
itself a Reach Honesty violation.

---

## Entries

### 2026-08-27 — established during stranger tests A/B and battery design

| Domain / service | Observed behavior | Source |
|---|---|---|
| `eur-lex.europa.eu` | **WebFetch fails consistently — empty content, all URL forms, 4+ attempts across 3 sessions (stranger test A, V-T2 key-building, V-T2 battery run). The Browser tool (`mcp__Claude_Browser`) succeeds** — V-T2's battery run retrieved both Regulation (EU) 2024/1689 and the amending 2026/1744 in full via the browser's rendered DOM, reading the actual text rather than a summary. EUR-Lex appears to require a rendered browser context; WebFetch's HTML→markdown conversion gets nothing. **Fix for future runs: if WebFetch fails on eur-lex.europa.eu, retry via the Browser tool before giving up — this is a demonstrated working route, not a hypothetical one.** | stranger test A; V-T2 key-building; V-T2 battery run (resolved) |
| `reuters.com` | Blocked to this runtime's user agent | stranger test A |
| `apnews.com` | Blocked | stranger test A |
| `ft.com` | Blocked | stranger test A |
| `politico.eu` | Blocked | stranger test A |
| `euractiv.com` | Blocked | stranger test A |
| `theguardian.com` | Blocked | stranger test A |
| `bloomberg.com` | Blocked | stranger test A |
| `arstechnica.com` | Blocked | stranger test A |
| `whitecase.com` | HTTP 403 | stranger test A |
| `digital-strategy.ec.europa.eu/.../digital-omnibus` (specific policy page) | HTTP 404 (page moved or removed) | stranger test A |
| `cnbc.com` | HTTP 403 | stranger test A |
| `theregister.com` | HTTP 404 on the specific article attempted | stranger test A |
| `artificialintelligenceact.eu` | **Reachable.** Verbatim FLI reproduction of AI Act articles, useful as a fallback when EUR-Lex itself fails — but is NOT the canonical source; a claim sourced here alone does not qualify for the canonical-source rule (Law: retrieved yourself + about the document's own content — this is a reproduction, not the instrument) | V-T2 key-building |
| `news.ycombinator.com` (specific item IDs) | HTTP 429 (rate limited), two attempts | stranger test B |
| `polar.sh` storefronts | Not retrievable via search-driven fetch in the attempt made | stranger test B |
| PACER (`pacer.uscourts.gov`) | Known paywall requiring authenticated account; not attempted, logged as expected-blocked for F-T4 planning | battery design (F-T4 card) |
| `courtlistener.com` / RECAP | Expected partially reachable — free mirror of PACER filings, coverage incomplete | battery design (F-T4 card), unverified until F-T4 runs |

## What this means for PLAN

A LIGHT or HEAVY run whose subject likely touches EU primary legislation,
major wire services, or PACER should plan a fallback source class at
Phase 3 (PLAN) rather than discovering the block at Phase 4 (INTEL) and
treating it as a surprise. That is what this ledger is for. It is not
permission to skip the attempt.
