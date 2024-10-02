# ejercicio_25.py
char = input("Enter a character (space to stop): ").lower()

while char != " ":
    if char in "aeiou":
        print("VOWEL")
    else:
        print("NOT VOWEL")
    char = input("Enter a character (space to stop): ").lower()

