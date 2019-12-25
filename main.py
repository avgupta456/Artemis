import places as p
import distance as d

import tsp
import maps

city = "New York City"
time_limit = 7200

places = p.getPlacesQuick(city)
p.quickPrintPlaces(places)
print(len(places))

matrix_approx = d.adjMatrixApprox(places)
d.printMatrix(matrix_approx)

order = tsp.find_route(matrix_approx, places, time_limit, tsp.metric_func)
for place in order: place.print()

matrix_real = d.adjMatrixReal(order)
d.printMatrix(matrix_real)

#maps.solve(order)
