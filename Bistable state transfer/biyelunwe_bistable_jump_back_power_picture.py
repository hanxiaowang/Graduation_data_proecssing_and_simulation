import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf


# #
forwardsin1=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=0.0ns\forwards.txt')
backwardsin1=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=0.0ns\backwards.txt')
evo_timesin=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\evo_times.txt')

forwardsin2=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=400.0ns\forwards.txt')
backwardsin2=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=400.0ns\backwards.txt')

forwardsin3=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=4000.0ns\forwards.txt')
backwardsin3=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=4000.0ns\backwards.txt')
# evo_timesin3=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=0.0ns\evo_times.txt')
# delta_Psin3=np.loadtxt(r'F:\change power\bistable jump back 8.18 and 1mW\jump back time=0.0ns\delta_fs.txt')

middle_number=50
# print(np.shape(forwardsin1))
plt.figure(figsize=(12,12))
ax1 = plt.subplot(111)
ax1.plot(evo_timesin[::middle_number], forwardsin1[::middle_number], 's',  markersize=4, label=r'$A \longrightarrow B]$',markerfacecolor='None')
ax1.plot(evo_timesin[::middle_number], forwardsin2[::middle_number], 's',  markersize=4, label=r'$A \longrightarrow B]$',markerfacecolor='None')
ax1.plot(evo_timesin[::middle_number], forwardsin3[::middle_number], 's',  markersize=4, label=r'$A \longrightarrow B]$',markerfacecolor='None')

ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend()
plt.show()

plt.figure(figsize=(12,12))
ax1 = plt.subplot(111)
ax1.plot(evo_timesin[::middle_number], backwardsin1[::middle_number], 's',  markersize=4, label=r'$C \longrightarrow D$',markerfacecolor='None')
ax1.plot(evo_timesin[::middle_number], backwardsin2[::middle_number], 's',  markersize=4, label=r'$C \longrightarrow D$',markerfacecolor='None')
ax1.plot(evo_timesin[::middle_number], backwardsin3[::middle_number], 's',  markersize=4, label=r'$C \longrightarrow D$',markerfacecolor='None')
ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend()
plt.show()