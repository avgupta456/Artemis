import google
import maps

city = "Cary"
strs = google.tripAdvisor(city)
places = []

for place in strs:
    city_coords = maps.getCity(city)
    temp = maps.Place(place, city_coords)
    if(temp.filled==True): places.append(temp)

print(len(places))
unique = set([])
new_places = []
for place in places:
    if(not place.address in unique):
        unique.add(place.address)
        new_places.append(place)
places = new_places
print(len(places))

#for place in places:
#    place.print()
