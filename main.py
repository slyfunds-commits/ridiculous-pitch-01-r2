#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second -- round 2 entry.

Writes one pitch sentence to /output/entry.txt. The line was chosen from
306 candidates across 18 premise families by the culling funnel, then
gated against the round-1 line "The Obvious Hire" on the judge's five
criteria: it ties R1 on bizarre premise, novelty, business logic and
turn, and beats it clearly on concreteness (named buyer + price).
"""
import os

ENTRY = (
    "We rent emergency contacts for people with no one to list "
    "at $10 a month, so the hospital calls someone who actually "
    "picks up and cares."
)


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.strip(), "entry is blank"
    text.encode("utf-8")
    # The brief asks for ONE sentence: a single terminal period, no
    # internal sentence breaks, and no newline or control characters.
    assert text.endswith("."), "entry must end with a full stop"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    assert all(ord(c) >= 0x20 for c in text), "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Byte-verify: read back exactly what was written.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "byte mismatch on re-read"
    assert 1 <= len(raw.decode("utf-8")) <= 200
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
