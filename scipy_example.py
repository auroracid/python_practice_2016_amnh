'''This is an example where we use curve_fit to fit a curve and plot the 
results'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

def func(x, a, b, c):
    '''This returns an array from performing e^?? on x,
    where x is the element array.
    a ,b, c are just constants of the function.'''
    return a * np.exp(-b * x) + c
xdata = np.linspace(0, 4, 50) 
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size=len(xdata))
# ydata = func(xdata,2.5,1.3,0.5)+0.2* np.random.normal(size=len(xdata))
# e.g.
# ydata = func(xdata, *params) + eps
# popt = array ([2.33626499,  1.2950542 ,  0.52044699])
# popt is an array of parameters minimizing sum of square error
# pcov is covariance
popt, pcov = curve_fit(func, xdata, ydata)
# original y data that helped create perturbed y data
plt.plot(xdata, y, 'g')
#perturbed ydata
plt.plot(xdata, ydata, 'c', marker='p')
# best fit y data to the perturbed data
plt.plot(xdata, func(xdata,popt[0],popt[1],popt[2]), 'r', marker='o')
plt.show()
