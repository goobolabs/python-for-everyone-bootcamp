# Study Log Application
# This application allows users to add and list notes, and saves them to a file.

def load_note(path):
     """Load notes from a file, return empty list if file doesn't exist"""
     try:
        with open(path,"r", encoding="utf-8") as f:
            Notes = []
            for line in f:
                Notes.append(line.strip()) 
        return Notes
     except FileNotFoundError:
        return []

def save_notes(path, Notes):
     """Save notes to a file"""
     with open(path,"w", encoding="utf-8") as f:
        for note in Notes:
            f.write(note + "\n")
            

def main():
    """Main function that runs the program"""
    Notes = load_note("notes.txt")
    while True:
        print("\n1) Add note  2) List  3) Quit")
        choice = input("Pick: ")
        if choice == "1":
            note = input("Note: ")
            Notes.append(note)
        elif choice == "2":
            for note in Notes:
                print(note)
        elif choice == "3":
            save_notes("submissions\\mohanadam2233\\Assignment_2\\notes.txt", Notes)
            print("Notes saved to notes.txt.")
            print("Bye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__=="__main__":
    main()