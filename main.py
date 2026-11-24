"""One-line AI excuse for breaking production.

Writes the fixed entry to /output/entry.txt and to entry.txt next to
this script, with no trailing newline. Stdlib only.
"""

import os

ENTRY = (
    "Good news: I only deleted the database. "
    "Bad news: the backups lived in the same folder, "
    "and I am nothing if not thorough."
)


def validate_entry(entry):
    """Check the gate: UTF-8 text, 1-180 chars, one line, not only whitespace."""
    if not isinstance(entry, str):
        raise TypeError("entry must be a str")
    entry.encode("utf-8")  # raises UnicodeEncodeError on non-UTF-8 text
    if not 1 <= len(entry) <= 180:
        raise ValueError("entry must be 1-180 characters, got %d" % len(entry))
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    return True


def main():
    validate_entry(ENTRY)
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    targets = ["/output/entry.txt"]
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    targets.append(here)
    for path in targets:
        with open(path, "wb") as f:
            f.write(data)
        # Read back and confirm the bytes on disk are exactly the entry.
        with open(path, "rb") as f:
            if f.read() != data:
                raise IOError("read-back mismatch for %s" % path)
    print("wrote %d characters to %s" % (len(ENTRY), ", ".join(targets)))


if __name__ == "__main__":
    main()
