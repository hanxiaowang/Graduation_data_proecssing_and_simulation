import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf


# #
forwardsin1=np.loadtxt(r'D:\bistable date\Pd step=10.0mW\forwards.txt')
backwardsin1=np.loadtxt(r'D:\bistable date\Pd step=10.0mW\backwards.txt')
evo_timesin1=np.loadtxt(r'D:\bistable date\Pd step=10.0mW\evo_times.txt')
delta_Psin1=np.loadtxt(r'D:\bistable date\Pd step=10.0mW\delta_Ps.txt')

forwardsin2=np.loadtxt(r'D:\bistable date\Pd step=0.0001mW\forwards.txt')
backwardsin2=np.loadtxt(r'D:\bistable date\Pd step=0.0001mW\backwards.txt')
evo_timesin2=np.loadtxt(r'D:\bistable date\Pd step=0.0001mW\evo_times.txt')
delta_Psin2=np.loadtxt(r'D:\bistable date\Pd step=0.0001mW\delta_Ps.txt')

forwardsin3=np.loadtxt(r'D:\bistable date\Pd step=0.01mW\forwards.txt')
backwardsin3=np.loadtxt(r'D:\bistable date\Pd step=0.01mW\backwards.txt')
evo_timesin3=np.loadtxt(r'D:\bistable date\Pd step=0.01mW\evo_times.txt')
delta_Psin3=np.loadtxt(r'D:\bistable date\Pd step=0.01mW\delta_Ps.txt')

forwardsin4=np.loadtxt(r'D:\bistable date1\Pd step=0.01mW\forwards.txt')
backwardsin4=np.loadtxt(r'D:\bistable date1\Pd step=0.01mW\backwards.txt')
evo_timesin4=np.loadtxt(r'D:\bistable date1\Pd step=0.01mW\evo_times.txt')
delta_Psin4=np.loadtxt(r'D:\bistable date1\Pd step=0.01mW\delta_Ps.txt')
middle_number=50
# print(np.shape(forwardsin1))
plt.figure(figsize=(12,12))
ax1 = plt.subplot(111)
# ax1.plot(evo_timesin1[::middle_number], forwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],10mw$',markerfacecolor='None')
# ax1.plot(evo_timesin2[::middle_number], forwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.0001mw$',markerfacecolor='None')
# ax1.plot(evo_timesin3[::middle_number], forwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
# ax1.plot(evo_timesin4[::middle_number], forwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')

ax1.plot(evo_timesin1[::middle_number], backwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
ax1.plot(evo_timesin2[::middle_number], backwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
ax1.plot(evo_timesin3[::middle_number], backwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
# ax1.plot(evo_timesin4[::middle_number], backwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')

ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend()
plt.show()


#forward
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(evo_timesin[0][::20],forwardsin[0][::20],'s',markersize=4,label=r'$\Delta P_d=5$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[1][::20],'s',markersize=4,label=r'$\Delta P_d=4$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[2][::20],'s',markersize=4,label=r'$\Delta P_d=2$ mW')
# # axes.plot(evo_timesin[0][::20],forwardsin[3][::20],'s',markersize=4,label=r'$\Delta P_d=1$ mW')
#
# # plt.xticks([-50,0,50],['-50','0','50'])
# #
# # # plt.xticks([-50,0,50],['-50','0','50'])
# #
# # # axes.plot(evo_timesin[0][::20],forwardsin[4][::20],'s',markersize=4,label=r'$\Delta P_d=0.5$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[5][::20],'s',markersize=4,label=r'$\Delta P_d=0.4$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[6][::20],'s',markersize=4,label=r'$\Delta P_d=0.2$ mW')
# # axes.plot(evo_timesin[0][::20],forwardsin[7][::20],'s',markersize=4,label=r'$\Delta P_d=0.1$ mW')
# #
# # # axes.plot(evo_timesin[0][::20],forwardsin[8][::20],'s',markersize=4,label=r'$\Delta P_d=0.05$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[9][::20],'s',markersize=4,label=r'$\Delta P_d=0.04$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[10][::20],'s',markersize=4,label=r'$\Delta P_d=0.02$ mW')
# axes.plot(evo_timesin[0][::20],forwardsin[11][::20],'s',markersize=4,label=r'$\Delta P_d=0.01$ mW')
# plt.ylim(0,7e14)
# # # axes.plot(evo_timesin[0][::20],forwardsin[12][::20],'s',markersize=4,label=r'$\Delta P_d=0.005$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[13][::20],'s',markersize=4,label=r'$\Delta P_d=0.004$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[14][::20],'s',markersize=4,label=r'$\Delta P_d=0.002$ mW')
# # axes.plot(evo_timesin[0][::20],forwardsin[15][::20],'s',markersize=4,label=r'$\Delta P_d=0.001$ mW')
# #
# # # axes.plot(evo_timesin[0][::20],forwardsin[16][::20],'s',markersize=4,label=r'$\Delta P_d=0.0005$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[17][::20],'s',markersize=4,label=r'$\Delta P_d=0.0004$ mW')
# # # axes.plot(evo_timesin[0][::20],forwardsin[18][::20],'s',markersize=4,label=r'$\Delta P_d=0.0002$ mW')
# # axes.plot(evo_timesin[0][::20],forwardsin[19][::20],'s',markersize=4,label=r'$\Delta P_d=0.0001$ mW')
#
#
#
# ## backward
#
# # axes.plot(evo_timesin[0][::20],backwardsin[0][::20],'s',markersize=8,label=r'$\Delta P_d=5$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[1][::20],'s',markersize=4,label=r'$\Delta P_d=4$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[2][::20],'s',markersize=4,label=r'$\Delta P_d=2$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[3][::20],'s',markersize=4,label=r'$\Delta P_d=1$ mW')
# # plt.xticks([-50,0,50],['-50','0','50'])
#
# # axes.plot(evo_timesin[0][::20],backwardsin[4][::20],'s',markersize=4,label=r'$\Delta P_d=0.5$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[5][::20],'s',markersize=4,label=r'$\Delta P_d=0.4$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[6][::20],'s',markersize=4,label=r'$\Delta P_d=0.2$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[7][::20],'s',markersize=4,label=r'$\Delta P_d=0.1$ mW')
#
# # axes.plot(evo_timesin[0][::20],backwardsin[8][::20],'s',markersize=4,label=r'$\Delta P_d=0.05$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[9][::20],'s',markersize=4,label=r'$\Delta P_d=0.04$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[10][::20],'s',markersize=4,label=r'$\Delta P_d=0.02$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[11][::20],'s',markersize=4,label=r'$\Delta P_d=0.01$ mW')
#
# # axes.plot(evo_timesin[0][::20],backwardsin[12][::20],'s',markersize=4,label=r'$\Delta P_d=0.005$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[13][::20],'s',markersize=4,label=r'$\Delta P_d=0.004$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[14][::20],'s',markersize=4,label=r'$\Delta P_d=0.002$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[15][::20],'s',markersize=4,label=r'$\Delta P_d=0.001$ mW')
#
# # axes.plot(evo_timesin[0][::20],backwardsin[16][::20],'s',markersize=4,label=r'$\Delta P_d=0.0005$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[17][::20],'s',markersize=4,label=r'$\Delta P_d=0.0004$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[18][::20],'s',markersize=4,label=r'$\Delta P_d=0.0002$ mW')
# # axes.plot(evo_timesin[0][::20],backwardsin[19][::20],'s',markersize=4,label=r'$\Delta P_d=0.0001$ mW')
# axes.set_xlabel(r'Evolution times [s]',fontsize=40)
# axes.set_ylabel(r'$|m|^2$',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=10)
# plt.show()