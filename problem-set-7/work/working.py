import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^((?:[0-9]|10|11|12)(?::[0-5][0-9])? (?:AM|PM)) to ((?:[0-9]|10|11|12)(?::[0-5][0-9])? (?:AM|PM))$", s):
        start = convert_time(matches.group(1))
        stop = convert_time(matches.group(2))
        return f"{start} to {stop}"
    else:
        raise ValueError


def convert_time(s):
    time, meridiem = s.split(" ")
    try:
        hour, minute = time.split(":")
    except ValueError:
        hour = time
        minute = "00"

    if meridiem == "PM":
        if hour != "12":
            hour = int(hour) + 12
    else:
        if int(hour) < 10:
            hour = f"0{int(hour)}"
        elif hour == "12":
            hour = "00"


    return f"{hour}:{minute}"

if __name__ == "__main__":
    main()