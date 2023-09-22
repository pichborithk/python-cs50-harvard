def main():
    greeting = input("Greeting: ").strip().lower()
    check_greeting(greeting)


def check_greeting(greeting):
    if "hello" in greeting:
        print("$0")
    elif greeting[0] == "h":
        print("$20")
    else:
        print("$100")


main()