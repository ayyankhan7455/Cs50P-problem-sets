import sys
import os
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]

    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")

    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    table = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)

        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    except OSError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
