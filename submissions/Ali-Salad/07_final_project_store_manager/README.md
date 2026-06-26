# Store Manager — final project
Name: Alisalad

A professional **Inventory & Staff Management System** CLI built in Python 3.10+.
Covers all concepts from Sections 1–6 of the Python bootcamp: comments, `print`/`input`,
conditions, lists and loops, functions and `main()`, files (UTF-8), `try`/`except` on bad
input, `__str__` on a class, `@dataclass`, and composition.

---

## Run

```bash
cd store_manager
python main.py
```

---

## What's where

| Path | Purpose |
|---|---|
| `main.py` | Main menu + sub-menu functions |
| `models/inventory.py` | `Product` (one item) + `Store` (all items in memory) |
| `models/staff.py` | `Employee` (one person) + `Roster` (all staff in memory) |
| `utils/storage.py` | Load / save `data/products.txt` and `data/staff.txt` |
| `utils/reports.py` | Formatted terminal reports |
| `utils/helpers.py` | Safe `ask()`, `ask_float()`, `ask_int()`, `confirm()` |
| `data/products.txt` | Saved product roster |
| `data/staff.txt` | Saved staff roster |

---

## Menus

### Main
```
[1] Inventory
[2] Staff
[3] Reports
[0] Save & Quit
```

### Inventory
Add, list, search by name, browse by category, update, restock, remove.

### Staff
Hire, list, search by name, browse by role, update, fire.
Valid roles: `manager`, `cashier`, `stock_clerk`, `supervisor`, `intern`

### Reports
- Inventory summary (with low-stock ⚠ flag)
- Low stock alert (configurable threshold, default ≤ 5 units)
- Category breakdown (units + value per category)
- Staff summary (roles + monthly payroll total)

---

## Data files

### `data/products.txt`
UTF-8 text. Lines starting with `#` are comments.
Header row: `id|name|category|price|quantity|supplier`
Supplier is optional (empty string if absent).

### `data/staff.txt`
UTF-8 text. Lines starting with `#` are comments.
Header row: `id|name|role|salary|phone`
Phone is optional (empty string if absent).

---

## Requirements
- Python 3.10+ (uses `str | None` union syntax)
- No third-party libraries — standard library only
