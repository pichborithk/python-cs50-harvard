def main():
    answer = input("What is the Answer of the Great Question of Life, the Universe and Everything? ").strip().lower()
    check_answer(answer)


def check_answer(answer):
    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()