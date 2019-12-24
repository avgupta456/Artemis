import numpy as np
import googlemaps
import datetime
import tsp

KEY_file = open('key2.txt', 'r')
KEY=KEY_file.readlines()[0]

def getDistance(lat1, lon1, lat2, lon2):
    dist = ((lat1-lat2)**2+(lon1-lon2)**2)**0.5
    return dist*69/3*3600 #conversion form lat/lon to miles to hours to seconds

def adjMatrixApprox(places):
    n = len(places)
    matrix = np.zeros(shape=(n, n), dtype='double')

    for i in range(0,n):
        for j in range(0,n):
            if(i==j): matrix[i][j] = 0
            elif(i>j): matrix[i][j] = matrix[j][i]
            else: matrix[i][j] = int(getDistance(places[i].lat, places[i].lon, places[j].lat, places[j].lon))

    return matrix

def adjMatrixReal(places):
    n = len(places)
    matrix = np.ndarray(dtype="double", shape=(n,n))
    now=datetime.datetime.now()

    coords = np.zeros(shape=(n,2), dtype='double')
    for i in range(n):
        coords[i]= [places[i].lat, places[i].lon]

    gmaps = googlemaps.Client(key=KEY)
    gmaps_matrix = gmaps.distance_matrix(coords, coords,
                        mode="walking",
                        avoid="ferries",
                        departure_time=now)

    for i in range(0,n):
        for j in range(0,n):
            if(i==j): matrix[i][j] = 0
            else: matrix[i][j] = gmaps_matrix['rows'][i]['elements'][j]['duration']['value']

    return matrix

def printMatrix(matrix):
    n = matrix.shape[0]
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=" ")
        print()
    print()
