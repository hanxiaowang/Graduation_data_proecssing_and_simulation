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

delta=3
phis=np.linspace(-0.5,1.5,3601)

omega_ps=8.25e9+np.linspace(-50,50,5001)*1e6

S12s1=[]
S21s1=[]
Isos1=[]
Isom=[]
max_deltaa=[]
min_deltaa=[]
max_deltaa_phi=[]
min_deltaa_phi=[]
for i,phi in enumerate(phis):
    delta_m = omega_m - omega_ps
    delta_a = omega_a - omega_ps
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)
    fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))
    ISO=S12-S21
    Iso_opt = np.abs(ISO)
    max_index = list(Iso_opt).index(max(Iso_opt))
    # Isom.append(ISO[1001])
    if ISO[max_index]>=0:
        max_deltaa.append(omega_ps[max_index])
        max_deltaa_phi.append(phi)
    if ISO[max_index] <0:
        min_deltaa.append(omega_ps[max_index])
        min_deltaa_phi.append(phi)
    S12s1.append(S12)
    S21s1.append(S21)
    Isos1.append(ISO)
    # Isom.append(ISO[1001])

# max_index = list(Isos1).index(max(Isom))
# min_index = list(Isos1).index(min(Isom))
#
# print(phis[max_index])
# print(phis[min_index])


## ISO at wp=wm vs phi
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(phis,Isom,'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\phi/\pi$ [GHz]',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
#
# plt.show()

## ISO at some phi vs wp
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# # axes1.plot(omega_ps/1e9,S12s1[90],'-',linewidth=5,label='S12')
# # axes1.plot(omega_ps/1e9,S21s1[90],'-',linewidth=5,label='S21')
# axes1.plot(omega_ps/1e9,Isos1[90],'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\phi/\pi$ [GHz]',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()

X,Y=np.meshgrid(phis,(omega_a-omega_ps)/1e9)

## S12,S21 and ISO vs phi and wm
#
extents=[phis[0],phis[-1],(omega_a-omega_ps)[0]/1e9,(omega_a-omega_ps)[-1]/1e9]
# plt.figure(figsize=(6,6))
# ax1=plt.subplot(111)
# im = ax1.imshow(np.transpose(S12s1), extent=extents,aspect='auto',origin='lower')
# plt.colorbar(im)
# ax1.set_ylabel(r'$\varphi$[$\pi$]',fontsize=10)
# ax1.set_xlabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()
#
# plt.figure(figsize=(6,6))
#
# ax2 = plt.subplot(111)
# im = ax2.imshow(np.transpose(S21s1), extent=extents,aspect='auto',origin='lower')
# ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=10)
# ax2.set_ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.colorbar(im)#
# plt.show()

plt.figure(figsize=(6,6))

ax3 = plt.subplot(111)
im = ax3.imshow(np.transpose(Isos1), extent=extents, cmap="bwr",aspect='auto',origin='lower')
# ax3.plot(max_deltaa_phi,(omega_a-np.array(max_deltaa))/1e9,'o',color='green',markersize=1,alpha=0.5)
# ax3.plot(min_deltaa_phi,(omega_a-np.array(min_deltaa))/1e9,'o',color='green',markersize=1,alpha=0.5)

ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=10)
ax3.set_ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.colorbar(im)#
plt.show()
