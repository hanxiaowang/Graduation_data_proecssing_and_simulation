import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf


#
# forwardsin1=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=2800.0ns\forwards.txt')
# backwardsin1=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=2800.0ns\backwards.txt')
# evo_timesin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\evo_times.txt')
# delta_Psin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time.txt')
#
# forwardsin2=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=3000.0ns\forwards.txt')
# backwardsin2=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=3000.0ns\backwards.txt')
#
#
# forwardsin3=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=3100.0ns\forwards.txt')
# backwardsin3=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time=3100.0ns\backwards.txt')
#
#
# middle_number=100
# # print(np.shape(forwardsin1))
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin[::middle_number], forwardsin1[::middle_number], 's',  markersize=4, label=r'$0$',markerfacecolor='None')
# ax1.plot(evo_timesin[::middle_number], forwardsin2[::middle_number], 's',  markersize=4, label=r'$3000$',markerfacecolor='None')
# ax1.plot(evo_timesin[::middle_number], forwardsin3[::middle_number], 's',  markersize=4, label=r'$6000$',markerfacecolor='None')
#
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend()
# plt.show()

# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin[::middle_number], backwardsin1[::middle_number], 's',  markersize=4, label=r'$0$',markerfacecolor='None')
# ax1.plot(evo_timesin[::middle_number], backwardsin2[::middle_number], 's',  markersize=4, label=r'$3000$',markerfacecolor='None')
# ax1.plot(evo_timesin[::middle_number], backwardsin3[::middle_number], 's',  markersize=4, label=r'$6000$',markerfacecolor='None')
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend()
# plt.show()



##0~6000
# jump_back_time=3000.0
# forwardsin1=np.loadtxt(f'F:\\change fre\\bistable jump back 100mW and 100kHz\\jump back time={jump_back_time}ns\\forwards.txt')
# backwardsin1=np.loadtxt(f'F:\\change fre\\bistable jump back 100mW and 100kHz\\jump back time={jump_back_time}ns\\backwards.txt')
# evo_timesin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\evo_times.txt')
# delta_Psin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time.txt')
#
#
# middle_number=50
# # print(np.shape(forwardsin1))
# plt.figure(figsize=(8,6))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin[::middle_number], forwardsin1[::middle_number], 's', color='red', markersize=4, label=r'$0$',markerfacecolor='None')
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$|m|^2$',fontsize=20)
# plt.tick_params(labelsize=20)
# # plt.legend()
# plt.ylim(-0.5e14,9e14)
# plt.show()
#
# plt.figure(figsize=(8,6))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin[::middle_number], backwardsin1[::middle_number], 's',  color='blue',markersize=4, label=r'$0$',markerfacecolor='None')
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$|m|^2$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.ylim(0,3.5e14)
# # plt.legend()
# plt.show()

jump_times = np.linspace(0,600000,601)
interval=1e-11
evo_timesin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\evo_times.txt')
delta_Psin=np.loadtxt(r'F:\change fre\bistable jump back 100mW and 100kHz\jump back time.txt')
formin=[]
backmax=[]
for i in range(len(jump_times)):
    forwardsin1 = np.loadtxt(f'F:\\change fre\\bistable jump back 100mW and 100kHz\\jump back time={round(interval*jump_times[i]*1e9, 10)}ns\\forwards.txt')
    backwardsin1=np.loadtxt(f'F:\\change fre\\bistable jump back 100mW and 100kHz\\jump back time={round(interval*jump_times[i]*1e9, 10)}ns\\backwards.txt')
