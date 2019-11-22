import google
import maps

def add_places(places, strs, city):
    city_coords = maps.getCity(city)
    for place in strs:
        temp = maps.Place(place, city_coords)
        if(temp.filled==True): places.append(temp)

def check_duplicates(places):
    unique = set([])
    new_places = []
    for place in places:
        if(not place.address in unique):
            unique.add(place.address)
            new_places.append(place)
    return new_places

def print_places(places):
    for place in places:
        place.print()

city = "Cary"
places = []

strs = google.tripAdvisor(city)
add_places(places, strs, city)

#can add more sources here

check_duplicates(places)
print_places(places)
print(len(places))
