import places as p
import distance as d

import tsp
import maps

city = "Charlotte"
time_limit = 3600

places = p.getPlaces(city)
p.quickPrintPlaces(places)
#print(len(places))

matrix_approx = d.adjMatrixApprox(places)
#d.printMatrix(matrix_approx)

order = tsp.find_route(matrix_approx, places, time_limit, tsp.metric_func)
order, distances, durations = maps.solve(order)

for i in range(len(distances)):
    order[i].print()
    print("Walk " + str(distances[i]) + " feet for " + str(durations[i]) + " seconds to the next stop\n")

order[-1].print()
