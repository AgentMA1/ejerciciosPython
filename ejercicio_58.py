#ejercicio_58.py
students = []

while True:
    name = input("Enter student name (* to stop): ")
    if name == "*":
        break
    age = int(input("Enter student age: "))
    students.append((name, age))

adults = [student for student in students if student[1] >= 18]
oldest_age = max(students, key=lambda student: student[1])[1]
oldest_students = [student for student in students if student[1] == oldest_age]

print("Adult students:", adults)
print("Oldest students:", oldest_students)

