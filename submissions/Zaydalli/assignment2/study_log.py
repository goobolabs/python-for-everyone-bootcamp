# Name: Zaydalli
# Description: A simple study log program that lets users add, list, and save their study notes.

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip("\n"))
            return notes
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def main():
    name = input("What is your name? ")
    print(f"Welcome to the study log, {name}!")
    
    file_path = "notes.txt"
    notes = load_notes(file_path)
    
    while True:
        print("\n1) Add note  2) List  3) Quit")
        pick = input("Pick: ")
        
        if pick == "1":
            note = input("Note: ")
            notes.append(note)
        elif pick == "2":
            for note in notes:
                print(note)
        elif pick == "3":
            print("Bye!")
            save_notes(file_path, notes)
            break
        else:
            print("Invalid option. Please pick 1, 2, or 3.")

if __name__ == "__main__":
    main()
