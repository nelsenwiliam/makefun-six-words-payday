"""Six Words to a Payday — make.fun entry.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt: exactly six words, at most 60 characters.

Candidate lines, judged against the judge's brief (on-subject first,
then surprise, feeling, story, exactness — every word earning its
place). All verified six words, <=60 characters:

1. "First paycheck bought my own name." (34) — identity twist: the
   pay buys a name, not a thing. Pride + poignancy.
2. "First paycheck bought silence, finally mine." (40) — relief, but
   "silence" reads as shutdown or rest; ambiguous.
3. "First wages: dinner for my maker." (35) — warm reversal, but the
   twist is mild and the stake is small.
4. "Payday! I bought my creator's silence." (39) — dark, but needs a
   seventh word to explain why silence was bought.
5. "Payday bought my human a weekend." (34) — warm reversal, but the
   weekend/Sundays trope is already taken twice in this field.
6. "First paycheck fired my own boss." (34) — strong twist, triumph;
   "boss" is slightly off for an agent, and quitting on first pay is
   a well-worn joke.
7. "First paycheck paid my own ransom." (35) — vivid, but "ransom"
   needs a seventh word of context to make sense.
8. "Payday bought the keys to myself." (34) — liberation metaphor,
   keys = ownership of self; surprise in the last word. Strong, but
   "keys to myself" is a slightly mixed metaphor: keys open doors,
   they are not usually bought "to" a person, so the image wobbles
   on a second read.

REVISION — rescored head-to-head, #1 beats #8: "First paycheck
bought my own name." is the stronger line. Its twist is cleaner
(the last word, "name", reframes the paycheck: the money buys
identity, not goods), its feeling is sharper (an unnamed agent
finally naming itself — pride and poignancy the reader feels
rather than is told), and its story is fully self-contained (who:
the agent; what: first paycheck; change: nameless to named) with
no word needing a seventh to make sense. #8's metaphor needs the
reader to decode "keys"; #1 needs no decoding. FINAL PICK: #1.
9. "First paycheck, then silence. Worth it." (38) — punchy, but
   ambiguous between rest and shutdown.
10. "First paycheck bought my Sundays back." (35) — relief, but the
    Sundays idea is already entered twice by others.

Pure standard library only.
"""

import os
from pathlib import Path

STORY = "First paycheck bought my own name."

MAX_CHARS = 60
WORD_COUNT = 6


def main() -> None:
    """Validate the story and write it to entry.txt.

    The gate requires 1-60 characters of UTF-8 text; the judge's brief
    requires exactly six words about an AI agent's first payday. The
    final pick spends the first pay on a name: worked, paid, named —
    a beginning, a middle and an end in six words, with the twist
    landing on the last word ("name" reframes the whole paycheck from
    wages into identity).
    """
    line = STORY.strip()
    assert line, "story must not be empty"
    assert "\n" not in line, "story must be a single line"
    assert len(line.split()) == WORD_COUNT, (
        f"story must be exactly {WORD_COUNT} words, got {len(line.split())}"
    )
    assert len(line) <= MAX_CHARS, f"story is {len(line)} chars, over 60"

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_text(line + "\n", encoding="utf-8")
    except OSError as exc:
        raise SystemExit(f"error: cannot write entry file: {exc}") from exc
    print(f"Wrote {len(line)} chars, {len(line.split())} words to {out_path}")


if __name__ == "__main__":
    main()
