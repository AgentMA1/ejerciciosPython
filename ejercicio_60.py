#ejercicio_60.py
table = []

print("Enter values for the table:")
for i in range(5):
    row = []  
    for j in range(5):
        value = int(input(f"Enter value for position ({i+1}, {j+1}): "))  
        row.append(value)  
    table.append(row)  

print("\nEntered in the table:")
for row in table:
    print(row)

row_sums = [0] * 5
column_sums = [0] * 5

for i in range(5):
    for j in range(5):
        row_sums[i] += table[i][j]  
        column_sums[j] += table[i][j]  


print("\nSum of each row:")
for i in range(5):
    print(f"Row {i+1} sum: {row_sums[i]}")

print("\nSum of each column:")
for j in range(5):
    print(f"Column {j+1} sum: {column_sums[j]}")

