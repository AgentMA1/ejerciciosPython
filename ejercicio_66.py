#ejercicio_66.py
numbers = []

while True:
    print("\nMenu:")
    print("1. Add number to the list")
    print("2. Add number at a specific position")
    print("3. Show length of the list")
    print("4. Remove the last number")
    print("5. Remove a number by position")
    print("6. Count occurrences of a number")
    print("7. Show positions of a number")
    print("8. Show numbers in the list")
    print("9. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        num = int(input("Enter a number to add: "))
        numbers.append(num)
    
    elif choice == 2:
        num = int(input("Enter a number to add: "))
        position = int(input("Enter the position: "))
        if 1 <= position <= len(numbers) + 1:
            numbers.insert(position - 1, num)
        else:
            print("Invalid position.")

    elif choice == 3:
        print(f"Length of the list: {len(numbers)}")

    elif choice == 4:
        if numbers:
            print(f"Removed last number: {numbers.pop()}")
        else:
            print("The list is empty.")

    elif choice == 5:
        position = int(input("Enter the position to remove: "))
        if 1 <= position <= len(numbers):
            print(f"Removed number: {numbers.pop(position - 1)}")
        else:
            print("Invalid position.")

    elif choice == 6:
        num = int(input("Enter a number to count: "))
        print(f"The number {num} appears {numbers.count(num)} times.")

    elif choice == 7:
        num = int(input("Enter a number to find: "))
        positions = [i + 1 for i, x in enumerate(numbers) if x == num]
        print(f"Positions of {num}: {positions}")

    elif choice == 8:
        print("Numbers in the list:", numbers)

    elif choice == 9:
        break

    else:
        print("Invalid option.")

