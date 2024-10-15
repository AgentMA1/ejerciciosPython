#ejercicio_6.py
num = int(input("Enter a number: "))

keys_list = [str(i) for i in range(1, num+1)]
values_list = [i**2 for i in range(1, num +1)]

squares_dict = dict(zip(keys_list, values_list))

print(squares_dict)
