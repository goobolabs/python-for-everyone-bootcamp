
# study_log.py
# Name: Hanad Ismail
# Simple study log program



def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        for n in notes:
            f.write(n + "\n")


def main():
    notes = load_notes("notes.txt")

    while True:
        print("\n1 Add  2 List  3 Quit")
        choice = input("Pick: ")

        if choice == "1":
            note = input("Note: ")
            notes.append(note)

        elif choice == "2":
            for n in notes:
                print(n)

        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!")
            break

        else:
            print("Invalid")


if __name__ == "__main__":
    main()