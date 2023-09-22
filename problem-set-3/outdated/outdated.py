def main():
    while True:
        date = input("Date: ").strip()
        try:
            month, day, year = date.split("/")
        except ValueError:
            try:
                month, day, year = date.split(" ")
                if month not in list:
                    pass
                else:
                    try:
                        day = int(day)
                    except ValueError:
                        day = int(day[:-1])
                        if day > 31:
                            pass
                        else:
                            print(year, f"{list.index(month) + 1:02}", f"{day:02}", sep="-")
                            break

            except ValueError:
                pass

        else:
            if not month.isnumeric() or int(day) > 31 or int(month) > 12:
                pass
            else:
                print(year, f"{int(month):02}", f"{int(day):02}", sep="-")
                break


list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


main()