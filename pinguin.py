import json
import webbrowser
import http.server
import socketserver
import os
import time

print(
    "Welkom bij de pinguin simulatie! \nWij raden u aan uw geluid op een zacht volume te zetten."
)
modulatie_jaren: int = 0
while True:
    try:
        modulatie_jaren = int(input("Hoeveel jaar wilt u moduleren? "))
        break
    except ValueError:
        print("Ongeldige invoer. Voer alstublieft een geldig geheel getal in.")

pinguins: int = 40_000_000


variabelen: list = [
    "Totale pinguins",
    "Geboren",
    "Gestorven",
    "Verrijkt",
    "Voedsel",
    "Temperatuur stijging",
    "Overschreden draagkracht in pinguïns",
    "Gestolen pinguins",
    "Verdwaalde pinguins",
]


def changenames(nieuw_namen: list) -> None:
    # Load the JSON data
    with open("./static/data.json", "r") as file:
        data = json.load(file)

    data_namen = list(data.keys())

    new_variable_names = {}
    for i in range(len(data_namen)):
        new_variable_names[data_namen[i]] = nieuw_namen[i]

    # Iterate over the dictionary and rename the keys
    for old_name, new_name in new_variable_names.items():
        if old_name in data:
            data[new_name] = data.pop(old_name)

    with open("./static/data.json", "w") as file:
        json.dump(
            data, file, indent=4
        )  # indent for pretty printing, you can remove it if you prefer compact JSON

changenames(variabelen)

def changedata(aantal: list, variabel: str) -> None:
    global modulatie_jaren
    # Load the JSON data
    with open("./static/data.json", "r") as file:
        data = json.load(file)

    jaren: list = [str(i + 2023) for i in range(modulatie_jaren)]

    data[variabel]["years"] = jaren
    data[variabel]["data"] = aantal

    with open("./static/data.json", "w") as file:
        json.dump(
            data, file, indent=4
        )  # indent for pretty printing, you can remove it if you prefer compact JSON


def changedata2(aantal: list, aantal2: list, variabel: str) -> None:
    global modulatie_jaren
    # Load the JSON data
    with open("./static/data.json", "r") as file:
        data = json.load(file)

    jaren: list = [str(i) for i in range(10)]

    data[variabel]["years"] = jaren
    data[variabel]["data"] = aantal
    data[variabel]["data2"] = aantal2

    with open("./static/data.json", "w") as file:
        json.dump(
            data, file, indent=4
        )  # indent for pretty printing, you can remove it if you prefer compact JSON


def geborenpinguins(pinguins: int) -> int:
    global modulatie_jaren
    factor: int = 73_000_000 / 8_027_000_000
    geborenpinguins = round(pinguins * factor)

    return geborenpinguins


def gestorvenpinguins(pinguins: int) -> int:
    global modulatie_jaren
    factor: int = 61_000_000 / 8_027_000_000
    gestorvenpinguins = round(pinguins * factor)

    return gestorvenpinguins


def natuur(pinguins: int) -> tuple:
    global modulatie_jaren
    pingi = []
    pingi_d = []

    for i in range(modulatie_jaren):
        pingi.append(geborenpinguins(pinguins))
        pinguins = pingi[i] + pinguins

        pingi_d.append(gestorvenpinguins(pinguins))

    return pingi, pingi_d


def diefstal(aantaljaar) -> list:
    aantaljaar = aantaljaar + 1
    gestolen: list = []
    gestolen_pinguins = 0
    for i in range(aantaljaar):
        gestolen.append(gestolen_pinguins)
        gestolen_pinguins += 3

    return gestolen


def verdwaald(aantaljaar) -> list:
    aantaljaar = aantaljaar + 1
    verdwaald: list = []
    verdwaalde_pinguins = 0

    for i in range(aantaljaar):
        verdwaald.append(verdwaalde_pinguins)
        verdwaalde_pinguins += 78

    return verdwaald


def biologisch_evenwicht() -> list:
    data1 = [
        160_000_000,
        140_000_000,
        100_000_000,
        110_000_000,
        105_000_000,
        95_000_000,
        90_000_000,
        110_000_000,
        120_000_000,
        105_000_000,
    ]
    data2 = [
        40_000_000,
        50_000_000,
        55_000_000,
        47_000_000,
        58_000_000,
        62_000_000,
        63_000_000,
        50_000_000,
        45_000_000,
        42_000_000,
    ]

    return data1, data2


def intro():
    webbrowser.open("https://www.youtube.com/watch?v=zvzhFn0n_PM")


def boeddhisme(pinguins) -> list:
    global modulatie_jaren

    boedisten = []

    for i in range(modulatie_jaren):
        boeddhistisch = int(gestorvenpinguins(pinguins) * 0.0647813629) - int(
            gestorvenpinguins(40_000_000) * 0.0647813629
        )
        boedisten.append(boeddhistisch)
        pinguins += natuur(40_000_000)[0][i] - natuur(40_000_000)[1][i]
    return boedisten


def temperatuur_stijging() -> float:
    global modulatie_jaren
    global_temperature_anomaly_2022 = 0.86 # graden celsius
    global_temperature_anomaly_1980 = 0 # graden celsius
    verschil = global_temperature_anomaly_2022 - global_temperature_anomaly_1980
    verschil_per_jaar = verschil / 42 # graden celsius per jaar = 0.020476190476190476

    verschillen = []
    for i in range(modulatie_jaren):
        verschillen.append(verschil_per_jaar*i)

    return verschillen

def pinguin_verlies(temp_stijging: float) -> float:
    # Berekeningen voor verlies aan ijsvolume en het daaruit voortvloeiende verlies aan pinguïnpopulatie
    ijs_smelt_snelheid_per_graad = 2.86  # miljard ton ijs per graad temperatuurstijging
    ijs_smelt_snelheid_basis = 0.84  # miljard ton ijs bij oorspronkelijke temperatuur
    totaal_ijs_verlies = ijs_smelt_snelheid_basis  # Start met het basisverlies
    for _ in range(int(temp_stijging)):  # Voeg het ijsverlies bij elke graad toe
        totaal_ijs_verlies += ijs_smelt_snelheid_per_graad
    totaal_ijs_verlies += (temp_stijging % 1) * ijs_smelt_snelheid_per_graad  # Voeg het resterende deel toe
    percentage_ijsverlies = (totaal_ijs_verlies / (24.38 * 10**6)) * 100  # Percentage ijsverlies
    volume_ijs_m3 = (totaal_ijs_verlies / 0.9) * 10**9  # Volume verloren ijs in kubieke meters
    oppervlak_ijs_m2 = volume_ijs_m3 / 2200  # Oppervlakte verloren ijs in vierkante meters
    aantal_pinguins_verlies_per_m2 = 1.46 * 10**-4  # Pinguïnverlies per vierkante meter ijsverlies
    aantal_pinguins_verlies = aantal_pinguins_verlies_per_m2 * oppervlak_ijs_m2  # Totale pinguïnverlies
    percentage_pinguinverlies = (aantal_pinguins_verlies / (20 * 10**6)) * 100  # Percentage pinguïnverlies
    
    return percentage_pinguinverlies

# Test met temperatuurstijging van 5 graden Celsius

def bereken_pinguin_verlies() -> float:
    global modulatie_jaren

    ping_vers = []

    for i in range(modulatie_jaren):
        temp_stijging = temperatuur_stijging()[i]
        pinguin = pinguin_verlies(temp_stijging) * (natuur(40_000_000)[0][i] - natuur(40_000_000)[1][i])
        ping_vers.append(int(pinguin))

    return ping_vers


def totalepinguins(pinguins: int, aantaljaar: int) -> list:
    dood = natuur(pinguins)[1]
    geboren = natuur(pinguins)[0]
    gestolen = diefstal(aantaljaar)
    verdwaalde = verdwaald(aantaljaar)
    verloren = bereken_pinguin_verlies()

    totaal = []
    for i in range(aantaljaar):
        totaal.append(pinguins)
        pinguins += geboren[i] - dood[i] - gestolen[i] - verdwaalde[i] - verloren[i]
        if pinguins < 0:
            pinguins = 0

    return totaal


def run_server():
    PORT = 8000
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        httpd.serve_forever()


intro()
time.sleep(13)
webbrowser.open("http://localhost:8000")

with open('./images/message.txt', 'r') as file: # negeer deze code maar dit betekent en doet helemaal niets
    content = file.read()
    print(content)

changedata(totalepinguins(pinguins, modulatie_jaren), variabelen[0])
changedata(natuur(pinguins)[0], variabelen[1])
changedata(natuur(pinguins)[1], variabelen[2])

changedata(boeddhisme(pinguins), variabelen[3])
changedata2(biologisch_evenwicht()[0], biologisch_evenwicht()[1], variabelen[4])


changedata(diefstal(modulatie_jaren), variabelen[7])
changedata(verdwaald(modulatie_jaren), variabelen[8])

changedata(temperatuur_stijging(), variabelen[5])
changedata(bereken_pinguin_verlies(), variabelen[6])





run_server()
