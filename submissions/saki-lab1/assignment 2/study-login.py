






# Name:sakariye 
# Description: a simple study log program that lets the user add notes,




def load_notes(path):
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    file = "notes.txt"
    #  Section 1
    name = input("Welcome What is your name? ")
    
   
    print(f"\nHello, {name}\n")

  
    notes = load_notes(file)

    #Section 2 & 3
    while True:
        print("\n1) Add note  2) List notes  3) Quit")
        choice = input("Pick: ")
#f
       
        if choice == "1":
            new_note = input("Note: ")
            notes.append(new_note)
            print("Added.")

        elif choice == "2":
            print("\nNotes:")
            if len(notes) == 0:
                print("Empty.")
            else:
                for n in notes:
                    print("- " + n)

        elif choice == "3":
            save_notes(file, notes)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")




if __name__ == "__main__":
    main()
