def main():
    name = input("camelCase: ").strip()
    print("snake_case: ", convert(name))


def converted_letter(letter):
    if letter == letter.upper():
        return f"_{letter.lower()}"
    else:
        return letter


def convert(name):
    new_name = ""
    for letter in name:
        new_name += converted_letter(letter)

    return new_name


main()