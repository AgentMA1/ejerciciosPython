# ejercicio_29.py
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1
for _ in range(exponent):
    result *= base

print(f"The result of {base} raised to the power of {exponent} is {result}")

