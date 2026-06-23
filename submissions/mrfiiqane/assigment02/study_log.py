# mrfiiqane == so dhowow magacaygu waa mohamed mohamud Kani waa assignment 2  ==

from pathlib import Path
BASE_DIR = Path(__file__).parent

note_path = BASE_DIR / "note.txt"

# soo jiido notes ka 
def load(path): 
  try:
    with open(path, "r", encoding="utf-8") as f:
      notes = []
      for line in f:
         notes.append(line.strip())
      return notes   
  except FileNotFoundError:
      print("File not found")
      return []
  
# save garee note ka 
def save(path, notes):
   with open(path, "w", encoding="utf-8") as f:
        # if not "./note.txt":
        #    mkdir("./note.txt")
        for note in notes:
           f.write(note + "\n")

# qeybta menu oo leh add,list,quit 
def menu():
  notes = load(note_path)
  print("Welcome to Study Log")
  
  while True:
    print("\n1. Add  \n2. List \n3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
       note = input("enter note: ")
       notes.append(note)

    elif choice == "2":
       if not notes:
          print("No notes found")
       else:
        print("\nYour Notes: ")
        for note in notes:
            print("-", note)

    elif choice == "3":
       save(note_path, notes)
       print("Notes saved. Bye!")
       break
    
    else:
      print("Invalid choice")
       
if __name__ == "__main__":
  menu()