# Function to load notes from a file
def load_notes(path):
    try:
        # Try to open the file in read mode
        with open(path, "r", encoding="utf-8") as file:
            notes = []  # create empty list to store notes
            
            # Read each line from the file
            for line in file:
                notes.append(line.strip())  # remove newline and add to list
            
            return notes  # return all notes
        
    except FileNotFoundError:
        # If file does not exist, return empty list (no notes yet)
        return []


# Function to save notes into a file
def save_notes(path, notes):
    # Open file in write mode (this will overwrite old content)
    with open(path, "w", encoding="utf-8") as file:
        
        # Write each note into the file
        for note in notes:
            file.write(note + "\n")  # add newline after each note


# Main program function
def main():
    print("Welcome to Study Log")

    # Ask user for their name
    name = input("Enter your name: ")
    print(f"Hello {name}! Let's track your study notes.\n")

    # Load existing notes from file
    notes = load_notes("notes.txt")

    # Start menu loop
    while True:
        print("\nMenu:")
        print("1 = Add note")
        print("2 = List notes")
        print("3 = Quit")

        # Get user choice
        choice = input("Choose an option: ")

        if choice == "1":
            # Add a new note
            note = input("Enter your note: ")
            notes.append(note)
            print("Note added!")

        elif choice == "2":
            # Show all notes
            print("\nYour notes:")
            if len(notes) == 0:
                print("No notes yet.")
            else:
                for note in notes:
                    print("-", note)

        elif choice == "3":
            # Save notes and exit program
            save_notes("notes.txt", notes)
            print("Notes saved. Goodbye!")
            break

        else:
            # Handle invalid input
            print("Invalid choice. Please select 1, 2, or 3.")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()