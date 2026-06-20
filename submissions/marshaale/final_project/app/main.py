from model.system_panel import SystemPanel
from utils.utils import print_message, validate_id_value


def cars_option(system: SystemPanel):
    prefix = "Cars->"
    while True:
        print(f"\n{prefix}")
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ").strip().lower()
        if user_pick == "1":
            print_message(f"----{prefix}Add----")
            car_name = input("Car name: ").strip()
            car_model = input("Car model: ").strip()
            car_year = input("Car year: ").strip()
            car_price_per_day = input("Car price per day: ").strip()
            if not car_name or not car_model or not car_year or not car_price_per_day:
                print_message("All fields are required")
                continue
            system.car_service.add_car(
                name=car_name,
                model=car_model,
                year=car_year,
                price_per_day=float(car_price_per_day),
            )

        if user_pick == "2":
            print_message(f"----{prefix}List----")
            system.car_service.list_cars()

        if user_pick == "3":
            print_message(f"----{prefix}Update----")
            car_id = input("Car id: ").strip()
            if not validate_id_value(car_id, "Car"):
                continue

            print("Hint: Leave blank to skip updating a field")
            car_name = input("Car name: ").strip()
            car_model = input("Car model: ").strip()
            car_year = input("Car year: ").strip()
            car_price_per_day = input("Car price per day: ").strip()

            if system.car_service.update_car(
                car_id=int(car_id),
                name=car_name,
                model=car_model,
                year=car_year,
                price_per_day=(
                    None if not car_price_per_day else float(car_price_per_day)
                ),
                is_rented=False,
            ):
                print_message("Car updated successfully")
            else:
                print_message(f"Car with id: {car_id} does not found")

        if user_pick == "4":
            print_message(f"----{prefix}Remove----")
            car_id = input("Car id to remove: ").strip()

            if not validate_id_value(car_id, "Car"):
                continue

            if system.car_service.remove_car(int(car_id)):
                print_message("Car removed successfully")
            else:
                print_message(f"Car with id: {car_id} does not found")

        if user_pick == "0":
            system.car_service.save_cars()
            print_message()
            break


def customers_option(system: SystemPanel):
    prefix = "Customers->"
    while True:
        print(f"\n{prefix}")
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ")

        if user_pick == "1":
            print_message(f"----{prefix}Add----")
            customer_name = input("Customer name: ")
            customer_phone = input("Customer phone: ")
            customer_identity = input(
                "Customer identity eg (passport,national identity): "
            )

            if not customer_name or not customer_phone or not customer_identity:
                print_message("All fields are required")
                continue

            system.customer_service.add_customer(
                name=customer_name, phone=customer_phone, identity=customer_identity
            )

        if user_pick == "2":
            print_message(f"----{prefix}List----")
            system.customer_service.list_customers()

        if user_pick == "3":
            print_message(f"----{prefix}Update----")
            customer_id = input("Customer id you want to update: ").strip()
            if not validate_id_value(customer_id):
                continue

            print("Hint: Leave blank to skip updating a field")
            customer_name = input("Customer name: ")
            customer_phone = input("Customer phone: ")
            customer_identity = input(
                "Customer identity eg (passport,national identity): "
            )

            if system.customer_service.update_customer(
                customer_id=int(customer_id),
                name=customer_name,
                phone=customer_phone,
                identity=customer_identity,
            ):
                print_message("Customer updated successfully")
            else:
                print_message(f"Customer with id: {customer_id} does not found")

        if user_pick == "4":
            print_message(f"----{prefix}Remove----")
            customer_id = input("Customer id you want to remove: ").strip()

            if not validate_id_value(customer_id):
                continue

            confirmation = (
                input(
                    f"Are you sure you want to remove customer id {customer_id} y/n: "
                )
                .strip()
                .lower()
            )

            if confirmation == "yes" or confirmation == "y":
                if system.customer_service.remove_customer(int(customer_id)):
                    print_message("Customer updated successfully")
                else:
                    print_message(f"Customer with id: {customer_id} does not found")

        if user_pick == "0":
            system.customer_service.save_customers()
            print_message()
            break


def rents_section(system: SystemPanel):
    prefix = "Rents->"
    while True:
        print(f"\n{prefix}")
        print("1 Add 2 List 3 Update 4 Remove 0 Exit")
        user_pick = input("Pick: ")

        if user_pick == "1":
            print_message(f"----{prefix}Add----")
            car_id = input("Car id: ").strip()
            customer_id = input("Customer id: ").strip()
            num_of_days = input("Number of days: ").strip()
            payment_type = (
                input("Payment type (pre payment,post payment): ").strip().lower()
            )

            if (
                not validate_id_value(car_id, "Car")
                or not validate_id_value(customer_id)
                or not num_of_days
                or not payment_type
                or not num_of_days.isnumeric()
            ):
                print("All fields are required")
                continue

            if not payment_type in ["pre payment", "post payment"]:
                payment_type = "pre payment"

            customer = system.customer_service.find_customer(int(customer_id))
            if not customer:
                print(f"Customer with id: {customer_id} not found")
                continue

            car = system.car_service.find_car(int(car_id))

            if not car:
                print(f"Car with id: {car_id} not found")
                continue

            if car.is_rented:
                print(f"Car with id: {customer_id} is already rented")
                continue

            if system.car_rent_service.add_car_rent(
                car_id=car.id,
                customer_id=customer.id,
                base_price=car.price_per_day,
                num_of_days=int(num_of_days),
                payment_type=payment_type,
            ):
                system.car_service.update_car(car_id=car.id, is_rented=True)
                print("\nSuccessfully registered")
            else:
                print("\nFailed to register")

        if user_pick == "2":
            print_message(f"----{prefix}List----")
            system.car_rent_service.list_rent_cars(
                system.car_service, system.customer_service
            )

        if user_pick == "3":
            print_message(f"----{prefix}Update----")
            # Rent validation
            rent_id = input("Rent id: ").strip()
            if not validate_id_value(rent_id, "Rent"):
                continue

            rent_car = system.car_rent_service.find_rent_car(int(rent_id))

            if not rent_car:
                print(f"Rent record with id: {rent_id} not found")
                continue

            # Input fields
            print("Hint: Leave blank to skip updating a field")
            car_id = input("Car id: ").strip()
            customer_id = input("Customer id: ").strip()
            num_of_days = input("Number of days: ").strip()
            payment_type = (
                input("Payment type (pre payment,post payment): ").strip().lower()
            )
            status = (
                input("Status Keep empty unless canceled or return_due_to_issue: ")
                .strip()
                .lower()
            )

            # Status validation
            if status and not status in [
                "canceled",
                "return_due_to_issue",
                "completed",
            ]:
                print(
                    "Status must be either ['canceled','return_due_to_issue','completed']"
                )
                continue

            # Id validation
            if (
                car_id
                and not validate_id_value(car_id, "Car")
                or customer_id
                and not validate_id_value(customer_id)
            ):
                continue

            print("Car id", car_id, "Customer id", customer_id)

            print("Here after validate_id_value")

            # payment type correction
            if payment_type and not payment_type in ["pre payment", "post payment"]:
                payment_type = "pre payment"

            # num_of_days validation
            if num_of_days and not num_of_days.isnumeric():
                print("Number of days must be numeric")
                continue

            # conditional find customer based on customer_id
            customer = (
                system.customer_service.find_customer(int(customer_id))
                if customer_id
                else None
            )

            # check
            if customer_id and not customer:
                print(f"Customer with id: {customer_id} not found")
                continue

            # conditional find car based car_id
            car = system.car_service.find_car(int(car_id)) if car_id else None

            # check
            if car_id and not car:
                print(f"Car with id: {car_id} not found")
                continue

            # check if selected car is a new car and if is already rented.
            if car and car.id != rent_car.car_id and car.is_rented:
                print(f"Car with id: {car_id} is already rented")
                continue

            print("Here starts updating..")

            print("Status", status)

            # update old car availability
            if car and car.id != rent_car.car_id:
                old_car = rent_car.car_id
                system.car_service.update_car(car_id=old_car, is_rented=False)
            
            if system.car_rent_service.update_rent_car(
                customer_car_rent_id=int(rent_id),
                car_id=int(car_id) if car_id else None,
                customer_id=int(customer_id) if customer_id else None,
                num_of_days=int(num_of_days) if num_of_days else None,
                base_price=float(car.price_per_day) if car else None,
                payment_type=payment_type,
                status=status,
            ):
                is_rented = False if status in ["canceled"] else True
                print("Here update car")
                print("Is canceled", is_rented)
                print(False if is_rented else True)

                car_id_pram = int(car_id) if car_id else rent_car.car_id

                if system.car_service.update_car(
                    car_id=car_id_pram,
                    is_rented=is_rented,
                ):
                    print("Updated successfully")
                    system.car_rent_service.save_rent_cars()
                    system.car_service.save_cars()
                else:
                    print(
                        f"Failed to update car: update manually car with id: {car_id_pram} "
                    )

            else:
                print("Failed to update rent car")
        
        if user_pick == "4":
            print_message(f"----{prefix}Remove----")
            # Rent validation
            rent_id = input("Rent id: ").strip()
            if not validate_id_value(rent_id, "Rent"):
                continue

            rent_car = system.car_rent_service.find_rent_car(int(rent_id))

            if not rent_car:
                print(f"Rent record with id: {rent_id} not found")
                continue

            if system.car_service.update_car(car_id=rent_car.car_id,is_rented=False):
                if system.car_rent_service.remove_rent_car(customer_car_rent_id=rent_car.id):
                    print("Successfully remove")
                    system.car_service.save_cars()
                    system.car_rent_service.save_rent_cars()

        if user_pick == "0":
            system.car_rent_service.save_rent_cars()
            print_message()
            break


def main():
    system = SystemPanel()
    while True:
        try:
            print("1: Cars 2: Customers 3: Rents 4: Report 101: Save 0: Exit")
            user_pick = input("Pick: ").strip().lower()
            if user_pick == "1":
                cars_option(system)

            if user_pick == "2":
                customers_option(system)

            if user_pick == "3":
                rents_section(system)

            if user_pick == "4":
                print("----Reports----")
                print(system.reports())

            if user_pick == "101":
                system.save_state()

            if user_pick == "0":
                print_message("Good bye")
                break

        except Exception as e:
            print("System exception: ", str(e))
        finally:
            system.save_state()
            pass


if __name__ == "__main__":
    main()
