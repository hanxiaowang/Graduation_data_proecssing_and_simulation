import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json
voltages=np.linspace(20,110,19)
phis=np.linspace(0,2,361)

v_index=15#Iso max
phi_index=143#phi max

voltage=voltages[v_index]
delta=0.97*voltage/45
# print(delta)
phi=phis[phi_index]
print(delta)
print(phi)
start=4000
stop=14000

S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
Isoe=S12e-S21e

omega_a = 8.247e9
omega_m12 = omega_a-5.93e6
omega_m21 = omega_a-3.8e6

omega_se = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]*1e9
k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6


## deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2



phi1 = 0.755
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2
delta1=0.97


# zhengti=-0.26
# chazhi=0.06  #63

# zhengti=-0.18
# chazhi=0.08 #-32

# zhengti=-0.2
# chazhi=0.1 #-2

# phi21=(-0.2+0.1)
# phi12=(-0.2)
phi21=-0.117
phi12=(-0.1779025)

omega_ss = np.linspace(omega_se[0],omega_se[-1],20001)
delta_m12 = omega_m12 - omega_ss
delta_m21 = omega_m21 - omega_ss

delta_a = omega_a - omega_ss
chi_a = 1j * delta_a + k_c / 2
chi_m12 = 1j * delta_m12 + gamma / 2
chi_m21 = 1j * delta_m21 + gamma / 2

fenmu12 = chi_a * chi_m12 + g ** 2
fenmu21 = chi_a * chi_m21 + g ** 2


fenzi21 = (chi_m21 * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
    -1j * (phi + phi21) * np.pi))
fenzi12 = (chi_m12 * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
    -1j * (phi + phi12) * np.pi))

t12 = fenzi12 / fenmu12
t21 = fenzi21 / fenmu21

# T12.append(rf.mag_2_db(np.abs(t12)))
# T21.append(rf.mag_2_db(np.abs(t21)))
S12s = rf.mag_2_db(np.abs(t12))
S21s = rf.mag_2_db(np.abs(t21))
Isos=S12s-S21s


# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(omega_s,S12e,'o',linewidth=2,label='E',color='blue')
# # axes.plot(omega_s,S12s,'--',linewidth=5,label='S',color='blue')
# axes.plot(omega_s,S21e,'o',linewidth=2,label='E',color='orange')
# axes.plot(omega_s,S21s,'--',linewidth=5,label='S',color='orange')
#
# # axes.plot(omega_s,Isoe,'--',linewidth=2,label='E',color='green')
# # axes.plot(omega_s,Isos,'--',linewidth=5,label='S',color='green')
# axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
# axes.set_ylabel(r'$S_{21}$ [dB]',fontsize=40)
#
# plt.tick_params(labelsize=35)
# # plt.legend(loc=1,fontsize=40)
# plt.show()
print(min(S12e))
print(min(S12s))
print(min(Isoe))
print(min(Isos))
# plt.figure(figsize=(18,6))
# #
# ax1 = plt.subplot(131)
# ax1.scatter(omega_s,S12e,s=10,label='E',color='blue',alpha=0.1)
# ax1.plot(omega_s,S12s,'-',linewidth=1,label='S',color='blue',zorder=2)
# ax1.set_ylim(-105,5)
#
# ax2 = plt.subplot(132)
# ax2.scatter(omega_s,S21e,s=10,label='E',color='orange',alpha=0.1)
# ax2.plot(omega_s,S21s,'-',linewidth=1,label='S',color='orange',zorder=2)
# ax2.set_ylim(-105,5)
#
# ax3 = plt.subplot(133)
# ax3.scatter(omega_s,Isoe,s=10,label='E',color='green',alpha=0.1)
# ax3.plot(omega_s,Isos,'-',linewidth=1,label='S',color='green',zorder=2)
# ax3.set_ylim(-105,105)
#
# ax1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=10)
# ax1.set_ylabel(r'$S_{12}$ [dB]',fontsize=10)
# ax2.set_ylabel(r'$S_{21}$ [dB]',fontsize=10)
# ax3.set_ylabel(r'$Iso$ [dB]',fontsize=10)
#
# # plt.tick_params(labelsize=35)
# # plt.legend(loc=1,fontsize=40)
# plt.show()



fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_se,S12e,'-',linewidth=10,label=r'$S_{12,exp}$',color='green',alpha=0.4)
axes1.plot(omega_ss,S12s,'-',linewidth=3,label=r'$S_{12,sim}$',color='green',zorder=2)
axes1.plot(omega_se,S21e,'-',linewidth=10,label=r'$S_{21,exp}$',color='orange',alpha=0.4)
axes1.plot(omega_ss,S21s,'-',linewidth=3,label=r'$S_{21,sim}$',color='orange',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-75,-50,-25,0],['-100','-75','-50','-25','0'])
plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()


fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_se,Isoe,'-',linewidth=10,label=r'$Iso._{exp}$',color='blue',alpha=0.4)
axes1.plot(omega_ss,Isos,'-',linewidth=3,label=r'$Iso._{sim}$',color='blue',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-50,0,50,100],['-100','-50','0','50','100'])
plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()
