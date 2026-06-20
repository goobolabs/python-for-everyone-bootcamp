def is_header_line(*, line: str, lookup: str) -> bool:
    if line.strip().lower() == lookup.strip().lower():
        return True
    return False


def convert_str_to_bool(value: str) -> bool:
    if value.strip().lower() == "true":
        return True
    else:
        return False


def print_message(message: str = "---Back to System Panel---"):
    print(message, "\n")


def validate_id_value(id_value: str, prefix: str = "Customer") -> bool:
    if not id_value:
        print(f"{prefix} id is required")
        return False

    if not id_value.isnumeric():
        print(f"{prefix} id must be numeric")
        return False

    return True
