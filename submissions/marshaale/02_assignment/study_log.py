# Marshaale

#
# This program is simple note taking program.
# allows users to add note or retrieve notes
#

def main():
    file_path = "notes.txt"
    notes = load_notes(file_path)
    while True:
        print("1) Add note  2) List  3) Quit ")
        user_choose = input("Pick: ")
        if user_choose == "1":
            note = input("Write your note... ").strip()
            if note:
                notes.append(note)
        elif user_choose == "2":
            for note in notes:
                print(note)
        elif user_choose == "3":
            save_notes(file_path,notes)
            print("Bye!")
            break
        else:
            print("invalid number picked")


def load_notes(path):
    notes = []
    try:
        with open(path,'r',encoding='utf-8') as f:
            lines = f.readlines()
            notes = [x.strip('\n') for x in lines]
    except FileNotFoundError:
        print(f"File {path} does not exists")
    return notes


def save_notes(path,notes):
    with open(path,'w',encoding='utf-8') as f:
        for note in notes:
            f.write(f"{note}\n")

if __name__ == "__main__":
    main()
