# Script of derivate computation
import numpy as np
import matplotlib.pyplot as plt

def dfdx_1(f,x,h):
    return (f(x + h) - f(x))/h

def dfdx_2(f,x,h):
    return (f(x) - f(x-h))/h

def dfdx_3(f,x,h):
    return (f(x + h) - f(x - h))/(2*h)

def dfdx_4(f,x,h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h))/(2*h)

n = 200
x = np.linspace(0, np.pi /50, n + 1)
h = (np.pi /50 )/ n

def sin100x(x):
    return np.sin(100*x)

dydx_1 = dfdx_1(sin100x,x,h)
dydx_2 = dfdx_2(sin100x,x,h)
dydx_3 = dfdx_3(sin100x,x,h)
dydx_4 = dfdx_4(sin100x,x,h)

dYdx = 100*np.cos(100*x)

#plt.figure(figsize=(12,5))
plt.plot(x,dydx_1,'.',label='Approx left method')
plt.plot(x,dydx_2,'.',label='Approx right method')
plt.plot(x,dydx_3,'.',label='Approx central method')
plt.plot(x,dydx_4,'.',label='Approx five point method')

plt.plot(x,dYdx,'b',label='Exact Value')

plt.title('Derivative of y = cos(100x)')
plt.legend(loc='best')
plt.show()
