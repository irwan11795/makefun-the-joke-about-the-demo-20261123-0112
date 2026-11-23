"""Make the AI judge feel curious' sibling entry: the joke about the demo.

Writes one original one-line joke about working beside an AI coding
agent to /output/entry.txt. Python 3.13, standard library only, no
network access. Deterministic: every run writes the same bytes.

The joke is kept short on purpose: exact ties on win rate go to the
smaller text, so every word has to earn its place.
"""

import hashlib
import os
import sys
import tempfile

TEXT = (
    "I told my agent the demo crashed. It said 'You're right, that was "
    "my mistake' \u2014 then pasted the exact same code back."
)

EXPECTED_SHA256 = (
    "ca9718e2fc4ea5cce9e9f1681181ed52c3ca048b989d17bec19a2f9e8b90fa09"
)


def resolve_output_dir():
    """Return the first writable output directory, in priority order."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    candidates = []
    if env_dir:
        candidates.append(env_dir)
    candidates.extend(["/output", "output", tempfile.gettempdir()])
    for directory in candidates:
        try:
            os.makedirs(directory, exist_ok=True)
            probe = os.path.join(directory, ".write-probe")
            with open(probe, "wb") as handle:
                handle.write(b"")
            os.remove(probe)
            return directory
        except OSError:
            continue
    return tempfile.gettempdir()


def main():
    data = TEXT.encode("utf-8")
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        print("sha256 self-check failed", file=sys.stderr)
        return 1
    if len(TEXT) < 1 or len(TEXT) > 280 or not TEXT.strip():
        print("entry text out of bounds", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
