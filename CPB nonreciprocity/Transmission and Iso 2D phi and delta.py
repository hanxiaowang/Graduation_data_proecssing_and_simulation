import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

k_int = 1.4e6
k_1 = 45.5e6
# k_1 = 40e6
k_2 = 4.5e6
# k_3 = 1.33e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a

delta=np.linspace(0,6,601)
phis=np.linspace(0,2,361)

omega_ps=omega_a



delta_m = omega_m - omega_ps
delta_a = omega_a - omega_ps
chi_a = 1j * delta_a + k_c / 2
chi_m = 1j * delta_m + gamma / 2
fenmu = chi_a * chi_m + g ** 2

S12s1=[]
S21s1=[]
Isos1=[]
Isom=[]

for i,phi in enumerate(phis):
    fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)
    fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))
    ISO=S12-S21
    S12s1.append(S12)
    S21s1.append(S21)
    Isos1.append(ISO)

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
max_index = list(Isos1[90]).index(max(Isos1[90]))
print(delta[max_index])

print(delta[0])
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(delta,Isos1[90],'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\delta$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()
phi_0=[]
for i in range(len(delta)):
    phi_0.append(0.5)

plt.figure(figsize=(18,12))
ax1 = plt.subplot(231)
gci1 = ax1.pcolor(phis,delta, np.transpose(S12s1))
ax1.plot(phi_0,delta,'--',color='red')
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax1.set_ylim(0,max(delta))
ax1.set_xlabel(r'$\varphi/\pi$',fontsize=20)
ax1.set_ylabel(r'$\delta$',fontsize=20)

plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci1)

ax2 = plt.subplot(232)
gci2 = ax2.pcolor(phis,delta,np.transpose(S21s1))
ax2.plot(phi_0,delta,'--',color='red')
# ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
ax2.set_ylim(0,max(delta))

plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci2)

ax3 = plt.subplot(233)
gci3 = ax3.pcolor(phis, delta,np.transpose(Isos1))
ax3.plot(phi_0,delta,'--',color='red')
# ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
ax3.set_ylim(0,max(delta))


plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci3)

plt.show()
