''' Our first simple plot'''
import numpy as np
import matplotlib.pyplot as plt

mydata = np.loadtxt('data.txt')
x=mydata[:,0]
y=mydata[:,1]
line = plt.plot(x,y,'cp', label='line1', linewidth=3)
plt.show()
