from contact import Contact
class Contact_List:
    def __init__(self):
        self.contacts = []
    def add_contact(self, name, telephone, email):
        new_contact = Contact(name, telephone, email)
        self.contacts.append(new_contact)
    def display(self):
        if not self.contacts:
            print('No contacts available.')
        else:
            for contact in self.contacts:
                print(contact)