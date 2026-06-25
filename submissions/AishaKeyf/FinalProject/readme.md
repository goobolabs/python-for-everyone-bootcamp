# Land Management System

A CLI-based Land Management System built with Python for managing land records, ownership, transfers, and registry administration.

This project simulates a real-world land registry system with authentication, ownership transfer tracking, validation, and reporting.

---

## Features

### Authentication & Security
- Admin login system
- Password hashing using SHA-256
- Change password functionality
- Protected admin operations

---

### Owner Management
- Register owners
- View all owners
- Prevent duplicate owner IDs

---

### Land Management
- Register land
- View all lands
- Search land by Plot ID
- Update land information
- Delete land records
- Prevent duplicate plot IDs

---

### Ownership Transfer
- Transfer ownership
- Transfer reason tracking
- Transfer history records
- Ownership validation

---

### Audit & Tracking
- Timestamps for:
  - Land creation
  - Land updates
  - Ownership transfers

- Land status tracking:
  - Owned
  - Transferred

---

### Reports
Generate system reports including:
- Total registered lands
- Total ownership transfers
- Lands grouped by location

---

## Project Structure

```bash
land_management/
│
├── main.py
│
├── database/
│   ├── admin.json
│   ├── owners.json
│   ├── lands.json
│   └── transfers.json
│
└── services/
    ├── auth.py
    ├── owner.py
    └── land.py
```

---

## Technologies Used

- Python 3
- JSON file storage
- hashlib
- datetime

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/land-management-system.git
cd land-management-system
```

---

## Run Project

```bash
python main.py
```

---

## Default Admin Login

```txt
Username: admin
Password: 1212
```

---

## Example Menu

```txt
===== LAND MANAGEMENT SYSTEM =====

1. Admin Login
2. Guest Access
3. Exit
```

---

## Admin Capabilities

Admin can:

- Register owners
- Register lands
- Update lands
- Delete lands
- Transfer ownership
- View reports
- Change password

---

## Guest Capabilities

Guest can:

- View owners
- View lands
- Search land
- View transfer history

---

## Sample Transfer Record

```json
{
  "plot_id": "PLT001",
  "from_owner": "OWN001",
  "to_owner": "OWN002",
  "reason": "Sale",
  "transferred_at": "2026-05-25 21:34:00"
}
```

---

## Learning Outcomes

This project helped practice:

- Python functions
- Modular programming
- File handling
- JSON persistence
- Authentication systems
- Password hashing
- CRUD operations
- Data validation
- Audit tracking

---

## Future Improvements

- SQLite database integration
- Dispute management
- Export reports
- Web-based dashboard
- Role-based access control
- FastAPI backend
- React frontend

---

## Author 
Built by [AishaKeyf]([https://github.com/AishaKeyf](https://github.com/AishaKeyf))

## The project link 
https://github.com/AishaKeyf/land-management-system-

Built as a Python CLI project for learning software engineering fundamentals.