#This can only be run if you have matplotlib, GL doesn't have it
##Please don't take off because GL doesn't have it
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pylab

f = open('stuff.dat')

x = []
y = []
for line in f:
	line = line.strip("\n").split(' ')
	x.append(line[0])
	y.append(line[2])

plt.plot(x,y)
plt.savefig('output.png')