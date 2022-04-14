import json


class ContactList:
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read

        with open("contacts.json", "r") as f:
            # 2) get the text from the file
            contacts_content = f.read()
            # 3) convert the text into a python dictionary (json.loads)
        contacts_dict = json.loads(contacts_content)
        # 4) get the list of contacts out of the dictionary
        contacts_dict["contacts"]
        # 5) assign the list of dictionaries to self.contacts
        self.contacts = contacts_dict["contacts"]

    def count(self):
        # return the length of self.contacts
        return len(self.contacts)
        ...

    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open("contacts.json", "w") as f:
            # 2) put self.contacts in a dictionary with the key 'contacts'
            saved_contacts_dict = {"contacts": self.contacts}
            # 3) convert the dictionary to a json string (json.dumps)
            # 4) write the json string to the file
            f.write(json.dumps(saved_contacts_dict, indent=2))
        ...

    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        for i in range(len(self.contacts)):
            # print(self.contacts[i])
            print(f"Name: {self.contacts[i]['name']}\n")
            print(f"Email: {self.contacts[i]['email']}\n")
            print(f"Phone #: {self.contacts[i]['phone_number']}\n")
            print("-------------------------\n")
        print(f">>> {ContactList.count(self)} contacts\n")
        ...

    def add(self, name, email, phone_number):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        new_contact_dict = {"name": name, "email": email, "phone_number": phone_number}
        self.contacts.append(new_contact_dict)
        print(f">>> Added {self.contacts[-1]['name']} to contacts")
        ...

    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        for contact in self.contacts:
            if name.lower() == contact["name"].lower():
                self.contacts.remove(contact)
        print(f">>> {contact['name']} has been removed\n")
        ...

    def update(self, old_name, new_name, new_email, new_phone_number):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        # for contact in self.contacts:
        for contact in self.contacts:
            if old_name.lower() == contact["name"].lower():
                self.contacts.remove(contact)
                updated_dict = {"name": new_name, "email": new_email, "phone_number": new_phone_number}
                self.contacts.append(updated_dict)
        print(f">>> {contact['name']} has been updated\n")


contact_list = ContactList()  # create an instance of our class
contact_list.load()
print("Welcome to the Contact List App (CLA)")
while True:
    print("The available commands are: load, save, print, add, remove, update, exit, and help")
    command = input("Enter a command: ")
    if command == "load":
        contact_list.load()
        print(f"Loaded ${contact_list.count()} contacts.")
    elif command == "save":
        contact_list.save()
        print(f"Saved ${contact_list.count()} contacts.")
    elif command == "print":
        contact_list.print()
    elif command == "add":
        print("Enter info of contact to add:")
        name = input("Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        contact_list.add(name, phone_number, email)
    elif command == "remove":
        name = input("Name of contact to remove: ")
        contact_list.remove(name)
    elif command == "update":
        print("Enter info of contact to add:")
        old_name = input("Name of contact to update: ")
        new_name = input("New Name: ")
        new_phone_number = input("New Phone Number: ")
        new_email = input("New Email: ")
        contact_list.update(old_name, new_name, new_phone_number, new_email)
    elif command == "help":
        print("Available commands:")
        print("load   - load all contacts from the file")
        print("save   - save contacts to a file")
        print("print  - print all contacts")
        print("add    - add a new contact")
        print("remove - remove a contact")
        print("update - update a contact")
        print("exit   - exit the program")
    elif command == "exit":
        break
    else:
        print("Command not recognized")
