def main():
    time = input("What time is it? ")
    check_meal(time)


def convert(time):
    h, m = time.split(":")
    return float(h) + float(m) / 60

def check_meal(time):
    converted_time = convert(time)
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("Lunch time")
    elif 18 <=  converted_time <= 19:
        print("Dinner time")
    else:
        pass


if __name__ == "__main__":
    main()