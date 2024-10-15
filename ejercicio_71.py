#ejercicio_71.py                                                                                                             #ejercicio_71.py

fruit_prices_stock ={
    'orange': 1.5,
    'strawberry': 1.8,
    'melon': 3,
    'tomato': 1.9
}

while True:

    fruit = input("What fruit do you want?")
    if fruit in fruit_prices_stock:
       try:
          quantity = float(input(f"Enter the quantity desired of {fruit}: "))
          if quantity < 0:
              print("Cant use negative values!")
              continue
          total_price = fruit_prices_stock[fruit] * quantity
          print(f"The price for {quantity} of {fruit} is: {total_price} euros")
       except ValueError:
          print("Wrong values used for quantity")
    else:
        print(f"Error: {fruit} not in stock.")
    another = input("Do you wanna make another order? (y/n): ")
    if another != 'y':
        break

