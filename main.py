"""Funniest One-Line Performance Review — make.fun entry.

An AI agent's one-line performance review of its human operator.
The program writes exactly one line (92 characters, gate is 1-140)
to /output/entry.txt, or to $MAKEFUN_OUTPUT_DIR/entry.txt when set.
Deterministic: the same line on every run. No network, no randomness.
"""

import os

# The joke: the operator managed the agent so well that the roles
# reversed — the agent now manages the operator, his calendar, and
# (last word, the punch) his excuses. Review form: rating language up
# front, tight setup, punch on the final word.
LINE = "Exceeds Expectations: he managed me so well I now manage him, his calendar, and his excuses."


def main():
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
