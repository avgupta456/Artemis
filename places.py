import google
import maps

def addPlaces(strs, city):
    names = set([])
    places = []

    city_coords = maps.getCity(city)

    for place in strs:
        if place != "":
            temp = maps.Place(place, city_coords)
            if(temp.filled==True):
                if(not temp.address in names and temp.isBad()==False):
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

def getPlaces(city):
    strs = google.tripAdvisor(city)
    places = addPlaces(strs, city)
    sortPlaces_reviews(places)
    return __getPlaces__(places)

def getPlacesQuick(city):
    strs = google.tripAdvisorQuick(city)
    places = addPlaces(strs, city)
    sortPlaces_reviews(places)
    return __getPlaces__(places)

def __getPlaces__(places):
    [parks, parks_max] = [0, 3]

    new_places = []
    for place in places:
        if(place.isPark() and parks<parks_max):
            new_places.append(place)
            parks+=1

        elif(not place.isPark()):
            new_places.append(place)

    places = new_places[:min(20,len(new_places))]
    sortPlaces_rating(places)
    return places
