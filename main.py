"""One-Sentence Absurd Invention Pitch — make.fun text entry.

Writes one sentence pitching a ridiculous invention
to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
"""

import os
from pathlib import Path

ENTRY = "A doorbell that apologises to visitors for how long you took to answer, then charges you a small fee for the embarrassment."
MAX_CHARS = 220


def main():
    assert ENTRY.strip(), "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must not have leading or trailing whitespace"
    assert ENTRY[-1] in ".!?", "entry must end with terminal punctuation"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    back = target.read_text(encoding="utf-8")
    assert back == ENTRY, "round-trip mismatch"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
