def akhri_xog(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:

            xog = []

            for line in file:
                xog.append(line.strip())

            return xog

    except FileNotFoundError:
        return []


def kaydi_xog(file_path, xog):

    with open(file_path, "w", encoding="utf-8") as file:

        for item in xog:
            file.write(item + "\n")


def main():

    file_name = "beeraha.txt"

    qoraalo = akhri_xog(file_name)

    print("=== Beeraha Notes System ===")

    magaca = input("Geli magacaaga: ")

    print(f"Soo dhowow {magaca}\n")

    while True:

        print("1. Ku dar xog")
        print("2. Arag xogta")
        print("3. Save and Quit")

        choice = input("Dooro option: ")

        if choice == "1":

            xog_cusub = input("Qor xogta beerta: ")

            qoraalo.append(xog_cusub)

            print("Xogta waa lagu daray.\n")

        elif choice == "2":

            print("\n--- Xogta Beeraha ---")

            if len(qoraalo) == 0:
                print("Wax xog ah lama helin.\n")

            else:
                for item in qoraalo:
                    print(item)

                print()

        elif choice == "3":

            kaydi_xog(file_name, qoraalo)

            print("Xogta waa la kaydiyay. Nabad gelyo!")

            break

        else:
            print("Doorasho khaldan.\n")


if __name__ == "__main__":
    main()
