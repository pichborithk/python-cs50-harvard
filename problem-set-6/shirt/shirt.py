import sys
from PIL import Image, ImageOps

def check_valid_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:].lower() != ".jpg" and sys.argv[1][-4:].lower() != ".png" and sys.argv[1][-5:].lower() != ".jpeg":
        sys.exit("Invalid input")

    if sys.argv[1][-4:].lower() != sys.argv[2][-4:].lower():
        sys.exit("Input and output have different extensions")


def convert_table(file):
    reader = csv.DictReader(file)
    data = []
    for row in reader:
        last, first = row["name"].split(", ")
        data.append({"first": first, "last": last, "house": row["house"]})

    return data


def main():
    check_valid_file()

    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        size = shirt.size
        resized_image = ImageOps.fit(image, size)
        resized_image.paste(shirt, shirt)
        resized_image.save(sys.argv[2])



if __name__ == "__main__":
    main()