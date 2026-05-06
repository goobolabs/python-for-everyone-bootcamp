# Name: Abdisalaam Salad Ali.
# Description: A simple program for managing and storing study notes in a text file.

def load_notes(path):
    """Reads the file and returns a list of notes."""
    try:
        # Open with mode 'r' and encoding 'utf-8'
        with open(path, "r", encoding="utf-8") as f:
            # Read all lines and strip the newline characters
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

def save_notes(path, notes):
    """Writes the list of notes to the file."""
    # Open with mode 'w' to overwrite the file with current list
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")

def main():
    # 1. Foundations: Variables and Input
    print("--- Welcome to the Study Log Manager ---")
    user_name = input("Please enter your name: ")
    print(f"Hello {user_name}, let's get started!")

    # 5. Files: Load existing notes at startup
    file_path = "notes.txt"
    notes = load_notes(file_path)

    # 3. Collections & Loops: 'while True' menu loop
    while True:
        print("\n--- MENU ---")
        print("1) Add note")
        print("2) List notes")
        print("3) Quit")
        
        choice = input("Pick an option (1, 2, or 3): ")

        # 2. Operators and Conditions: if/elif/else
        if choice == "1":
            new_note = input("What did you learn? ")
            # 3. Collections: Append note to the list
            notes.append(new_note)
            print("Note added successfully.")
            
        elif choice == "2":
            print("\n--- Your Study Notes ---")
            if not notes:
                print("Your log is currently empty.")
            else:
                # 3. Loops: For loop to print each note
                for n in notes:
                    print(f"- {n}")
                    
        elif choice == "3":
            # 5. Files: Save notes before exiting
            save_notes(file_path, notes)
            print(f"Goodbye {user_name}  Your notes have been saved.")
            break # Exit the loop
            
        else:
            print("Invalid choice, please try again.")

# 4. Functions: Standard entry point
if __name__ == "__main__":
    main()