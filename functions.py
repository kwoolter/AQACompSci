import csv
import globals


def load_airport_data():

    with open("Airports.csv", "r") as airports_file:

        reader = csv.DictReader(airports_file)
        for row in reader:
            globals.AIRPORTS_OVERSEAS[row.get(globals.OVERSEAS_AIRPORT_CODE)] = row

        print(f"{len(globals.AIRPORTS_OVERSEAS)} rows loaded")
        print(f"{reader.fieldnames} information loaded for these airports {globals.AIRPORTS_OVERSEAS.keys()}")

def print_airport(airport_dict):
    for k,v in airport_dict.items():
        print(f"{k}:\t{v}")

def load_aircraft_data():

    with open("Aircraft.csv", "r") as airports_file:

        reader = csv.DictReader(airports_file)
        for row in reader:
            globals.AIRCRAFT[row.get(globals.AIRCRAFT_TYPE)] = row

        print(f"{len(globals.AIRCRAFT)} rows loaded")
        print(f"{reader.fieldnames} information loaded for these aircraft types {globals.AIRCRAFT.keys()}")

def print_aircraft(aircaft_dict):
    for k,v in aircaft_dict.items():
        print(f"{k}:\t{v}")
