import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    numbers = ip.strip().split(".")
    if len(numbers) != 4:
        return False
    for n in numbers:
        try:
            num = int(n)
        except ValueError:
            return False
        if num > 255 or num < 0:
            return False

    return True


if __name__ == "__main__":
    main()