import google
import maps

city = "Cary"
strs = google.tripAdvisor(city)
places = []

for place in strs:
    city_coords = maps.getCity(city)
    temp = maps.Place(place, city_coords)
    if(temp.filled==True): places.append(temp)

for place in places:
    place.print()
