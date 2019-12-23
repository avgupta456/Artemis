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

def getMat(iArr, matrix):
    n = len(iArr)
    new_mat = np.ndarray(dtype="double", shape=(n,n))
    for i in range(n):
        for j in range(n):
            new_mat[i][j] = matrix[iArr[i]][iArr[j]]

    return new_mat

def binary(n, digits):
    binary = str("{0:b}".format(n))
    return (digits-len(binary))*"0"+binary

def contains(a, b):
    for i in range(len(a)):
        if(a[i]=='1' and b[i]=='0'): return False
    return True


def find_route(matrix, locations, time_limit, metric_func):
    bads = []

    best_value = -1
    best_order = []

    n = len(locations)
    for i in range(1, 2**(n-1)):
        if(i%1000==0): print(i)
        bin = "1"+binary(i, n-1)

        cont = True
        for j in range(len(bads)):
            if(contains(bads[j], bin)):
                cont = False
                break

        if(cont):
            iArr, posArr = [], []
            for j in range(n):
                if(bin[j]=='1'):
                    iArr.append(j)
                    posArr.append(locations[j])

            time, order = tsp.optimize(posArr, getMat(iArr, matrix))

            if(time<time_limit):
                value = metric_func(order)
                if(value>best_value):
                    best_value, best_order = value, order
                    print("New Best")
                    print(value)
                    print(iArr)
            else: bads.append(bin)

    return best_order

def printMatrix(matrix):
    n = matrix.shape[0]
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=" ")
        print()
    print()
