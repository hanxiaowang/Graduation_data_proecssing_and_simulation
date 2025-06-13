import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json


de = 1

start = 4000
stop = 14001

voltage=70

phi_target=270


# 0
# 48
# 62
# 90
# 147
# 155
# 180

S12r=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_target]+33
S21r=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_target]+33
Isor=S12r-S21r
# print(np.shape(S12r))
# print((S12r))

S12e=S12r
S21e=S21r
Isoe=Isor

fe=np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]

fe_start=fe[0]
fe_stop=fe[-1]
# print(fe_start)
# print(fe_stop)
phie=np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\phi.txt')

# print(np.shape(S12r))
# print(np.shape(fe))
omega_a = 8.247e9

omega_m12 = omega_a-4.7*1e6
omega_m21 = omega_a-5*1e6
omega_s = np.linspace(fe_start,fe_stop,10001)*1e9

k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

phis = np.linspace(0, 2, 361)

## deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2

delta=0.97*voltage/45
print(delta)
print(phis[phi_target])

phi1 = 0.75
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2

delta1=0.97


# zhengti=-0.26
# chazhi=0.06  #63

# zhengti=-0.18
# chazhi=0.08 #-32

# zhengti=-0.2
# chazhi=0.1 #-2

phi21=(-0.1)
phi12=(-0.1602)



phi = phis[phi_target]

delta_m12 = omega_m12 - omega_s
delta_m21 = omega_m21 - omega_s
delta_a = omega_a - omega_s
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

S12s = rf.mag_2_db(np.abs(t12))
S21s = rf.mag_2_db(np.abs(t21))
Isos=S12s-S21s

print(max(Isoe))
print(min(Isoe))

fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_s,S12e,'-',linewidth=10,label=r'$S_{12,exp}$',color='green',alpha=0.4)
axes1.plot(omega_s,S12s,'-',linewidth=3,label=r'$S_{12,sim}$',color='green',zorder=2)
axes1.plot(omega_s,S21e,'-',linewidth=10,label=r'$S_{21,exp}$',color='orange',alpha=0.4)
axes1.plot(omega_s,S21s,'-',linewidth=3,label=r'$S_{21,sim}$',color='orange',zorder=2)
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
axes1.plot(omega_s,Isoe,'-',linewidth=10,label=r'$Iso._{exp}$',color='pink',alpha=1)
axes1.plot(omega_s,Isos,'-',linewidth=3,label=r'$Iso._{sim}$',color='purple',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-50,0,50,100],['-100','-50','0','50','100'])
plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()
