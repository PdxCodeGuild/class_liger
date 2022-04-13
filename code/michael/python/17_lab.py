# contact list lab

import json

class ContactList:
    
    def __init__(self):
        self.contacts = []

    def load(self):
        # 1) open 'contacts.json' with option 'r' for read
        # 2) get the text from the file
        # 3) convert the text into a python dictionary (json.loads)
        # 4) get the list of contacts out of the dictionary
        # 5) assign the list of dictionaries to self.contacts
        with open('contacts.json', 'r') as cont_json:
            cont = cont_json.read()
            cont = json.loads(cont)
            for i in range(len(cont['contacts'])):
                if cont['contacts'][i] not in self.contacts:
                    self.contacts.append(cont['contacts'][i])
                # print(cont['contacts'][i])
            # print(cont)
            # print(type(cont))

    
    def count(self):
        # return the length of self.contacts
        cont_count = len(self.contacts)
        return cont_count
    
    def save(self):
        # 1) open 'contacts.json' with open 'w' for write
        # 2) put self.contacts in a dictionary with the key 'contacts'
        # 3) convert the dictionary to a json string (json.dumps)
        # 4) write the json string to the file
        new_dict = {'contacts': self.contacts}
        new_json = json.dumps(new_dict)
        with open('contacts.json', 'w') as cont_json:
            cont_json.write(new_json)
        


    def print(self):
        # loop over self.contacts
        # print the information for each contact on a separate line
        for i in range(len(self.contacts)):
            print(self.contacts[i])

    def add(self, name, phone_number, email):
        # create a new dictionary using the 3 parameters
        # add the new dictionary to self.contacts
        new_dict = {'name': name, 'phone_number': phone_number, 'email': email}
        self.contacts.append(new_dict)
    
    def remove(self, name):
        # find the contact in self-contacts with the given name
        # remove the element at that index
        in_list = False
        for i in range(len(self.contacts)):
            if name == self.contacts[i]['name']:
                print(f'{name} and all associated info has been removed from the contact list.\nInfo removed:')
                print(self.contacts.pop(i))
                in_list = True
                break
        if in_list != True:
            print(f'{name} not found in contact list and couldn\'t be removed')
    
    def update(self, old_name, new_name, new_phone_number, new_email):
        # find the contact in self.contacts with the given old_name
        # set that contacts' name, phone number, etc to the given values
        in_list = False
        for i in range(len(self.contacts)):
            if old_name == self.contacts[i]['name']:
                self.contacts[i]['name'] = new_name
                self.contacts[i]['phone_number'] = new_phone_number
                self.contacts[i]['email'] = new_email
                print(f'{old_name} and all associated info has been updated.\nInfo updated to:')
                print(self.contacts[i])
                in_list = True
        if in_list != True:
            print(f'{old_name} not found in contact list and couldn\'t be updated')

    
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
        print('print  - print all contacts')
        print('add    - add a new contact')
        print('remove - remove a contact')
        print('update - update a contact')
        print('exit   - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')