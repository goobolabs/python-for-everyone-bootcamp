# Project Name:  Expense Tracker

A command-line(CL) Expense Tracker application :  built with Python using Object-Oriented Programming (OOP), file handling, functions, loops, and modular programming principles.

## Project Purpose

The purpose of this project is to help users manage and track their daily expenses directly from the terminal. Users can 
* Add 
* view 
* edit
* delete 
* filter 
* save expenses.

During building this project , I manage to practice these concepts:

* Classes and Objects (OOP)
* Functions
* Lists
* Loops and Conditions
* File Handling
* Modular Programming
* CRUD Operations

---

# Features: 

this project has the following features

##  1. Add Expenses

Users can add new expenses with:
* Title
* Amount
* Category
* Date
---

## 2. View Expenses

Displays all saved expenses in a clean formatted table.

---

##  3. Calculate Total Expenses

Calculates and displays the total amount spent.

---

## 4. Filter Expenses by Category

Users can filter expenses by categories such as:
* Food
* Transport
* Bills
* Shopping
  

---

## 5. Edit Expenses

 Users can update existing expenses by ID.

---

## 6. Delete Expenses

Users can remove expenses from the tracker.

---

## 7. Save Expenses to File

Expenses are saved to a text file so data is not lost after closing the application.

---

##  8. Load Expenses from File

Previously saved expenses are automatically loaded when the application starts.

---

---

# Project Structure

---

```text
expense_tracker/
│
├── expense.py
├── main.py
├── add.py
├── calculations.py
├── edit_expense.py
├── file_handling.py
├── filter.py
├── data/ expenses.txt
└── README.md
```

## Example: How our expense data  will look like .

```text
Id   Title           Amount     Category     Date        
--------------------------------------------------------
1    sugar           $66.00     food           2026-05-22
2    wheat           $212.00    food           2026-05-22
3    oil             $15.00     liquid         2026-05-22
4    chocolate       $12.20     sweets         2026-05-22

------------------- YOUR TOTAL SPENDING------------------
Total spending: $305.20

```
