import urllib
from utils import simplejson, geocoder_factory

# https://developers.google.com/maps/documentation/geocoding/

#update:google apply no policy in using geocoding api, including 'https' instead of 'http',2500 requests/day.
#you can apply google api key in website https://console.developers.google.com after  creating project, then turn on the service "Geocoding API" and create new key for browser application in "Credentials".
#you can then test your google api key in browser like this:https://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=new york&key=AIzaSyCTiFJreqzvYieWdH555m--bVnO70qeJ4E

def geocode(q, api_key=None):
    json = simplejson.load(urllib.urlopen(
        'https://maps.googleapis.com/maps/api/geocode/json?' + urllib.urlencode({
            'address': q,
            'key':api_key,
            'sensor': 'false',
        })
    ))
    try:
        lon = json['results'][0]['geometry']['location']['lng']
        lat = json['results'][0]['geometry']['location']['lat']
    except (KeyError, IndexError):
        return None, (None, None)
    name = json['results'][0]['formatted_address']
    return name, (lat, lon)

geocoder = geocoder_factory(geocode)
