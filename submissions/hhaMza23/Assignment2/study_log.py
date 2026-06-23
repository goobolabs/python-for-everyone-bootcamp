
#Hamse Omer Mal
# This programming i create Simple Study Log
#if user log  add notes, view them saves and loads notes from a file/text

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


def main():
    notes = load_notes("notes.txt")

    name = input("What is your name? ").strip()
    print("You welcome", name)


    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ").strip()

        if choice == "1":
            note = input("Note: ").strip()
            notes.append(note)

        elif choice == "2":
            print("\nYour notes:")
            for note in notes:
                print(note)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Gooood Bye!")
            break

        else:
            print("Invalid tyr agin good luck.")


if __name__ == "__main__":
    main()