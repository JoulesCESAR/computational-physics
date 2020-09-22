# Script of derivate computation several h's
# five point method
import numpy as np
import matplotlib.pyplot as plt

def dfdx(f,x,h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h))/(2*h)

n = 200
x = np.linspace(0, np.pi /50, n + 1)
h1 = (np.pi /50 )/ n
epsilon = 5e-324
ho = np.sqrt( (4*epsilon*100)/(10000))


def sin100x(x):
    return np.sin(100*x)

dydx_1 = dfdx(sin100x,x,h1)
dydx_2 = dfdx(sin100x,x,ho)

dYdx = 100*np.cos(100*x)

#plt.figure(figsize=(12,5))
plt.plot(x,dydx_1,'.',label='Approx with adjusting h')
plt.plot(x,dydx_2,'.',label='Approx with optimal h')

plt.plot(x,dYdx,'b',label='Exact Value')

plt.title('Derivative of y = cos(100x)')
plt.legend(loc='best')
plt.show()
