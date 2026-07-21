from dataclasses import dataclass


@dataclass
class Member:
    member_id: int
    member_name: str
    membership_type: str

    def __str__(self):
        return f"{self.member_id} | {self.member_name} | {self.membership_type}"


class Gym:
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def search_member(self, name):
        for member in self.members:

            if member.member_name.lower() == name.lower():
                return member

        return None

    def get_member_by_id(self, member_id):
        for member in self.members:

            if member.member_id == member_id:
                return member

        return None

    def remove_member(self, member_id):

        member = self.get_member_by_id(member_id)

        if member:
            self.members.remove(member)
            return True

        return False