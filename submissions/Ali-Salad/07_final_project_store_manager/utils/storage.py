"""
utils/storage.py  —  Read / write products.txt and staff.txt (UTF-8 pipe-delimited).

Products format:
  # comment lines ignored
  id|name|category|price|quantity|supplier
  1|USB Cable|Electronics|4.99|30|TechSupply Co.

Staff format:
  # comment lines ignored
  id|name|role|salary|phone
  1|Ali Salad|manager|850.00|+252612345678
"""
from __future__ import annotations
from pathlib import Path
from models.inventory import Product, Store
from models.staff import Employee, Roster

PRODUCTS_FILE = Path("data/products.txt")
STAFF_FILE = Path("data/staff.txt")


# ── Products ──────────────────────────────────────────────────────────────────

def load_products(store: Store) -> None:
    if not PRODUCTS_FILE.exists():
        return
    store.products.clear()
    with PRODUCTS_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("id|"):
                continue
            parts = line.split("|")
            if len(parts) < 5:
                continue
            try:
                store.products.append(Product(
                    id=int(parts[0]),
                    name=parts[1],
                    category=parts[2],
                    price=float(parts[3]),
                    quantity=int(parts[4]),
                    supplier=parts[5] if len(parts) > 5 and parts[5] else None,
                ))
            except ValueError:
                pass
    store.sync_ids()


def save_products(store: Store) -> None:
    PRODUCTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with PRODUCTS_FILE.open("w", encoding="utf-8") as f:
        f.write("# Store Manager — products data\n")
        f.write("id|name|category|price|quantity|supplier\n")
        for p in store.products:
            f.write(f"{p.id}|{p.name}|{p.category}|{p.price}|"
                    f"{p.quantity}|{p.supplier or ''}\n")


# ── Staff ─────────────────────────────────────────────────────────────────────

def load_staff(roster: Roster) -> None:
    if not STAFF_FILE.exists():
        return
    roster.employees.clear()
    with STAFF_FILE.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("id|"):
                continue
            parts = line.split("|")
            if len(parts) < 4:
                continue
            try:
                roster.employees.append(Employee(
                    id=int(parts[0]),
                    name=parts[1],
                    role=parts[2],
                    salary=float(parts[3]),
                    phone=parts[4] if len(parts) > 4 and parts[4] else None,
                ))
            except ValueError:
                pass
    roster.sync_ids()


def save_staff(roster: Roster) -> None:
    STAFF_FILE.parent.mkdir(parents=True, exist_ok=True)
    with STAFF_FILE.open("w", encoding="utf-8") as f:
        f.write("# Store Manager — staff data\n")
        f.write("id|name|role|salary|phone\n")
        for e in roster.employees:
            f.write(f"{e.id}|{e.name}|{e.role}|{e.salary}|"
                    f"{e.phone or ''}\n")
