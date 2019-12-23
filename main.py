import places as p
import distance as d

city = "New York City"
places = p.getPlacesQuick(city)
p.quickPrintPlaces(places)
print(len(places))

matrix_approx = d.adjMatrixApprox(places)
matrix_real = d.adjMatrixReal(places[0:min(10, len(places))])
d.printMatrix(matrix_approx)
d.printMatrix(matrix_real)
