# ejercicio_28.py
while True:
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    
    if lower_limit < upper_limit:
        break

sum_in_interval = 0
count_outside = 0
limit_number_count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break
    
    if lower_limit < number < upper_limit:
        sum_in_interval += number
    else:
        count_outside += 1
        
    if number == lower_limit or number == upper_limit:
        limit_number_count += 1

print(f"Sum inside the interval: {sum_in_interval}")
print(f"Numbers outside the interval: {count_outside}")
print(f"Numbers equal to the limits: {limit_number_count}")

