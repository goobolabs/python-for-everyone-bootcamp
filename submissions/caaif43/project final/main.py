#_final_project_gym_management_system/main.py
from models.members import Member, Gym
from utils.storage import load_members, save_members


gym = Gym()
gym.members = load_members()


def add_member():
    try:
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Invalid ID")
        return

    member_name = input("Enter member name: ")
    membership_type = input("Enter membership type: ")

    member = Member(member_id, member_name, membership_type)

    gym.add_member(member)

    print("Member added successfully")


def list_members():
    if not gym.members:
        print("No members found")
        return

    for member in gym.members:
        print(member)


def search_member():
    name = input("Enter member name: ")

    member = gym.search_member(name)

    if member:
        print(member)
    else:
        print("Member not found")


def update_member():
    try:
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Invalid ID")
        return

    member = gym.get_member_by_id(member_id)

    if not member:
        print("Member not found")
        return

    new_name = input("Enter new name: ")
    new_type = input("Enter new membership type: ")

    if new_name:
        member.member_name = new_name

    if new_type:
        member.membership_type = new_type

    print("Member updated successfully")


def remove_member():
    try:
        member_id = int(input("Enter member ID to remove: "))
    except ValueError:
        print("Invalid ID")
        return

    if gym.remove_member(member_id):
        print("Member removed")
    else:
        print("Member not found")


def main():
    while True:

        print("\n===== GYM MENU =====")
        print("1. Add Member")
        print("2. List Members")
        print("3. Search Member")
        print("4. Update Member")
        print("5. Remove Member")
        print("6. Save")
        print("7. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_member()

        elif choice == "2":
            list_members()

        elif choice == "3":
            search_member()

        elif choice == "4":
            update_member()

        elif choice == "5":
            remove_member()

        elif choice == "6":
            save_members(gym.members)
            print("Members saved")

        elif choice == "7":
            save_members(gym.members)
            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()