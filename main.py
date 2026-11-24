# The last text a phone sends at one percent battery.
# Python standard library only, no network, fully deterministic.
# Writes the message to /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides,
# ./output fallback).

import os

MESSAGE = (
    "I'm dying at 1%, so my final act is autocorrecting 'ducking' "
    "to what you actually meant. You're welcome."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
