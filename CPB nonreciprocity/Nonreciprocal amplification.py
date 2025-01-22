import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from mpl_toolkits.mplot3d import Axes3D
import os
import json

k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6

# k_2 = 4.5e6
# k_1 = 5*k_2
# k_3 = 1.33e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a-0e6


##12<21 >>1.6,0.05    10~-50, 20~-40
##12>21 >>2.9,0.9     10~-60, 50~-20
# delta=1.6
# phi=0.05

# delta=2.035
# # phi=0.953
# phi=0.047


phi=0.5
##毕业观察对称情况
# delta=3
# phi=0.965#point1
# phi=0.035#point2
# phi=0.91#point3
# phi=0.09#point4



# omega_ps=8.25e9+np.linspace(-50,50,2001)*1e6
omega_ps=np.linspace(8.2,8.3,10001)*1e9


def S_and_Iso(delta):
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
    delta_s=[]
    for i in range(len(omega_ps)):
        delta_s.append(delta)
    return S12,S21,ISO,delta_s



zeros=[]
for i in range(len(omega_ps)):
    zeros.append(0)

delta1 = 0
S121,S211,ISO1,delta_s1=S_and_Iso(delta1)

delta2 = 1
S122,S212,ISO2,delta_s2=S_and_Iso(delta2)

delta3 = 2
S123,S213,ISO3,delta_s3=S_and_Iso(delta3)

delta4 = 3
S124,S214,ISO4,delta_s4=S_and_Iso(delta4)

delta5 = 4
S125,S215,ISO5,delta_s5=S_and_Iso(delta5)

delta6 = 5
S126,S216,ISO6,delta_s6=S_and_Iso(delta6)

delta7 = 6
S127,S217,ISO7,delta_s7=S_and_Iso(delta7)

delta8 = 7
S128,S218,ISO8,delta_s8=S_and_Iso(delta8)

delta9 = 8
S129,S219,ISO9,delta_s9=S_and_Iso(delta9)

delta10 = 9
S1210,S2110,ISO10,delta_s10=S_and_Iso(delta10)

delta11 = 10
S1211,S2111,ISO11,delta_s11=S_and_Iso(delta11)

# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s1,S121)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s2,S122)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s3,S123)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s4,S124)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s5,S125)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s6,S126)
# ax.set_ylim(0,25)
# ax.set_xlim(-60,60)
# ax.auto_scale_xyz(None,[0,25],None)
# ax.grid(None)
# ax.view_init(elev=19, azim=35)
# # ax.view_init(elev=7, azim=18)
# plt.show()


fig=plt.figure(figsize=(12, 6))
ax=fig.add_subplot(projection='3d')
ax=Axes3D(fig)
fig.add_axes(ax)
ax.set_box_aspect([2,3,1])
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s1,S121)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s2,S122)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s3,S123)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s4,S124)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s5,S125)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s6,S126)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s7,S127)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s8,S128)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s9,S129)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s10,S1210)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s11,S1211)
ax.set_ylim(0,10)
ax.set_xlim(-60,60)
plt.xticks([-50,0,50],['-50','0','50'])

# ax.grid(None)
ax.view_init(elev=15, azim=17)
# ax.view_init(elev=7, azim=18)
plt.show()


# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\omega_ps.txt',omega_ps)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s1.txt',delta_s1)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S121.txt',S121)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s2.txt',delta_s2)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S122.txt',S122)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s3.txt',delta_s3)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S123.txt',S123)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s4.txt',delta_s4)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S124.txt',S124)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s5.txt',delta_s5)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S125.txt',S125)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s6.txt',delta_s6)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S126.txt',S126)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\delta_s7.txt',delta_s7)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12 amp 1d\S127.txt',S127)
#
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot((8.25-omega_ps/1e9)*1e3,S12,'-',linewidth=5,label=r'$S_{12}$',alpha=0.5)
# axes1.plot((8.25-omega_ps/1e9)*1e3,zeros,'--',linewidth=2,color='black')
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# axes1.set_ylim(-60,10)
# plt.xticks([-50,0,50],['-50','0','50'])
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,prop={'family':'Cambria','size':20})
# plt.show()

fig=plt.figure(figsize=(12, 6))
ax=fig.add_subplot(1,1,1,projection='3d')
ax=Axes3D(fig)
fig.add_axes(ax)
ax.set_box_aspect([2,3,1])
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s1,S211)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s2,S212)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s3,S213)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s4,S214)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s5,S215)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s6,S216)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s7,S217)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s8,S218)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s9,S219)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s10,S2110)
ax.plot((8.25-omega_ps/1e9)*1e3,delta_s11,S2111)
ax.set_ylim(0,10)
ax.set_xlim(-60,60)
plt.xticks([-50,0,50],['-50','0','50'])
# ax.grid(None)
ax.view_init(elev=15, azim=17)
# ax.view_init(elev=7, azim=18)
plt.show()

# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([2,3,1])
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s1,ISO1)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s2,ISO2)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s3,ISO3)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s4,ISO4)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s5,ISO5)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s6,ISO6)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s7,ISO7)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s8,ISO8)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s9,ISO9)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s10,ISO10)
# ax.plot((8.25-omega_ps/1e9)*1e3,delta_s11,ISO11)
# ax.set_ylim(0,10)
# ax.set_xlim(-60,60)
# plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=15, azim=17)
# # ax.view_init(elev=7, azim=18)
# plt.show()


# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\omega_ps.txt',omega_ps)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s1.txt',delta_s1)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S211.txt',S211)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s2.txt',delta_s2)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S212.txt',S212)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s3.txt',delta_s3)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S213.txt',S213)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s4.txt',delta_s4)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S214.txt',S214)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s5.txt',delta_s5)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S215.txt',S215)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\delta_s6.txt',delta_s6)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21 amp 1d\S216.txt',S216)


# print(S121[1000])
# print(S122[1000])
# print(S123[1000])
# print(S124[1000])
# print(S125[1000])
# print(S126[1000])
# print(S127[1000])

# delta_ss=np.linspace(0,700,70001)
# S12ss=[]
# S21ss=[]
# Isoss=[]
# zeross=[]
# for i in range(len(delta_ss)):
#     S12s, S21s, ISOs, delta_s = S_and_Iso(delta_ss[i])
#     S12ss.append(S12s[5000])
#     S21ss.append(S21s[5000])
#     Isoss.append(S12s[5000]-S21s[5000])
#     zeross.append(0)
# #
# # index7 = list(delta_ss).index(7)
# # print('max')
# # print(Isoss[index7])
# #
# index12min = list(S12ss).index(min(S12ss))
# index21min = list(S21ss).index(min(S21ss))
#
# print(delta_ss[index12min])
# print(delta_ss[index21min])
#
# print(min(Isoss))
# print(max(Isoss))
# print(min(S12ss))
# print(min(S21ss))

# plt.figure(figsize=(12, 6))
# axes1 = plt.subplot(111)
# axes1.plot(delta_ss,S12ss,'-',linewidth=5,label=r'$S_{12}$',alpha=0.5)
# axes1.plot(delta_ss,S21ss,'-',linewidth=5,label=r'$S_{21}$',alpha=0.5)
# axes1.plot(delta_ss,zeross,'--',linewidth=2,color='black')
# # axes1.plot(delta_ss,Isoss,'-',linewidth=5,label=r'$\text{Iso.   }$',color='green')
# axes1.set_xlabel(r'$\delta$',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,prop={'family':'Cambria','size':20})
# plt.show()
# print(Isoss[-1])
# print(S21ss[0])

# print(S121[1000])
# print(S1211[1000])
# print(S211[1000])
# print(S2111[1000])
#

#
# print(S12ss[-1])
# print(S21ss[-1])



