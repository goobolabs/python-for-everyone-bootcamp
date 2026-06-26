"""
utils/reports.py  —  Print formatted reports to the terminal.
"""
from __future__ import annotations
from models.inventory import Store
from models.staff import Roster

_SEP = "─" * 54


def _header(title: str) -> None:
    print(f"\n{_SEP}")
    print(f"  {title.upper()}")
    print(_SEP)


def inventory_summary(store: Store) -> None:
    _header("inventory summary")
    if not store.products:
        print("  No products on file.")
        return
    print(f"  {'ID':<5} {'Name':<22} {'Category':<14} {'Qty':>5} {'Price':>8}")
    print("  " + "·" * 52)
    for p in store.products:
        flag = " ⚠ LOW" if p.is_low_stock() else ""
        print(f"  {p.id:<5} {p.name:<22} {p.category:<14} "
              f"{p.quantity:>5} ${p.price:>7.2f}{flag}")
    print("  " + "·" * 52)
    print(f"  Total products  : {len(store.products)}")
    print(f"  Inventory value : ${store.inventory_value():,.2f}")
    print(f"  Categories      : {', '.join(store.categories()) or 'none'}")


def low_stock_report(store: Store, threshold: int = 5) -> None:
    _header(f"low stock report (≤ {threshold} units)")
    items = store.low_stock_report(threshold)
    if not items:
        print("  All products are sufficiently stocked.")
        return
    for p in items:
        print(f"  [{p.id}] {p.name}  —  {p.quantity} left")


def staff_summary(roster: Roster) -> None:
    _header("staff summary")
    if not roster.employees:
        print("  No employees on file.")
        return
    print(f"  {'ID':<5} {'Name':<22} {'Role':<14} {'Salary':>10}")
    print("  " + "·" * 52)
    for e in roster.employees:
        print(f"  {e.id:<5} {e.name:<22} {e.role:<14} ${e.salary:>9,.2f}")
    print("  " + "·" * 52)
    print(f"  Total staff   : {len(roster.employees)}")
    print(f"  Monthly payroll: ${roster.total_payroll():,.2f}")


def category_breakdown(store: Store) -> None:
    _header("category breakdown")
    if not store.products:
        print("  No products on file.")
        return
    cats: dict[str, tuple[int, float]] = {}
    for p in store.products:
        qty, val = cats.get(p.category, (0, 0.0))
        cats[p.category] = (qty + p.quantity, val + p.total_value())
    print(f"  {'Category':<20} {'Items':>6} {'Value':>12}")
    print("  " + "·" * 40)
    for cat, (qty, val) in sorted(cats.items()):
        print(f"  {cat:<20} {qty:>6} ${val:>11,.2f}")
