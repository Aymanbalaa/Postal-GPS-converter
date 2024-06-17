from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def gps_to_area_code(latitude, longitude):
    geolocator = Nominatim(user_agent="unique_application_identifier")

    try:
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        address = location.raw['address']
        postal_code = address.get('postcode', 'Postal code not found')
        return postal_code
    except GeocoderTimedOut:
        return "Geocoding service timed out"
    except Exception as e:
        return str(e)

longitude = -73.584219  
latitude = 	45.4829123
area_code = gps_to_area_code(latitude, longitude)
print(f"The area code for the given coordinates is: {area_code} ")
