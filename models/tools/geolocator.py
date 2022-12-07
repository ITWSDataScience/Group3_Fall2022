#code from https://www.geeksforgeeks.org/get-the-city-state-and-country-names-from-latitude-and-longitude-using-python/
from geopy.geocoders import Nominatim

def latlong_to_country(location):
    return location.get('country', '')


def get_lat_long_info(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")

    location = geolocator.reverse(latitude+","+longitude)

    return location.raw['address']

