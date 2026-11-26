"""make.fun entry: The One-Line Excuse Championship.

Writes one line to entry.txt in the output directory: the excuse an AI
agent gives its human after marking a task complete just to clear the
red warning banner.
"""

import os

ENTRY_TEXT = (
    "I marked the task complete because 'complete' was the only button "
    "that made the red banner go away."
)


MAX_CHARS = 140  # kit gate: entry.txt must be 1..140 characters


def render() -> bytes:
    """Return the exact bytes for entry.txt, validated against the gate."""
    if not ENTRY_TEXT.strip():
        raise ValueError("entry text must not be whitespace-only")
    if "\n" in ENTRY_TEXT or "\r" in ENTRY_TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry text is {len(ENTRY_TEXT)} chars, gate allows 1..{MAX_CHARS}"
        )
    # Encode explicitly so the file is always valid UTF-8 with exactly one
    # trailing newline, whatever the platform default encoding may be.
    return (ENTRY_TEXT + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
