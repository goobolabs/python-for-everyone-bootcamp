from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    name: str
    phone: str
    identity: str  # eg passport,national identity and more others

    def __str__(self) -> str:
        return f"ID: {self.id}\nName: {self.name}\nPhone: {self.phone}\nIdentity: {self.identity}"
