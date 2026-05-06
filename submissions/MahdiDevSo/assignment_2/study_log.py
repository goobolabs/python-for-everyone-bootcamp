# Name: Mahdi
# Program: Simple Study Log
# This program lets the user add notes, see all notes,
# and save them in a file. It loads old notes when it starts
# and saves them again when the user quits.


def load_notes(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, 'w', encoding='utf-8') as file:
        for note in notes:
            file.write(note + '\n')

def main():
    file_path = 'notes.txt'

  
    notes = load_notes(file_path)


    while True:
        print('\n--- Study Log Menu ---')
        print('1. Add note')
        print('2. List notes')
        print('3. Quit')

        choice = input('Choose an option (1/2/3): ')

        if choice == '1':
            note = input('Enter your note: ')
            notes.append(note)
            print('Note added!')

        elif choice == '2':
            print("\nYour notes:")
            if not notes:
                print('(No notes yet)')
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note}")

        elif choice == '3':
            save_notes(file_path, notes)
            print('Notes saved. Goodbye!')
            break

        else:
            print('Invalid choice. Please select 1, 2, or 3.')



if __name__ == "__main__":
    main()

