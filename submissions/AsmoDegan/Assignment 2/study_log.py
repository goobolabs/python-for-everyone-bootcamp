# Magaca: Asmo Abdulaahi
# Assegment 2: Barnaamijkan wuxuu kuu oggolaanayaa inaad casharada aad barato xafidato.

def load_notes(path):
    """Function-kan wuxuu soo ridaa qoraaladii hore haddii ay jiraan."""
    liiska_casharada = []
    try:
        # Waxaan furaynaa faylka si aan u akhrino
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                # Mid mid ayaan u soo qaadaynaa xariiqyada
                liiska_casharada.append(line.strip())
    except FileNotFoundError:
        # Haddii faylka la waayo, barnaamijku ma istaagayo ee liis madan ayuu celinayaa
        return []
    return liiska_casharada

def save_notes(path, notes):
    """Function-kan wuxuu casharada ku qoraa faylka marka qofku baxayo."""
    with open(path, "w", encoding="utf-8") as file:
        for xariiq in notes:
            file.write(xariiq + "\n")

def main():
    faylka = "my_notes.txt"
    # Marka barnaamijku bilowdo, wuxuu soo akhrinayaa wixii hore u qornaa
    notes = load_notes(faylka)
    
    print("--- Diiwaanka Barashada ---")
    magaca = input("Magacaa? ")
    print("Soo dhowow, " + magaca + "!")

    while True:
        # Menu-ga barnaamijka
        print("\nDoorashooyinka:")
        print("1) Add a note (Qor cashar)")
        print("2) List all notes (Eeg casharada)")
        print("3) Quit (Xafid oo ka bax)")
        
        pick = input("Pick (1, 2, or 3): ")

        if pick == "1":
            qoraal = input("Maxaad baratay maanta? ")
            notes.append(qoraal)
            print("Waa lagu Daray!")

        elif pick == "2":
            print("\n--- Casharadaadii horay u qornaa ---")
            if len(notes) == 0:
                print("Diiwaankaagu waa madhan yahay weli.")
            else:
                # Loop-kan wuxuu soo saarayaa cashar kasta oo ku jira liiska
                for n in notes:
                    print("- " + n)

        elif pick == "3":
            # Halkan ayaan ku xafidaynaa faylka ka hor intaanan bixin
            save_notes(faylka, notes)
            print("Nabad gelyo " + magaca + "! Casharadaada waa la xafiday.")
            break

        else:
            print("Khalad! Fadlan dooro 1, 2, ama 3.")

if __name__ == "__main__":
    main()
