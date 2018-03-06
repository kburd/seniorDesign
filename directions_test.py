import googlemaps
from direction_consts import API_KEY, TRAVEL_MODE
from datetime import datetime as dt
from pprint import pprint
from samGPSedits import check_serial, getLatLong
directions = googlemaps.directions
#Set the API-KEY
gmap = googlemaps.Client(key=API_KEY)

#destination_address=input('Enter Destination: ') #WORKS!!!


#39.680, -75.751  THIS IS THE LOCATION OF EVANS HALL


#the stuff below this is what elton has to work
now = dt.now()
#print(getLatLong())
starting_address = getLatLong()
#starting_address = '39.680,-75.751'
ending_address = "Morris Library Newark, DE"
directions_result = gmap.directions(starting_address,
                                    ending_address,
                                    mode=TRAVEL_MODE)
results_dict = directions_result[0]
steps = results_dict['legs'][0]['steps']
pprint(results_dict)
#print("\nsteps: ")
#print(steps)
