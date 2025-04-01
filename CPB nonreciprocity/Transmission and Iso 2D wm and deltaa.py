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
omega_ms=omega_a+np.linspace(-50,50,251)*1e6

delta1=3
delta2=0.28
phi=0.5

omega_ps=omega_a+np.linspace(-50,50,251)*1e6


S12s1=[]
S21s1=[]
Isos1=[]
Isom1=[]
for i,omega_m in enumerate(omega_ms):
    delta_m = omega_m - omega_ps
    delta_a = omega_a - omega_ps
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta1 * np.exp(
        -1j * phi * np.pi)
    fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta1 * np.exp(
        -1j * phi * np.pi)

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))
    ISO=S21-S12
    S12s1.append(S12)
    S21s1.append(S21)
    Isos1.append(ISO)
    Isom1.append(min(ISO))


S12s2=[]
S21s2=[]
Isos2=[]
Isom2=[]
for i,omega_m in enumerate(omega_ms):
    delta_m = omega_m - omega_ps
    delta_a = omega_a - omega_ps
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta2 * np.exp(
        -1j * phi * np.pi)
    fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta2 * np.exp(
        -1j * phi * np.pi)

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))
    ISO=S21-S12
    S12s2.append(S12)
    S21s2.append(S21)
    Isos2.append(ISO)
    Isom2.append(max(ISO))





# plt.figure(figsize=(6,6))
# ax1 = plt.subplot(111)
# # gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S12s1),cmap='spring')
# # gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S21s1),cmap='spring')
# # gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(Isos1),cmap='spring')
# # gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S12s2),cmap='spring')
# # gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S21s2),cmap='spring')
# gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(Isos2),cmap='spring')
# ax1.plot(omega_ms/1e9,omega_ms/1e9,'--',color='black',alpha=0.5,linewidth=5)
# ax1.set_xlabel(r'$\omega_m/2\pi$[GHz]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.xticks([8,8.5],['8','8.5'])

# cbar = plt.colorbar(gci1)
# plt.show()

extents=[omega_ms[0]/1e9, omega_ms[-1]/1e9, omega_ps[0]/1e9,omega_ps[-1]/1e9]

plt.figure(figsize=(6,6))
ax2 = plt.subplot(111)
im = ax2.imshow(np.transpose(Isos1), extent=extents,aspect='auto',origin='lower',cmap='bwr')
ax2.plot(omega_ms/1e9,omega_ms/1e9,'--',color='yellow',alpha=1,linewidth=5)
plt.colorbar(im)
plt.show()

plt.figure(figsize=(6,6))
ax2 = plt.subplot(111)
im = ax2.imshow(np.transpose(Isos2), extent=extents,aspect='auto',origin='lower',cmap='bwr')
# im = ax2.imshow(np.transpose(Isos1), extent=extents,aspect='auto',origin='lower',cmap='bwr')
ax2.plot(omega_ms/1e9,omega_ms/1e9,'--',color='yellow',alpha=1,linewidth=5)
plt.colorbar(im)
plt.show()
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso1\omega_ms.txt',omega_ms/1e9)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso1\omega_ps.txt',omega_ps/1e9)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso1\Isos1.txt',Isos1)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso2\omega_ms.txt',omega_ms/1e9)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso2\omega_ps.txt',omega_ps/1e9)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\Iso2\Isos2.txt',Isos2)

# plt.figure(figsize=(18,12))
# ax1 = plt.subplot(231)
# gci1 = ax1.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S12s1))
# ax1.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# # cmap='bwr'
# #
# ax2 = plt.subplot(232)
# gci2 = ax2.pcolor(omega_ms/1e9, omega_ps/1e9,np.transpose(S21s1))
# ax2.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci2)
#
# ax3 = plt.subplot(233)
# gci3 = ax3.pcolor(omega_ms/1e9, omega_ps/1e9,np.transpose(Isos1))
# ax3.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci3)
#
# ax4 = plt.subplot(234)
# gci4 = ax4.pcolor(omega_ms/1e9,omega_ps/1e9, np.transpose(S12s2))
# ax4.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax4.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci4)
# # cmap='bwr'
# #
# ax5 = plt.subplot(235)
# gci5 = ax5.pcolor(omega_ms/1e9, omega_ps/1e9,np.transpose(S21s2))
# ax5.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci5)
#
# ax6 = plt.subplot(236)
# gci6 = ax6.pcolor(omega_ms/1e9, omega_ps/1e9,np.transpose(Isos2))
# ax6.plot(omega_ms/1e9,omega_ms/1e9,'--',color='red',alpha=0.5,linewidth=5)
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci6)
# #
# #
# plt.show()
#
plt.figure(figsize=(12, 6))
axes1 = plt.subplot(111)
axes1.plot(omega_ms/1e9,Isom1,'-',linewidth=5,label='$\delta=3$')
axes1.plot(omega_ms/1e9,Isom2,'-',linewidth=5,label='$\delta=0.28$')
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
plt.tick_params(labelsize=20)
axes1.set_ylim(-20,40)
plt.legend(loc=0,prop={'family':'Cambria','size':20})
plt.show()
# #


print(Isom1[0])
print(Isom2[0])

wm11=[]
wm12=[]
wm13=[]
wm14=[]
wm15=[]
wm16=[]

for i in range(len(omega_ps)):
    wm11.append(omega_ms[0])
    wm12.append(omega_ms[50])
    wm13.append(omega_ms[100])
    wm14.append(omega_ms[150])
    wm16.append(omega_ms[200])