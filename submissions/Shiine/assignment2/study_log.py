# my name is Abdihamidhussein >Shiine
# A simple study log that takes a notes from user saves and displays All notes
#empty list
notes=[]
# afunction that reads old note  from file
def read_old_note() :
  try:
   with open('notes.txt','r',encoding='utf8') as  file:
     for line in file:
       notes.append(line.strip())
  except:
    pass
# this function writes note in to a file
def save_note():
  with open('notes.txt','w',encoding='utf8') as  file:
    for items in notes:
      file.write(items+'\n')
# this function appends note into the empty list
def add_note():
    user_input=input("write a note:")
    if len(user_input)==0:
      print("empty note note allowed")
    else:
       notes.append(user_input)
# show_note shows the current notes we write
def show_note():
  if len(notes)==0:
    print("not a note yet to show")
  else:
   
    for i, note in enumerate(notes,1) :
      
      print(i,'.',note)
# main proram
# reads old notes from file
read_old_note()
while True:
  print('\n welcome note program')
  print("1.Add note")
  print("2.show a note")
  print("3.quit")

  select=input("choose:")
#   if select=="":
   #  print("please choose 1 to 3 only")
  if select=="1":
      add_note()
      save_note()
      print("note created successfuly")
  elif select=="2":
      
      show_note()
      
  elif select=="3":
    print("Thanks for you using note program have a nice day.")
    break
  else:

    print("invalid")

   
  
   
    


    
  
  

