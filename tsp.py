import numpy
import mlrose

#the first element passed in posArr is the starting location
def optimize(posArr, matrix):
    n, time, order = len(posArr), 0, []
    for i in range(n-1):
        time += matrix[i][i+1]
        order.append(posArr[i])
    order.append(posArr[-1])
    return time, order

#the first element passed in posArr is the starting location
def metric_func(posArr):
    n, sum = len(posArr), 0
    for i in range(1, n):
        sum += posArr[i].rating
    return sum/n**(0.5)
