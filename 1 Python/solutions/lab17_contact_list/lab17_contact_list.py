import json

# CRUD
# Create
# Retrieve
# Update
# Delete
class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        with open('contacts.json', 'r') as contacts_file:
            # 2) get the text from the file
            contents = contacts_file.read()
            # 3) convert the text into a python dictionary (json.loads)
            contents = json.loads(contents)
            # 4) get the list of contacts out of the dictionary
            contacts = contents['contacts']
            # 5) assign the list of dictionaries to self.contacts
            self.contacts = contacts

    @property
    def count(self):
        # return the length of self.contacts
        return len(self.contacts) # A list's length is available at O(1) speed
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        with open('contacts.json', 'w') as contacts_file:
            # 2) put self.contacts in a dictionary with the key 'contacts'
            contacts_dict = {
                'contacts': self.contacts
            }
            # 3) convert the dictionary to a json string (json.dumps)
            contents = json.dumps(contacts_dict, indent=2)
            # 4) write the json string to the file
            contacts_file.write(contents)

    def print(self, contact=None):
        # if a contact is specified, print just that contact
        if contact:
            display = (
                f"Name: {contact['name']}\n"
                f"Phone: {contact['phone_number']}\n"
                f"Email: {contact['email']}\n"
            )
            print(display)
        else:
            # otherwise, loop over self.contacts and print each
            for contact in self.contacts:
                # print the information for each contact on a separate line
                display = (
                    f"Name: {contact['name']}\n"
                    f"Phone: {contact['phone_number']}\n"
                    f"Email: {contact['email']}\n"
                )

                print(display)

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        self.contacts.append({
            'name': name,
            'phone_number': phone_number,
            'email': email
        })

    def find(self, name):
        # find the contact with a given name
        for contact in self.contacts:
            if contact['name'] == name:
                return contact

        print('Not found!')

    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == name:
                return self.contacts.pop(index)
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        for index in range(self.count):
            contact = self.contacts[index]
            if contact['name'] == old_name:
                self.contacts[index] = {
                    'name': new_name,
                    'phone_number': new_phone_number,
                    'email': new_email
                }

    
contact_list = ContactList() # create an instance of our class
contact_list.load()



print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded {contact_list.count} contacts.')

    elif command == 'save':
        contact_list.save()
        print(f'Saved {contact_list.count} contacts.')

    elif command == 'print':
        contact_list.print()

    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)

    elif command == 'find':
        print('Enter the name of the contact you want to find:')
        name = input('Name: ')
        contact = contact_list.find(name) # returns a dict or None

        if contact:
            contact_list.print(contact)

    elif command == 'remove':
        name = input('Name of contact to remove: ')
        removed = contact_list.remove(name)
        print(f"Removed: {removed['name']}")

    elif command == 'update':
        print('Enter info of contact to add:')
        old_name = input('Name of contact to update: ')
        new_name = input('New Name: ')
        new_phone_number = input('New Phone Number: ')
        new_email = input('New Email: ')
        contact_list.update(old_name, new_name, new_phone_number, new_email)

    elif command == 'help':
        print('Available commands:')
        print('load   - load all contacts from the file')
        print('save   - save contacts to a file')
        print('print  - print all contacts')
        print('find   - find a contact')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')

    elif command == 'exit':
        break

    else:
        print('Command not recognized')