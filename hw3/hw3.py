"""
Christopher S. Sidell
CMSC 455 - HW3 - Tyler Simon

This homework demonstrates the difference between two types of integration
"""


import math

exact = 1-math.cos(1.0)
granularity = [16, 32, 64, 128]

def trapezoidal():
    for gran in granularity:
        print "Points: ", gran
        for n in range(1,gran):
            h = 1.0/n

            esum = 0
            for i in range(1,n-1):
                esum += i*h

            value = h * ((math.sin(0)+math.sin(1.0))/2 + esum)

            print "\t",value, value-exact

gaulGranularity = [8,16]
#http://www.csee.umbc.edu/portal/help/python/gauleg.py
def gaulegf(a, b, n):
    x = list(range(n+1)) # x[0] unused
    w = list(range(n+1)) # w[0] unused
    eps = 3.0E-14
    m = (n+1)/2
    xm = 0.5*(b+a)
    xl = 0.5*(b-a)
    for i in range(1,int(m)+1):
        z = math.cos(3.141592654*(i-0.25)/(n+0.5))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1,n+1):
                p3 = p2
                p2 = p1
                p1 = ((2.0*j-1.0)*z*p2-(j-1.0)*p3)/j

            pp = n*(z*p1-p2)/(z*z-1.0)
            z1 = z
            z = z1 - p1/pp
            if abs(z-z1) <= eps:
                break

        x[i] = xm - xl*z
        x[n+1-i] = xm + xl*z
        w[i] = 2.0*xl/((1.0-z*z)*pp*pp)
        w[n+1-i] = w[i]

    return x, w

def gaulegfInt():
    for gran in gaulGranularity:
        print "Points: ", gran
        x, w = gaulegf(0.0, 1.0, gran)

        value = 0
        for i in range(gran):
            value += w[i] * math.sin(x[i])

            print "\t",value, value-exact


def main():
    print "Trapezoidal"
    trapezoidal()
    print "Gauss Legendre"
    gaulegfInt()


main()
