# PhoneBook Application
def display_menu():
    print("\nPhonebook Application")
    print("1. Add a New Contact")
    print("2. Search for a Contact")
    print("3. Delete a Contact")
    print("4. List All Contacts")
    print("5. Exit")

def add_contact(phonebook):
    name = input("Enter contact name: ").strip()
    if name in phonebook:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ").strip()
        phonebook[name] = phone
        print("Contact added successfully!")

def search_contact(phonebook):
    name = input("Enter contact name to search: ").strip()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found!")

def delete_contact(phonebook):
    name = input("Enter contact name to delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_contacts(phonebook):
    if phonebook:
        print("\nContacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty!")

def main():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            delete_contact(phonebook)
        elif choice == '4':
            list_contacts(phonebook)
        elif choice == '5':
            print("Exiting the Phonebook Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
