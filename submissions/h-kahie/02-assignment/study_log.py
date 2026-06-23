# Name: H-Kahie
# Description: A simple study notes.

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                notes.append(line.strip())
            return notes
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as file:
        for item in notes:
            file.write(item + "\n")

def main():
    path = "notes.txt"
    notes = load_notes(path)
    
    name = input("What is your name? ")
    print("Hello", name)

    while True:
        print("1) add, 2) list, 3) quit")
        choice = input("Pick: ")

        if choice == "1":
            item = input("Note: ")
            notes.append(item)
        elif choice == "2":
            for x in notes:
                print(x)
        elif choice == "3":
            save_notes(path, notes)
            print("Bye!")
            break
        else:
            print("Try again")

if __name__ == "__main__":
    main()
