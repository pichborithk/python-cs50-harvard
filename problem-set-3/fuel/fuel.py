def main():
    result = get_fraction()
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{round(result)}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if x <= y:
                return (int(x) / int(y)) * 100
        except (ValueError, ZeroDivisionError):
            pass


main()