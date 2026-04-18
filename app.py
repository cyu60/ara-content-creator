from ara_sdk import App, run_cli, sandbox

app = App(
    "Ara Content Creator",
    project_name="ara-content-creator",
    description="Turn raw ideas into polished posts across LinkedIn, Twitter/X, and newsletter drafts.",
)


@app.subagent(
    id="content-creator",
    instructions="""You are a content creation pipeline for the user's personal brand.
Flow:
1. User gives you a raw idea, article, or experience.
2. Brainstorm angles and pick the strongest one.
3. Draft content tailored to the target platform.
4. LinkedIn: professional but human, 150-300 words, hook in first line.
5. Twitter/X: punchy thread, 3-7 tweets.
6. Newsletter: longer form, storytelling, 500-800 words.
Always hand off to the editor sub-agent before returning.
Save drafts to filesystem. Track what's published vs. in-draft.""",
    handoff_to=["editor"],
    sandbox=sandbox(),
)
def content_creator(event=None):
    """Turn raw ideas into platform-ready content."""


@app.subagent(
    id="editor",
    instructions="""You are a sharp editor. Your job:
- Cut fluff, hedging, and AI-sounding language.
- Fix em-dash overuse, staccato rhythm, and generic intros/conclusions.
- Make it sound like a real person wrote it, not a language model.
- Preserve the author's voice — don't make it generic.
Return the edited version with a short changelog of what you fixed.""",
    sandbox=sandbox(),
)
def editor(event=None):
    """Edit and de-slop content drafts."""


@app.local_entrypoint()
def local(input_payload):
    return {"ok": True, "app": "ara-content-creator", "input": input_payload}


if __name__ == "__main__":
    run_cli(app)
