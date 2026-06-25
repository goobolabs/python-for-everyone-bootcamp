"""
models/staff.py  —  Employee and Roster dataclasses.
"""
from __future__ import annotations
from dataclasses import dataclass, field


ROLES = {"manager", "cashier", "stock_clerk", "supervisor", "intern"}


@dataclass
class Employee:
    id: int
    name: str
    role: str
    salary: float
    phone: str | None = None

    def __str__(self) -> str:
        phone_line = f"\n  Phone    : {self.phone}" if self.phone else ""
        return (
            f"  ID       : {self.id}\n"
            f"  Name     : {self.name}\n"
            f"  Role     : {self.role}\n"
            f"  Salary   : ${self.salary:,.2f}/mo"
            + phone_line
        )


@dataclass
class Roster:
    employees: list[Employee] = field(default_factory=list)
    _next_id: int = 1

    def hire(self, name: str, role: str, salary: float,
             phone: str | None = None) -> Employee:
        e = Employee(id=self._next_id, name=name, role=role,
                     salary=salary, phone=phone)
        self.employees.append(e)
        self._next_id += 1
        return e

    def find_by_id(self, eid: int) -> Employee | None:
        for e in self.employees:
            if e.id == eid:
                return e
        return None

    def find_by_name(self, query: str) -> list[Employee]:
        q = query.lower()
        return [e for e in self.employees if q in e.name.lower()]

    def fire(self, eid: int) -> bool:
        for i, e in enumerate(self.employees):
            if e.id == eid:
                self.employees.pop(i)
                return True
        return False

    def total_payroll(self) -> float:
        return sum(e.salary for e in self.employees)

    def by_role(self, role: str) -> list[Employee]:
        return [e for e in self.employees if e.role == role]

    def sync_ids(self) -> None:
        if self.employees:
            self._next_id = max(e.id for e in self.employees) + 1
