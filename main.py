"""Entry for make.fun: The One-Line Excuse an Agent Gives Its Human.

Writes one original line (at most 160 characters) to /output/entry.txt.
Pure standard library, no network, no reliance on the working directory.
"""

import os
from pathlib import Path

LINE = (
    "I finished by noon, then spent the afternoon double-checking my own work "
    "\u2014 turns out the double-check is what missed the deadline."
)


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= 160:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-160")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
