import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

k_int = 1.4e6
k_2 = 4.5e6
# k_2 = 50e6

# rates=np.linspace(0.01,50,501)
rates=np.linspace(0.1,15,150)
k_1 = rates*k_2
# k_1 = 40e6

# k_3 = 1.33e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a

deltas=np.linspace(0,7,351)
phi=0.5

omega_ps=omega_a

S12s1=[]
S21s1=[]
Isos1=[]
Isom=[]

zerodelta12=[]
zerorate12=[]
zerodelta21=[]
zerorate21=[]
for i, delta in enumerate(deltas):
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
    S12s1.append(S12)
    S21s1.append(S21)
    Isos1.append(ISO)



## 透射能谱为0
# print(S12s1)
threshold1=5e-1
Sthre=[]
for i in range(len(rates)):
    t=np.abs(np.array(S12s1)[:,i])
    index = list(t).index(min(t))
    if (S12s1[index][i])<0 and np.abs(S12s1[index][i])<threshold1:
        zerodelta12.append(deltas[index])
        zerorate12.append(rates[i])
        Sthre.append(S12s1[index][i])
    if (S12s1[index][i]) > 0 and np.abs(S12s1[index][i]) <threshold1:
        zerodelta12.append(deltas[index-1])
        zerorate12.append(rates[i])
        Sthre.append(S12s1[index][i])
    # for j in range(len(rates)):
    #     if np.abs(S12s1[i][j]) < 3.5e-3:
    #         zerodelta12.append(deltas[i])
    #         zerorate12.append(rates[j])
# print(Sthre)

threshold2=1e-2
for i in range(len(rates)):
    t=np.abs(np.array(S21s1)[:,i])
    index = list(t).index(min(t))
    if (S21s1[index][i])<0 and np.abs(S21s1[index][i])<threshold2:
        zerodelta21.append(deltas[index])
        zerorate21.append(rates[i])
        Sthre.append(S21s1[index][i])
    if (S21s1[index][i]) > 0 and np.abs(S21s1[index][i]) <threshold2:
        zerodelta21.append(deltas[index-1])
        zerorate21.append(rates[i])
        Sthre.append(S21s1[index][i])

# print(np.shape(S12s1))
# print(S12s1[182][499])
# print(S12s1[181][499])
# print(zerorate12)
# plt.figure(figsize=(15, 5))
# axes1 = plt.subplot(111)
# axes1.plot(zerorate12,zerodelta12,'-',color='blue',marker='o',markersize=10,linewidth=5,label='S12')
# axes1.plot(zerorate21,zerodelta21,'-',color='red',linewidth=5,label='S21')
# axes1.set_xlabel(r'$rate$',fontsize=10)
# axes1.set_ylabel(r'$\delta$',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.legend(loc=0,fontsize=10)
# plt.show()
# print(type(Isos1))

print(np.shape(Isos1))
S12s2=np.array(S12s1)
S21s2=np.array(S21s1)
Isos2=np.array(Isos1)
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
# print(delta[max_index])
#
# print(delta[0])
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(delta,Isos1[90],'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\delta$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()

# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# # axes1.plot(rates,Isos1[27],'-',linewidth=5,label='Iso')
# # axes1.plot(rates,S12s1[27],'-',linewidth=5,label='S12')
# axes1.plot(rates,S21s1[27],'-',linewidth=5,label='S21')
#
# axes1.set_xlabel(r'$\delta$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(deltas,Isos2[:,100],'-',linewidth=5,label='Iso')
# # axes1.plot(deltas,S12s2[:,100],'-',linewidth=5,label='S12')
# # axes1.plot(deltas,S21s2[:,100],'-',linewidth=5,label='S21')
#
# axes1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()

# print(rates)




## ISO max and ISO min vs k1/k2

Imax=[]
Imin=[]
for i in range(len(rates)):
    if rates[i]==1.00:
        Imax.append(Imin[i-5])
        Imin.append(Imin[i-5])
        print('yes')
    else:
        max_index = list(Isos2[:,i]).index(max(Isos2[:,i]))
        min_index = list(Isos2[:,i]).index(min(Isos2[:,i]))
        Imax.append(deltas[max_index])
        Imin.append(deltas[min_index])

print(Imin[0])
    # max_index = list(Isos2[:,i]).index(max(Isos2[:,i]))
    # min_index = list(Isos2[:,i]).index(min(Isos2[:,i]))
    # Imax.append(deltas[max_index])
    # Imin.append(deltas[min_index])


# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(rates,Imax,'-',linewidth=5,label='Iso')
# axes1.plot(rates,Imin,'-',linewidth=5,label='Iso')
# axes1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()




# print(S12s1[-1][-1])
# ##S12, S21 and ISO va delta and k1/k2
# #
# plt.figure(figsize=(24,5))
# ax1 = plt.subplot(131)
# gci1 = ax1.pcolor(rates,deltas, (S12s1))
# ax1.plot(rates,Imin,'--',color='red')
# ax1.plot(zerorate12,zerodelta12,'-',linewidth=3,color='blue')
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\delta$',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
#
# ax2 = plt.subplot(132)
# gci2 = ax2.pcolor(rates,deltas,(S21s1))
# ax2.plot(rates,Imax,'--',color='red')
# ax2.plot(zerorate21,zerodelta21,'-',linewidth=3,color='blue')
#
# # ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci2)
#
# ax3 = plt.subplot(133)
# gci3 = ax3.pcolor(rates, deltas,(Isos1))
# ax3.plot(rates,Imax,'--',color='red')
# ax3.plot(rates,Imin,'--',color='red')
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# ax1.set_xlabel(r'$\kappa_1/\kappa_2$',fontsize=20)
# cbar = plt.colorbar(gci3)
# #
# plt.show()

plt.figure(figsize=(6, 6))
ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(rates,deltas, (S12s1),cmap='spring')
# # ax1.plot(rates,Imin,'--',color='red')
# ax1.plot(zerorate12,zerodelta12,'-',linewidth=3,color='blue')

# gci1 = ax1.pcolor(rates,deltas,(S21s1),cmap='spring')
# # ax1.plot(rates,Imax,'--',color='red')
# ax1.plot(zerorate21,zerodelta21,'-',linewidth=3,color='blue')
#
gci1 = ax1.pcolor(rates, deltas,(Isos1),cmap='bwr')
ax1.plot(rates,Imax,'--',color='red',alpha=0.5,linewidth=5)
ax1.plot(rates,Imin,'--',color='blue',alpha=0.5,linewidth=5)

ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax1.set_ylabel(r'$\delta$',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci1)
plt.show()
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\rates.txt',rates)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\deltas.txt',deltas)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\S21s1.txt',S21s1)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\Imax.txt',Imax)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\Imin.txt',Imin)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\zerorate21.txt',zerorate21)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S21\zerodelta21.txt',zerodelta21)

# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\rates.txt',rates)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\deltas.txt',deltas)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\S12s1.txt',S12s1)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\Imax.txt',Imax)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\Imin.txt',Imin)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\zerorate21.txt',zerorate12)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\try txt\S12\zerodelta21.txt',zerodelta12)

# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(deltas,np.array(S12s1)[:,0],'-',linewidth=5,label='S12')
# axes1.plot(deltas,np.array(S21s1)[:,0],'-',linewidth=5,label='S21')
# axes1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()

# z1=np.polyfit(rates,Imax,2)
# p1=np.poly1d(z1)
# print(p1)
# y_pre=p1(rates)
#
# z1=np.polyfit(Imax,rates,4)
# p1=np.poly1d(z1)
# print(p1)
# y_pre=p1(Imax)
#
# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(121)
# axes1.plot(rates,Imax,'-',linewidth=5,label='Sim')
# axes1.plot(rates,y_pre,'-',linewidth=5,label='curvefit')
# axes1.set_xlabel(r'$\kappa_1/\kappa_2$ ',fontsize=40)
# axes1.set_ylabel(r'$ISO$ [dB]',fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=0,fontsize=10)
# plt.show()
# print(Imax)