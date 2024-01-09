import json
contact = []  #dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    contact[name] = number
    print(f"added {name} with number {number} to contacts.")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        print(f"{name}'s number is {contact[name]}.")
    else:
        print(f"{name} is not in contact.")

def display_contacts():
    if contact:
        print("contacts:")
        for name, number in contact.items():
            print(f"{name}: {number}")
    else:
        print("no contacts available")
1
def delete_contact():
    name = input("Enter contact name to delete:")
    if name in contact:
        del contact[name]
        print(f"{name} has been deleted from contacts.")
    else:
        print(f"{name} is not in contacts.")
# user interaction loop
while True:
    print("\n***contact book menu***")
    print("1. Add contacts")
    print("2. search contacts")
    print("3. display contacts")
    print("4. delete contacts")
    print("5. exit")

    choice =input("enter your choice (1-5): ")

    if choice == '1':
     add_contact()
    elif choice == '2':
     search_contact()
    elif choice == '3':
     display_contacts()
    elif choice == '4':
     delete_contact()
    elif choice == '5':
     print("existing contact book, Goodbye!")
     break
    else:
     print("Invalid choice, please enter a number between 1 and 5.")