# full_Name: Ismail Nouh  Hudhuun
# Program: Simple Study Log - allows user to add, view, and save study notes

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")



def main():
    notes = load_notes("notes.txt")

    name = input("Enter your name: ")
    print(f"Welcome {name}!")

    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Enter note: ")
            notes.append(note)

        elif choice == "2":
            print("\nYour Notes:")
            for note in notes:
                print(note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()



    # output
    # Enter your name: Ismail
    # Welcome Ismail!
    # 1) Add note  2) List notes  3) Quit
    # Pick: 1
    # Enter note: Learn Python
    # 1) Add note  2) List notes  3) Quit
    # Pick: 2
    # Your Notes:
    # Learn Python
    # 1) Add note  2) List notes  3) Quit
    # Pick: 3
    # Bye!