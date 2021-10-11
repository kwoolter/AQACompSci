import globals
from functions import *
from utils import *

def main():

    # Load in the airport and aircraft data
    load_airport_data()
    load_aircraft_data()

    # Pick the UK airport that you want to travel from
    selection = pick("UK Airport", list(globals.AIRPORTS_UK.keys()))
    from_airport = globals.AIRPORTS_UK[selection]
    print(f"Travelling from {from_airport}.")

    # Pick the overseas Airport that you want to travel to
    selection = pick("Overseas Airport", list(globals.AIRPORTS_OVERSEAS.keys()))
    to_airport = globals.AIRPORTS_OVERSEAS[selection]
    print(f"Travelling to {to_airport[globals.OVERSEAS_AIRPORT_NAME]}.")

    # Pick the type of Aircraft that will make teh flight
    selection = pick("Aircraft Type", list(globals.AIRCRAFT.keys()))
    aircraft = globals.AIRCRAFT[selection]

    print(f"\n\nTravelling from {from_airport} to {to_airport[globals.OVERSEAS_AIRPORT_NAME]} on a {aircraft[globals.AIRCRAFT_TYPE]} aircraft...")


if __name__ == '__main__':
    main()
