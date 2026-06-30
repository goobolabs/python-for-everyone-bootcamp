from models.employee import Employee
from utils.store import load_employees, save_employees


# Function-kan wuxuu soo bandhigayaa menu-ga system-ka
def show_menu():
    print("\n===== Human Resource Management System =====")
    print("1. Add Employee")
    print("2. List Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Remove Employee")
    print("6. Save and Exit")


# Function-kan wuxuu bilaabayaa program-ka HR Management System
def main():
    # Halkan waxaa laga load-gareynayaa xogtii hore ee employees.txt
    hr = load_employees()

    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        # 1. Ku dar shaqaale cusub
        if choice == "1":
            employee_id = int(input("Enter employee ID: "))
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))

            employee = Employee(employee_id, name, position, department, salary)

            if hr.add_employee(employee):
                print("Employee added successfully.")
            else:
                print("Employee ID already exists.")

        # 2. Soo bandhig dhammaan shaqaalaha
        elif choice == "2":
            employees = hr.list_employees()

            if not employees:
                print("No employees found.")
            else:
                for employee in employees:
                    print(employee)

        # 3. Raadi shaqaale
        elif choice == "3":
            q = input("Enter name, ID, position, or department to search: ")
            results = hr.search_employees(q)

            if not results:
                print("No matching employees found.")
            else:
                for employee in results:
                    print(employee)

        # 4. Update garee xogta shaqaalaha
        elif choice == "4":
            employee_id = int(input("Enter employee ID to update: "))

            name = input("Enter new name, or leave empty: ").strip()
            position = input("Enter new position, or leave empty: ").strip()
            department = input("Enter new department, or leave empty: ").strip()
            salary_text = input("Enter new salary, or leave empty: ").strip()

            salary = None
            if salary_text:
                salary = float(salary_text)

            updated = hr.update_employee(
                employee_id,
                name=name if name else None,
                position=position if position else None,
                department=department if department else None,
                salary=salary
            )

            if updated:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")

        # 5. Tirtir shaqaale
        elif choice == "5":
            employee_id = int(input("Enter employee ID to remove: "))

            if hr.remove_employee(employee_id):
                print("Employee removed successfully.")
            else:
                print("Employee not found.")

        # 6. Save garee kadibna ka bax
        elif choice == "6":
            save_employees(hr)
            print("Employees saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


# Haddii file-kan si toos ah loo run-gareeyo, main() ayuu bilaabayaa
if __name__ == "__main__":
    main()