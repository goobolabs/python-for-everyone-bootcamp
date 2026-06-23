#   8o8-nouradin 
#   Study Log Program

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes_list = []
            for line in file:
                notes_list.append(line.strip())
            return notes_list
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for item in notes:
            file.write(item + "\n")

def main():
    file_name = "notes.txt"
    notes = load_notes(file_name)
    
    print("--- Study Log ---")
    user_name = input("Enter your name: ")
    print(f"Hello {user_name}!")

    while True:
        print("\n1) Add note")
        print("2) List notes")
        print("3) Quit")
        
        choice = input("Pick (1, 2, or 3): ")

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
            save_notes(file_name, notes)
            print("Saved. Bye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
