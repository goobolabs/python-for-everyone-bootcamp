# LAWS Water Tracking System

## Final Python OOP Project

**Student Name:** Hassan Bille Hassan

---

## Project Description

LAWS Water Tracking System is a simple Python application used to manage water customers and track their water usage.

The system helps a water company store customer information, calculate water bills, and manage records using a text file.

This project was developed using Object-Oriented Programming (OOP) concepts in Python.

---

## Problem Solved

Managing customer records manually can be difficult and time-consuming.

This system helps to:

- Store customer information
- Track water barrel usage
- Calculate customer payments
- Search customer records
- Update customer information
- Save data permanently

---

## Features

- Add Customer
- View All Customers
- Search Customer
- Update Customer Information
- Remove Customer
- Calculate Water Bills
- Save Data to Text File
- Load Data from Text File
- View Statistics

---

## Customer Information

Each customer has:

- Customer ID
- Name
- Phone Number
- District
- Category
- Barrels Used
- Bill Payment

---

## Bill Calculation

The cost of one water barrel is:

```text
$0.80
```

Formula:

```text
Bill = Barrels × 0.80
```

Example:

```text
30 Barrels × $0.80 = $24.00
```

---

## Customer Categories

The system supports:

- House
- Hotel
- Restaurant

---

## Statistics

The system can display:

- Total Customers
- Total Barrels Used
- Total Income
- Total Houses
- Total Hotels
- Total Restaurants

---

## Project Structure

```text
laws_water_tracking_system/
│
├── data/
│   └── customers.txt
│
├── models/
│   ├── __init__.py
│   └── customers.py
│
├── utils/
│   ├── __init__.py
│   └── storage.py
│
└── main.py
```

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Dataclasses
- File Handling
- Text File Storage

---

## How to Run

1. Open the project folder.
2. Run the main file:

```bash
python main.py
```

3. Use the menu to manage customers.

---

## Conclusion

This project demonstrates the use of Python OOP, file handling, and problem-solving skills to build a simple water customer management system.

---

## Author

**Hassan Bille Hassan**

Final Python OOP Project
