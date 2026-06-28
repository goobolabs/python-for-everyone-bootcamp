# 🎓 Online Course Management System CLI

## 📌 Project Description

Online Course Management System CLI is a command-line based application developed using Python.  
The system helps manage students, teachers, courses, enrollments, and grades efficiently.

This project uses:
* Python 3
* JSON file storage
* Object-Oriented Programming (OOP)
* Role-Based Authentication System

---

# 🚀 Features

## 👨‍💼 Admin
* Manage students (CRUD)
* Manage teachers (CRUD)
* Manage courses (CRUD)
* Manage enrollments
* Manage grades
* Register and manage users

## 👨‍🏫 Teacher
* View students
* View courses
* Add and manage grades

## 👨‍🎓 Student
* View enrolled courses
* View grades

---

# 🔐 Authentication System

* Login system
* Register system
* Role-based access control (RBAC)

### Roles:
* Admin → Full system access
* Teacher → Manage grades + view data
* Student → View only

---

# 👤 User Management (Admin Only)

Admin can:
* Register users
* View users
* Update users
* Delete users

---

# 📚 Modules Included

* Student Management
* Teacher Management
* Course Management
* Enrollment Management
* Grade Management
* Authentication System
* User Management System

---

# 🧠 Grade System

The grading system supports:

* Numeric grades (0–100)
* Automatic letter grade conversion

Example:

* 90–100 → A+
* 80–89 → A
* 70–79 → B
* 60–69 → C
* 50–59 → D
* Below 50 → F

---

# 🗂️ Project Structure

```bash
project/
│
├── main.py
├── auth.py
├── dashboards.py
│
├── services/
│   ├── student_service.py
│   ├── teacher_service.py
│   ├── course_service.py
│   ├── grade_service.py
│   ├── user_service.py
│
├── utils/
│   ├── helpers.py
│   ├── storage.py
│
├── data/
│   └── data.json
│
└── README.md
```

---

# ⚙️ Technologies Used

* Python 3
* JSON
* OOP Concepts
* CLI Interface

---
## 🔗Link Github for Project
[Online-Course-Management-System-CLI](https://github.com/Eng-saacid/Online-Course-Management-System-CLI)

----

# ▶️ How to Run

## 1. Clone Repository

```bash
git clone <repository-link>
```

## 2. Open Project Folder

```bash
cd project-folder
```

## 3. Run Application

```bash
python main.py
```

---

# 📦 Data Storage

The project stores all data inside:

```bash
data.json
```

Data includes:

* Users
* Students
* Teachers
* Courses
* Enrollments
* Grades

---

# 🛡️ System Validation

The system prevents:

* Duplicate users
* Duplicate enrollments
* Duplicate grades
* Invalid grade values (0–100 only)

---

# 🎯 Learning Objectives

This project demonstrates:

* Python OOP
* File Handling
* CRUD Operations
* Authentication System
* Role-Based Access Control (RBAC)
* Data Validation
* CLI Application Development

---

# 👨‍💻 Author

Developed by: Eng-Saacid Abdiaziz yusuf

---

# 📄 License

This project is for educational purposes.
