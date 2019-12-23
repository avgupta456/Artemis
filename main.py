import places as p
import distance as d

city = "Raleigh"
list = p.getPlacesQuick(city)
p.quickPrintPlaces(list)
print(len(list))

matrix = d.adjMatrix(list)
d.printMatrix(matrix)
