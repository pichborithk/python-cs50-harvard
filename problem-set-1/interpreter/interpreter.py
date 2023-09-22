def main():
    x, y, z = input("Expression: ").strip().split(" ")
    calculate(x, y, z)


def calculate(x, y, z):
    match y:
        case "+":
            print(float(x) + float(z))
        case "-":
            print(float(x) - float(z))
        case "*":
            print(float(x) * float(z))
        case "/":
            print(float(x) / float(z))
        case _:
            print("Error")


main()