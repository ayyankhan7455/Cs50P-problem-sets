def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Length check: min 2, max 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # First two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check characters and number rules
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            # First number cannot be '0'
            if not number_started and char == '0':
                return False
            number_started = True
        elif char.isalpha():
            # Letters cannot appear after numbers have started
            if number_started:
                return False
        else:
            # Punctuation, spaces, or symbols are not allowed
            return False

    return True


if __name__ == "__main__":
    main()
