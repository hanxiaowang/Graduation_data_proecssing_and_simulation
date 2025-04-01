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

deltas=np.linspace(0,7,14001)
phi=0.75

omega_ps=8.25e9+np.linspace(-50,50,100001)*1e6

S12s1=[]
S21s1=[]
Isos1=[]
Isom=[]
max_deltaa=[]
min_deltaa=[]
max_Iso=[]
min_Iso=[]

max_S12=[]
min_S12=[]
max_S21=[]
min_S21=[]

max_deltaa_delta=[]
min_deltaa_delta=[]
for i,delta in enumerate(deltas):
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
    ISO=S21-S12
    S12s1.append(S12)
    S21s1.append(S21)
    Isos1.append(ISO)
    Iso_opt=np.abs(ISO)
    max_index = list(Iso_opt).index(max(Iso_opt))
    # Isom.append(ISO[1001])
    if ISO[max_index] >= 0:
        max_deltaa.append(omega_ps[max_index])
        max_deltaa_delta.append(delta)
        max_Iso.append(ISO[max_index])
        max_S12.append(S12[max_index])
        max_S21.append(S21[max_index])

    if ISO[max_index] < 0:
        min_deltaa.append(omega_ps[max_index])
        min_deltaa_delta.append(delta)
        min_Iso.append(ISO[max_index])
        min_S12.append(S12[max_index])
        min_S21.append(S21[max_index])
#
# max_index = list(Isos1).index(max(Isom))
# min_index = list(Isos1).index(min(Isom))

# print(phis[max_index])
# print(phis[min_index])

max_deltaa_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'max_deltaa.txt')
max_deltaa_delta_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'max_deltaa_delta.txt')
max_Iso_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'max_Iso.txt')
min_deltaa_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'min_deltaa.txt')
min_deltaa_delta_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'min_deltaa_delta.txt')
min_Iso_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'min_Iso.txt')
max_S12_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'max_S12.txt')
min_S12_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'min_S12.txt')
max_S21_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'max_S21.txt')
min_S21_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta', 'min_S21.txt')


np.savetxt(max_deltaa_path, max_deltaa, fmt='%.4f')
np.savetxt(max_deltaa_delta_path, max_deltaa_delta, fmt='%.4f')
np.savetxt(max_Iso_path, max_Iso, fmt='%.4f')
np.savetxt(min_deltaa_path, min_deltaa, fmt='%.4f')
np.savetxt(min_deltaa_delta_path, min_deltaa_delta, fmt='%.4f')
np.savetxt(min_Iso_path, min_Iso, fmt='%.4f')
np.savetxt(max_S12_path, max_S12, fmt='%.4f')
np.savetxt(min_S12_path, min_S12, fmt='%.4f')
np.savetxt(max_S21_path, max_S21, fmt='%.4f')
np.savetxt(min_S21_path, min_S21, fmt='%.4f')

# ISO at wp=wm vs phi
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(phis,Isom,'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\phi/\pi$ [GHz]',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
#
# plt.show()

# ISO at some phi vs wp
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


## S12,S21 and ISO vs phi and wm
#
extents=[deltas[0],deltas[-1],(omega_a-omega_ps)[0]/1e9,(omega_a-omega_ps)[-1]/1e9]

# plt.figure(figsize=(6,6))
# ax1=plt.subplot(111)
# im = ax1.imshow(np.transpose(S12s1), extent=extents,aspect='auto',origin='lower')
# plt.tick_params(labelsize=10)
# ax1.set_xlabel(r'$\delta$',fontsize=10)
# ax1.set_ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
# plt.colorbar(im)
# plt.show()
#
plt.figure(figsize=(6,6))

ax2 = plt.subplot(111)
im = ax2.imshow(np.transpose(S21s1), extent=extents,aspect='auto',origin='lower')

ax2.set_xlabel(r'$\delta$',fontsize=10)
ax2.set_ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.colorbar(im)
plt.show()
# #
# plt.figure(figsize=(6,6))
#
# ax3 = plt.subplot(111)
# im = ax3.imshow(np.transpose(Isos1),cmap='bwr', extent=extents,aspect='auto',origin='lower')
# # ax3.plot(max_deltaa_delta,(omega_a-np.array(max_deltaa))/1e9,'o',color='green',markersize=1)
# # ax3.plot(min_deltaa_delta,(omega_a-np.array(min_deltaa))/1e9,'o',color='green',markersize=1,alpha=0.5)
#
# ax3.set_xlabel(r'$\delta$',fontsize=10)
# ax3.set_ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.colorbar(im)
# plt.show()



# max_index1=list(max_Iso).index(max(max_Iso))
# print(omega_a-max_deltaa[max_index1])
# print(max_deltaa_delta[max_index1])
# print(max_Iso[max_index1])
#
# min_index1=list(min_Iso).index(min(min_Iso))
# print(omega_a-min_deltaa[min_index1])
# print(min_deltaa_delta[min_index1])
# print(min_Iso[min_index1])


# phis=np.linspace(-0.5,1.5,361)
# phi_max=[]
# omega_max=[]
# phi_min=[]
# omega_min=[]
# for j in range(len(phis)):
#     S12s1=[]
#     S21s1=[]
#     Isos1=[]
#     Isom=[]
#     max_deltaa=[]
#     min_deltaa=[]
#     max_Iso=[]
#     min_Iso=[]
#     max_deltaa_delta=[]
#     min_deltaa_delta=[]
#     for i,delta in enumerate(deltas):
#         delta_m = omega_m - omega_ps
#         delta_a = omega_a - omega_ps
#         chi_a = 1j * delta_a + k_c / 2
#         chi_m = 1j * delta_m + gamma / 2
#         fenmu = chi_a * chi_m + g ** 2
#
#         fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
#             -1j * phis[j] * np.pi)
#         fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
#             -1j * phis[j] * np.pi)
#
#         t12 = fenzi12 / fenmu
#         t21 = fenzi21 / fenmu
#         S12 = rf.mag_2_db(np.abs(t12))
#         S21 = rf.mag_2_db(np.abs(t21))
#         ISO=S21-S12
#         S12s1.append(S12)
#         S21s1.append(S21)
#         Isos1.append(ISO)
#         Iso_opt=np.abs(ISO)
#         max_index = list(Iso_opt).index(max(Iso_opt))
#         # Isom.append(ISO[1001])
#         if ISO[max_index] >= 0:
#             max_deltaa.append(omega_ps[max_index])
#             max_deltaa_delta.append(delta)
#             max_Iso.append(ISO[max_index])
#         if ISO[max_index] < 0:
#             min_deltaa.append(omega_ps[max_index])
#             min_deltaa_delta.append(delta)
#             min_Iso.append(ISO[max_index])
#
#     if len(max_Iso)!=0:
#         max_index1 = list(max_Iso).index(max(max_Iso))
#         phi_max.append(phis[j])
#         omega_max.append(max_deltaa[max_index1])
#     if len(min_Iso)!=0:
#         min_index1 = list(min_Iso).index(min(min_Iso))
#         phi_min.append(phis[j])
#         omega_min.append(min_deltaa[min_index1])
# # print(max_deltaa)
# # print(max_index1)
# # print(min_index1)
# # print(min_deltaa)
# plt.figure(figsize=(6,6))
# #
# plt.plot(phi_max,(omega_a-np.array(omega_max))/1e9,'s',color='red',markersize=5,markerfacecolor='None')
# plt.plot(phi_min,(omega_a-np.array(omega_min))/1e9,'o',color='green',markersize=5,markerfacecolor='None')
#
# # plt.xlabel(r'$\delta$',fontsize=10)
# # plt.ylabel(r'$\delta_a/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()