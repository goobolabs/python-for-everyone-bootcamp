# Name:Abdiaziz Bishar
# Description: A simple study log that saves and loads notes to/from a text file.

def load_notes(path):
    """Tries to read notes from a file; returns an empty list if file not found."""
    notes = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # .strip() removes the newline character (\n) from the end
                notes.append(line.strip())
    except FileNotFoundError:
        # If file doesn't exist, we just return the empty list
        return []
    return notes

def save_notes(path, notes):
    """Writes each note from the list into the specified file."""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def main():
    # Section 1: Foundations (Variables and Input)
    filename = "notes.txt"
    user_name = input("Enter your name: ")
    print(f"Welcome to the Study Log, {user_name}!")
    
    # Section 5: Load notes at startup
    notes_list = load_notes(filename)

    # Section 3: Loop for the menu
    while True:
        print("\n--- Study Log Menu ---")
        print("1) Add note")
        print("2) List all notes")
        print("3) Save and Quit")
        
        choice = input("Pick an option (1-3): ")

        # Section 2: Operators and Conditions
        if choice == "1":
            new_note = input("Enter your study note: ")
            notes_list.append(new_note)
            print("Note added!")
        
        elif choice == "2":
            print("\n--- Your Notes ---")
            # Section 3: Loop to print every note
            if not notes_list:
                print("(No notes found)")
            else:
                for note in notes_list:
                    print(f"- {note}")
        
        elif choice == "3":
            # Section 5: Save notes before exiting
            save_notes(filename, notes_list)
            print(f"Notes saved to {filename}. Goodbye, {user_name}!")
            break
        
        else:
            print("Invalid choice, please try again.")

# Section 4: Main entry point
if __name__ == "__main__":
    main()