# Study Log Program by Abdullahi4444
# This program allows users to add and list study notes, saving them to a file.

import os

def load_notes(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, 'w', encoding='utf-8') as f:
        for note in notes:
            f.write(note + '\n')

def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Welcome to your study log.")
    notes_file = os.path.join(os.path.dirname(__file__), "notes.txt")
    notes = load_notes(notes_file)
    while True:
        print("1) Add note  2) List  3) Quit")
        choice = input("Pick: ")
        if choice == "1":
            note = input("Note: ")
            notes.append(note)
        elif choice == "2":
            for note in notes:
                print(note)
        elif choice == "3":
            save_notes(notes_file, notes)
            print("Bye!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")

if __name__ == "__main__":
    main()