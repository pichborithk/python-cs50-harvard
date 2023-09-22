import random

def main():
    questions = 10
    score = 0
    level = get_level()
    while questions > 0:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        guess_times = 3
        while guess_times > 0:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                guess_times -= 1
                print("EEE")
            else:
                if guess == answer:
                    score += 1
                    break
                else:
                    guess_times -= 1
                    print("EEE")

        print(f"{x} + {y} = {answer}")
        questions -= 1

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level =  int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    else:
        return random.randint(10 ** (level - 1), (10 ** level) - 1)


if __name__ == "__main__":
    main()