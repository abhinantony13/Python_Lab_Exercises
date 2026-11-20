# Contact book using lists and dictionaries
contacts = []

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    contacts.append({"name": name, "phone": phone})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact():
    name = input("Enter name to search: ").strip().lower()
    found = [c for c in contacts if name in c["name"].lower()]
    if found:
        for contact in found:
            print(contact["name"], "-", contact["phone"])
    else:
        print("Contact not found.")

while True:
    print("\\n1. Add  2. View  3. Search  4. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
