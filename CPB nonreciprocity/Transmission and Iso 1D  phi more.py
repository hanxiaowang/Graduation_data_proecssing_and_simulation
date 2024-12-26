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

omega_ps=np.linspace(8.2,8.3,2001)*1e9

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


delta1 = 0
S121,S211,ISO1,phi_s1=S_and_Iso(delta1)

delta2 = 0.25
S122,S212,ISO2,phi_s2=S_and_Iso(delta2)

delta3 = 0.5
S123,S213,ISO3,phi_s3=S_and_Iso(delta3)

delta4 = 0.75
S124,S214,ISO4,phi_s4=S_and_Iso(delta4)

delta5 = 1
S125,S215,ISO5,phi_s5=S_and_Iso(delta5)

delta6 = 1.25
S126,S216,ISO6,phi_s6=S_and_Iso(delta6)

delta7 = 1.5
S127,S217,ISO7,phi_s7=S_and_Iso(delta7)

delta8 = 1.75
S128,S218,ISO8,phi_s8=S_and_Iso(delta8)

delta9 = 2
S129,S219,ISO9,phi_s9=S_and_Iso(delta9)


ISOS=[ISO1,ISO2,ISO3,ISO4,ISO5,ISO6,ISO7,ISO8,ISO9]
ISOline=[]
philine=[]
deltaline=[]



for i in range(9):
    max_index = list(np.abs(ISOS[i])).index(max(np.abs(ISOS[i])))

    ISOline.append(-15)
    philine.append(i*0.25)
    deltaline.append(omega_ps[max_index])

# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([2,5,1])
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s1,S121)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s2,S122)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s3,S123)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s4,S124)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s5,S125)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s6,S126)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s7,S127)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s8,S128)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s9,S129)
#
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s1,S211)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s2,S212)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s3,S213)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s4,S214)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s5,S215)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s6,S216)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s7,S217)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s8,S218)
# # ax.plot((8.25-omega_ps/1e9)*1e3,phi_s9,S219)
#
#
#
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s1,ISO1)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s2,ISO2)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s3,ISO3)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s4,ISO4)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s5,ISO5)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s6,ISO6)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s7,ISO7)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s8,ISO8)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s9,ISO9)
# ax.plot((8.25-np.array(deltaline)/1e9)*1e3,philine,ISOline,'-s',markersize=5,color='black')
#
# ax.set_ylim(0,2)
# ax.set_xlim(-60,60)
# plt.xticks([-50,0,50],['-50','0','50'])
#
# # ax.grid(None)
# ax.view_init(elev=15, azim=17)
# # ax.view_init(elev=7, azim=18)
# plt.show()


# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([2,3,1])
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s1,ISO1)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s2,ISO2)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s3,ISO3)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s4,ISO4)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s5,ISO5)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s6,ISO6)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s7,ISO7)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s8,ISO8)
# ax.plot((8.25-omega_ps/1e9)*1e3,phi_s9,ISO9)
# ax.set_ylim(0,10)
# ax.set_xlim(-60,60)
# plt.xticks([-50,0,50],['-50','0','50'])
#
# # ax.grid(None)
# ax.view_init(elev=15, azim=17)
# # ax.view_init(elev=7, azim=18)
# plt.show()
picture1=np.linspace(-15,25,401)
p1sy=[]
for i in range(len(picture1)):
    p1sy.append(0)


# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot((8.25-omega_ps/1e9)*1e3,ISO1,'-',alpha=0.5,label=r'$\varphi=0$',linewidth=10)
# # axes.plot((8.25-omega_ps/1e9)*1e3,ISO5,'-',alpha=0.5,label=r'$\varphi=\pi$',linewidth=10)
# # axes.plot(p1sy,picture1,'--',color='black',label=r'$\delta_a=0$',linewidth=5)
#
# # (-15,15)
# axes.plot((8.25-omega_ps/1e9)*1e3,ISO2,'-',alpha=0.5,label=r'$\varphi=025\pi$',linewidth=10)
# axes.plot((8.25-omega_ps/1e9)*1e3,ISO4,'-',alpha=0.5,label=r'$\varphi=0.75\pi$',linewidth=10)
# axes.plot(p1sy,picture1,'--',color='black',label=r'$\delta_a=0$',linewidth=5)
# plt.ylim(-16,26)
# # (-5,20)
# axes.set_xlabel(r'$\varphi$ [s]',fontsize=40)
# axes.set_ylabel(r'$Iso$',fontsize=40)
# # plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.legend(fontsize=20)
# plt.show()


# max_index1 = list(ISO1).index(max(ISO1))
# min_index1 = list(ISO1).index(min(ISO1))
# print('max')
# print((8.25-omega_ps[max_index1]/1e9)*1e3)
# print(ISO1[max_index1])
# print('min')
# print((8.25-omega_ps[min_index1]/1e9)*1e3)
# print(ISO1[min_index1])

# max_index3 = list(ISO3).index(max(ISO3))
# min_index3 = list(ISO3).index(min(ISO3))
# print('max')
# print((8.25-omega_ps[max_index3]/1e9)*1e3)
# print(ISO3[max_index3])
# print('min')
# print((8.25-omega_ps[min_index3]/1e9)*1e3)
# print(ISO3[min_index3])

max_index7 = list(ISO7).index(max(ISO7))
min_index7 = list(ISO7).index(min(ISO7))
print('max')
print((8.25-omega_ps[max_index7]/1e9)*1e3)
print(ISO7[max_index7])
print('min')
print((8.25-omega_ps[min_index7]/1e9)*1e3)
print(ISO7[min_index7])

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot((8.25-omega_ps/1e9)*1e3,ISO1,'-',alpha=0.5,label=r'$\varphi=0$',linewidth=10)
# axes.plot((8.25-omega_ps/1e9)*1e3,ISO3,'-',alpha=0.5,label=r'$\varphi=0.5\pi$',linewidth=10)
axes.plot((8.25-omega_ps/1e9)*1e3,ISO7,'-',alpha=0.5,label=r'$\varphi=1.5\pi$',linewidth=10)

# axes.plot((8.25-omega_ps/1e9)*1e3,ISO5,'-',alpha=0.5,label=r'$\varphi=\pi$',linewidth=10)
# axes.plot(p1sy,picture1,'--',color='black',label=r'$\delta_a=0$',linewidth=5)

# (-15,15)
# (-5,20)
axes.set_xlabel(r'$\varphi$ [s]',fontsize=40)
axes.set_ylabel(r'$Iso$',fontsize=40)
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.legend(fontsize=20)
plt.show()