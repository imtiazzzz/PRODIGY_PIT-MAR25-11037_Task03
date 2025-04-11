import json

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

    def edit_contact(self, index, name, phone_number, email):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            print("Contact edited successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact index.")

    def save_to_file(self, filename):
        data = []
        for contact in self.contacts:
            data.append({
                "name": contact.name,
                "phone_number": contact.phone_number,
                "email": contact.email
            })

        with open(filename, 'w') as file:
            json.dump(data, file)
            print("Contacts saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.contacts = []
                for contact_data in data:
                    self.contacts.append(Contact(
                        contact_data["name"],
                        contact_data["phone_number"],
                        contact_data["email"]
                    ))
            print("Contacts loaded from file.")
        except FileNotFoundError:
            print("No saved contacts found.")

def main():
    contact_manager = ContactManager()

    while True:
        print("\nSimple Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Load Contacts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact_manager.add_contact(name, phone_number, email)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact you want to edit: "))
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.edit_contact(index, name, phone_number, email)
        elif choice == "4":
            contact_manager.view_contacts()
            index = int(input("Enter the index of the contact you want to delete: "))
            contact_manager.delete_contact(index)
        elif choice == "5":
            filename = input("Enter filename to save contacts: ")
            contact_manager.save_to_file(filename)
        elif choice == "6":
            filename = input("Enter filename to load contacts from: ")
            contact_manager.load_from_file(filename)
        elif choice == "7":
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()