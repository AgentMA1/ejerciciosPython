#ejercicio_70

string =input("Enter a Phrase!: ")

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character frequency in the Phrase:")
print(char_count)
