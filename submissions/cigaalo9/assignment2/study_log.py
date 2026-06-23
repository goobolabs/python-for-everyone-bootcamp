# Abdullahi

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
    print("Welcome,", name)

    while True:
        print("\n1) Add note")
        print("2) List notes")
        print("3) Quit")

        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)
            print("Note added!")

        elif choice == "2":
            if len(notes) == 0:
                print("No notes yet.")
            else:
                print("\nYour notes:")

                for note in notes:
                    print("-", note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid choice. Please pick 1, 2, or 3.")


if __name__ == "__main__":
    main()







# output
# PS C:\Users\hp\OneDrive\Desktop\ABDULLAHI\Python> python study_log.py
# Enter your name: abdullahi
# Welcome, abdullahi

# 1) Add note
# 2) List notes
# 3) Quit
# Pick: 1
# Note: learn python seriously
# Note added!

# 1) Add note
# 2) List notes
# 3) Quit
# Pick: go to the gym
# Invalid choice. Please pick 1, 2, or 3.

# 1) Add note
# 2) List notes
# 3) Quit
# Pick: 2

# Your notes:
# - learn python seriesly
# - learn python seriously

# 1) Add note
# 2) List notes
# 3) Quit
# Pick: 3
# Bye!