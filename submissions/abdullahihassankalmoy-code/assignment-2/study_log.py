# assigment 2
# name: abdullahi hassan kalmoy
# this is assignment 2 that covers all the sections we have learnt

def load_notes(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def save_notes(path, notes):
    with open(path, 'w', encoding='utf-8') as f:
        for note in notes:
            f.write(notes + '\n')


def main():
    filename = 'note.txt'
    notes = load_notes(filename)
    name = input('whats is your name? ')
    print(f"welcome mr {name}")

    while True:
        print('\n1) add note 2) list note 3) quit ')
        choice = input('pick: ')
        if choice == "1":
            note = input('write your note: ')
            notes.append(note)
            print('note added')

        elif choice == '2':
            print('\nyour notes')
            for n in notes:
                print(n)

        elif choice == '3':
            save_notes('notes.txt', notes)
            print('bye notes saved. ')
            break

        else:
            print('"Invalid choice. Try again."')


if __name__ == "__main__":
    main()
