import places as p
import distance as d
import tsp

city = "New York City"
time_limit = 7200
start_loc = True

places = p.getPlaces(city, start_loc)
p.quickPrintPlaces(places)
print(len(places))

matrix_approx = d.adjMatrixApprox(places)
#matrix_real = d.adjMatrixReal(places[0:min(10, len(places))])
#d.printMatrix(matrix_approx)
#d.printMatrix(matrix_real)

order = tsp.find_route(matrix_approx, places, time_limit, tsp.metric_func, start_loc)
for place in order:
    place.print()
