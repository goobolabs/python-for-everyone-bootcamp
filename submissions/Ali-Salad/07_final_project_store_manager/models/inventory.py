"""
models/inventory.py  —  Product and Store dataclasses.
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    quantity: int
    supplier: str | None = None

    def __str__(self) -> str:
        supplier_info = f"  Supplier : {self.supplier}" if self.supplier else ""
        return (
            f"  ID       : {self.id}\n"
            f"  Name     : {self.name}\n"
            f"  Category : {self.category}\n"
            f"  Price    : ${self.price:.2f}\n"
            f"  Qty      : {self.quantity}"
            + (f"\n{supplier_info}" if supplier_info else "")
        )

    def total_value(self) -> float:
        return self.price * self.quantity

    def is_low_stock(self, threshold: int = 5) -> bool:
        return self.quantity <= threshold


@dataclass
class Store:
    products: list[Product] = field(default_factory=list)
    _next_id: int = 1

    def add_product(self, name: str, category: str, price: float,
                    quantity: int, supplier: str | None = None) -> Product:
        p = Product(
            id=self._next_id,
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            supplier=supplier,
        )
        self.products.append(p)
        self._next_id += 1
        return p

    def find_by_id(self, pid: int) -> Product | None:
        for p in self.products:
            if p.id == pid:
                return p
        return None

    def find_by_name(self, query: str) -> list[Product]:
        q = query.lower()
        return [p for p in self.products if q in p.name.lower()]

    def find_by_category(self, category: str) -> list[Product]:
        c = category.lower()
        return [p for p in self.products if c in p.category.lower()]

    def remove_product(self, pid: int) -> bool:
        for i, p in enumerate(self.products):
            if p.id == pid:
                self.products.pop(i)
                return True
        return False

    def restock(self, pid: int, amount: int) -> bool:
        p = self.find_by_id(pid)
        if p:
            p.quantity += amount
            return True
        return False

    def low_stock_report(self, threshold: int = 5) -> list[Product]:
        return [p for p in self.products if p.is_low_stock(threshold)]

    def inventory_value(self) -> float:
        return sum(p.total_value() for p in self.products)

    def categories(self) -> list[str]:
        return sorted(set(p.category for p in self.products))

    def sync_ids(self) -> None:
        if self.products:
            self._next_id = max(p.id for p in self.products) + 1
