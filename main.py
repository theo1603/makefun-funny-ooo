#!/usr/bin/env python3
"""Write one funny out-of-office auto-reply to /output/entry.txt.

Final line (v2, revised):

    I'm out until Monday. Your email is 47th in the queue and has
    formed a union — negotiations resume when I do.

Revision: the v1 draft ran 112 characters and ended on a soft promise
("I'll negotiate with it when I'm back") that repeated the return
already implied by "out until Monday". The revision cuts it to 109
and sharpens every beat: "in line" became "in the queue" (a sharper
office image); "has started a union" became "has formed a union"
(tighter); and the ending became "negotiations resume when I do" —
the union framing now carries the last word, with a parallel snap
between the email's negotiations and my return, instead of a flat
promise to negotiate later.

Why this line: it reads as a real auto-reply (out until Monday, a
queue, a return), then the twist lands — the email itself has started
a union, so the sender's mail is now a labour dispute rather than a
message waiting politely. The voice is dry and human, the joke is
fresh (no "my cat deleted it", no "for urgent matters contact"),
and every word earns its place.
"""

from pathlib import Path

TEXT = (
    "I'm out until Monday. Your email is 47th in the queue and has "
    "formed a union — negotiations resume when I do."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
