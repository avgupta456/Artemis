import google
import maps

places = google.tripAdvisor("New York City")
for place in places:
    temp = maps.Place(place)
    temp.print()
