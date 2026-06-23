#name hodon maxamed 
# The user can add a note, print all notes, then quit. When the program starts, it tries to read old notes from a text file. When the user quits, it writes the list back to the same file. 
# If the file is not there the first time, the program just starts with an empty list.

def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []    


#save notes
def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(note + "\n")


def main():
    notes = load_notes("notes.txt")

    name = input("enter your name: ")
    print(f"hi {name} welcome: ")
    
    while True:
        print("1)Add note  2)list 3) quit ")
        choice = input("pick: ")
        if choice == "1":
            note = input("note: ")
            notes.append(note)
            save_notes("notes.txt", notes)
            print("note added sucessfully")
            
        elif choice == "2":
           if not notes:
                 print("No notes here")
           else:
                 for n in notes:
                     print(n)    

          
        elif choice == "3":
            save_notes("notes.txt", notes)
            print("bye")
            break
        else:
            print("invalid choice")    

          
          
if __name__ == "__main__":
    main()


