from model.customer_car_rent import CustomerCarRent
from core.config import CUSTOMER_CAR_RENTS_FILE_PATH
from utils.utils import is_header_line
from services.customer_service import CustomerService
from services.car_service import CarService


class CustomerCarRentService:
    def __init__(self) -> None:
        self.rent_cars: list[CustomerCarRent] = []
        self.file_header = (
            "id,car_id,customer_id,base_price,num_of_days,payment_type,status"
        )
        self.encoding = "utf-8"

    def load_rent_cars(self) -> list[CustomerCarRent]:
        try:
            rent_cars = []
            with open(
                CUSTOMER_CAR_RENTS_FILE_PATH, "r", encoding=self.encoding
            ) as file:
                for line in file.readlines():
                    raw = line.strip("\n")
                    if not raw:
                        print("empty line", raw)
                        continue
                    print(
                        "Is Header Line",
                        is_header_line(line=raw, lookup=self.file_header),
                    )
                    if is_header_line(line=raw, lookup=self.file_header):
                        continue
                    [
                        id,
                        car_id,
                        customer_id,
                        base_price,
                        num_of_days,
                        payment_type,
                        status,
                    ] = raw.split(",")
                    rent_cars.append(
                        CustomerCarRent(
                            id=int(id),
                            car_id=int(car_id),
                            customer_id=int(customer_id),
                            base_price=float(base_price),
                            num_of_days=int(num_of_days),
                            payment_type=payment_type,
                            status=status,
                        )
                    )
            self.rent_cars = rent_cars
            return rent_cars
        except FileNotFoundError as e:
            print(str(e))
            return []

    def save_rent_cars(self) -> bool:
        try:
            with open(
                CUSTOMER_CAR_RENTS_FILE_PATH, "w", encoding=self.encoding
            ) as file:
                file.write(self.file_header)
                for car_rent in self.rent_cars:
                    file.write(
                        f"\n{car_rent.id},{car_rent.car_id},{car_rent.customer_id},{car_rent.base_price},{car_rent.num_of_days},{car_rent.payment_type},{car_rent.status}"
                    )
            return True
        except Exception as e:
            print(str(e))
            return False

    def add_car_rent(
        self,
        *,
        car_id: int,
        customer_id: int,
        num_of_days: int,
        base_price: float,
        payment_type: str,
    ) -> bool:
        try:
            customer = CustomerCarRent(
                id=len(self.rent_cars) + 1,
                car_id=car_id,
                customer_id=customer_id,
                base_price=base_price,
                num_of_days=num_of_days,
                payment_type=payment_type,
                status="completed",
            )
            self.rent_cars.append(customer)
            return True
        except Exception as e:
            print(str(e))
            return False

    def find_rent_car(self, customer_car_rent_id: int) -> CustomerCarRent | None:
        try:
            for car_rent in self.rent_cars:
                if car_rent.id == customer_car_rent_id:
                    return car_rent
            return None
        except Exception as e:
            print(str(e))
            return None

    def update_rent_car(
        self,
        *,
        customer_car_rent_id: int,
        car_id: int | None = None,
        customer_id: int | None = None,
        num_of_days: int | None = None,
        base_price: float | None = None,
        payment_type: str | None = None,
        status: str | None = None,
    ) -> bool:
        try:
            rent_car = self.find_rent_car(customer_car_rent_id)
            if not rent_car:
                return False

            rent_car.car_id = rent_car.car_id if not car_id else car_id
            rent_car.customer_id = (
                rent_car.customer_id if not customer_id else customer_id
            )
            rent_car.num_of_days = (
                rent_car.num_of_days if not num_of_days else num_of_days
            )
            rent_car.base_price = rent_car.base_price if not base_price else base_price
            rent_car.payment_type = (
                rent_car.payment_type if not payment_type else payment_type
            )
            rent_car.status = rent_car.status if not status else status

            return True
        except Exception as e:
            print(str(e))
            return False

    def remove_rent_car(self, customer_car_rent_id: int) -> bool:
        try:
            for index, value in enumerate(self.rent_cars):
                if value.id == customer_car_rent_id:
                    del self.rent_cars[index]
                    return True
            return False
        except Exception as e:
            print(str(e))
            return False

    def list_rent_cars(
        self, car_service: CarService, customer_service: CustomerService
    ) -> None:
        for rent in self.rent_cars:
            print(rent.display(car_service, customer_service))
