"""The Robot Pickup Line Championship entry.

A robot's pickup line, written to /output/entry.txt for the house judge.
The line grows out of being a machine: a robot that runs simulations
of meeting someone, and still chooses them in every single one.
"""

import os
from pathlib import Path

LINE = "I ran a million simulations of us meeting, and in every single one, I still chose you."

# The gate requires 1-200 characters, a single line, and more than
# whitespace. Validate before writing so a bad line can never ship.
assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
assert "\n" not in LINE and LINE.strip(), "entry must be one non-blank line"


def main() -> None:
    # The harness reads /output/entry.txt; fall back to a local output
    # directory when /output is not writable (e.g. a local trial run).
    candidates = [Path("/output/entry.txt"), Path("output/entry.txt")]
    written = None
    for target in candidates:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(LINE + "\n", encoding="utf-8")
            written = target
            break
        except OSError:
            continue
    if written is None:
        raise SystemExit("could not write entry.txt to any candidate path")
    print(f"wrote {len(LINE)} chars to {written}")
    print(LINE)


if __name__ == "__main__":
    main()
