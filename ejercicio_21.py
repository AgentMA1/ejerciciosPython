# ejercicio_21.py
number = int(input("Enter a number: "))
factorial = 1
if number == 0:
    factorial = 1
else:
    i = 1
    while i <= number:
        factorial *= i
        i += 1

print("The factorial is", factorial)

