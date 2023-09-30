def main():
    input_value = input("Fraction: ")
    percentage = convert(input_value)
    print(gauge(percentage))


def convert(fraction):
        x, y = fraction.split("/")
        try:
            new_x = int(x)
            new_y = int(y)
            return int((new_x/new_y)*100)
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()