
# Name: Sundus
# Description: A simple study log that saves notes to a text file.

def main():
    file = "notes.txt"
    
    try:
        with open(file, "r", encoding="utf-8") as f:
            notes = f.read().splitlines()
    except FileNotFoundError:
        notes = []

    while True:
        print("1: Add  2: List  3: Quit")
        choice = input("Select option: ")

        if choice == "1":
            new_note = input("Enter note: ")
            notes.append(new_note)
            print("Note added.")
        
        elif choice == "2":
            print("Your Notes")
            if not notes:
                print("The list is empty.")
        
        elif choice == "3":
            with open(file, "w", encoding="utf-8") as f:
                f.write("\n".join(notes))
            print("Notes saved. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
