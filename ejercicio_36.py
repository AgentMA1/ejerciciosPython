# ejercicio_36.py
num_workers = int(input("Enter number of workers: "))
total_payment = 0

for worker in range(num_workers):
    hours_worked = float(input(f"Enter hours worked for worker {worker + 1}: "))
    hourly_rate = float(input(f"Enter hourly rate for worker {worker + 1}: "))
    total_payment += hours_worked * hourly_rate

print("Total payment for all workers:", total_payment)

