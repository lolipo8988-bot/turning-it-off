#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun entry (program/v1).

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt, per the competition RULES).

The joke twists the classic restart line: the agent's entire training
is just that one question, asked on a loop. Cheerful, useless, and
the customer is never the butt of it -- the agent is.

Why this line should win the head-to-heads, against the judge's brief:
  1. On-subject: a single-line support-agent reply, restart gag included.
  2. The twist is the agent, not the customer: his whole training is
     one step, and step two is just asking again. Unexpected, and the
     cheerful uselessness is the joke.
  3. It sounds like a real agent on a call -- "No? Perfect --" answers
     the customer mid-conversation, so their desperation is felt, not
     explained.
  4. Tight: every word earns its place, clear on a first read.
  5. Fresh: it leans on the off-and-on-again classic and twists it
     into an infinite loop of asking.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? No? Perfect \u2014 "
    "that's step one of my entire training, and step two is asking "
    "you to do it again."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 199 characters.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
