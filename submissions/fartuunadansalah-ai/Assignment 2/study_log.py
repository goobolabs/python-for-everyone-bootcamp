# Description: Simple study log program that allows user to add, list, and save notes to a file.

# -------- Section 5: Files & Error Handling --------
def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")


# -------- Section 4: Functions --------
def main():
    # Optional: ask user name
    name = input("Enter your name: ")
    print(f"Welcome {name} 👋")

    notes = load_notes("notes.txt")

    while True:
        # -------- Section 1 & 2: Basics + Conditions --------
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note added ✅")

        elif choice == "2":
            print("\nYour Notes:")
            if len(notes) == 0:
                print("No notes yet.")
            else:
                # -------- Section 3: Loop --------
                for n in notes:
                    print("-", n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye! 👋 Notes saved.")
            break

        else:
            print("Invalid choice. Try again.")


# -------- Run Program --------
if __name__ == "__main__":
    main()