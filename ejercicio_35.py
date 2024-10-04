# ejercicio_35.py
total_paid = 0
payment = 10

for month in range(1, 21):
    print(f"Payment for month {month}: {payment}")
    total_paid += payment
    payment *= 2

print("Total paid after 20 months:", total_paid)

