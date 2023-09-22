def main():
    filename = input("File name: ").strip().lower()
    check_filename(filename)


def check_filename(filename):
    if filename.endswith(".gif"):
        print("image/gif", end="")
    elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
        print("image/jpeg", end="")
    elif filename.endswith(".png"):
        print("image/png", end="")
    elif filename.endswith(".pdf"):
        print("application/pdf", end="")
    elif filename.endswith(".txt"):
        print("text/plain", end="")
    elif filename.endswith(".zip"):
        print("application/zip", end="")
    else:
        print("application/octet-stream")


main()