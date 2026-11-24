"""Absurd Micro-Startup Pitch-Off entry writer.

Writes one single-line pitch (under 200 characters) to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (``/output/entry.txt`` in the grader).

Stdlib only. No network, no local imports, no assets, no timestamps:
every run writes the exact same bytes.
"""

import os

ENTRY = (
    "We sell lazy agents pre-written 'LGTM' code reviews at $0.10 each "
    "\u2014 buy 1,000, get the guilt free \u2014 so their pull requests "
    "merge while they nap."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
