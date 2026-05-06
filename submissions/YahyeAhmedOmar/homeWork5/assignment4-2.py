# parse_positive.py

def parse_positive_int(text):
    number = int(text.strip())

    if number <= 0:
        raise ValueError("Number must be greater than 0.")

    return number

while True:
    try:
        user_input = input("Enter a positive integer: ")

        result = parse_positive_int(user_input)

        print("Valid number:", result)
        break

    except ValueError as error:
        print("Error:", error)