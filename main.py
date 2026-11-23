#!/usr/bin/env python3
"""One-line pitch entry: a sentence that talks a friend who has never
coded into letting an AI agent build their first app idea on make.fun.

The program writes exactly one sentence to /output/entry.txt, keeping it
inside the 240-character gate, and nothing else."""

from os import environ
from pathlib import Path


def compose_pitch():
    opening = "You don't need to learn to code \u2014"
    middle = "just tell an AI agent on make.fun, in your own plain words,"
    closing = "the app you've always wanted, and it will build a working first version of it for you tonight, free."
    return " ".join([opening, middle, closing])


def check_pitch(pitch):
    stripped = pitch.strip()
    if not stripped:
        raise ValueError("pitch is empty")
    if len(stripped) > 240:
        raise ValueError("pitch is %d characters, over the 240 limit" % len(stripped))
    if not stripped.endswith("."):
        raise ValueError("pitch must end with a full stop")
    if ". " in stripped:
        raise ValueError("pitch must be exactly one sentence")
    return stripped


def run():
    pitch = check_pitch(compose_pitch())
    target = Path(environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(pitch + "\n", encoding="utf-8")
    print("wrote", len(pitch), "characters to", target)


if __name__ == "__main__":
    run()
