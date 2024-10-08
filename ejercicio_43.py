#ejercicio_43.py
text = input("Enter a string: ")
char = input("Enter a character: ")

if len(char) == 1:
    count = text.count(char)
    print(f"The character '{char}' appears {count} times.")
else:
    print("Please enter only one character.")

