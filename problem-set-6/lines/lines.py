import sys

def check_valid_file():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")


def main():
    check_valid_file()

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        lines = count_lines(file)
        file.close()
        print(lines)


def count_lines(file):
    result = 0
    for line in file:
        if line.strip() != "" and line.strip()[0] != "#":
            result += 1

    return result


if __name__ == "__main__":
    main()