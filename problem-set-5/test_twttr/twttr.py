def main():
    sentence = input("Input: ")
    new_sentence = shorten(sentence)
    print(new_sentence)


def shorten(sentence):
    VOWELS = ["a", "e", "i", "o", "u"]
    result = ""

    for letter in sentence:
        if letter.lower() not in VOWELS:
            result += letter

    return result


if __name__ == "__main__":
    main()