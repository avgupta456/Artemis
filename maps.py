import googlemaps

f = open("key.txt", "r")
key = f.readlines()[0]
gmaps = googlemaps.Client(key=key)

#rating parameters
[a, b] = [1, -0.5]

class Place:
    def __init__(self, location):
        self.update(location)

    def update(self, location):
        data = gmaps.places(location)
        self.lat = data['results'][0]['geometry']['location']['lat']
        self.lon = data['results'][0]['geometry']['location']['lng']
        self.address = data['results'][0]['formatted_address']
        self.name = data['results'][0]['name']
        self.rating = data['results'][0]['rating']
        self.reviews = data['results'][0]['user_ratings_total']
        self.types = data['results'][0]['types']

        self.rating = self.rating - a*(self.reviews)**b

    def print(self):
        print(self.name)
        print(self.address)
        print("("+str(self.lat)+", "+str(self.lon)+")")
        print(str(self.rating)+" ("+str(self.reviews)+")")
        print(self.types)


Yale = Place("Yale University")
Yale.print()
