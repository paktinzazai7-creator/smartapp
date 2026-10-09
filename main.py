
from smartappcontroller import smart_app_controller
from smartapi import weer_utrecht


def start_platform():
    while True:
        print("\n========== SMARTHUB =========")
        print("1. Smart App Controller")
        print("2. Weer in Utrecht")
        print("3. Stoppen")

        try:
            keuze = int(input("Kies een optie: "))

        except (ValueError, EOFError):
            print("Vul een geldig getal in")
            continue

        if keuze == 1:
            try:
                smart_app_controller()
            except (OSError, ValueError) as fout:
                print("Fout:", fout)

        elif keuze == 2:
            weer_utrecht()

        elif keuze == 3:
            print("Programma gestopt")
            break

        else:
            print("Ongeldige keuze")


start_platform()
