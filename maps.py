import googlemaps
import distance as d

f = open("key2.txt", "r")
KEY = f.readlines()[0]
gmaps = googlemaps.Client(key=KEY)

def getCity(city):
    data =gmaps.places(city)
    lat = data['results'][0]['geometry']['location']['lat']
    lon = data['results'][0]['geometry']['location']['lng']
    return [lat, lon]

def get_sp(place):
    if place == 'current':
        g = geocoder.ip('me')
        return [g.latlng[0], g.latlng[1]]
    else:
        gmaps = googlemaps.Client(key=KEY)
        geocode_result = gmaps.geocode(place)
        lat = geocode_result[0]['geometry']['location']['lat']
        lon = geocode_result[0]['geometry']['location']['lng']
        return [lat, lon]

#rating parameters
[a, b] = [2e-3, 0.5]

def getData(location, city):
    data = gmaps.places(location, location=city)
    if(data['status']=='ZERO_RESULTS'): return False

    try:
        lat = data['results'][0]['geometry']['location']['lat']
        lon = data['results'][0]['geometry']['location']['lng']
        address = data['results'][0]['formatted_address']
        name = data['results'][0]['name']
        rating = data['results'][0]['rating']
        reviews = data['results'][0]['user_ratings_total']
        types = data['results'][0]['types']

        rating = rating + a*(reviews)**b
        return [lat, lon, address, name, rating, reviews, types]

    except KeyError: return False
