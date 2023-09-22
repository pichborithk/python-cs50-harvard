VOWELS = ["a", "e", "i", "o", "u"]

def main():
    sentence = input("Input: ")
    new_sentence = ""
    for letter in sentence:
        new_sentence += remove_vowel(letter)

    print(new_sentence)

def remove_vowel(letter):
    if letter.lower() in VOWELS:
        return ""
    else:
        return letter


main()