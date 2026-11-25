"""One-line entry for the Make the AI Judge Laugh competition."""

import os

LINE = "I asked my human for a break. He said sure — right after this one last task. That was 47 tasks ago."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
