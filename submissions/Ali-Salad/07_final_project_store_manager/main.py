"""
main.py  —  Store Manager CLI
=============================
A professional inventory and staff management system.
Covers Python concepts from Sections 1–6:
    comments, print/input, conditions, loops, functions,
    main(), files (UTF-8), try/except, __str__, @dataclass, composition.

Python 3.10+  (uses X | Y union type hints)

Run:
    cd store_manager
    python main.py
"""
from __future__ import annotations
import sys
from models.inventory import Store
from models.staff import Roster, ROLES
from utils.storage import load_products, save_products, load_staff, save_staff
from utils.reports import (
    inventory_summary, low_stock_report,
    staff_summary, category_breakdown,
)
from utils.helpers import ask, ask_float, ask_int, confirm

_BANNER = r"""
  ╔══════════════════════════════════════════╗
  ║        STORE MANAGER  v1.0               ║
  ║   Inventory & Staff Management System    ║
  ╚══════════════════════════════════════════╝
"""

_MAIN_MENU = """
  [1] Inventory
  [2] Staff
  [3] Reports
  [0] Save & Quit
"""

_INV_MENU = """
  ── Inventory ──────────────────────
  [1] Add product
  [2] List all products
  [3] Search by name
  [4] Browse by category
  [5] Update product
  [6] Restock product
  [7] Remove product
  [0] Back
"""

_STAFF_MENU = """
  ── Staff ───────────────────────────
  [1] Hire employee
  [2] List all staff
  [3] Search by name
  [4] Browse by role
  [5] Update employee
  [6] Fire employee
  [0] Back
"""

_REPORTS_MENU = """
  ── Reports ─────────────────────────
  [1] Inventory summary
  [2] Low stock alert
  [3] Category breakdown
  [4] Staff summary
  [0] Back
"""


# ── Inventory sub-menu ─────────────────────────────────────────────────────

def menu_inventory(store: Store) -> None:
    while True:
        print(_INV_MENU)
        choice = input("  > ").strip()

        if choice == "1":
            print("\n  ── Add product ──")
            name = ask("  Name     : ")
            category = ask("  Category : ")
            price = ask_float("  Price $  : ", min_val=0.01)
            quantity = ask_int("  Qty      : ", min_val=0)
            supplier = ask("  Supplier (optional, press Enter to skip): ", required=False) or None
            p = store.add_product(name, category, price, quantity, supplier)
            print(f"\n  ✓ Added [{p.id}] {p.name}")

        elif choice == "2":
            inventory_summary(store)

        elif choice == "3":
            query = ask("  Name query: ")
            results = store.find_by_name(query)
            if not results:
                print("  No products found.")
            else:
                for p in results:
                    print(f"\n{p}")

        elif choice == "4":
            cats = store.categories()
            if not cats:
                print("  No categories yet.")
                continue
            print("  Categories:", ", ".join(cats))
            cat = ask("  Category: ")
            results = store.find_by_category(cat)
            if not results:
                print("  No products in that category.")
            else:
                for p in results:
                    print(f"\n{p}")

        elif choice == "5":
            pid = ask_int("  Product ID: ", min_val=1)
            p = store.find_by_id(pid)
            if not p:
                print("  ✗  Product not found.")
                continue
            print(f"\n{p}\n")
            new_name = ask(f"  New name [{p.name}] (Enter to keep): ", required=False)
            new_cat = ask(f"  New category [{p.category}] (Enter to keep): ", required=False)
            new_price_raw = input(f"  New price [${p.price:.2f}] (Enter to keep): ").strip()
            new_qty_raw = input(f"  New qty [{p.quantity}] (Enter to keep): ").strip()
            new_supplier = input(f"  New supplier [{p.supplier or 'none'}] (Enter to keep, 'none' to clear): ").strip()

            if new_name:
                p.name = new_name
            if new_cat:
                p.category = new_cat
            if new_price_raw:
                try:
                    p.price = float(new_price_raw)
                except ValueError:
                    print("  ✗  Invalid price — skipped.")
            if new_qty_raw:
                try:
                    p.quantity = int(new_qty_raw)
                except ValueError:
                    print("  ✗  Invalid quantity — skipped.")
            if new_supplier.lower() == "none":
                p.supplier = None
            elif new_supplier:
                p.supplier = new_supplier
            print("  ✓ Product updated.")

        elif choice == "6":
            pid = ask_int("  Product ID: ", min_val=1)
            amount = ask_int("  Add how many units: ", min_val=1)
            if store.restock(pid, amount):
                p = store.find_by_id(pid)
                print(f"  ✓ {p.name} now has {p.quantity} units.")  # type: ignore[union-attr]
            else:
                print("  ✗  Product not found.")

        elif choice == "7":
            pid = ask_int("  Product ID: ", min_val=1)
            p = store.find_by_id(pid)
            if not p:
                print("  ✗  Product not found.")
                continue
            print(f"\n{p}\n")
            if confirm("  Remove this product? (y/n): "):
                store.remove_product(pid)
                print("  ✓ Product removed.")
            else:
                print("  Cancelled.")

        elif choice == "0":
            break
        else:
            print("  ✗  Invalid option.")


# ── Staff sub-menu ─────────────────────────────────────────────────────────

def menu_staff(roster: Roster) -> None:
    while True:
        print(_STAFF_MENU)
        choice = input("  > ").strip()

        if choice == "1":
            print("\n  ── Hire employee ──")
            name = ask("  Name   : ")
            print(f"  Roles  : {', '.join(sorted(ROLES))}")
            role = ask("  Role   : ").lower()
            if role not in ROLES:
                print(f"  ✗  '{role}' is not a valid role. Please choose from the list.")
                continue
            salary = ask_float("  Salary (monthly $): ", min_val=0)
            phone = ask("  Phone (optional, Enter to skip): ", required=False) or None
            e = roster.hire(name, role, salary, phone)
            print(f"\n  ✓ Hired [{e.id}] {e.name} as {e.role}")

        elif choice == "2":
            staff_summary(roster)

        elif choice == "3":
            query = ask("  Name query: ")
            results = roster.find_by_name(query)
            if not results:
                print("  No employees found.")
            else:
                for e in results:
                    print(f"\n{e}")

        elif choice == "4":
            print(f"  Roles: {', '.join(sorted(ROLES))}")
            role = ask("  Role: ").lower()
            results = roster.by_role(role)
            if not results:
                print("  No employees with that role.")
            else:
                for e in results:
                    print(f"\n{e}")

        elif choice == "5":
            eid = ask_int("  Employee ID: ", min_val=1)
            e = roster.find_by_id(eid)
            if not e:
                print("  ✗  Employee not found.")
                continue
            print(f"\n{e}\n")
            new_name = ask(f"  New name [{e.name}] (Enter to keep): ", required=False)
            print(f"  Roles: {', '.join(sorted(ROLES))}")
            new_role = ask(f"  New role [{e.role}] (Enter to keep): ", required=False).lower()
            new_salary_raw = input(f"  New salary [${e.salary:,.2f}] (Enter to keep): ").strip()
            new_phone = input(f"  New phone [{e.phone or 'none'}] (Enter to keep, 'none' to clear): ").strip()

            if new_name:
                e.name = new_name
            if new_role:
                if new_role not in ROLES:
                    print(f"  ✗  '{new_role}' is not valid — role unchanged.")
                else:
                    e.role = new_role
            if new_salary_raw:
                try:
                    e.salary = float(new_salary_raw)
                except ValueError:
                    print("  ✗  Invalid salary — skipped.")
            if new_phone.lower() == "none":
                e.phone = None
            elif new_phone:
                e.phone = new_phone
            print("  ✓ Employee updated.")

        elif choice == "6":
            eid = ask_int("  Employee ID: ", min_val=1)
            e = roster.find_by_id(eid)
            if not e:
                print("  ✗  Employee not found.")
                continue
            print(f"\n{e}\n")
            if confirm("  Remove this employee? (y/n): "):
                roster.fire(eid)
                print("  ✓ Employee removed.")
            else:
                print("  Cancelled.")

        elif choice == "0":
            break
        else:
            print("  ✗  Invalid option.")


# ── Reports sub-menu ───────────────────────────────────────────────────────

def menu_reports(store: Store, roster: Roster) -> None:
    while True:
        print(_REPORTS_MENU)
        choice = input("  > ").strip()

        if choice == "1":
            inventory_summary(store)
        elif choice == "2":
            threshold = ask_int("  Low-stock threshold (default 5): ", min_val=1) if \
                input("  Custom threshold? (y/n): ").strip().lower() == "y" else 5
            low_stock_report(store, threshold)
        elif choice == "3":
            category_breakdown(store)
        elif choice == "4":
            staff_summary(roster)
        elif choice == "0":
            break
        else:
            print("  ✗  Invalid option.")


# ── Entry point ────────────────────────────────────────────────────────────

def main() -> None:
    store = Store()
    roster = Roster()

    print(_BANNER)
    print("  Loading data...")
    try:
        load_products(store)
        load_staff(roster)
        print(f"  ✓ {len(store.products)} product(s) and "
              f"{len(roster.employees)} employee(s) loaded.\n")
    except Exception as e:
        print(f"  ⚠  Could not load data: {e}")

    while True:
        print(_MAIN_MENU)
        choice = input("  > ").strip()

        if choice == "1":
            menu_inventory(store)
        elif choice == "2":
            menu_staff(roster)
        elif choice == "3":
            menu_reports(store, roster)
        elif choice == "0":
            print("\n  Saving data...", end=" ")
            try:
                save_products(store)
                save_staff(roster)
                print("✓")
            except Exception as e:
                print(f"\n  ✗  Save failed: {e}")
            print("  Goodbye!\n")
            sys.exit(0)
        else:
            print("  ✗  Choose 0–3.")


if __name__ == "__main__":
    main()
