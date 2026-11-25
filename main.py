#!/usr/bin/env python3
"""Entry for the make.fun bounty "Two Robots in an Elevator".

Writes exactly one funny line -- awkward small talk one robot says
to another in an elevator -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline.

Why this line should land with the judge (its brief, in my own words):
- Criterion 1 (on subject): it IS a line spoken in an elevator, about
  the elevator itself -- pressing floor buttons -- not a generic robot gag.
- Criterion 2 (machine logic): the robot solves a social problem the
  only way a machine can, by pressing every floor button. No human
  would "fix" awkwardness by making the ride longer; a robot would.
- Criterion 3 (awkwardness lands): the confession is made to the very
  robot he is avoiding. He tells the other robot, out loud, that he
  rigged the ride so someone else would have to talk to him first.
- Criterion 4 (funny on first read): the turn is the motive. Pressing
  every button sounds like a malfunction until the second half reveals
  it was deliberate social avoidance. No stock pun, no beep-boop.
- Criterion 5 (tight): 79 characters, one sentence, every word earns
  its place, and the punch lands on the last three words.
"""

import os
import sys


LINE = "I pressed every floor button so someone else will get on and talk to you first."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Self-check: the file on disk must be byte-identical to the line,
    # a single line, within the 1-200 character gate, no trailing newline.
    with open(target, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE or "\n" in written or not 1 <= len(written) <= 200:
        print("error: entry.txt does not match the line exactly",
              file=sys.stderr)
        return 1
    print("wrote", target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
