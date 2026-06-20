from pathlib import Path
from models.books import Library


FILE_NAME = "data/books.txt"


# Save books
def save_books(books: list[Library]) -> None:

    with open(FILE_NAME, "w", encoding="utf-8") as file:

        for book in books:

            line = (
                f"{book.book_id},"
                f"{book.book_name},"
                f"{book.author_name}\n"
            )

            file.write(line)


# Load books
def load_books() -> list[Library]:

    books: list[Library] = []

    try:

        with open(FILE_NAME, "r", encoding="utf-8") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) != 3:
                    continue

                book_id, book_name, author_name = data

                book = Library(
                    book_id=book_id,
                    book_name=book_name,
                    author_name=author_name
                )

                books.append(book)

    except FileNotFoundError:
        pass

    return books