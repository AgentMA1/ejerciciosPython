#ejercicio_42.py
text = input("Enter a string: ")
substring = input("Enter a substring: ")

if text.startswith(substring):
    print("The string starts with the substring.")
else:
    print("The string does not start with the substring.")
