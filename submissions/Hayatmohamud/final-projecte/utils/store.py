from pathlib import Path
from models.employee import HumanResource, Employee


# File-ka xogta shaqaalaha lagu kaydinayo
DATA_FILE = Path("data/employees.txt")


# Function-kan wuxuu akhriyaa shaqaalaha ku jira employees.txt
def load_employees() -> HumanResource:
    hr = HumanResource()

    # Haddii file-ku aanu jirin, samee folder-ka data iyo file-ka employees.txt
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.touch()
        return hr

    # Akhri file-ka employees.txt
    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Haddii line-ku madhan yahay, ka bood
            if not line:
                continue

            # Data-ga waxaa loo kala jarayaa calaamada |
            # Tusaale: 1|Ayoub|Manager|HR|500
            parts = line.split("|")

            employee_id = int(parts[0])
            name = parts[1]
            position = parts[2]
            department = parts[3]
            salary = float(parts[4])

            employee = Employee(employee_id, name, position, department, salary)
            hr.add_employee(employee)

    return hr


# Function-kan wuxuu shaqaalaha ku kaydiyaa employees.txt
def save_employees(hr: HumanResource) -> None:
    # Hubi in folder-ka data uu jiro
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Ku qor xogta shaqaalaha file-ka employees.txt
    with DATA_FILE.open("w", encoding="utf-8") as file:
        for employee in hr.list_employees():
            file.write(
                f"{employee.employee_id}|"
                f"{employee.name}|"
                f"{employee.position}|"
                f"{employee.department}|"
                f"{employee.salary}\n"
            )