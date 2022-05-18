import json





class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        j = open('contacts.json', 'r')                                   # 1) open 'contacts.json' with option 'r' for read
        contacts = json.load(j)                                     # 2) get the text from the file
        for i in contacts['contacts']:
            self.contacts.append(i)                                 # 3) convert the text into a python dictionary (json.loads)
    

    def count(self):
        return len(self.contacts)                                       # return the length of self.contacts
    

    def save(self):
        i = open('contacts.json', 'w')
        new_contacts = {'contacts': self.contacts}
        i.write(json.dumps(new_contacts))                                       # 1) open 'contacts.json' with open 'w' for write
                                                                    # 2) put self.contacts in a dictionary with the key 'contacts'
                                                                    # 3) convert the dictionary to a json string (json.dumps)
                                                                    # 4) write the json string to the file
        

    def print(self):
        for i in self.contacts:                                         # loop over self.contacts
            print(f"\n{i}\n")                                           # print the information for each contact on a separate line
    

    def add(self, name, phone_number, email):
        new_dict = {'name': name, 'phone_number': phone_number, 'email': email}                          # create a new dictionary using the 3 parameters
        self.contacts.append(new_dict)                                                               # add the new dictionary to self.contacts
        ...

    def remove(self, name):
        for i in self.contacts:
            if i['name'].lower() == name.lower():                                                                # find the contact in self-contacts with the given name
                self.contacts.remove(i)                                                    # remove the element at that index
        

    def update(self, old_name, new_name, new_phone_number, new_email):
        for i in self.contacts:                                                   # find the contact in self.contacts with the given old_name
            if old_name.lower() == i['name'].lower():
                self.contacts = self.contacts.replace(old_name,new_name)                                                           # set that contacts' name, phone number, etc to the given values
        ...

contact_list = ContactList() # create an instance of our class
contact_list.load()
print('Welcome to the Contact List App (CLA)')
while True:
    command = input('Enter a command: ')
    if command == 'load':
        contact_list.load()
        print(f'Loaded ${contact_list.count()} contacts.')
    elif command == 'save':
        contact_list.save()
        print(f'Saved ${contact_list.count()} contacts.')
    elif command == 'print':
        contact_list.print()
    elif command == 'add':
        print('Enter info of contact to add:')
        name = input('Name: ')
        phone_number = input('Phone Number: ')
        email = input('Email: ')
        contact_list.add(name, phone_number, email)
    elif command == 'remove':
        name = input('Name of contact to remove: ')
        contact_list.remove(name)
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
        print('print_2  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')