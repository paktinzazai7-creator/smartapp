from pathlib import Path
import os

inputFile = Path(r"C:\Users\pakti\python\input.txt")
outputFile = Path(r"C:\Users\pakti\python\output.txt")


def lees_dagen(inputFile):
    voorbeeld = """date numPeople tempSetpoint tempOutside precip
05-10-2024 2 19 8 7
06-10-2024 2 19 8 7
07-10-2024 1 19 9 3
08-10-2024 1 19 11 0
09-10-2024 1 19 10 3
10-10-2024 3 21 6 0
11-10-2024 3 21 4 0
"""

    if not inputFile.exists() or len(inputFile.read_text(encoding="utf-8-sig").splitlines()) < 2:
        inputFile.write_text(voorbeeld, encoding="utf-8")
        print("Voorbeeldgegevens in input.txt gezet")

    with open(inputFile, "r", encoding="utf-8-sig") as bestand:
        regels = bestand.readlines()[1:]

    return [regel for regel in regels if regel.strip()]


def aantal_dagen(inputFile):
    return len(lees_dagen(inputFile))


def auto_bereken(inputFile, outputFile):
    regels = lees_dagen(inputFile)
    uitvoer = []

    for regel in regels:
        datum, personen, setpoint, buiten, regen = regel.split()

        verschil = float(setpoint) - float(buiten)

        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = min(int(personen) + 1, 4)
        bewatering = float(regen) < 3

        uitvoer.append(f"{datum};{cv};{ventilatie};{bewatering}")

    with open(outputFile, "w") as bestand:
        for regel in uitvoer:
            bestand.write(regel + "\n")

    print(len(uitvoer), "dagen opgeslagen")
    print("Bestand:", outputFile)
    print(outputFile.read_text())

    os.startfile(str(outputFile))


def overwrite_settings(outputFile):
    datum = input("Datum: ").strip()
    systeem = input("Systeem (1=CV, 2=Ventilatie, 3=Bewatering): ").strip()

    if systeem not in ["1", "2", "3"]:
        return -3

    with open(outputFile, "r") as bestand:
        regels = bestand.readlines()

    for i in range(len(regels)):
        gegevens = regels[i].strip().split(";")

        if gegevens[0] == datum:
            waarde = input("Nieuwe waarde: ").strip()

            try:
                getal = int(waarde)
            except ValueError:
                return -3

            if systeem == "1" and 0 <= getal <= 100:
                gegevens[1] = str(getal)
            elif systeem == "2" and 0 <= getal <= 4:
                gegevens[2] = str(getal)
            elif systeem == "3" and waarde in ["0", "1"]:
                gegevens[3] = str(bool(getal))
            else:
                return -3

            regels[i] = ";".join(gegevens) + "\n"

            with open(outputFile, "w") as bestand:
                bestand.writelines(regels)

            return 0

    return -1


def smart_app_controller():
    while True:
        print("\nSMART APP CONTROLLER")
        print("1. Aantal dagen")
        print("2. Automatisch berekenen")
        print("3. Waarde overschrijven")
        print("4. Stoppen")

        keuze = input("Kies een optie: ")

        try:
            if keuze == "1":
                print("Aantal dagen:", aantal_dagen(inputFile))

            elif keuze == "2":
                auto_bereken(inputFile, outputFile)

            elif keuze == "3":
                resultaat = overwrite_settings(outputFile)

                if resultaat == 0:
                    print("Waarde aangepast")
                    os.startfile(str(outputFile))
                elif resultaat == -1:
                    print("Datum niet gevonden")
                else:
                    print("Ongeldige waarde of systeem")

            elif keuze == "4":
                print("Programma gestopt")
                break

            else:
                print("Ongeldige keuze")

        except FileNotFoundError:
            print("Bestand niet gevonden. Kies eerst optie 2.")

        except (ValueError, OSError) as fout:
            print("Fout:", fout)
            
if __name__ == "__main__":
    smart_app_controller()
