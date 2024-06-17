from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def load_postal_codes(filename):
    """Load postal codes and their corresponding area names from a text file."""
    postal_code_map = {}
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                postal_code_map[parts[0].strip()] = parts[1].strip()
    return postal_code_map

def get_area_name(postal_code, postal_code_map):
    """Get the area name from the first three letters of a postal code."""
    first_three = postal_code[:3]
    return postal_code_map.get(first_three, "Area name not found")

def gps_to_area_code(latitude, longitude):
    geolocator = Nominatim(user_agent="unique_application_identifier")

    try:
      
        location = geolocator.reverse((latitude, longitude), exactly_one=True)
        address = location.raw['address']
        postal_code = address.get('postcode', 'Postal code not found')

        return postal_code
    except GeocoderTimedOut:
        return "Geocoding service timed out", "", "", "", ""
    except Exception as e:
        return str(e), "", "", "", ""

postal_code_map = load_postal_codes('postal_codes.txt')
longitude = -73.64952850446572
latitude = 45.48225659061988
postal_code = gps_to_area_code(latitude, longitude)
area_name = get_area_name(postal_code, postal_code_map)


print(f"The postal code for the given coordinates is: {postal_code}")
print(f"The area name for it is: {area_name}")


