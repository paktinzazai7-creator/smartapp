def Fahrenheit(temp_celsius):
    return 32 + 1.8 * temp_celsius
#functie voor fahrenheit omrekenen

def gevoelstemperatuur(temp_celsius, windsnelheid, luchtvochtigheid):
    return temp_celsius - (luchtvochtigheid / 100 * windsnelheid)
#functie om gevoelstemperatur te berekenen

def weerrapport(temp_celsius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(temp_celsius,windsnelheid, luchtvochtigheid)

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif 0 <= gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif 0 <= gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif 10 <= gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"
#functie eerst berekent die gevoelstemperatuur en bewaart die een in een ander variabel, daarna controleert hij met elif en if hoe warm het is
def weerstation():
    totaal_temperatuur = 0
    antl_dagen = 0

    for dag in range(1, 8):
        temperatuur_input = float(input(f"Wat is op dag {dag} de temperatuur[C]: "))

        if temperatuur_input == "":
            print("doei")
            break

        temp_celsius = temperatuur_input

        windsnld_input = float(input(f"Wat is op dag {dag} de windsnelheid[m/s]: "))

        if windsnld_input == "":
            print("doei")
            break

        windsnelheid = windsnld_input

        vochtigheid_input = int(input(f"Wat is op dag {dag} de vochtigheid[%]: "))

        if vochtigheid_input == "":
            print("doei")
            break

        luchtvochtigheid = vochtigheid_input

        temp_fahrenheit = Fahrenheit(temp_celsius)
        raport = weerrapport(temp_celsius,windsnelheid,luchtvochtigheid)

        totaal_temperatuur += temp_celsius
        antl_dagen += 1

        gemiddelde = round(totaal_temperatuur / antl_dagen)

        print(f"Het is {temp_celsius}C ({temp_fahrenheit}F)")
        print(raport)
        print(f"Gem. temp tot nu toe is {gemiddelde}")
        print("====================================================")
weerstation()
#de for in loop is gewoon van 7 dagen, print en als de gebruiker niks invult zegt die doei, += houdt dagen bij, 