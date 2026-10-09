
import json
from urllib.request import urlopen
from urllib.error import URLError


def weer_utrecht():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.09&longitude=5.12&current=temperature_2m"

    try:
        with urlopen(url, timeout=10) as antwoord:
            gegevens = json.load(antwoord)

        temperatuur = gegevens["current"]["temperature_2m"]
        print("Temperatuur in Utrecht:", temperatuur, "°C")

    except (URLError, ValueError, KeyError, TimeoutError):
        print("Kan de temperatuur niet ophalen")
