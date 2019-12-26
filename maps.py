import googlemaps
import distance as d

f = open("key.txt", "r")
KEY = f.readlines()[0]
gmaps = googlemaps.Client(key=KEY)

def getCity(city):
    data =gmaps.places(city)
    lat = data['results'][0]['geometry']['location']['lat']
    lon = data['results'][0]['geometry']['location']['lng']
    return [lat, lon]

def getData(location, city):
    data = gmaps.places(location, location=city)
    if(data['status']=='ZERO_RESULTS'): return False

    try:
        lat = data['results'][0]['geometry']['location']['lat']
        lon = data['results'][0]['geometry']['location']['lng']
        address = data['results'][0]['formatted_address']
        name = data['results'][0]['name']
        rating = data['results'][0]['rating']
        reviews = data['results'][0]['user_ratings_total']
        types = data['results'][0]['types']

        return [lat, lon, address, name, rating, reviews, types]

    except KeyError: return False

def solve(locations):
    start = [locations[0].lat, locations[0].lon]
    end = [locations[-1].lat, locations[-1].lon]

    waypoints = []
    for i in range(1, len(locations)-1):
        waypoint = [locations[i].lat, locations[i].lon]
        waypoints.append(waypoint)


    directions = gmaps.directions(origin=start,
                            destination=end,
                            mode="walking",
                            waypoints=waypoints,
                            avoid="ferries",
                            optimize_waypoints=True)

    order, distances, durations = [locations[0]], [], []
    waypoint_order = directions[0]['waypoint_order']
    for waypoint in waypoint_order: order.append(locations[waypoint+1])
    order.append(locations[-1])

    for i in range(len(directions[0]['legs'])):
        distances.append(directions[0]['legs'][i]['distance']['value'])
        durations.append(directions[0]['legs'][i]['duration']['value'])

    return order, distances, durations
