import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    m1 = int(m1) if m1 is not None else 0
    h2 = int(h2)
    m2 = int(m2) if m2 is not None else 0

    return f"{to_24(h1, m1, p1)} to {to_24(h2, m2, p2)}"


def to_24(h, m, p):
    if p == "AM":
        h_24 = 0 if h == 12 else h
    else:
        h_24 = 12 if h == 12 else h + 12
    return f"{h_24:02}:{m:02}"


if __name__ == "__main__":
    main()
