import googlemaps

f = open("key.txt", "r")
key = f.readlines()[0]
gmaps = googlemaps.Client(key=key)

#rating parameters
[a, b] = [1, -0.5]

class Place:
    filled = False
    def __init__(self, location, city):
        self.filled = self.update(location, city)

    def update(self, location, city):
        data = gmaps.places(location, open_now=True, location=city)
        if(data['status']=='ZERO_RESULTS'): return False

        try:
            self.lat = data['results'][0]['geometry']['location']['lat']
            self.lon = data['results'][0]['geometry']['location']['lng']
            self.address = data['results'][0]['formatted_address']
            self.name = data['results'][0]['name']
            self.rating = data['results'][0]['rating']
            self.reviews = data['results'][0]['user_ratings_total']
            self.types = data['results'][0]['types']

            if(self.reviews==0): self.rating = 3
            else: self.rating = self.rating - a*(self.reviews)**b

            return True
        except KeyError:
            return False

    def print(self):
        print(self.name)
        print(self.address)
        print("("+str(self.lat)+", "+str(self.lon)+")")
        print(str(self.rating)+" ("+str(self.reviews)+")")
        print(self.types)
        print()

def getCity(city):
    data =gmaps.places(city)
    lat = data['results'][0]['geometry']['location']['lat']
    lon = data['results'][0]['geometry']['location']['lng']
    return [lat, lon]

#Yale = Place("Yale University")
#Yale.print()
