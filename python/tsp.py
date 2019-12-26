import numpy as np

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
    for i in range(1, 2**n):
        if(i%100000==0): print(i)

        bin = binary(i, n)

        cont = True
        for j in range(len(bads)):
            if(contains(bads[j], bin)):
                cont = False
                break

        if(cont):
            iArr, posArr = [], []

            for j in range(n):
                if(bin[j]=='1'): iArr.append(j)

            time, order = optimize2(getMat(iArr, matrix))
            for i in range(len(iArr)): posArr.append(locations[iArr[order[i]]])
            if(time<=time_limit and f(posArr)>best_value): best_value, best_order = f(posArr), posArr
            elif(time>time_limit): bads.append(bin)

    return best_order

def optimize(matrix):
    n, time, order = len(matrix[0]), 0, [0]
    for i in range(n-1):
        time += matrix[i][i+1]
        order.append(i+1)
    time += matrix[n-1][0]
    return time, order

def optimize2(matrix):
    n, max_dist, loc = len(matrix[0]), 0, -1
    for i in range(0, n-1):
        for j in range(i+1, n):
            if(matrix[i][j]>max_dist):
                max_dist, loc = matrix[i][j], i

    time, order, dist = 0, [loc], 0
    for i in range(0, n-1):
        min_dist, loc = 1e10, -1
        for j in range(n):
            if(not j in set(order)):
                dist = matrix[order[-1]][j]
                if(dist<min_dist): min_dist, loc = dist, j

        order.append(loc)
        time+= min_dist

    time += matrix[order[0]][order[-1]]
    return time, order

#rating parameters
[a, b] = [2e-3, 0.5]

def metric_func(posArr):
    n, sum = len(posArr), 0
    for i in range(0, n):
        sum += posArr[i].rating + a*(posArr[i].reviews)**b
    return sum/n**(0.5)

def metric_func_2(posArr):
    n, sum = len(posArr), 0
    for i in range(0, n): sum += posArr[i].reviews
    return sum
