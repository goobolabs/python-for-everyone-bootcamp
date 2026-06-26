"""Customers in memory: the record (Customer) and the group (WaterCompany)."""

from dataclasses import dataclass


@dataclass
class Customer:
    customer_id: str
    name: str
    phone: str
    district: str
    category: str
    barrels: int

    PRICE_PER_BARREL = 0.8

    def calculate_bill(self) -> float:
        return self.barrels * self.PRICE_PER_BARREL

    def __str__(self) -> str:
        return (
            f"{self.customer_id} | "
            f"{self.name} | "
            f"{self.phone} | "
            f"{self.district} | "
            f"{self.category} | "
            f"barrels={self.barrels} | "
            f"bill=${self.calculate_bill():.2f}"
        )


class WaterCompany:

    def __init__(self) -> None:
        self._customers: list[Customer] = []

    def add(self, customer: Customer) -> bool:

        if self.find_by_id(customer.customer_id):
            return False

        self._customers.append(customer)
        return True

    def remove(self, customer_id: str) -> bool:

        cid = customer_id.strip()

        for i, c in enumerate(self._customers):

            if c.customer_id == cid:

                del self._customers[i]
                return True

        return False

    def find_by_id(self, customer_id: str) -> Customer | None:

        cid = customer_id.strip()

        for c in self._customers:

            if c.customer_id == cid:
                return c

        return None

    def search(self, query: str) -> list[Customer]:

        q = query.strip().lower()

        if not q:
            return []

        results = []

        for c in self._customers:

            if (
                q in c.customer_id.lower()
                or q in c.name.lower()
            ):
                results.append(c)

        return results

    def all(self) -> list[Customer]:
        return list(self._customers)

    def update(
        self,
        customer_id: str,
        *,
        name: str | None = None,
        phone: str | None = None,
        district: str | None = None,
        category: str | None = None,
        barrels: int | None = None,
    ) -> bool:

        c = self.find_by_id(customer_id)

        if c is None:
            return False

        if name is not None:
            c.name = name

        if phone is not None:
            c.phone = phone

        if district is not None:
            c.district = district

        if category is not None:
            c.category = category

        if barrels is not None:
            c.barrels = barrels

        return True

    def clear(self) -> None:
        self._customers = []