# ejercicio_22.py
import random

number_to_guess = random.randint(1, 100)
attempts_left = 10
guess = -1
attempts = 0

while attempts_left > 0:
    guess = int(input("Enter your guess: "))
    attempts += 1
    attempts_left -= 1

    if guess == number_to_guess:
        print("Congratulations! You guessed it in", attempts, "attempts.")
        break
    elif guess < number_to_guess:
        print("The number is higher.")
    else:
        print("The number is lower.")

    print("Attempts left:", attempts_left)

if guess != number_to_guess:
    print("You've run out of attempts. The number was", number_to_guess)

