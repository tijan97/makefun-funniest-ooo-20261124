"""Funniest Out-of-Office entry for make.fun.

Writes a single-line out-of-office auto-reply (140 characters or fewer)
to /output/entry.txt.
"""

import os

ENTRY = (
    "Out of office until Monday. My dog is answering emails now - "
    "she has approved two budgets and declined the one meeting I wanted."
)


def validate_entry(text: str) -> None:
    """Enforce the competition gate: 1-140 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(text) > 140:
        raise ValueError(f"entry is {len(text)} chars, over the 140 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    validate_entry(ENTRY)
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
