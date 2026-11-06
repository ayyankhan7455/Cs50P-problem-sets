def main():
    text = input("Input: ")
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    output = ""

    for char in text:
        if char not in vowels:
            output += char

        print(f"Output: {output}")


if __name__ == "__main__":
    main()
