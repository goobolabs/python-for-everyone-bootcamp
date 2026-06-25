# Section 1 — Foundations
name = input("magac:")
print("hello", name)

#Section 2 — Operators and Conditions

notes=[]
choice = input("Dooro (1: Add, 2: View, 3: Quit): ")

if choice == "1":
    pass
elif choice == "2":
    pass
elif choice == "3":
    pass
else:
    print("Doorasho khaldan.")


# Section 3
    # Loop keeps menu running
notes = []
if len (notes) == 0:
    print("Ma jiraan wax notes ah.")
else:
    print("\n--- Notes-kaaga ---")
    for note in notes:
        print(f"-{note}")

        # section 4


def main():
# (menu loop-ka)
   print("halkan ka bilwanaya!")
   if __name__ == "__main__":

   #section 5 & error handling


#def load_notes(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_notes(path, notes):
    with open(path, "w", encoding="utf-8") as f:
        for item in notes:
            f.write(f"{item}\n")

def main():
    print("halkan ka bilwanaya!")
    
if name == "__main__":
    main()