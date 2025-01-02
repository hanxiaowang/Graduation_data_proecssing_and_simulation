import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf


# #
forwardsin1=np.loadtxt(r'F:\change power\bistable date\Pd step=1.0mW\forwards.txt')
backwardsin1=np.loadtxt(r'F:\change power\bistable date\Pd step=1.0mW\backwards.txt')
evo_timesin1=np.loadtxt(r'F:\change power\bistable date\Pd step=1.0mW\evo_times.txt')
delta_Psin1=np.loadtxt(r'F:\change power\bistable date\Pd step=1.0mW\delta_Ps.txt')
print(min(backwardsin1))
forwardsin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0009mW\forwards.txt')
backwardsin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0009mW\backwards.txt')
evo_timesin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0009mW\evo_times.txt')
delta_Psin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0009mW\delta_Ps.txt')

forwardsin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\forwards.txt')
backwardsin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\backwards.txt')
evo_timesin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\evo_times.txt')
delta_Psin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\delta_Ps.txt')
#
# forwardsin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\forwards.txt')
# backwardsin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\backwards.txt')
# evo_timesin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\evo_times.txt')
# delta_Psin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\delta_Ps.txt')
middle_number=50
print(np.shape(forwardsin1))
plt.figure(figsize=(12,12))
ax1 = plt.subplot(111)
ax1.plot(evo_timesin1[::middle_number], forwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],1mw$',markerfacecolor='None')
ax1.plot(evo_timesin2[::middle_number], forwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.0009mw$',markerfacecolor='None')
ax1.plot(evo_timesin3[::middle_number], forwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.0001mw$',markerfacecolor='None')
# ax1.plot(evo_timesin4[::middle_number], forwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend()
plt.show()

#
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# # ax1.plot(evo_timesin1[::middle_number], backwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
# # ax1.plot(evo_timesin2[::middle_number], backwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
# # ax1.plot(evo_timesin3[::middle_number], backwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
# # ax1.plot(evo_timesin4[::middle_number], backwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
#
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend()
plt.show()

