#ejercicio_73.py

agenda = {}

def add_modify_contact():
    name = input("Enter the name: ")
    if name in agenda:
        print(f"{name.title()} is already in the agenda, its phone number is: {agenda[name]}")
        modify = input("Do you want to modify the phone number? (y/n): ")
        if modify == 'y':
            new_phone = input("Enter the new phone number: ")
            agenda[name] = new_phone
            print(f"Phone number updated for {name.title()}.")
    else:
        phone = input("Enter the phone number: ")
        agenda[name] = phone
        print(f"Contact {name.title()} added to the agenda.")

def search_contact():
    search = input("Enter the name to search: ").lower()
    results = {name: phone for name, phone in agenda.items() if name.startswith(search)}
    
    if results:
        print("Search results:")
        for name, phone in results.items():
            print(f"{name.title()}: {phone}")
    else:
        print("No contacts found.")

def delete_contact():
    name = input("Enter the contact to delete: ").lower()
    if name in agenda:
        confirm = input(f"Do you really want to delete {name.title()}? (y/n): ").lower()
        if confirm == 'y':
            del agenda[name]
            print(f"Contact {name.title()} deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No contact found with the name {name.title()}.")

def list_contacts():
    if agenda:
        print("List of contacts:")
        for name, phone in agenda.items():
            print(f"{name.title()}: {phone}")
    else:
        print("The agenda is empty.")

while True:
    print("\n--- Agenda Menu ---")
    print("1. Add/Modify Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List Contacts")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_modify_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        list_contacts()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid option.")
