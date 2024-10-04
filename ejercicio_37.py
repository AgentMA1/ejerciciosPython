# ejercicio_37.py
num_workers = int(input("Enter number of workers: "))
total_payment = 0

for worker in range(num_workers):
    total_hours = 0
    for day in range(6):
        hours = float(input(f"Enter hours worked on day {day + 1} for worker {worker + 1}: "))
        total_hours += hours
    hourly_rate = float(input(f"Enter hourly rate for worker {worker + 1}: "))
    total_payment += total_hours * hourly_rate

print("Total payment for all workers:", total_payment)

