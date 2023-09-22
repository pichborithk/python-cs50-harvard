def main():
    result = input("Please enter your emoji: ")
    print(convert(result))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()