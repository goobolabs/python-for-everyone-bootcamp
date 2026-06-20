

# def generate_id(students):
#     if not students:
#         return "ST_01"

#     max_num = max(
#         int(student["id"].split("_")[1])
#         for student in students
#     )

#     return f"ST_{max_num + 1:02d}"

# def generate_id(items, prefix):
#     if not items:
#         return f"{prefix}_01"

#     max_num = max(
#         int(item["id"].split("_")[1])
#         for item in items
#     )

#     return f"{prefix}_{max_num + 1:02d}"

def generate_id(items, prefix):

    max_num = 0

    for item in items:

        try:
            num = int(item["id"].replace(prefix, ""))
            max_num = max(max_num, num)

        except:
            continue

    return f"{prefix}{max_num + 1:03}"

def pause():
    input("Press Enter to continue...")