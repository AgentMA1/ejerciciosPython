#ejercicio_56.py
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_number = int(input("Enter the month number (1-12): "))

if 1 <= month_number <= 12:
    month_name = months[month_number - 1]
    days_in_month = days[month_number - 1]
    print(f"{month_name} has {days_in_month} days.")
else:
    print("Invalid month number.")

