from datetime import date
import re
import inflect
import sys

p = inflect.engine()

class MinuteOfDate:
    def __init__(self, dof):
        self.minute = dof

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, dof):
        if re.search(r"[0-9]{4}-(?:(?:0[1-9])|10|11|12)-(?:(?:0[1-9])|(?:[1-2][0-9])|30|31)", dof):
            days = (date.today() - date.fromisoformat(dof)).days
            minutes = int(days) * 24 * 60
            self._minute = p.number_to_words(minutes, andword="").capitalize()
        else:
            raise ValueError

    @classmethod
    def get(cls):
        dof = input("Date of Birth: ")
        try:
            minute = cls(dof)
        except ValueError:
            sys.exit("Invalid date")
        else:
            return minute

    def __str__(self):
        return f"{self.minute}"

def main():
    minute = MinuteOfDate.get()
    print(minute, "minutes")


if __name__ == "__main__":
    main()