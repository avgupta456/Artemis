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
                    print(place)

    return places

def printPlaces(places):
    for place in places:
        place.print()

def sortPlaces(places):
    places.sort(key=lambda x: x.rating, reverse=True)

city = "New York City"
strs = google.tripAdvisor(city)
places = addPlaces(strs, city)

sortPlaces(places)
printPlaces(places)
print(len(places))
