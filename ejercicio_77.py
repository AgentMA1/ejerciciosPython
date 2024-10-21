#ejercicio_73.py
def login(username, password, attempts):
    if username == "user1" and password == "password123":
        return True, None
    else:
        attempts += 1
        return False, attempts

attempts = 0
while attempts < 3:
    user = input("Enter username: ")
    passwd = input("Enter password: ")

    success, attempts = login(user, passwd, attempts)

    if success:
        print("Login successful!")
        break
    else:
        print(f"Login failed. Attempts remaining: {3 - attempts}")

if attempts == 3:
    print("Login failed. No more attempts left.")

