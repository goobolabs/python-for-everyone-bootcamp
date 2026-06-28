from models.airport import planes, airport
from utils.storage import DATA_PATH,load_airport,purse_seat,save_airport

def menu_add(airport:airport)->None:
    flen = input("FLEET_NUMBER:").strip()
    name= input("NAME:").strip
    if not flen or name:
        print("fleet_number and name are required")
        return
    try:
        seats = purse_seat(list)
    except ValueError:
        print("seats must be numbers sepparated by coma(e.g 33,56).")
        return
    fn= airport(fleet_number=flen, name=name, seats=seats)
    if airport.add(fn):
        print("added")
    else:
        print("fleet_number already exist")
        
def print_airport(rows:list[airport])->None:
        if not rows:
            print("no airport yet")
        for a in rows:
         print(f"(a)")
         
def menu_list(airport: airport)->None:
    print_airport(airport.all())
        
def remove_menu(airport:airport)->None:
        flen = input("fleet_number to remove").strip()
        if airport.remove(flen):
            print("removed")
        else:
            print("no fleet_number to remove");
            
def menu_search(airport:airport)->None:
        q = input("serch(flen or name): ").strip()
        found = airport.search(q)
        if not found:
            print("not match")
        return
        print_airport(found)
    
def menu_update(airport:airport)->None:
    flen = input("enter fleet_number to apdate" ).strip
    if airport.find_by_fleet(flen) is None:
        print("no plane this fleet_number")
        return
    new_name = input("new_name(enter to keep:)").strip
    raw = input("new seats coma separated (enter to keep:type name to clear): ").strip()
    name_arg = new_name if new_name else None
    if raw.lower() == "None":
        seat_arag: list[float] | None = []
    elif raw:
        try:
            seat_arag =purse_seat(raw)
        except ValueError:
            print("invailed seat : no thing changed ")
            return
    else:
        seat_arag = None
    if not airport.update(flen, name=name_arg,seats=seat_arag):
        print("update filed")   
        return
print("updated")

def print_menu()->None:
    print()
    print("--- airport management---")
    print( "1) Add airport")
    print( "2) List all")
    print( "3)remove plane")
    print( "3)Search")
    print( "4) update airport")
    print( "5) Save to file")
    print( "0)quite (alse saves)")
    
  
def main()-> None:
        airport= airport()
        load_airport(DATA_PATH,airport,)
        
    
    
    
try:
    while True:
        print_menu()
        choice = input("choice: ").strip()
        if choice == "1":
            menu_add(airport)
        elif choice == "2":
            list(airport)
        elif choice == "3":
            remove_menu(airport)
        elif choice == "4":
            menu_search(airport)
        elif choice == "5":
            menu_update(airport)
        elif choice == "6":
            save_airport(DATA_PATH, airport)   
        elif choice == '0':
            print("have anice time ")
        break
finally: 
    try:
        save_airport(DATA_PATH.airport) 
        print(f"(data saved by {DATA_PATH}")
    except OSError as e:
        print("couldn't save:",e)
        
        
if __name__ =="__main__":
    main()
            
            
        
    
