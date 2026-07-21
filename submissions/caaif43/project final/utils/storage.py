from models.members import Member


FILE_PATH = "data/members.txt"


def load_members():

    members = []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                if line.startswith("#"):
                    continue

                if line == "id|member_name|membership_type":
                    continue

                parts = line.split("|")

                if len(parts) != 3:
                    continue

                member_id = int(parts[0])
                member_name = parts[1]
                membership_type = parts[2]

                member = Member(
                    member_id,
                    member_name,
                    membership_type
                )

                members.append(member)

    except FileNotFoundError:
        pass

    return members


def save_members(members):

    with open(FILE_PATH, "w", encoding="utf-8") as file:

        file.write("# Gym Members\n")
        file.write("id|member_name|membership_type\n")

        for member in members:

            line = (
                f"{member.member_id}|"
                f"{member.member_name}|"
                f"{member.membership_type}\n"
            )

            file.write(line)