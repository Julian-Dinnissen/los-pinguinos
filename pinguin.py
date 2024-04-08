import json
import webbrowser
import http.server
import socketserver
import os
import time


modulatie_jaren: int = int(input("Hoeveel jaar wilt u moduleren? "))
pinguins: int = 40_000_000


variabelen: list = [
    "Totale pinguins",
    "Geboren",
    "Gestorven",
    "Verrijkt",
    "Voedsel",
    "Leefoppervlakte",
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


boedisten = boeddhisme(pinguins)


def totalepinguins(pinguins: int, aantaljaar: int) -> list:
    dood = natuur(pinguins)[1]
    geboren = natuur(pinguins)[0]
    gestolen = diefstal(aantaljaar)
    verdwaalde = verdwaald(aantaljaar)
    totaal = []
    for i in range(aantaljaar):
        totaal.append(pinguins)
        pinguins += geboren[i] - dood[i] - gestolen[i] - verdwaalde[i]
        if pinguins < 0:
            pinguins = 0

    return totaal

def run_server():
        # Set the port you want to use
    PORT = 8000

    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Change to the directory containing the HTML file
    os.chdir(current_dir)

    # Create a simple HTTP server handler
    Handler = http.server.SimpleHTTPRequestHandler

    # Create the server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server started at localhost:" + str(PORT))
        # Start the server
        httpd.serve_forever()



# intro()
# time.sleep(12)
webbrowser.open("http://localhost:8000")

with open('./images/message.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Print the content
    print(content)

changedata(totalepinguins(pinguins, modulatie_jaren), variabelen[0])
changedata(diefstal(modulatie_jaren), variabelen[6])
changedata(verdwaald(modulatie_jaren), variabelen[7])
changedata(natuur(pinguins)[0], variabelen[1])
changedata(natuur(pinguins)[1], variabelen[2])


changedata2(biologisch_evenwicht()[0], biologisch_evenwicht()[1], variabelen[4])
changedata(boeddhisme(pinguins), variabelen[3])

run_server()



