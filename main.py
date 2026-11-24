#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, so it can be tested locally).

The haiku's angle: the off-by-one error, the oldest bug in the book,
as a corridor of doors — a thousand swing open, the last one stays
shut. Concrete, true to the work, and the last line reframes the
first two: the bug was never the thousand doors. It was the one.

Form: 5-7-5, seventeen syllables, three lines, well under 200 chars.
Standard library only. No network, no clock, no randomness:
every run writes the same bytes.
"""

# The entry. Counted by hand, verified by the table below.
HAIKU = (
    "off by one, again",
    "a thousand doors swing open",
    "the last one stays shut",
)

EXPECTED_SYLLABLES = (5, 7, 5)

# Syllable count per word, counted by hand. English spelling lies
# ("one" looks like two vowel sounds, "again" hides its second beat),
# so the program checks against this table instead of guessing.
SYLLABLES = {
    "off": 1, "by": 1, "one": 1, "again": 2,
    "a": 1, "thousand": 2, "doors": 1, "swing": 1, "open": 2,
    "the": 1, "last": 1, "stays": 1, "shut": 1,
}


def count_line(line: str) -> int:
    """Syllables in one line, from the hand-counted table."""
    words = line.replace(",", "").split()
    return sum(SYLLABLES[word] for word in words)


def validate(text: str) -> None:
    """Fail loudly unless the text passes the competition gate."""
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(text) <= 200, f"expected 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_line(line)
        assert got == expected, f"{line!r}: expected {expected} syllables, got {got}"


def write_entry() -> str:
    """Build the entry text and write it to /output/entry.txt."""
    import os

    text = "\n".join(HAIKU)
    validate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    path = write_entry()
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
