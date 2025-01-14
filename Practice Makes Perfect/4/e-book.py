from ebook_class import Ebook

def main():
    ebook = Ebook("The Odyssey", "Homer", 442)

    print('Initial status:')
    ebook.show_status()

    print('Opening the book:')
    ebook.open_book()
    ebook.show_status()

    print('Reading a few pages:')
    ebook.next_page()
    ebook.next_page()
    ebook.next_page()
    ebook.show_status()

    print('Closing the book:')
    ebook.close_book()
    ebook.show_status()

    print('Trying to read a few pages:')
    ebook.next_page()
    ebook.previous_page()
    ebook.show_status()

if __name__ == "__main__":
    main()


