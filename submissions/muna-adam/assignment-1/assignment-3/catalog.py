
# magacaygu waa muna
# assignmentgaan wuxuu ku saabsan yahay banaamij fudud oo kaydinaya soona bandhigayay books



class bookitem:
    title: str
    year: int

    def __str__(self):
        return f"{self.title} ({self.year})"



class books:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if len(self.books) == 0:
            print("buuugaag hada kuma jiraan.")
        else:
            for book in self.books:
                print(book)


# 3. Load books (file ka akhri)
def load_books(filename, library):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                title, year = line.split("|")
                book = bookitem(title, int(year))
                library.add_book(book)

    except FileNotFoundError:
        pass


# 4. Save books (file ku qor)
def save_books(filename, library):
    with open(filename, "w", encoding="utf-8") as file:
        for book in library.books:
            file.write(f"{book.title}|{book.year}\n")


# 5. Main function (menu + logic)
def main():
    library = books()
    file_name = "books.txt"

    load_books(file_name, library)

    while True:
        print("\n--- books ---")
        print("1) add book")
        print("2) list books")
        print("3) save")
        print("4) quit")

        choice = input("dooro ")

        if choice == "1":
            title = input("book title: ")
            year = input("year: ")

            try:
                year = int(year)
                book = bookitem(title, year)
                library.add_book(book)
                print("buugii waa lagu daray!")

            except ValueError:
                print("sanadku waa inuu noqdaa number.")

        elif choice == "2":
            library.list_books()

        elif choice == "3":
            save_books(file_name, library)
            print("buugii wa la kaydiayay!")

        elif choice == "4":
            save_books(file_name, library)
            print("waa la kaydiayay. salaam!")
            break

        else:
            print("number khaldan baad galisay!")