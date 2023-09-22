def main():
    dict = {}

    while True:
        try:
            item = input("").strip().upper()
        except EOFError:
            for key, value in sorted(dict.items()):
                print(value, key)
            break
        else:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1


main()