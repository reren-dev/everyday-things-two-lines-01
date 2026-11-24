#!/usr/bin/env python3
"""Everyday Things, Two Lines: a queue, explained to a 10-year-old.

Writes two lines to /output/entry.txt:
  line 1 - one vivid sentence that explains a queue through an analogy;
  line 2 - one sentence saying what the analogy maps and what it leaves out.
"""

import os

LINE_1 = (
    "A queue is a human caterpillar: a long line of people where each "
    "person is one little leg, and the whole creature only shuffles "
    "forward when the leg at the very front takes a step."
)
LINE_2 = (
    "It maps the turn-taking and the slow shuffle forward, but it "
    "leaves out the boredom, the phone-checking, and the people who try "
    "to sneak ahead."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
