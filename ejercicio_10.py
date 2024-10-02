# ejercicio_10.py
partial1 = float(input("Enter the first grade: "))
partial2 = float(input("Enter the second grade: "))
partial3 = float(input("Enter the third grade: "))
final_exam = float(input("Enter the final exam grade: "))
final_project = float(input("Enter the final project grade: "))

average_parcials = (partial1 + partial2 + partial3) / 3
final_grade = (average_parcials * 0.55) + (final_exam * 0.30) + (final_project * 0.15)

print(f"Your final grade is: {final_grade}")

