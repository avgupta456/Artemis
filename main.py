import google
import maps

strs = google.tripAdvisor("New York City")
places = []

for place in strs:
    temp = maps.Place(place)
    if(temp.filled==True): places.append(temp)

for place in places:
    place.print()
