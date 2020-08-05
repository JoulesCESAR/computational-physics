# Bisection.py    Find zero via Bisection algorithm
# This script is working only with a half of interval

from numpy import *

def f(x):
	return 2*cos(x) - x

def bisection(xminus, xplus, Nmax, eps):
	for it in range(0,Nmax):
		x = (xplus + xminus)/2.0        # Mid point
		print("iteration",it,"x=",x,"f(x)=",f(x))
		if( f(xplus)*f(x)>0.0):    #Root on the other half
			xplus = x              # change x+ to x 
		else:
			xminus = x              # change x- to x
		if( abs(f(x)) < eps):        # converge??
			print("\n Root found with precision eps= ", eps)
			break
		if it  == Nmax -1:
		    print("\n Root NOT found after Nmax iterations\n")
	return x

eps = 1e-8
a = 0.0; b = 7.0  # Root in [a,b]
imax = 10000        # Max no. iterations
root = bisection(a,b, imax, eps)
print("  Root =", root )

