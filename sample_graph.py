# Using the numpy (numerical python) library
import numpy as np
mydata = np.loadtxt('data.txt')
# We use this magic function (%) to allow us to plot inline in this ipython notebook
%matplotlib inline
import matplotlib.pyplot as plt
x=mydata[:,0]
y=mydata[:,1]
plt.plot(x,y)
line = plt.plot(x,y,'m+')
