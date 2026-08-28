"""
search_provider.py — the one place a URL is allowed to come from real.

Everything in this file makes a genuine outbound network call and
returns exactly what came back — no paraphrase, no interpretation, no
model in the loop. That is the whole point of this file existing: the
result it returns is inserted into the model's conversation by
executor.py, not typed by the model, so there is nothing for the model
to fabricate a URL as a substitute for.

Provider: Tavily (https://tavily.com), chosen because it's built for
exactly this use case — LLM tool-calling — and has a free tier (1,000
searches/month) that's enough to build and test against before anyone
commits to ongoing spend. Swapping in Brave Search or Serper later means
implementing the same two functions below against their APIs; nothing
in executor.py should need to change.
"""

import os
import requests

TAVILY_API_URL = "https://api.tavily.com"


class SearchProviderError(Exception):
    """Raised when the provider itself fails — auth, quota, network.
    Distinct from a search returning zero results, which is not an
    error (Law 5: not finding is a finding)."""


def _api_key() -> str:
    key = os.environ.get("TAVILY_API_KEY")
    if not key:
        raise SearchProviderError(
            "TAVILY_API_KEY is not set. Get a free key at "
            "https://tavily.com and export it before running the "
            "harness — there is no fallback that fabricates results "
            "instead."
        )
    return key


def search(query: str, max_results: int = 5) -> list:
    """
    Real web search. Returns a list of dicts, each:
      {"title": str, "url": str, "content": str, "published_date": str|None}

    Every field here came from Tavily's response — nothing is
    synthesized. If Tavily returns zero results, this returns an empty
    list, which the executor must treat as a real "not found," not
    retry-until-something-appears.
    """
    resp = requests.post(
        f"{TAVILY_API_URL}/search",
        json={
            "api_key": _api_key(),
            "query": query,
            "max_results": max_results,
            "include_answer": False,
        },
        timeout=20,
    )
    if resp.status_code != 200:
        raise SearchProviderError(
            f"Tavily search failed: HTTP {resp.status_code} — {resp.text[:300]}"
        )
    data = resp.json()
    results = []
    for r in data.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", ""),
            "published_date": r.get("published_date"),
        })
    return results


def fetch_url(url: str, max_chars: int = 6000) -> dict:
    """
    Real page fetch — opens the URL, strips markup, returns text. This
    is the difference between "a search result mentioned this" and "I
    opened the document" that sbr.py's INTEL phase instructions require
    (Law: "A SEARCH RESULT IS NOT A SOURCE").

    Returns {"url": str, "status": int|None, "text": str, "error": str|None}.
    A failed fetch is not swallowed into an empty string — `error` is set
    so the executor can log it as a Failed Retrieval, per sbr.py's own
    instruction not to substitute something else and move on.
    """
    from bs4 import BeautifulSoup

    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "Mozilla/5.0 (SuperBasicResearch/1.0)"},
        )
    except requests.RequestException as e:
        return {"url": url, "status": None, "text": "", "error": str(e)}

    if resp.status_code != 200:
        return {
            "url": url, "status": resp.status_code, "text": "",
            "error": f"HTTP {resp.status_code}",
        }

    soup = BeautifulSoup(resp.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()
    text = " ".join(soup.get_text(separator=" ").split())
    return {"url": url, "status": 200, "text": text[:max_chars], "error": None}
