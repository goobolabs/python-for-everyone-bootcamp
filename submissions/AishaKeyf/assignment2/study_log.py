# assignment 2 from aisha keyf , this is a simple note book


def load_notes (path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return []

def save_notes (path,notes):
    with open(path,"w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def main():
    notes = load_notes("notes.txt")

    name=input(" inter your name: ")
    print(f"welcome, {name}")

    while True:
        print ("\n1) Addd note 2)List 3)Quit")
        choice = input("choose an option: ")
        
        if choice == "1":
            note = input("Note: ")
            notes.append(note)
        
                
        elif choice == "2":
            if not notes:
                print ("no notes yet")
            else:
                for n in notes:
                    print(n)

        elif choice =="3":
            save_notes("notes.txt", notes)
            print("Bye")
            break

        else:
            print(" invalid choice, please pick 1, 2 or 3")

if __name__ == "__main__":
    main()

