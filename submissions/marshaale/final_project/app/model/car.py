from dataclasses import dataclass


@dataclass
class Car:
    id: int
    name: str
    model: str
    year: str
    price_per_day: float
    is_rented: bool

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nModel: {self.model}\nYear: {self.year}\nAvailable: {"No" if self.is_rented else "Yes"}\nDaily Price: ${self.price_per_day}"
