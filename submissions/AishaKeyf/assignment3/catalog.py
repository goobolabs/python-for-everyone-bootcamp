# A simple book catalog application from aisha keyf, assignment 3

class Book:
    def __init__(self,title ,author,year):
        self.title = title
        self.author = author
        self.year = year
    def __str__(self):
        return f" [{self.year}] {self.title} by {self.author}"
    

class Catalog:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    title, author, year = line.strip().split(",")
                    book = Book(title, author, year)
                    self.add_book(book)
        except FileNotFoundError:
            pass

    def list_books(self):
        if not self.books:
            print("No books in the catalog.")
        else:
            print("📚 Books in the catalog:")
            print("---------------------")

            for index, book in enumerate(self.books, start=1):
                print(f"{index}. {book}")


    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.year}\n")            
    


def main():
    catalog = Catalog()
    catalog.load_from_file("catalog.txt")

    name=input(" inter your name: ")
    print(f"welcome, {name}")

    while True:
        print("\n 1) Add book 2) List books 3) Quit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = input("Year: ")
            book = Book(title, author, year)
            catalog.add_book(book)
        
        elif choice == "2":
            catalog.list_books()
        
        elif choice == "3":
            catalog.save_to_file("catalog.txt")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please pick 1, 2 or 3")


if __name__ == "__main__":
    main()