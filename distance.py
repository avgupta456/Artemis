import numpy as np

def getDistance(lat1, lon1, lat2, lon2):
    dist = ((lat1-lat2)**2+(lon1-lon2)**2)**0.5
    return dist*69/3*3600 #conversion form lat/lon to miles to hours to seconds

def adjMatrix(places):
    n = len(places)
    matrix = np.zeros(shape=(n, n), dtype='double')

    for i in range(0,n):
        for j in range(0,n):
            if(i==j): matrix[i][j] = 0
            elif(i>j): matrix[i][j] = matrix[j][i]
            else: matrix[i][j] = getDistance(places[i].lat, places[i].lon, places[j].lat, places[j].lon)

    return matrix

def printMatrix(matrix):
    n = matrix.shape[0]
    for i in range(0, n):
        for j in range(0, n):
            print(matrix[i][j], end=" ")
        print()
    print()
