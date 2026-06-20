from services.car_service import CarService
from services.customer_service import CustomerService
from services.customer_car_rent import CustomerCarRentService


class SystemPanel:
    def __init__(self) -> None:
        self.car_service = CarService()
        self.car_service.load_cars()
        self.customer_service = CustomerService()
        self.customer_service.load_customers()
        self.car_rent_service = CustomerCarRentService()
        self.car_rent_service.load_rent_cars()

    def save_state(self) -> None:
        self.car_service.save_cars()
        self.customer_service.save_customers()
        self.car_rent_service.save_rent_cars()

    def reports(self) -> str:
        available_cars = [car for car in self.car_service.cars if not car.is_rented]
        return f"Cars: {len(self.car_service.cars)}\nCustomers: {len(self.customer_service.customers)}\nAll time rents: {len(self.car_rent_service.rent_cars)}\nAvailable cars: {len(available_cars)}\n"
