import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *

import math as m
import cmath
import time
from matplotlib import cm
import skrf as rf
from scipy.optimize import curve_fit

x1=[3.388,3.467,3.508,3.548,3.589,3.631,3.673]
y1=[39.36,37.2,24.6,23.2,13.8,16.4,10.4]

x2=[3.707,3.758,3.802,3.89,3.981]
y2=[0.534,0.606,0.562,0.818,0.546]



x3=[3.388,3.467,3.508,3.548,3.589,3.631,3.673,3.707,3.758,3.802,3.89,3.981]
y3=[39.36,37.2,24.6,23.2,13.8,16.4,10.4,0.534,0.606,0.562,0.818,0.546]

x11=np.linspace(3.388,3.75,100)
x21=np.linspace(3.75,3.981,100)
z1=np.polyfit(x1,y1,1)
z2=np.polyfit(x2,y2,1)
p1=np.poly1d(z1)
p2=np.poly1d(z2)
n1=p1(x11)
n2=p2(x21)


# print(n1)
# print(n2)
fig, axes = plt.subplots(1, 1, figsize=(8, 8))

axes.plot(x11,n1,'--',label='Curvefit',color='red',linewidth=2)
axes.plot(x21,n2,'--',color='red',linewidth=2)
axes.scatter(x3,y3,label='Experiment',color='none',edgecolors='blue',s=200,linewidth=3)
axes.set_xlabel(r'$P_d$ [mW]',fontsize=20)
axes.set_ylabel(r'$\kappa_b$ [Hz]',fontsize=20)
axes.set_title(r'$\kappa_b$ vs $P_d$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=3,fontsize=20)

plt.show()
