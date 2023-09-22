def main():
    mass = int(input("Please enter the mass as integer in kilogram: "))
    print(calculate(mass))

def calculate(mass):
    c = 300000000
    return mass * pow(c, 2)

main()