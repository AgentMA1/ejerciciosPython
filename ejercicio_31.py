# ejercicio_30.py
for number in range(1, 6):  # Loop with `for`
    print("Multiplication table for", number)
    
    for i in range(1, 11):  # Nested loop with `for`
        print(number, "x", i, "=", number * i)
    print()

