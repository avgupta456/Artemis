import numpy as np
import mlrose

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


def find_route(matrix, locations, time_limit, f):
    bads = []

    best_value = -1
    best_order = []

    n = len(locations)
    for i in range(1, 2**(n-1)):
        if(i%10000==0): print(i)
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

            time, order = optimize2(posArr, getMat(iArr, matrix))

            if(time<time_limit):
                value = f(order)
                if(value>best_value):
                    best_value, best_order = value, order
                    print("New Best")
                    print(value)
                    print(iArr)
            else: bads.append(bin)

    return best_order

#the first element passed in posArr is the starting location
def optimize(posArr, matrix):
    n, time, order = len(posArr), 0, [posArr[-1]]
    for i in range(n-1):
        time += matrix[i][i+1]
        order.append(posArr[i])
    return time, order

def optimize2(posArr, matrix):
    n, time, order, dist = len(posArr), 0, [0], 0
    for i in range(0, n-1):
        min_dist, loc = 1e10, -1
        for j in range(n):
            if(len(set([j])&set(order))==0):
                dist = matrix[order[-1]][j]
                if(dist<min_dist): min_dist, loc = dist, j
        order.append(loc)
        time+= min_dist

    #print(order)

    time += matrix[order[0]][order[-1]]

    new_order = []
    for i in range(len(order)):
        new_order.append(posArr[order[i]])

    order = new_order
    return time, order

#the first element passed in posArr is the starting location
def metric_func(posArr):
    n, sum = len(posArr), 0
    for i in range(1, n):
        sum += posArr[i].rating
    return sum/n**(0.5)
