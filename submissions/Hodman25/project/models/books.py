from dataclasses import dataclass


@dataclass
class Library:
    book_id: str
    book_name: str
    author_name: str

    def __str__(self):
        return f"{self.book_id} | {self.book_name} | {self.author_name}"


class Book:
    def __init__(self) -> None:
        self._books: list[Library] = []

    # Add book
    def add_book(self, book: Library) -> bool:
        if self.find_by_id(book.book_id) is not None:
            return False

        self._books.append(book)
        return True

    # Remove book
    def remove_book(self, book_id: str) -> bool:
        bid = book_id.strip()

        for i, b in enumerate(self._books):
            if b.book_id == bid:
                del self._books[i]
                return True

        return False

    # Find by ID
    def find_by_id(self, book_id: str) -> Library | None:
        bid = book_id.strip()

        for b in self._books:
            if b.book_id == bid:
                return b

        return None

    # Search book
    def search_book(self, query: str) -> list[Library]:
        q = query.strip().lower()

        if not q:
            return []

        output: list[Library] = []

        for s in self._books:
            if q in s.book_id.lower() or q in s.book_name.lower():
                output.append(s)

        return output

    # List all books
    def all_books(self) -> list[Library]:
        return list(self._books)

    # Update book
    def update_books(
        self,
        book_id: str,
        *,
        book_name: str | None = None,
        author_name: str | None = None
    ) -> bool:

        s = self.find_by_id(book_id)

        if s is None:
            return False

        if book_name is not None:
            s.book_name = book_name

        if author_name is not None:
            s.author_name = author_name

        return True

    # Clear all books
    def clear(self) -> None:
        self._books = []

