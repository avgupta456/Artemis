import googlemaps
import distance as d

f = open("key2.txt", "r")
KEY = f.readlines()[0]
gmaps = googlemaps.Client(key=KEY)

#rating parameters
[a, b] = [1, -0.5]

bad = ['atm', 'bar', 'beauty_salon', 'bicycle_store', 'bus_station',
    'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'dentist',
    'doctor', 'drugstore', 'electrician', 'electronics_store',
    'funeral_home', 'gas_station', 'hair_care', 'hardware_store',
    'insurance_agency', 'laundry', 'liquor_store', 'locksmith',
    'lodging', 'meal_delivery', 'meal_takeaway', 'movie_rental',
    'moving_company', 'night_club', 'painter', 'pharmacy',
    'physiotherapist', 'plumber', 'post_office', 'real_estate_agency',
    'restaurant', 'roofing_contractor', 'rv_park', 'shoe_store', 'storage',
    'taxi_stand', 'transit_station', 'veterinary_care']

park = ['park']

restaurant = ['restaurant']
#restaurant = ['restaurant', 'meal_delivery', 'meal_takeaway']

class Place:
    filled = False

    def __init__(self, start, location, city):
        if(start):
            self.lat = location[0]
            self.lon = location[1]
            self.address = "Start Address"
            self.name = "Start"
            self.rating = 5
            self.reviews = 0
            self.types = []
            self.filled = False

        else:
            self.city_coords = city
            self.filled = self.update(location, city)

    def update(self, location, city):
        data = gmaps.places(location, location=city)
        if(data['status']=='ZERO_RESULTS'): return False

        try:
            self.lat = data['results'][0]['geometry']['location']['lat']
            self.lon = data['results'][0]['geometry']['location']['lng']
            self.address = data['results'][0]['formatted_address']
            self.name = data['results'][0]['name']
            self.rating = data['results'][0]['rating']
            self.reviews = data['results'][0]['user_ratings_total']
            self.types = data['results'][0]['types']

            if(self.reviews<100): return False
            else: self.rating = self.rating - a*(self.reviews)**b

            if(self.rating<4.0): return False

            return True

        except KeyError: return False

    def print(self):
        print(self.name)
        print(self.address)
        print("("+str(self.lat)+", "+str(self.lon)+")")
        print(str(self.rating)+" ("+str(self.reviews)+")")
        print(self.types)
        print()

    def quickPrint(self):
        print(str(self.name) + " - " + str(self.rating) + " (" + str(self.reviews) + ")")

    def isBad(self):
        if(d.getDistance(self.city_coords[0], self.city_coords[1], self.lat, self.lon)>72000): return True
        return len(list(set(bad) & set(self.types)))>0

    def isPark(self):
        return len(list(set(park) & set(self.types)))>0

    def isRestaurant(self):
        return len(list(set(restaurant) & set(self.types)))>0 and len(self.types)<=3

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
