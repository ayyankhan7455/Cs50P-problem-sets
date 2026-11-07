import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Validates each octet (0-255) while properly disallowing leading zeros
    octet = r"(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)"
    if re.search(f"^{octet}\\.{octet}\\.{octet}\\.{octet}$", ip):
        return True
    return False

if __name__ == "__main__":
    main()
