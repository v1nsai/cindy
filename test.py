import googlemaps
from datetime import datetime
import keys
import json
import pandas as pd

gmaps = googlemaps.Client(key=keys.api_key)

nearby = gmaps.places_nearby(location="38.968291, -77.357840", radius=1000)

with open('nearby.json', 'w') as file:
    file.write(json.dumps(nearby))


print()