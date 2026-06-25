# Mahdi iltireh
# Simple personal book catalog using classes, files, and menu system.

from dataclasses import dataclass



@dataclass
class Book:
    title: str
    year: int


class Catalog:
    def __init__(self):
        self.items = []

    def add_book(self, book):
        self.items.append(book)

    def show_books(self):
        if len(self.items) == 0:
            print('No books jaale .')
        else:
            for book in self.items:
                print(book.title, '-', book.year)


def load_books(file_name, catalog):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split("|")

                title = data[0]
                year = int(data[1])

                book = Book(title, year)

                catalog.add_book(book)

    except FileNotFoundError:
        print('File lama helin. Catalog cusub ayaa bilaabanaya.')


def save_books(file_name, catalog):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in catalog.items:
            file.write(book.title + "|" + str(book.year) + '\n')


def main():
    catalog = Catalog()

    load_books('books.txt', catalog)

    while True:
        print('\nBook Catalog')
        print('1. Add Book')
        print('2. Show Book')
        print('3. Save ')
        print('4. Quit ')

        choice = input('Enter choice: ')

        if choice == '1':
            title = input('Enter  title: ')
            year = int(input('Enter  year: '))

            new_book = Book(title, year)

            catalog.add_book(new_book)

            print('Book added.')

        elif choice == '2':
            catalog.show_books()

        elif choice == '3':
            save_books('books.txt', catalog)

            print('Books Saved .')

        elif choice == '4':
            save_books('books_list.txt', catalog)

            print('Goodbye Jaale !')
            break
        else:
            print('Wrong Choice........')


if __name__ == "__main__":
 main()
