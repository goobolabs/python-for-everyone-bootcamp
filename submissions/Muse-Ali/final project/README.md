# 💊 E-Pharmacy Management System

A terminal-based (Command-Line Interface) E-Pharmacy Management System application. This system is built with **Python** using **Object-Oriented Programming (OOP)**, file handling, functions, loops, and modular programming principles.

---

## 🎯 Project Purpose

The purpose of this project is to help pharmacists and administrators efficiently manage medicine inventories, track sales, and handle prescriptions directly from the terminal. 

While building this project, I successfully practiced and implemented the following core concepts:
* **Classes and Objects (OOP):** Modeling medicines and sales logs.
* **Modular Programming:** Splitting the logic into multiple reusable python files.
* **File Handling:** Persisting inventory and sales data into text files.
* **CRUD Operations:** Implementing Create, Read, Update, and Delete functionalities.
* **Data Structures:** Managing data using lists and dictionaries.
* **Control Flow:** Utilizing loops and conditions for user navigation and data filtering.

---

## ✨ Features

This application provides the following key functionalities:

### 1. ➕ Add Medicine
Users can add new medicines into the system by specifying:
* ID & Name
* Category
* Price
* Stock Quantity
* Expiry Date

### 2. 📋 View Inventory
Displays all currently saved medicines in a clean, human-readable, and well-formatted table.

### 3. 💰 Calculate Total Sales
Tracks, calculates, and displays the total amount of revenue generated from completed sales.

### 4. 🔍 Filter Medicines by Category
Allows users to quickly filter and find medicines based on specific categories such as:
* Antibiotics
* Painkillers
* Syrups
* Vitamins

### 5. ✏️ Edit Medicine Details
Provides the ability to update existing medicine records (such as adjusting stock quantity or modifying the price) using the unique Medicine ID.

### 6. ❌ Delete Medicine
Enables users to completely remove expired, recalled, or discontinued medicines from the inventory system.

### 7. 💾 Save Data to File
Automatically saves medicine and sales data to text files so that no progress or inventory information is lost after closing the application.

### 8. 🔄 Load Data from File
Previously saved data is automatically fetched and loaded back into the system whenever the application starts up.

---

## 📂 Project Structure

Here is how the project files are organized:

```text
e_pharmacy/
│
├── main.py            # The main entry point of the application
├── medicine.py        # Defines the Medicine class (OOP structure)
├── inventory.py       # Contains logic for managing the medicine inventory (CRUD)
├── sales.py           # Handles sales calculations and logs
├── file_handler.py    # Manages saving and loading data from text files
├── utils.py           # Helper functions (validations, clearing terminal, etc.)
│
├── data/
│   ├── inventory.txt       # Flat file database storing medicine records
│   └── sales_history.txt   # Flat file database storing sales logs
│
└── README.md          # Documentation file
## 📊 Example Data Representation

This is a preview of how the pharmacy inventory data is formatted and rendered inside the terminal:

| Id | Name | Category | Price | Quantity | Expiry Date |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Paracetamol | Painkiller | $2.50 | 150 | 2028-12-01 |
| **2** | Amoxicillin | Antibiotic | $12.00 | 80 | 2027-06-15 |
| **3** | CoughSyrup | Syrup | $4.50 | 45 | 2026-11-20 |
| **4** | Ibuprofen | Painkiller | $3.20 | 200 | 2028-02-10 |
