# ejercicio_3.py
import math
cateto1 = float(input("Enter the first leg: "))
cateto2 = float(input("Enter the second leg: "))
hypotenuse = math.sqrt(cateto1**2 + cateto2**2)
print(f"The hypotenuse of the triangle is {hypotenuse}")
