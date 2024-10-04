# ejercicio_31.py
number = int(input("Enter a number: "))

if number < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2

    while i * i <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(number, "is prime")
    else:
        print(number, "is not prime")

