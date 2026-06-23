# messages.py

# Mutable defaults like [] or {} can cause unexpected behavior
# because the same object is reused between function calls.

def send_message(name, message="Welcome!"):
    print(name, "receives message:", message)

send_message("Yahye")
send_message("Ahmed", "Your account is ready.")