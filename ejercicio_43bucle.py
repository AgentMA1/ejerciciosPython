#ejercicio_43bucle.py
text = input("Enter a string: ")
char = input("Enter a character: ")

if len(char) == 1:
    count = 0
    for c in text:
        if c == char:
            count += 1
    print(f"The character '{char}' appears {count} times.")
else:
    print("Please enter only one character.")
