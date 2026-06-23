movies = []
filename = "movies.txt"

# Load movies from file if exists
try:
    with open(filename, "r") as f:
        for line in f:
            title, year = line.strip().split(",")
            movies.append({"title": title, "year": year})
except FileNotFoundError:
    pass

while True:
    print("\nMy catalog — movies")
    print("1) Add 2) List 3) Save 4) Quit")
    choice = input("Pick: ").strip()
    
    if choice == "1":
        title = input("Title: ").strip()
        year = input("Year: ").strip()
        movies.append({"title": title, "year": year})
        print(f"Added {title} ({year})")
    
    elif choice == "2":
        if len(movies) == 0:
            print("No movies yet.")
        else:
            for m in movies:
                print(f"{m['title']} ({m['year']})")
    
    elif choice == "3":
        with open(filename, "w") as f:
            for m in movies:
                f.write(f"{m['title']},{m['year']}\n")
        print("Saved.")
    
    elif choice == "4":
        with open(filename, "w") as f:
            for m in movies:
                f.write(f"{m['title']},{m['year']}\n")
        print("Saved. Bye!")
        break
    
    else:
        print("Invalid choice. Pick 1, 2, 3, or 4.")
