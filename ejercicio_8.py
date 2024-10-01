# ejercicio_8.py
base_salary = float(input("Enter your base salary: "))
sale1 = float(input("Enter the value of the first sale: "))
sale2 = float(input("Enter the value of the second sale: "))
sale3 = float(input("Enter the value of the third sale: "))
commission = (sale1 + sale2 + sale3) * 0.10
total = base_salary + commission
print(f"Commission: {commission}")
print(f"Total to receive in the month: {total}")

