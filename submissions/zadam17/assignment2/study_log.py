def load_notes(filename):
    try:
        with open(filename, 'r' , encoding="utf-8") as file:
            notes=[line.strip() for line in file]
            return notes
    except FileNotFoundError:
        return []
    
def save_notes(filename, notes):
    with open(filename , "w", encoding="utf-8") as file:
        for note in notes:
            file.write(note + "\n")

def main():
    notes=load_notes("notes.txt")
    
    

    while True:
        print("\nMenu:")
        print("1 = Add note")
        print("2 = List notes")
        print("3 = Quit")

        choice= input ( "choose an option: ")
        
        if choice == '1':
            note=input("Enter Your Note: ")
            notes.append(note)
        elif choice == '2':
            print("\n Your Notes" )
            for note in notes:
                print(note)
        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Notes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
