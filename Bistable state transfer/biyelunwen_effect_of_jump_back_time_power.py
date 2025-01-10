import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

jbt=np.loadtxt(r'F:\change power\jump back start and final\jump back time.txt')*1e-11
evo_time=np.loadtxt(r'F:\change power\jump back start and final\evo_times.txt')
jstartf=np.loadtxt(r'F:\change power\jump back start and final\jump start forward.txt')
jstopf=np.loadtxt(r'F:\change power\jump back start and final\jump stop forward.txt')
jstartb=np.loadtxt(r'F:\change power\jump back start and final\jump start backward.txt')
jstopb=np.loadtxt(r'F:\change power\jump back start and final\jump stop backward.txt')


plt.figure(figsize=(8,6))
ax1 = plt.subplot(111)
ax1.plot(jbt, jstartf, '-',  linewidth=4, color='gray',label='initial $|m|^2$')
ax1.plot(jbt, jstopf, '-',  linewidth=10, color='blue',label='final $|m|^2$',alpha=0.5)
ax1.set_xlabel(r'$t_{P,back}$ [s]',fontsize=20)
ax1.set_ylabel(r'$|m|^2$',fontsize=20)
plt.tick_params(labelsize=20)
# plt.xscale('log')
plt.legend(loc='center right',fontsize=15)
plt.show()


plt.figure(figsize=(8,6))
ax1 = plt.subplot(111)
ax1.plot(jbt, jstartb, '-',  linewidth=4, color='gray',label='initial $|m|^2$')
ax1.plot(jbt, jstopb, '-',  linewidth=10, color='red',label='final $|m|^2$',alpha=0.5)
ax1.set_xlabel(r'$t_{P,back}$ [s]',fontsize=20)
ax1.set_ylabel(r'$|m|^2$',fontsize=20)
plt.tick_params(labelsize=20)
# plt.xscale('log')
plt.legend(loc='center right',fontsize=15)
plt.show()