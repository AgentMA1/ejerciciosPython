# ejercicio_23.py
total = 0
count = 0
number = float(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    count += 1
    number = float(input("Enter a number (0 to stop): "))

if count > 0:
    print("Sum is", total)
    print("Average is", total / count)
else:
    print("No numbers entered")

