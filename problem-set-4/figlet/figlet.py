import sys
from pyfiglet import Figlet

list = ["slant", "rectangles", "alphabet"]


if len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in list:
        sys.exit("Invalid usage")
    else:
        f = Figlet(font=sys.argv[2])
elif len(sys.argv) == 1:
    f = Figlet()
else:
    sys.exit("Invalid usage")


sentence = input("Input: ")
print(f.renderText(sentence))
