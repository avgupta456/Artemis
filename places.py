import google

import distance as d
import maps

def addPlaces(strs, city):
    names = set([])
    places = []

    city_coords = maps.getCity(city)

    for place in strs:
        if place != "":
            temp = maps.Place(False, place, city_coords)
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
        print(locs)
        cont = True
        for loc in locs:
            #print(d.getDistance(loc[0], loc[1], place.lat, place.lon))
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

    places = new_places[:min(20,len(new_places))]
    sortPlaces_rating(places)

    if(not start): return places
    new_places = [maps.Place(True, maps.get_sp(city),0)]
    for place in places: new_places.append(place)
    return new_places
