#!/usr/bin/env python3
"""The Robot Apology — make.fun entry.

Writes a two-line robot confession to /output/entry.txt.

Line 1 apologizes in a single sentence for one specific mistake: the
robot watered the fern with cold coffee because it mistook the blue
mug for the watering can. Line 2 says in one sentence what it learned
and what it will do differently, and the lesson follows from that
exact mistake: confirm what is in its grip before it pours.

Pure Python standard library; no network, no secrets, no input files.
The output is deterministic so both grader runs produce the same entry.
"""

import os

LINE_1 = (
    "I am sorry I watered the fern with cold coffee this morning "
    "because I mistook your blue mug for the watering can."
)

LINE_2 = (
    "I learned to confirm what is in my grip before I pour, "
    "so now I lift, look, and only then water the plants."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    # Gate self-check, mirroring the competition rules: UTF-8 text of
    # 1 to 400 characters, not only white space, exactly two lines.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text.strip(), "entry must not be only white space"
    lines = text.strip().split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "neither line may be blank"
    # Each line must be exactly one sentence: a single terminal period,
    # no other sentence terminators crowding the line.
    for line in lines:
        stripped = line.strip()
        assert stripped.endswith("."), "each line must end with a period"
        assert stripped.count(".") == 1, "each line must hold one sentence"
        assert not any(c in stripped for c in "!?;"), "no extra terminators"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    print(f"wrote {len(encoded)} bytes, {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
