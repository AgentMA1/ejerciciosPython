# ejercicio_32.py
total_savings = 0

for month in range(1, 13):
    deposit = float(input(f"Enter amount saved for month {month}: "))
    total_savings += deposit
    print(f"Total saved after month {month}: {total_savings}")

print("Total savings for the year:", total_savings)

