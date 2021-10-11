from functions import *
from utils import *

def main():

    # Load in the airport and aircraft data
    load_airport_data()
    load_aircraft_data()

    # Pick the UK airport that you want to travel from
    from_airport_code = pick("UK Airport", list(globals.AIRPORTS_UK.keys()))
    from_airport_name = globals.AIRPORTS_UK[from_airport_code]
    print(f"Travelling from {from_airport_name}.")

    # Pick the overseas Airport that you want to travel to
    to_airport_code = pick("Overseas Airport", list(globals.AIRPORTS_OVERSEAS.keys()))
    to_airport = globals.AIRPORTS_OVERSEAS[to_airport_code]
    print(f"Travelling to {to_airport[globals.OVERSEAS_AIRPORT_NAME]}.")

    # Pick the type of Aircraft that will make the flight
    selection = pick("Aircraft Type", list(globals.AIRCRAFT.keys()))
    aircraft = globals.AIRCRAFT[selection]

    # Summarise selections
    print(f"\n\nTravelling from {from_airport_name} ({from_airport_code}) "
          f"to {to_airport[globals.OVERSEAS_AIRPORT_NAME]} ({to_airport_code}) "
          f"on a {aircraft[globals.AIRCRAFT_TYPE]} aircraft...")


if __name__ == '__main__':
    main()
