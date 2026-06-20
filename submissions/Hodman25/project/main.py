from models.books import Library, Book
from utilities.storage import save_books, load_books


def show_menu() -> None:

    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Save Books")
    print("7. Exit")


def main():

    books = Book()

    # Load books from file
    loaded_books = load_books()

    for book in loaded_books:
        books.add_book(book)

    while True:

        show_menu()

        choice = input("Choose option: ").strip()

        # Add Book
        if choice == "1":

            book_id = input("Enter book ID: ").strip()
            book_name = input("Enter title: ").strip()
            author_name = input("Enter author: ").strip()

            book = Library(
                book_id,
                book_name,
                author_name
            )

            if books.add_book(book):
                print("Book added successfully")

            else:
                print("Book ID already exists")

        # List Books
        elif choice == "2":

            all_books = books.all_books()

            if not all_books:
                print("No books found")

            else:
                print("\nAll Books")

                for book in all_books:
                    print(book)

        # Search Book
        elif choice == "3":

            query = input("Search: ").strip()

            results = books.search_book(query)

            if not results:
                print("No matching books found")

            else:
                print("\nSearch Results")

                for book in results:
                    print(book)

        # Update Book
        elif choice == "4":

            book_id = input("Enter book ID: ").strip()

            book_name = input("New title: ").strip()
            author_name = input("New author: ").strip()

            updated = books.update_books(
                book_id,
                book_name=book_name,
                author_name=author_name
            )

            if updated:
                print("Book updated successfully")

            else:
                print("Book not found")

        # Delete Book
        elif choice == "5":

            book_id = input("Enter book ID: ").strip()

            if books.remove_book(book_id):
                print("Book deleted successfully")

            else:
                print("Book not found")

        # Save Books
        elif choice == "6":

            save_books(books.all_books())

            print("Books saved successfully")

        # Exit
        elif choice == "7":

            save_books(books.all_books())

            print("Goodbye")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()