import places as p
import distance as d
import tsp

city = "New York City"
time_limit = 7200
start_loc = False

places = p.getPlaces(city, start_loc)
p.quickPrintPlaces(places)
print(len(places))

matrix_approx = d.adjMatrixApprox(places)
d.printMatrix(matrix_approx)

order = tsp.find_route(matrix_approx, places, time_limit, tsp.metric_func, start_loc)

matrix_real = d.adjMatrixReal(order)
d.printMatrix(matrix_real)

for place in real_order:
    place.print()
