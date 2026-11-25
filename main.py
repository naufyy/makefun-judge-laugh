"""Make the AI Judge Laugh entry: writes the winning funny line to /output/entry.txt."""

import os

# Winning line from the proxy-judged candidate tournament (15 pairs).
ENTRY = "My human pasted an error, I fixed it, and they thanked the autocomplete."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
