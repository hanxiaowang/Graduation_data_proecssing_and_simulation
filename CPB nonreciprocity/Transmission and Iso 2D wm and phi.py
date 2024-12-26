import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json
from mpl_toolkits.mplot3d import Axes3D


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
omega_m=omega_a-0e6

omega_ps=np.linspace(8.2,8.3,20001)*1e9

delta=2

def S_and_Iso(phi):
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
    phi_s=[]
    for i in range(len(omega_ps)):
        phi_s.append(phi)
    return S12,S21,ISO,phi_s


# phis=np.linspace(-0.5,1.5,361)
phis=np.linspace(0,2,361)


Iso=[]
omega_pp=[]
phiss=[]
# (8.25-omega_ps/1e9)*1e3
Iso_1D=[]
omega_P_1Dlarge=[]
phis_1Dlarge=[]
omega_P_1Dsmall=[]
phis_1Dsmall=[]
Iso_1Dlarge=[]
Iso_1Dsmall=[]
length=50
max_index_need=[]
baseline=[]
for i in range(len(phis)):
    S12, S21, ISO, phi_s = S_and_Iso(phis[i])
    S120, S210, ISO0, phi_s0 = S_and_Iso(0.5)

    Iso_opt=np.abs(ISO)
    max_index = list(Iso_opt).index(max(Iso_opt))
    max_index_need.append(max_index)
    # Iso.append(ISO[max_index-length:max_index+length])
    # omega_pp.append(omega_ps[max_index-length:max_index+length])
    # phiss.append(phi_s[max_index-length:max_index+length])
    Iso.append(ISO)
    omega_pp.append(omega_ps)
    phiss.append(phi_s)
    if ISO[max_index]>0:
        omega_P_1Dlarge.append(omega_ps[max_index])
        phis_1Dlarge.append(phis[i])
        Iso_1Dlarge.append(ISO[max_index])
    else:
        omega_P_1Dsmall.append(omega_ps[max_index])
        phis_1Dsmall.append(phis[i])
        Iso_1Dsmall.append(ISO[max_index])

    Iso_opt0 = np.abs(ISO0)
    max_index0 = list(Iso_opt0).index(max(Iso_opt0))
    baseline.append(ISO0[max_index0])
# plt.figure(figsize=(6, 6))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(phis, (8.25-omega_ps/1e9)*1e3,(Iso),cmap='bwr')
# # ax1.plot(rates,Imax,'--',color='red',alpha=0.5,linewidth=5)
# # ax1.plot(rates,Imin,'--',color='blue',alpha=0.5,linewidth=5)
#
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\delta$',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# plt.show()
zero_need=np.zeros(len(omega_pp))-50
# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([2,3,1])
# for i in range(len(phis)):
#     # print(np.shape(omega_pp[i]))
#     # print(np.shape(phiss[i]))
#     # print(np.shape(Iso[i]))
#     if (Iso[i][max_index_need[i]])>0:
#         ax.plot((8.25-omega_pp[i]/1e9)*1e3,phiss[i],Iso[i],color='red',alpha=0.2)
#     else:
#         ax.plot((8.25-omega_pp[i]/1e9)*1e3,phiss[i],Iso[i],color='blue',alpha=0.2)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=15, azim=17)
# # ax.view_init(elev=7, azim=18)
# plt.show()


# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(phis_1Dlarge,(8.25-np.array(omega_P_1Dlarge)/1e9)*1e3,'s',markersize=10,color='red')
# axes.plot(phis_1Dsmall,(8.25-np.array(omega_P_1Dsmall)/1e9)*1e3,'s',markersize=10,color='blue')
# axes.plot(0.5,0,'*',markersize=50,color='green')
# axes.set_xlabel(r'Evolution times [s]',fontsize=40)
# axes.set_ylabel(r'$|m|^2$',fontsize=40)
# plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.show()
#
# omega_P_1Dlarge.append(omega_ps[max_index])
# phis_1Dlarge.append(phis[i])
# else:
# omega_P_1Dsmall.append(omega_ps[max_index])
# phis_1Dsmall.append(phis[i])

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(phis_1Dlarge,Iso_1Dlarge,'s',markersize=10,color='red',markerfacecolor='None')
axes.plot(phis_1Dsmall,np.abs(Iso_1Dsmall),'s',markersize=10,color='blue',markerfacecolor='None')
axes.plot(phis,baseline,'--',linewidth=3,color='black')

axes.set_xlabel(r'$\varphi$ [s]',fontsize=40)
axes.set_ylabel(r'$Iso$',fontsize=40)
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.show()
#