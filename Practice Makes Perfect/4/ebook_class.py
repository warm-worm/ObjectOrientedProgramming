class Ebook:
    def __init__(self, title, author, pages_number):
        self.title = title
        self.author = author
        self.pages_number = pages_number
        self.current_page = 1
        self.is_open = False
    def open_book(self):
        if not self.is_open:
            self.is_open = True #open the book
            print(f'Book "{self.title}" is now open.')
        else:
            print('The book is already open.')
    def close_book(self):
        if self.is_open:
            self.is_open = False
            print('The book has been closed.')
        else:
            print("The book is already closed.")
    def next_page(self):
        if self.is_open:
            if self.current_page < self.pages_number:
                self.current_page += 1
                print(f'Moved to page {self.current_page}')
            else:
                print('There is no next page.')
        else:
            print('Open the book first.')
    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f'Moved to page {self.current_page}')
            else:
                print('There is no previous page.')
        else:
            print('Open the book first.')
    def show_status(self):
        if self.is_open:
            print(f'The book "{self.title}" is open. You are on page {self.current_page} out of {self.pages_number}.')
        else:
            print(f'The book "{self.title}" is closed.')