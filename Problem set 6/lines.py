import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".py"):
        sys.exit("Not a Python file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    loc = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()

                if not stripped_line:
                    continue

                if stripped_line.startswith("#"):
                    continue

                loc += 1

        print(loc)
    except OSError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
