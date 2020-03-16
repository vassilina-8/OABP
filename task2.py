from math import *

def temp_dist(x1, y1, x2, y2):
	return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def p_k(k, n1, n2):
	ans = 0
	for i in range(1, k+1):
		ind_mas1 = n1 - k - i
		ind_mas2 = n2 - k - i
		if (ind_mas1 < 0) or (ind_mas2 < 0):
			break
		ans += temp_dist(x[ind_mas1], y[ind_mas1], x[ind_mas2], y[ind_mas2])**2
	return sqrt(ans)

def teta(z):
	if z < 0:
		return 0
	else:
		return 1

def c_k_l(k, l):
	sum_ans = 0
	for i in range(1, N+1):
		for j in range(1, N+1):
			sum_ans += teta(l - p_k(k, i, j))
	return sum_ans / (N**2)

t = 100
N = 1000
a, b = 2, 1
k = 10
step = 3
x = [a * cos(j/t) for j in range(N * t + 1)]
y = [b * sin(j/t) for j in range(N * t + 1)]

prev = log(c_k_l(k, 0.75)) / log(0.75)
print(prev)
cur = log(c_k_l(k, 0.5)) / log(0.5)
print(cur)
l = 1.0
while (l > 0.001) and (abs(prev - cur) > 0.05):
	prev = cur
	l = 1.0 / step
	cur = log(c_k_l(k, l)) / log(l)
	print(cur)
	step *= 2
