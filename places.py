import google
import maps

def add_places(places, strs, city):
    unique = set([])
    for place in places:
        unique.add(place.address)

    city_coords = maps.getCity(city)
    for place in strs:
        temp = maps.Place(place, city_coords)
        if(temp.filled==True):
            if(not temp.address in unique):
                places.append(temp)
                unique.add(temp.address)

def print_places(places):
    for place in places:
        place.print()

city = "Cary"
places = []

strs = google.tripAdvisor(city)
add_places(places, strs, city)
#can add more sources here

print_places(places)
print(len(places))
