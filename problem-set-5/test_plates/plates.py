def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6 or s[0].isnumeric() or s[1].isnumeric():
        return False
    else:
        remain_string = s[2:]
        has_number = False
        for letter in remain_string:
            if not has_number:
                if letter == "0":
                    return False
                elif letter.isnumeric():
                    has_number = True
            else:
                if not letter.isnumeric():
                    return False

        return True

if __name__ == "__main__":
    main()