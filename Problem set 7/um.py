import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Use regular expression with word boundaries (\b) and case-insensitive flag (re.IGNORECASE)
    # to find "um" as a standalone word.
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
