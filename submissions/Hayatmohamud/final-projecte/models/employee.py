from dataclasses import dataclass, field


# Employee class-kan wuxuu matalayaa hal shaqaale oo company-ga ka tirsan
@dataclass
class Employee:
    employee_id: int          # Aqoonsiga shaqaalaha
    name: str                 # Magaca shaqaalaha
    position: str             # Jagada shaqaalaha
    department: str           # Waaxda uu ka shaqeeyo
    salary: float             # Mushaharka shaqaalaha

    # Method-kan wuxuu soo celinayaa xogta shaqaalaha si qurux badan
    def __str__(self) -> str:
        return (
            f"{self.employee_id} | {self.name} | "
            f"{self.position} | {self.department} | Salary=${self.salary}"
        )


# HumanResource class-kan wuxuu maamulayaa dhammaan shaqaalaha
class HumanResource:
    def __init__(self):
        # List-kan waxaa lagu kaydinayaa shaqaalaha oo dhan
        self.employees: list[Employee] = []

    # Method-kan wuxuu ku darayaa shaqaale cusub
    # Haddii employee ID hore u jiray, wuxuu celinayaa False
    def add_employee(self, employee: Employee) -> bool:
        if self.get_employee(str(employee.employee_id)) is not None:
            return False

        self.employees.append(employee)
        return True

    # Method-kan wuxuu tirtirayaa shaqaale iyadoo la isticmaalayo employee ID
    def remove_employee(self, employee_id: int) -> bool:
        for i, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                del self.employees[i]
                return True

        return False

    # Method-kan wuxuu raadinayaa shaqaale gaar ah iyadoo la adeegsanayo ID
    def get_employee(self, employee_id: str) -> Employee | None:
        eid = employee_id.strip()

        for emp in self.employees:
            if str(emp.employee_id) == eid:
                return emp

        return None

    # Method-kan wuxuu raadinayaa shaqaale adigoo isticmaalaya magac, ID, department ama position
    def search_employees(self, q: str) -> list[Employee]:
        q = q.strip().lower()

        if not q:
            return []

        results: list[Employee] = []

        for emp in self.employees:
            if (
                q in emp.name.lower()
                or q in str(emp.employee_id)
                or q in emp.position.lower()
                or q in emp.department.lower()
            ):
                results.append(emp)

        return results

    # Method-kan wuxuu soo bandhigayaa dhammaan shaqaalaha
    def list_employees(self) -> list[Employee]:
        return list(self.employees)

    # Method-kan wuxuu update-gareynayaa xogta shaqaalaha
    def update_employee(
        self,
        employee_id: int,
        name: str | None = None,
        position: str | None = None,
        department: str | None = None,
        salary: float | None = None
    ) -> bool:
        employee = self.get_employee(str(employee_id))

        if employee is None:
            return False

        if name is not None:
            employee.name = name.strip()

        if position is not None:
            employee.position = position.strip()

        if department is not None:
            employee.department = department.strip()

        if salary is not None:
            employee.salary = salary

        return True