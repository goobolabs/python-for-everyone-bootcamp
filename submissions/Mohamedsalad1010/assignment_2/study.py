# Name: Mohamed salad
# Program: Simple study notes 

# loading notes
def  load_notes(path):
    try : 
        with open(path , 'r' , encoding='utf-8') as    file:
            lines = file.read()
            return [lines.strip() for lines in file]
    except FileNotFoundError :
        return []
    
    # saving notes 
def save_notes (path , notes) : 
    with open(path , "w", encoding='utf-8') as file :
        for note in notes :
            file.write(note + "\n")
            
            
# appending notes 

def main () :
  notes =  load_notes("notes.txt")
  name = input('what is your name?')
  print("welcome" + name +  " to the study note log.")
  while  True:
    
    print('\n 1. add 2.list 3.quit')
    choice = input("pick:")
    
    if choice == '1':
        note = input('Enter YOUR  note?')
        notes.append(note)
    
    elif choice == "2":
        print('\n notes') 
        for n in notes :
         print('-' + n)
            
    elif choice == "3": 
        save_notes("notes.txt"  , notes)
        print('Bye!')
        break
    else:
        print('invalid pick notes please  try again.')
        
if __name__ == "__main__":
    main()