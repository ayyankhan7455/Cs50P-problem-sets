
import sys
import random
from pyfiglet import Figlet

def main():
    fig = Figlet()
    available_fonts = fig.getFonts()

    # Check command-line arguments
    if len(sys.argv) == 1:
        # Choose a random font if no arguments are provided
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3:
        # Check if the first argument is valid and the second is an existing font
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in available_fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Set the font and prompt the user for text
    fig.setFont(font=font)
    text = input("Input: ")
    print(fig.renderText(text))

if __name__ == "__main__":
    main()
