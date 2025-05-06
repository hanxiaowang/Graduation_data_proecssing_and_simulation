import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

k_int = 1.4e6

# k_1 = 40e6
k_2 = 4.5e6
# rates=np.linspace(0.01,15,1500)
rates=np.logspace(-1,1,101)
k_1 = rates*k_2
# k_3 = 1.33e6
k_3 = 0e6

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a

delta=3
phis=np.linspace(-0.5,1.5,361)

omega_ps=omega_a+np.linspace(-50e6,50e6, 10001)



S12s1=[]
S21s1=[]
Isos1=[]
Isoneed=[]
Isom=[]
for j in range(len(k_1)):
    delta_m = omega_m - omega_ps
    delta_a = omega_a - omega_ps
    k_c = k_int + k_1[j] + k_2 + k_3
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2
    Isos1=[]
    for i,phi in enumerate(phis):
        fenzi21 = chi_m * np.sqrt(k_1[j] * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
            -1j * phi * np.pi)
        fenzi12 = chi_m * np.sqrt(k_1[j] * k_2) - 1j * g * np.sqrt(k_1[j] * gamma_e) * delta * np.exp(
            -1j * phi * np.pi)

        t12 = fenzi12 / fenmu
        t21 = fenzi21 / fenmu
        S12 = rf.mag_2_db(np.abs(t12))
        S21 = rf.mag_2_db(np.abs(t21))
        ISO=S21-S12
        # S12s1.append(S12)
        # S21s1.append(S21)
        isoabs=np.abs(ISO)
        index = list(isoabs).index(max(isoabs))
        Isos1.append(ISO[index])
    Isoneed.append(Isos1)
# print(type(Isos1))
print(np.shape(Isos1))


# max_index = list(Isos1).index(max(Isom))
# min_index = list(Isos1).index(min(Isom))
#
# print(phis[max_index])
# print(phis[min_index])

# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(phis,Isos1[:,1],'-',linewidth=5,label='S12')
# axes1.set_xlabel(r'$\phi$ [$\pi$]',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()
# max_index = list(Isos1[90]).index(max(Isos1[90]))
# print(rates[max_index])
#
# print(rates[0])
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(rates,Isos1[90],'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\delta$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()
phi_0=[]
for i in range(len(rates)):
    phi_0.append(0.5)
no_non=[]
for j in range(len(phis)):
    no_non.append(1)

print(np.shape(np.transpose(Isoneed)))
extents=[rates[0],rates[-1],phis[0],phis[-1]]
plt.figure(figsize=(6,6))
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(Isoneed), extent=extents, cmap="bwr",aspect='auto',origin='lower')
plt.colorbar(im)
# ax1.plot(rates,phi_0,'--',color='green',linewidth=3)
ax1.plot(no_non,phis,'--',color='black',linewidth=3)
ax1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=10)
ax1.set_ylabel(r'$\varphi$[$\pi$]',fontsize=10)
ax1.set_xscale('log')
plt.tick_params(labelsize=10)
plt.show()
#
# ax1 = plt.subplot(111)
# im = ax1.imshow((Isos1), extent=extents,aspect='auto',origin='lower')
# plt.colorbar(im)
# # ax1.plot(rates,phi_0,'--',color='green',linewidth=3)
# ax1.plot(no_non,phis,'--',color='black',linewidth=3)
# ax1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=10)
# ax1.set_ylabel(r'$\varphi$[$\pi$]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()
