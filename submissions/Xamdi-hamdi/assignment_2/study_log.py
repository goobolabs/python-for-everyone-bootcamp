# note program

def load_notes(path):
    try:
        with open(path,"r", encoding='utf-8') as file:
            return[line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return[]
    
def save_notes(path,notes):
    with open(path,"w" , encoding="utf-8") as file:
        file.write(notes )


def main():
    fileName= 'note.text'
    notes=load_notes(fileName)
    
    user_Name= input('enter your name: ')
    print(f"welcome to your study log, {user_Name}")

    while True:
        print('\n-----menu------')
        print('1) Add a note')
        print('2) List All  notes')
        print('3) Save and  Quit')

        choice=input('pick 1-3: ')

        if choice=="1":
            new_note=input('what did you do?')
            notes.append(new_note)
            print('note is added !')
        
        elif choice=="2":
            print('\nyour notes: ')
            if not notes:
                print('no notes found')
            else:
                for note in notes:
                    print(f"- {note}")
        
        elif choice=="3":
            save_notes(fileName, notes)
            print('notes saved bye')
            break
        else:
            print('invalid choice please try again!')

if __name__ == "__main__":

    main()



