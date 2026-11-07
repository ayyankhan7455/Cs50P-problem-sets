import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    valid_extensions = (".jpg", ".jpeg", ".png")

    ext1 = os.path.splitext(input_path)[1].lower()
    ext2 = os.path.splitext(output_path)[1].lower()

    if ext1 not in valid_extensions or ext2 not in valid_extensions:
        sys.exit("Invalid output")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    try:
        input_image = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")

    fitted_image = ImageOps.fit(input_image, shirt.size)

    fitted_image.paste(shirt, shirt)

    fitted_image.save(output_path)

if __name__ == "__main__":
    main()
