# iam TheShakirr 
# here is my little program it's a simple study log that saves notes to a file....

def load_notes(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return[]
    

def save_notes(filename, notes):
    with open (filename, "w") as file:
        for note in notes:
            file.write(note + "\n")



def main():
    name = input("Enter your name: ")
    print(f"welcome {name}, ")
    notes = load_notes("notes.txt")


    while True:
        print("1) Add note 2) List 3) Quit")

        choice = input("pick: ")


        if choice == "1":
            notes.append(input("Note: "))

        elif choice == "2":
            for note in notes:
                print(note)


        elif choice == "3":
            save_notes("notes.txt", notes)
            print("Bye!!!!!!!!")
            break
        else:
            print(" Pick 1, 2, or 3.")


if __name__ == "__main__":
    main()