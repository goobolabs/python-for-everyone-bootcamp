from model.customer import Customer
from core.config import CUSTOMERS_FILE_PATH
from utils.utils import is_header_line


class CustomerService:
    def __init__(self) -> None:
        self.customers: list[Customer] = []
        self.customer_file_header = "id,name,phone,identity"
        self.encoding = "utf-8"

    def load_customers(self) -> list[Customer]:
        try:
            customers = []
            with open(CUSTOMERS_FILE_PATH, "r", encoding=self.encoding) as file:
                for line in file.readlines():
                    raw = line.strip("\n")
                    if not raw:
                        print("empty line", raw)
                        continue
                    print(
                        "Is Header Line",
                        is_header_line(line=raw, lookup=self.customer_file_header),
                    )
                    if is_header_line(line=raw, lookup=self.customer_file_header):
                        continue
                    [id, name, phone, identity] = raw.split(",")
                    customers.append(
                        Customer(id=int(id), name=name, phone=phone, identity=identity)
                    )
            self.customers = customers
            return customers
        except FileNotFoundError as e:
            print(str(e))
            return []

    def save_customers(self) -> bool:
        try:
            with open(CUSTOMERS_FILE_PATH, "w", encoding=self.encoding) as file:
                file.write(self.customer_file_header)
                for customer in self.customers:
                    file.write(
                        f"\n{customer.id},{customer.name},{customer.phone},{customer.identity}"
                    )
            return True
        except Exception as e:
            print(str(e))
            return False

    def add_customer(self, *, name: str, phone: str, identity: str) -> bool:
        try:
            customer = Customer(
                id=len(self.customers) + 1, name=name, phone=phone, identity=identity
            )
            self.customers.append(customer)
            return True
        except Exception as e:
            print(str(e))
            return False

    def find_customer(self, customer_id: int) -> Customer | None:
        try:
            for customer in self.customers:
                if customer.id == customer_id:
                    return customer
            return None
        except Exception as e:
            print(str(e))
            return None

    def update_customer(
        self,
        *,
        customer_id: int,
        name: str | None = None,
        phone: str | None = None,
        identity: str | None = None,
    ) -> bool:
        try:
            customer = self.find_customer(customer_id)
            if not customer:
                return False
            customer.name = customer.name if not name else name.strip()
            customer.phone = customer.phone if not phone else phone.strip()
            customer.identity = customer.identity if not identity else identity.strip()
            return True
        except Exception as e:
            print(str(e))
            return False

    def remove_customer(self, customer_id: int) -> bool:
        try:
            for index, value in enumerate(self.customers):
                if value.id == customer_id:
                    del self.customers[index]
                    return True
            return False
        except Exception as e:
            print(str(e))
            return False

    def list_customers(self) -> None:
        for customer in self.customers:
            print(customer)
