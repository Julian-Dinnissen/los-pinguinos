import json

modulatie_jaren: int = 10  # het aantal jaren dat we moduleren

variabelen: list = [
    "Totale pinguins",
    "Geboren",
    "Gestorven",
    "Bekeerde",
    "Beschikbaar voedsel",
    "Vervuild water",
    "Leefoppervlakte",
    "Gestolen pinguins",
    "Verdwaalde pinguins",
    "Tot coma gezopen pinguins",
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


def changedata(jaren: list, aantal: list, variabel: str) -> None:
    # Load the JSON data
    with open("./static/data.json", "r") as file:
        data = json.load(file)

    data[variabel]["years"] = jaren
    data[variabel]["data"] = aantal

    with open("./static/data.json", "w") as file:
        json.dump(
            data, file, indent=4
        )  # indent for pretty printing, you can remove it if you prefer compact JSON


def diefstal(aantaljaar) -> tuple:
    aantaljaar = aantaljaar + 1
    gestolen = []
    gestolen_pinguins = 0
    jaren = [str(i + 2020) for i in range(aantaljaar)]
    for i in range(aantaljaar):
        gestolen.append(gestolen_pinguins)
        gestolen_pinguins += 3

    return jaren, gestolen


def verdwaald(aantaljaar) -> tuple:
    aantaljaar = aantaljaar + 1
    verdwaald = []
    verdwaalde_pinguins = 0
    jaren = [str(i + 2020) for i in range(aantaljaar)]
    for i in range(aantaljaar):
        verdwaald.append(verdwaalde_pinguins)
        verdwaalde_pinguins += 78

    return jaren, verdwaald


changedata(diefstal(modulatie_jaren)[0], diefstal(modulatie_jaren)[1], variabelen[7])
changedata(verdwaald(modulatie_jaren)[0], verdwaald(modulatie_jaren)[1], variabelen[8])
