def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum()):
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            return s[i] != "0" and s[i:].isdigit()

    return True


if __name__ == "__main__":
     main()
