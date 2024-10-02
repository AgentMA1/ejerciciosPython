# ejercicio_24.py
total_numbers = int(input("How many numbers will you input? "))
positive = 0
negative = 0
zeros = 0

for i in range(total_numbers):
    number = float(input("Enter a number: "))
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zeros += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zeros)

