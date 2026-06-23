# Kifah Abdihah
# Description: Assignment 2 - A simple study log program that saves and loads notes.

def load_notes(path):
    """Reads notes from a text file and returns them as a list."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            # Create a list and strip newlines from each line
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return []

def save_notes(path, notes):
    """Writes the current list of notes back to the text file."""
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def main():
    file_name = "notes.txt"
    # Load any existing notes at the start
    notes = load_notes(file_name)
    
    print("Welcome to the Study Log System")
    name = input("Enter your name: ")
    print(f"Hello {name}! You can now manage your study notes.\n")

    while True:
        # Display the menu
        print("Menu:")
        print("1 = Add note")
        print("2 = List notes")
        print("3 = Save and Quit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new note to the list
            new_note = input("Enter your note: ")
            notes.append(new_note)
            print("Note added!")

        elif choice == "2":
            # Show all notes in the list
            print("\n--- Your Study Notes ---")
            if not notes:
                print("No notes found.")
            else:
                for item in notes:
                    print(f"- {item}")

        elif choice == "3":
            # Save the list to the file and exit
            save_notes(file_name, notes)
            print(f"Success! Your notes are saved to {file_name}. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()