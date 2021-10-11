import globals
from functions import *
from utils import *

def main():
    load_airport_data()
    load_aircraft_data()

    from_airport = pick("UK airport", globals.AIRPORTS_UK)

    selection = pick("Overseas Airport", list(globals.AIRPORTS_OVERSEAS.keys()))
    to_airport = globals.AIRPORTS_OVERSEAS[selection]

    print_airport(globals.AIRPORTS_OVERSEAS[selection])

    selection = pick("Aircraft", list(globals.AIRCRAFT.keys()))
    aircraft = globals.AIRCRAFT[selection]

    print_aircraft(globals.AIRCRAFT[selection])

    print(f"Travelling from {from_airport} to {to_airport[globals.OVERSEAS_AIRPORT_NAME]} on a {aircraft[globals.AIRCRAFT_TYPE]} aircraft")


if __name__ == '__main__':
    main()
