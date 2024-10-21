#ejercicio_78.py
def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def convert_to_hms(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

while True:
    print("Menu:")
    print("1. Convert to seconds")
    print("2. Convert to hours, minutes, and seconds")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total_seconds = convert_to_seconds(hours, minutes, seconds)
        print(f"The total time in seconds is: {total_seconds}")
    elif choice == "2":
        seconds = int(input("Enter total seconds: "))
        h, m, s = convert_to_hms(seconds)
        print(f"{seconds} seconds equals {h} hours, {m} minutes, and {s} seconds")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option.Try again.")

