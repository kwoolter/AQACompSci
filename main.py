import globals
from functions import *
from utils import *

def main():
    load_airport_data()
    load_aircraft_data()

    selection = pick("UK airport", list(globals.AIRPORTS_UK.keys()))
    from_airport = globals.AIRPORTS_UK[selection]

    selection = pick("Overseas Airport", list(globals.AIRPORTS_OVERSEAS.keys()))
    to_airport = globals.AIRPORTS_OVERSEAS[selection]

    print_airport(globals.AIRPORTS_OVERSEAS[selection])

    selection = pick("Aircraft", list(globals.AIRCRAFT.keys()))
    aircraft = globals.AIRCRAFT[selection]

    print_aircraft(globals.AIRCRAFT[selection])

    print(f"\n\nTravelling from {from_airport} to {to_airport[globals.OVERSEAS_AIRPORT_NAME]} on a {aircraft[globals.AIRCRAFT_TYPE]} aircraft")


if __name__ == '__main__':
    main()
