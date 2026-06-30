# Library Management System (CLI)

A small command-line Library Management System built with Python 3.10+.

This project demonstrates the core concepts covered in Sections 1–6 of the Python Bootcamp, including:

* Comments
* `print()` and `input()`
* Conditional statements (`if`, `elif`, `else`)
* Lists and loops
* Functions and `main()`
* File handling (UTF-8)
* Error handling with `try` / `except`
* Object-Oriented Programming (OOP)
* `@dataclass`
* `__str__()` methods
* Composition

---

## Run the Project

```bash
cd 07_final_project_library_management_system
python main.py
```

---

## Project Structure

```text
07_final_project_library_management_system/
│
├── main.py
│
├── models/
│   └── books.py
│
├── utils/
│   └── storage.py
│
├── data/
│   └── books.txt
│
└── README.md
```

---

## Features

The system allows a librarian to:

1. Add a new book
2. View all books
3. Remove a book
4. Search for a book by ID
5. Update book information
6. Save library data
7. Quit the application (automatically saves data)

---

## Book Information

Each book contains:

* Book ID
* Title
* Author
* Year Published

Example:

```text
ID: 101
Title: Python Basics
Author: Abdullahi hassan
Year: 2026
```

---

## Data Storage

All library data is stored in:

```text
data/books.txt
```

The file uses UTF-8 encoding and a simple pipe-separated format.

Example:

```text
# Library Database
id|title|author|year
101|Python Basics|Abdullahi|2026
```

### Notes

* Lines beginning with `#` are treated as comments.
* The header row is ignored when loading data.
* Data is automatically loaded when the application starts.
* Data is automatically saved when the application exits.

---

## Error Handling

The project uses `try` / `except` blocks to prevent crashes caused by invalid user input.

Examples:

* Entering text instead of a numeric ID
* Entering an invalid publication year
* Loading a missing data file

---

## OOP Concepts Used

### Book Class

Represents a single book in the library.

Responsibilities:

* Store book information
* Display formatted book details using `__str__()`

### Library Class

Represents the entire library collection.

Responsibilities:

* Store books in memory
* Add books
* Remove books
* Search books
* Manage library records

This demonstrates **composition**, where a `Library` object contains multiple `Book` objects.

---

## Technologies

* Python 3.10+
* Dataclasses
* File Handling
* UTF-8 Text Storage
* Command-Line Interface (CLI)

---

## Learning Objectives

After completing this project, students should be able to:

* Build a complete CLI application
* Organize code into modules
* Work with classes and objects
* Read and write files
* Handle user input safely
* Apply Python best practices
* Create maintainable project structures

---

## Author

Abdullahi Hassan Shire

Python Bootcamp Final Project
Library Management System
