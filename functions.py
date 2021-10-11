import csv
import globals

def load_airport_data():

    # Load UK Airport Data into a global dictionary keyed by Airport Code - hardcoded!
    globals.AIRPORTS_UK = {"LPL": "Liverpool John Lennon", "BOH": "Bournemouth International"}

    # Load Overseas Airport data from csv file
    with open("Airports.csv", "r") as airports_file:

        reader = csv.DictReader(airports_file)

        # Store data in a global dictionary keyed by Airport Code
        for row in reader:
            globals.AIRPORTS_OVERSEAS[row.get(globals.OVERSEAS_AIRPORT_CODE)] = row

        print(f"{len(globals.AIRPORTS_OVERSEAS)} overseas airports loaded")
        print(f"{reader.fieldnames} attributes loaded for these overseas airports {list(globals.AIRPORTS_OVERSEAS.keys())}")

def print_airport(airport_dict):
    for k,v in airport_dict.items():
        print(f"{k}:\t{v}")

def load_aircraft_data():

    # Load Aircraft type data from csv file
    with open("Aircraft.csv", "r") as airports_file:

        reader = csv.DictReader(airports_file)

        # Store data in a global dictionary keyed by Aircraft Type
        for row in reader:
            globals.AIRCRAFT[row.get(globals.AIRCRAFT_TYPE)] = row

        print(f"{len(globals.AIRCRAFT)} rows loaded")
        print(f"{reader.fieldnames} attributes loaded for these aircraft types {list(globals.AIRCRAFT.keys())}")

def print_aircraft(aircaft_dict):
    for k,v in aircaft_dict.items():
        print(f"{k}:\t{v}")
