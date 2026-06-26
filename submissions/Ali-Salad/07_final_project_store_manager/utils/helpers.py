"""
utils/helpers.py  —  Safe input helpers shared across menus.
"""
from __future__ import annotations


def ask(prompt: str, *, required: bool = True) -> str:
    while True:
        val = input(prompt).strip()
        if val or not required:
            return val
        print("  ✗  This field cannot be empty.")


def ask_float(prompt: str, *, min_val: float = 0.0) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
            if val < min_val:
                print(f"  ✗  Must be ≥ {min_val}.")
                continue
            return val
        except ValueError:
            print("  ✗  Enter a valid number (e.g. 9.99).")


def ask_int(prompt: str, *, min_val: int = 0) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if val < min_val:
                print(f"  ✗  Must be ≥ {min_val}.")
                continue
            return val
        except ValueError:
            print("  ✗  Enter a whole number.")


def confirm(prompt: str = "Are you sure? (y/n): ") -> bool:
    return input(prompt).strip().lower() in {"y", "yes"}
