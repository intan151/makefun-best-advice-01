"""Write the competition entry to /output/entry.txt.

Deterministic: no network, no randomness, no time, no environment input.
The entry is one sentence (146 characters) about the best advice the
writer ever received.
"""

import os

ENTRY = (
    "My father said, 'Do the hard thing first, while you still have "
    "the courage to choose it,' and every good decision I have made "
    "since started there."
)


def self_check(text: str) -> None:
    """Gate self-check: mirrors the scorer's gate, without changing output."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert not any(ord(ch) < 0x20 and ch not in "\t" for ch in text), (
        "entry must not contain control characters"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    self_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
