# Thin entry: menu
# Domain in models/customers.py;
# disk format in utils/storage.py.

from models.customers import (
    Customer,
    WaterCompany,
)

from utils.storage import (
    DATA_PATH,
    load_company,
    save_company,
)


def menu_add(company: WaterCompany):

    cid = input("Customer id: ").strip()
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    district = input("District: ").strip()
    category = input("Category (house/hotel/restaurant): ").strip()

    try:
        barrels = int(input("Barrels: "))

    except ValueError:
        print("Barrels must be a number.")
        return

    customer = Customer(
        cid,
        name,
        phone,
        district,
        category,
        barrels,
    )

    if company.add(customer):
        print("Customer added.")
    else:
        print("Customer id already exists.")


def print_customers(
    rows: list[Customer]
):

    if not rows:
        print("No customers found.")
        return

    for c in rows:
        print(c)


def menu_list(
    company: WaterCompany
):

    print_customers(
        company.all()
    )


def menu_remove(
    company: WaterCompany
):

    cid = input(
        "Customer id to remove: "
    ).strip()

    if company.remove(cid):
        print("Removed.")
    else:
        print("Customer not found.")


def menu_search(
    company: WaterCompany
):

    q = input(
        "Search by id or name: "
    ).strip()

    print_customers(
        company.search(q)
    )


def menu_update(
    company: WaterCompany
):

    cid = input(
        "Customer id: "
    ).strip()

    if company.find_by_id(cid) is None:
        print("Customer not found.")
        return

    name = input(
        "New name (Enter to keep): "
    ).strip()

    phone = input(
        "New phone (Enter to keep): "
    ).strip()

    district = input(
        "New district (Enter to keep): "
    ).strip()

    category = input(
        "New category (Enter to keep): "
    ).strip()

    raw = input(
        "New barrels (Enter to keep): "
    ).strip()

    barrels = None

    if raw:

        try:
            barrels = int(raw)

        except ValueError:
            print("Invalid barrels value.")
            return

    company.update(
        cid,
        name=name or None,
        phone=phone or None,
        district=district or None,
        category=category or None,
        barrels=barrels,
    )

    print("Updated.")


def menu_statistics(
    company: WaterCompany
):

    customers = company.all()

    total_customers = len(customers)

    total_barrels = 0
    total_income = 0

    houses = 0
    hotels = 0
    restaurants = 0

    for c in customers:

        total_barrels += c.barrels

        total_income += c.calculate_bill()

        if c.category.lower() == "house":
            houses += 1

        elif c.category.lower() == "hotel":
            hotels += 1

        elif c.category.lower() == "restaurant":
            restaurants += 1

    print()
    print("=== LAWS WATER SYSTEM STATISTICS ===")
    print(f"Total Customers : {total_customers}")
    print(f"Total Barrels   : {total_barrels}")
    print(f"Total Income    : ${total_income:.2f}")
    print(f"Houses          : {houses}")
    print(f"Hotels          : {hotels}")
    print(f"Restaurants     : {restaurants}")


def print_menu():

    print()
    print("=== LAWS WATER TRACKING SYSTEM ===")
    print("1) Add customer")
    print("2) List customers")
    print("3) Remove customer")
    print("4) Search customer")
    print("5) Update customer")
    print("6) Statistics")
    print("7) Save")
    print("0) Quit")


def main():

    company = WaterCompany()

    load_company(
        DATA_PATH,
        company,
    )

    try:

        while True:

            print_menu()

            choice = input(
                "Choice: "
            ).strip()

            if choice == "1":
                menu_add(company)

            elif choice == "2":
                menu_list(company)

            elif choice == "3":
                menu_remove(company)

            elif choice == "4":
                menu_search(company)

            elif choice == "5":
                menu_update(company)

            elif choice == "6":
                menu_statistics(company)

            elif choice == "7":

                save_company(
                    DATA_PATH,
                    company,
                )

                print("Data saved.")

            elif choice == "0":
                print("Bye!")
                break

            else:
                print("Pick 0-7.")

    finally:

        try:

            save_company(
                DATA_PATH,
                company,
            )

            print("Data saved.")

        except OSError as e:

            print(
                "Could not save:",
                e,
            )


if __name__ == "__main__":
    main()