import validators

def main():
    email = input("What's your email address? ")
    result = "Valid" if validators.email(email) else "Invalid"
    print(result)


if __name__ == "__main__":
    main()