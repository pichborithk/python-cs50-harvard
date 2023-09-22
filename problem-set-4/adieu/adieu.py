import inflect

p = inflect.engine()

def main():
    list: str = []
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            print("Adieu, adieu, to", p.join(list))
            break
        else:
            list.append(name)


if __name__ == "__main__":
    main()