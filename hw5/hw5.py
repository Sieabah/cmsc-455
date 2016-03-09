import math
import random
import sys

# define any function here!
def f(x):
    return math.exp(-x**2/2)/math.sqrt(2*math.pi)

def integrate(iters):
	# define any xmin-xmax interval here! (xmin < xmax)
	xmin = -3
	xmax = 3

	# find ymin-ymax
	ymin = f(xmin)
	ymax = ymin
	for i in xrange(iters):
		x = xmin + (xmax - xmin) * float(i) / iters
		y = f(x)
		if y < ymin:
			ymin = y
		if y > ymax:
			ymax = y

	# Monte Carlo
	a = (xmax - xmin) * (ymax - ymin)
	ctr = 0
	for j in xrange(iters):
		x = xmin + (xmax - xmin) * random.random()
		y = ymin + (ymax - ymin) * random.random()
		if math.fabs(y) <= math.fabs(f(x)):
			if f(x) > 0 and y > 0 and y <= f(x):
				ctr += 1 # area over x-axis is positive
			if f(x) < 0 and y < 0 and y >= f(x):
				ctr -= 1 # area under x-axis is negative

	return a * float(ctr) / iters

def main():
	for i in xrange(int(sys.argv[1])):
		if i > 0:
			val = integrate(i)
			print i, val, val-0.9973, (val-0.9973)*100

main()