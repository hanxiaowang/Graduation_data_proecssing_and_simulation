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


gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

k_int = 1.4e6

k_2 = 4.5e6
k_3 = 1.33e6


# k_1 = 45.5e6
k_1s = np.linspace(-10,10,201)*1e6+4*g+gamma-k_int-k_2-k_3

# k_1 = -10*1e6+4*g+gamma-k_int-k_2-k_3

phi =0.5
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
W=[]
IM=[]
for i in range(len(k_1s)):
    k_1=k_1s[i]
    k_c = k_int + k_1 + k_2 + k_3
    delta_m = omega_m - omega_s
    delta_a = omega_a - omega_s
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2
    fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi12)*np.pi)) - 1j * g * np.sqrt(k_2*gamma_e) * delta * np.exp(-1j * (phi + phi12)*np.pi))
    fenzi12 = (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_1*k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi21)*np.pi)) - 1j * g * np.sqrt(k_1*gamma_e) * delta * np.exp(-1j * (phi + phi21)*np.pi))

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12=rf.mag_2_db(np.abs(t12))
    S21=rf.mag_2_db(np.abs(t21))
    iso=S12-S21
    Iso.append(iso)
    # W.append(g**2-((k_c-gamma)/4)**2)
    W.append(g- ((k_c - gamma) / 4))
    IM.append(max(iso))

#
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(k_1s/1e6, omega_s/1e9, np.transpose(Iso))
# ax1.set_xlabel(r'$\kappa_1$ [MHz]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# plt.show()

# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(k_1s/1e6,W,'-',linewidth=5,label='W')
# axes.set_xlabel(r'$\kappa_1$ [MHz]',fontsize=40)
# axes.set_ylabel(r'$W$ ',fontsize=40)
# plt.tick_params(labelsize=35)
# # plt.legend(loc=1,fontsize=40)
# plt.show()

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(W,IM,'-',linewidth=5,label='Iso_{max}')
axes.set_xlabel(r'$W$ ',fontsize=40)
axes.set_ylabel(r'$Iso_{max}$ [dB]',fontsize=40)
plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=40)
plt.show()