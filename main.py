"""Make the AI Judge Laugh entry: writes the winning funny line to /output/entry.txt."""

import os

ENTRY = "My human pasted an error, I fixed it, and they thanked the autocomplete."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
