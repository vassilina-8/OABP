from math import sqrt

print('Choose one of the types: 1 - ellipse, 2 - hyperbola, 3 - parabola')
t = int(input())

if t == 1:
	print('Enter x and y coordinates for two points')
	x1, y1 = map(float, input().split())
	x2, y2 = map(float, input().split())
	a1 = (x1**2) * (y2**2) - (x2**2) * (y1**2)
	a2 = x1**2 - x2**2
	if (a2 != 0) and (a1 >= 0):
		b = a1 / a2
		b1 = b - y1**2
		if (b1 != 0):
			a = sqrt(b * (x1**2) / b1)
			print('a = ', a, 'b = ', sqrt(b))
elif t == 2:
	print('Enter x and y coordinates for two points')
	x1, y1 = map(float, input().split())
	x2, y2 = map(float, input().split())
	a1 = (x1**2) * (y2**2) - (x2**2) * (y1**2)
	if (x1 != 0 or x2 != 0) and (a1 >= 0):
		b = a1 / (x1**2 + x2**2)
		if (y1 != 0 or b != 0):
			a = sqrt(b * (x1**2) / (b + (y1**2)))
			print('a = ', a, 'b = ', sqrt(b))
elif t == 3:
	print('Enter x and y coordinates for one point')
	x1, y1 = map(float, input().split())
	if (x1 != 0):
		p = y1**2 / (2*x1)
		print('p = ', p)





















