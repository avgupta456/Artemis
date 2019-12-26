import google

import distance as d
import maps

bad = ['atm', 'bar', 'beauty_salon', 'bicycle_store', 'bus_station',
    'car_dealer', 'car_rental', 'car_repair', 'car_wash', 'dentist',
    'doctor', 'drugstore', 'electrician', 'funeral_home', 'gas_station',
    'hair_care', 'insurance_agency', 'laundry', 'liquor_store', 'locksmith',
    'lodging', 'movie_rental', 'moving_company', 'night_club', 'painter',
    'pharmacy', 'physiotherapist', 'plumber', 'post_office',
    'real_estate_agency', 'roofing_contractor', 'rv_park', 'storage',
    'taxi_stand', 'veterinary_care']

park = ['park']

restaurant = ['meal_delivery', 'meal_takeaway', 'restaurant']

class Place:
    filled = False

    def __init__(self, start, location, city):
        self.city_coords = city
        self.filled = self.update(location, city)

    def update(self, location, city):
        data = maps.getData(location, city)
        if(data==False): return False
        self.lat, self.lon, self.address, self.name, self.rating, self.reviews, self.types = data
        return True

    def print(self):
        print(self.name)
        print(self.address)
        print("("+str(self.lat)+", "+str(self.lon)+")")
        print(str(self.rating)+" ("+str(self.reviews)+")")
        print(self.types)
        print()

    def quickPrint(self):
        print(str(self.name) + " - " + str(self.rating)[:4] + " (" + str(self.reviews) + ")")

    def isBad(self):
        if(d.getDistance(self.city_coords[0], self.city_coords[1], self.lat, self.lon)>72000): return True
        if(self.rating<3 or self.reviews<25): return True
        return len(list(set(bad) & set(self.types)))>0

    def isPark(self):
        return len(list(set(park) & set(self.types)))>0

    def isRestaurant(self):
        return len(list(set(restaurant) & set(self.types)))>0

def addPlaces(strs, city):
    names = set([])
    places = []

    city_coords = maps.getCity(city)

    for place in strs:
        if place != "":
            temp = Place(False, place, city_coords)
            if(temp.filled==True):
                if(len(set([temp.address])&names)==0 and temp.isBad()==False):
                    places.append(temp)
                    names.add(temp.address)

    return places

def printPlaces(places):
    for place in places:
        place.print()

def quickPrintPlaces(places):
    for place in places:
        place.quickPrint()

def sortPlaces_reviews(places):
    places.sort(key=lambda x: x.reviews, reverse=True)

def sortPlaces_rating(places):
    places.sort(key=lambda x: x.rating, reverse=True)

def getPlaces(city, start=True):
    strs = google.tripAdvisor(city)
    places = addPlaces(strs, city)
    sortPlaces_reviews(places)
    return __cleanPlaces__(places, city, start)

def getPlacesQuick(city, start=True):
    strs = google.tripAdvisorQuick(city)
    places = addPlaces(strs, city)
    sortPlaces_reviews(places)
    return __cleanPlaces__(places, city, start)

def __cleanPlaces__(places, city, start):
    [parks, parks_max] = [0, 3]
    [rests, rests_max] = [0, 3]

    locs = []
    new_places = []

    for place in places:

        cont = True
        for loc in locs:
            if(d.getDistance(loc[0], loc[1], place.lat, place.lon)<120):
                cont = False
                break

        if(cont):
            if(place.isPark() and parks<parks_max):
                new_places.append(place)
                locs.append([place.lat, place.lon])
                parks+=1

            elif(place.isRestaurant() and rests<rests_max):
                new_places.append(place)
                locs.append([place.lat, place.lon])
                rests+=1

            elif(not place.isPark() and not place.isRestaurant()):
                new_places.append(place)
                locs.append([place.lat, place.lon])

    print("Acceptable Locations: " + str(len(new_places)))
    print()

    places = new_places[:min(20,len(new_places))]
    sortPlaces_rating(places)
    return places
