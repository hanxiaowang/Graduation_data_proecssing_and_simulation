import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

omega_a = 8.247e9
# delta_ms=np.linspace(-100,100,41)
delta_ms = [-500*1e6,-300*1e6,-100*1e6,-50*1e6,50*1e6,100*1e6,300*1e6,500*1e6,0]

de = 8
omega_m = omega_a+delta_ms[de]
omega_s = np.linspace(omega_m - 60e6, omega_m + 60e6, 2001)
# omega_s = np.linspace(8.16e9, 8.36e9, 20001)



gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

k_int = 1.4e6

k_2 = 4.5e6
k_3 = 1.33e6


# k_1 = 45.5e6

# k_1s = np.linspace(-10,10,201)*1e6+4*g+gamma-k_int-k_2-k_3

k_1 = -10*1e6+4*g+gamma-k_int-k_2-k_3

k_c = k_int + k_1 + k_2 + k_3


phis = np.linspace(0, 2, 361)
voltage = np.linspace(20, 110, 19)
deltas = 0.97 * voltage / 45



phis = np.linspace(0,2,361)
delta = 2


# phi1 = 0.77
# delta1 = 1

phi1 = 0
delta1 = 0

zhengti=0
chazhi=0  #63
phi12=(zhengti+chazhi)
phi21=(zhengti)

Iso = []

delta_m = omega_m - omega_s
delta_a = omega_a - omega_s
chi_a = 1j * delta_a + k_c / 2
chi_m = 1j * delta_m + gamma / 2
fenmu = chi_a * chi_m + g ** 2

# Iso_c=[]
# for i in range(len(phis)):
#     phi=phis[i]
#     fenzi21 =  (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_2*k_3) * delta1 * delta * np.exp(
#         -1j * (phi + phi1 + phi12)*np.pi)) - 1j * g * np.sqrt(k_2*gamma_e) * delta * np.exp(-1j * (phi + phi12)*np.pi))
#     fenzi12 = (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_1*k_3) * delta1 * delta * np.exp(
#         -1j * (phi + phi1 + phi21)*np.pi)) - 1j * g * np.sqrt(k_1*gamma_e) * delta * np.exp(-1j * (phi + phi21)*np.pi))
#
#     t12 = fenzi12 / fenmu
#     t21 = fenzi21 / fenmu
#     S12=rf.mag_2_db(np.abs(t12))
#     S21=rf.mag_2_db(np.abs(t21))
#     iso=S12-S21
#     Iso_c.append(iso[1000])
#     # print(iso[1000])
# # -0.032
# # +0.063
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(omega_s/1e9,iso,'--',linewidth=5,label='ISO')
# axes.plot(phis,Iso_c,'-',linewidth=5,label='S12')
#
# axes.set_xlabel(r'$\phi/2\pi$ [GHz]',fontsize=40)
# axes.set_ylabel(r'$ISO.$ [dB]',fontsize=40)
#
# plt.tick_params(labelsize=35)
# # plt.legend(loc=1,fontsize=40)
# plt.show()


phi=0.5
fenzi21 =  (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_2*k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi12)*np.pi)) - 1j * g * np.sqrt(k_2*gamma_e) * delta * np.exp(-1j * (phi + phi12)*np.pi))
fenzi12 = (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_1*k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi21)*np.pi)) - 1j * g * np.sqrt(k_1*gamma_e) * delta * np.exp(-1j * (phi + phi21)*np.pi))

t12 = fenzi12 / fenmu
t21 = fenzi21 / fenmu
S12=rf.mag_2_db(np.abs(t12))
S21=rf.mag_2_db(np.abs(t21))
iso=S12-S21
fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(omega_s/1e9,iso,'--',linewidth=5,label='ISO')
axes.plot(omega_s/1e9,S12,'-',linewidth=5,label='S12')
axes.plot(omega_s/1e9,S21,'-',linewidth=5,label='S21')
axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
axes.set_ylabel(r'$S$ [dB]',fontsize=40)

plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=40)
plt.show()


