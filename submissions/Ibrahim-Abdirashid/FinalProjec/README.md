# 🔐 Secure Password Generator & Saver
> **Bootcamp Final Project:** Python for Everyone (15-Day Intensive)

This is a complete, lightweight Python application that allows users to either automatically generate strong, secure passwords or manually save their own custom passwords. All credentials are safely logged into an external text file (`passwords.txt`). This project serves as a graduation milestone demonstrating core Python programming proficiencies.

---

## 🚀 Key Features

* **Randomized Generation (Auto):** Blends uppercase/lowercase letters, digits, and special characters (`@#$%`) to create unhackable passwords.
* **Manual Input (Custom):** Allows users to manually type and save their own existing passwords for safe keeping.
* **Data Persistence:** Automatically appends new passwords to `passwords.txt` without overwriting previous data.
* **Robust Error Handling:** The program gracefully catches inputs like text strings when a number is expected, preventing sudden crashes.
* **Interactive CLI Menu:** A clean, terminal-based text interface that is user-friendly and intuitive.

---

## 🛠️ Python Core Concepts Applied

This project synthesizes the core building blocks learned throughout the 15-day bootcamp:
1. **Standard Modules:** Utilizes `random` (for unpredictable selection) and `string` (for pre-built character datasets).
2. **Control Flow:** Employs an infinite `while True` loop for the menu system and `if/elif/else` blocks for conditional logic.
3. **Modular Programming:** Separates duties into clean, independent functions (`generate_password`, `save_password`, and `view_passwords`).
4. **File Handling:** Implements context managers (`with open`) using the `"a"` (append) mode for writing and `"r"` (read) mode for displaying logs.
5. **Exception Handling:** Uses `try/except` blocks to handle `ValueError` and `FileNotFoundError` safely.

---

## 📈 Future Roadmap (Upcoming Enhancements)

To take this project further, the following features are planned for future development:
* **🔒 Password Encryption:** Encrypt the `passwords.txt` file using the `cryptography` module so that saved passwords cannot be read as plain text.
* **🖥️ Graphical User Interface (GUI):** Transition from a terminal-based interface to a visual desktop application using `Tkinter`.
* **🔍 Search & Edit Functionality:** Add features to search for a specific account's password or delete/update outdated credentials.
* **📋 Copy to Clipboard:** Integrate a feature to automatically copy the generated password to the system clipboard for immediate use.

---

## 📂 Project Structure

```text
FINAL PROJECT OF PYTHON/
│
├── main.py            # Main application script containing the executable logic
├── passwords.txt      # Automated text file where credentials are securely logged
└── README.md          # Comprehensive project documentation (This file)
```

---

## Installation

```
git clone https://github.com/Ibrahim-Abdirashid/Password-generator
cd Password-generator
```
---

## 💻 How to Run and Use
```
python main.py
```

---

## 📝 Sample Program Output

```

========================================
  WELCOME TO SECURE PASSWORD GENERATOR  
========================================

--- MENU ---
1) Dhalis Kedis ah (Auto Generate)
2) Gacanta ku qoro Password aad leedahay (Custom Password)
3) Arag Password-ada kaydsan
4) Xir barnaamijka

Choose an option (1, 2, 3, or 4): 2
Enter Account Name: Facebook
Enter Custom Password: MySuperSecret123!

[Success] Your custom password has been safely logged for Facebook.

```

---
## Author
Built by Ibrahim Abdirashid

## The project link
```
https://github.com/Ibrahim-Abdirashid/Password-generator
```






