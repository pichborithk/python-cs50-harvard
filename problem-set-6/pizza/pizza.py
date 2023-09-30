import sys
import csv
from tabulate import tabulate


def check_valid_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a CSV file")


def convert_csv(file):
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append(row)

    return data[0], data[1:]


def main():
    check_valid_file()

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        headers, table = convert_csv(file)
        file.close()
        print(tabulate(table, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()