import gmaps

#configure api
f = open("key2.txt", "r")
KEY = f.readlines()[0]
gmaps.configure(api_key=KEY)

#Define location 1 and 2
Durango = (37.2753,-107.880067)
SF = (37.7749,-122.419416)

#Create the map
fig = gmaps.figure()

#create the layer
layer = gmaps.directions.Directions(Durango, SF,mode='car')

#Add the layer
fig.add_layer(layer)
print(fig)
