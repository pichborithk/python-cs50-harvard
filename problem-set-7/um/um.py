import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    result = 0
    words = s.strip().split(" ")
    # print(words)
    for word in words:
        if matches := re.search(r"^um[^a-z0-9]*$", word, re.IGNORECASE):
            # print(matches.group())
            result += 1

    return result


if __name__ == "__main__":
    main()