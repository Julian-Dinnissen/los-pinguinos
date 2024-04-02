import json


def edit_json(new_years: list, new_data: list) -> None:
    with open("./static/data.json", "r") as file:
        data = json.load(file)

    data["years"] = new_years
    data["populationData"] = new_data

    updated_json = json.dumps(data, indent=4)

    with open("./static/data.json", "w") as file:
        file.write(updated_json)

    print("data.json file has been successfully edited.")


new_years = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"]
new_population_data = [100, 120, 140, 160, 180, 200, 360]

edit_json(new_years, new_population_data)
