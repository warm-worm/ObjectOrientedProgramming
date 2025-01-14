from contact import Contact
from contact_list import Contact_List

def main ():
    contact_list = Contact_List()

    contact_list.add_contact("John Brown", "555234000", "brown@onet.pl")
    contact_list.add_contact("Anna May", "232000199", "am@o2.pl")
    contact_list.add_contact("George Small", "222999100", "smallg@google.pl")
    contact_list.add_contact("Paola Big", "100200300", "bigpaola@poczta.pl")

    contact_list.display()

if __name__ == "__main__":
    main()

