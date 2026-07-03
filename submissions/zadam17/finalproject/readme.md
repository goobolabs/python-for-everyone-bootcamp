# Smart Inventory Management System

A Python command-line inventory application built using Object-Oriented Programming (OOP). The project allows users to manage store or warehouse stock, add new products, view current inventory records, update stock quantities, and delete items from a file.

📌 Features

* Add new products (ID, Name, Price, Quantity)
* View all saved inventory records
* Update existing product quantities
* Delete product records
* Prevent duplicate product IDs
* Error handling for invalid numeric input
* File-based data storage (JSON format for reliability)

🛠 Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* File Handling
* Exception Handling

📂 Project Structure

inventory-management-system/
│
├── main.py
│
├── models/
│   └── product.py
│
├── utils/
│   └── storage.py
│
├── data/
│   └── inventory.txt
│
└── README.md

▶️ How to Run

Clone the repository:
git clone https://github.com/zadam17/inventory-management-system.git

Navigate to the project directory:
cd inventory-management-system

Run the application:
python main.py

📋 Menu Options

1. Add New Product
2. View All Products
3. Update Product Quantity
4. Delete Product
5. Exit

⚠️ Error Handling

The application handles:
* Invalid numeric input (e.g., text instead of price)
* Duplicate product IDs
* Missing inventory file (creates it automatically)
* Invalid menu selections

🎯 Learning Objectives

This project demonstrates:
* Classes and Objects
* Modular Programming
* Functions
* Loops and Conditions
* File Operations
* Exception Handling
* CRUD (Create, Read, Update, Delete) Operations

🔮 Future Improvements

* Add timestamps to records
* GUI version using Tkinter
* Export history to CSV for Excel reporting
* Unit testing

👤 Author

https://github.com/zadam17/Inventory-Management-System