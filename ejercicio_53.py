#ejercicio_53.py
grades = []

for i in range(5):
    while True:
        grade = float(input(f"Enter grade {i+1} (0-10): "))
        if grade < 0:
            print('You can\'t have negative grades!')
        else:
            grades.append(grade)
            break

average_grade = sum(grades) / len(grades)
highest_grade = max(grades)
lowest_grade = min(grades)

print(f"Grades: {grades}")
print(f"Average grade: {average_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Lowest grade: {lowest_grade}")
