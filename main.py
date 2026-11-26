"""Write the one-star review of the Moon to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

ENTRY = "One star. Ordered a full moon, got a sliver. No refund, no tracking number, and it still shows up late every month."
# ENTRY is 115 characters: within the competition gate of 1-120 characters.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
