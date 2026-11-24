"""Worst AI Advice entry.

Writes one original line of deliberately terrible AI advice to
entry.txt in the output directory. The line is a fixed string: the
program is fully deterministic, so two runs produce byte-identical
output.
"""

import os

ADVICE = (
    "For best security, use the same password everywhere and email it "
    "to yourself as a backup \u2014 that way you can never be locked out."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
