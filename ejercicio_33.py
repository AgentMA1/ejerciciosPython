# ejercicio_33.py
total_hours = 0
hourly_wage = float(input("Enter hourly wage: "))

for day in range(6):
    hours = float(input(f"Enter hours worked for day {day + 1}: "))
    total_hours += hours

total_salary = total_hours * hourly_wage
print("Total hours worked:", total_hours)
print("Total salary:", total_salary)

