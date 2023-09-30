import sys
import csv


def check_valid_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


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
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        data = convert_table(file)
        file.close()

    with open(sys.argv[2], "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    main()