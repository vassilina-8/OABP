from math import *
import matplotlib.pyplot as plt

N = 10000
dt = 1.3301
t = 0.01
T = [[cos(dt * i + t), sin(dt * i + t)] for i in range(1, N + 2)]

def metrics(x_i, x_j, m):
    sum = 0
    for k in range(m):
        sum += (abs(x_i[k][0] - x_j[k][0]) + abs(x_i[k][1] - x_j[k][1]))/m
    return sum

def neighbors(x_i, i, m):
    min_ind, min_val = N + 1, N + 1
    for j in range(i + 1, N - m):
        x_j = T[j : j + m]
        d = metrics(x_i, x_j, m)
        if (d < min_val):
            min_ind = j
            min_val = d
    return min_ind, min_val

m = 1
points = {}
while m < 15:
    val = 0
    for i in range(N - m - 1):
        x_i = T[i : i + m]
        j, delta = neighbors(x_i, i, m)
        x_j = T[j : j + m]
        x_i_next = T[i : i + m + 1]
        x_j_next = T[j : j + m + 1]
        d = metrics(x_i, x_j, m)
        d_next = metrics(x_i_next, x_j_next, m + 1)
        if (d_next/d) > (m/(m + 1))*delta:
            val += 1
    points[m] = val
    print(points[m])
    m += 1

x, y = zip(*list(points.items()))
plt.plot(x, y)
plt.show()




















