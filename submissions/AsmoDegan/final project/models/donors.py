from dataclasses import dataclass, field

@dataclass
class Donor:
    donor_id: str
    name: str
    blood_group: str  # Tusaale: A+, O-, B+
    age: int          # Da'da deeqbixiyaha

    def __str__(self) -> str:
        return f"ID: {self.donor_id} | Name: {self.name} | Blood: {self.blood_group} | Age: {self.age}"


class BloodBank:
    def __init__(self) -> None:
        self._donors: list[Donor] = []

    def add(self, donor: Donor) -> bool:
        if self.find_by_id(donor.donor_id) is not None:
            return False
        self._donors.append(donor)
        return True

    def find_by_id(self, donor_id: str) -> Donor | None:
        for d in self._donors:
            if d.donor_id == donor_id:
                return d
        return None

    def remove(self, donor_id: str) -> bool:
        donor = self.find_by_id(donor_id)
        if donor is None:
            return False
        self._donors.remove(donor)
        return True

    def search(self, query: str) -> list[Donor]:
        results = []
        query = query.lower()
        for d in self._donors:
            # Habkan wuxuu u baarayaa wax kasta oo la qoro xitaa hadday da'da tahay
            if (query in d.donor_id.lower() or 
                query in d.name.lower() or 
                query in d.blood_group.lower() or 
                query in str(d.age)):
                results.append(d)
        return results

    def all(self) -> list[Donor]:
        return list(self._donors)

    def update(
        self,
        donor_id: str,
        *,
        name: str | None = None,
        blood_group: str | None = None,
        age: int | None = None,
    ) -> bool:
        d = self.find_by_id(donor_id)
        if d is None:
            return False
        if name is not None:
            d.name = name
        if blood_group is not None:
            d.blood_group = blood_group
        if age is not None:
            d.age = age
        return True

    def clear(self) -> None:
        self._donors = []
