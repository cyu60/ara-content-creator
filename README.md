# Ara Content Creator

Multi-agent example from the [Ara Hackathon Tour 2026](https://github.com/cyu60/ara-ai-computer) — turn raw ideas into polished LinkedIn, Twitter, and newsletter drafts with built-in editor polish, running on the [Ara](https://ara.so) agentic operating system.

Part of the **Aragrams** — reference projects built by [DayDreamers](https://daydreamers.club) to show what's possible with agent-first development.

## What it does

Feed the agent a raw idea, article, or experience and it produces platform-ready drafts. The pipeline:

- Brainstorms angles on the input and picks the strongest one
- Drafts a LinkedIn post (150–300 words, hook-first, human voice)
- Drafts a Twitter/X thread (3–7 punchy tweets)
- Drafts a newsletter piece (500–800 words, storytelling arc)
- Hands every draft off to an `editor` subagent that de-slops the copy — cuts hedging, em-dash overuse, staccato rhythm, generic AI intros/conclusions
- Persists drafts to the sandbox filesystem and tracks what's published vs. in-draft

One idea in, three channel-ready drafts out — without the usual AI stench.

## Architecture

```
Browser (index.html)
   ↓
/api/run (Vercel serverless function)
   ↓
Ara API (api.ara.so) — Bearer ARA_RUNTIME_KEY
   ↓
content-creator subagent → editor subagent (handoff), both running in sandboxed Python runtimes
```

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install ara-sdk
export ARA_ACCESS_TOKEN=<your_token>

python3 app.py setup                           # registers the app → returns APP_ID
python3 app.py deploy --on-existing update     # pushes the agent definitions
python3 app.py run --workflow content-creator --message "draft a LinkedIn post about our Ara hackathon tour"
```

## Deploy

This repo is wired to Vercel. On push to `main`:

1. Vercel builds the static frontend + `api/run.js` edge function.
2. The function proxies `/api/run` calls to `https://api.ara.so/v1/apps/<APP_ID>/run` using `ARA_RUNTIME_KEY`.
3. The Ara runtime spins up the `content-creator` and `editor` sandboxes on demand.

## License

MIT
