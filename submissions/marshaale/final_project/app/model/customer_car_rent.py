from dataclasses import dataclass
from services.customer_service import CustomerService
from services.car_service import CarService


@dataclass
class CustomerCarRent:
    id: int
    car_id: int
    customer_id: int
    num_of_days: int
    base_price: float
    payment_type: str  # pre payment or post payment
    status: str  # completed,return_due_to_issue,canceled

    def display(
        self, car_service: CarService, customer_service: CustomerService
    ) -> str:
        car = car_service.find_car(car_id=self.car_id)
        car_name = self.car_id if not car else car.name
        customer = customer_service.find_customer(customer_id=self.customer_id)
        customer_name = self.customer_id if not customer else customer.name
        return f"ID: {self.id}\nCar: {car_name}\nCustomer: {customer_name}\nRent days: {self.num_of_days}\nDaily Price: ${self.base_price}\nPrice to pay: ${self.num_of_days * self.base_price}"
