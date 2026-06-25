notes = []

while True:
    print("\n1) Add note 2) List 3) Quit")
    choice = input("Pick: ").strip()
    
    if choice == "1":
        note = input("Note: ")
        notes.append(note)
        print("Note added!")
    
    elif choice == "2":
        if len(notes) == 0:
            print("No notes yet.")
        else:
            for i, n in enumerate(notes, 1):
                print(f"{i}. {n}")
    
    elif choice == "3":
        print("Bye!")
        break
    
    else:
        print("Invalid choice. Pick 1, 2, or 3.")
