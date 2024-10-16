#ejercicio_72.py

classroom = {}

num_students = int(input("Enter the student ID: "))

for _ in range(num_students):
    name = input("Enter the student Name: ")

    if name in classroom:
        print("Error: This student is already in the system.")
    else:
        grades = []
        while True:
            grade = float(input(f"Enter a grade for {name.title()} (negative number to stop): "))
            if grade < 0:
                break
            grades.append(grade)
        
        classroom[name] = grades

print("\n=== Final List of Students ===")
for name, grades in classroom.items():
    if grades:
        avg_grade = sum(grades) / len(grades)
        print(f"{name.title()} - Average grade: {avg_grade:.2f}")
    else:
        print(f"{name.title()} - No grades recorded.")
