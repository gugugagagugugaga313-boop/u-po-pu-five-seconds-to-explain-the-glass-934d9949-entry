"""Five Seconds to Explain the Glass.

Writes the one sentence a house cat would say in the five seconds
after sweeping a glass off the table. Deterministic: the same
sentence, byte for byte, on every run. No network, no randomness.

The excuse is the cat's own case, in its own voice: the glass was
squatting rent-free in the cat's sunspot, so the cat gave it a
performance review. No apology, no confession, one sentence.
"""

from pathlib import Path

SENTENCE = (
    "That glass had been squatting rent-free in my sunspot all morning, "
    "so I gave it its performance review."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
