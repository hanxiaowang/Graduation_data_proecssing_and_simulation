import numpy as np
import matplotlib.pyplot as plt
import Curve_decay_func



drive_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\drive fre.txt')
drive_power=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\drive power.txt')
vna_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\vna fre.txt')
Delta_omega_up=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\Delta omega up.txt',delimiter=',')
print(len(drive_fre))
D_E=[]
D_T=[]
D_X=[]
for i in range(len(drive_power)):
    Decay_exp=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power[i],1)}mW\\Kappa_experiment.txt')
    Decay_th=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power[i],1)}mW\\Kappa_theory.txt')
    Decay_xz=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power[i],1)}mW\\Kappa_xiuzheng.txt')
    D_E.append(Decay_exp)
    D_T.append(Decay_th)
    D_X.append(Decay_xz)
print(np.shape(D_E))
print(np.shape(D_T))
print(np.shape(D_X))

# plt.figure(figsize=(18,6))
# ax1 = plt.subplot(131)
# gci1 = ax1.pcolor(drive_fre,drive_power, D_E)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_d/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=10)
# cbar = plt.colorbar(gci1)
# # cmap='bwr'
# #
# ax2 = plt.subplot(132)
# gci2 = ax2.pcolor(drive_fre,drive_power, D_T)
# ax2.set_xlabel(r'$P_d$[mW]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=10)
# cbar = plt.colorbar(gci2)
#
# ax3 = plt.subplot(133)
# gci3 = ax3.pcolor(drive_fre,drive_power, D_X)
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=10)
# cbar = plt.colorbar(gci3)
#
# plt.show()
print(np.shape(D_E))
j=50
plt.figure(figsize=(12 , 9))
axes1 = plt.subplot(311)
axes1.patch.set_alpha(0)
axes1.plot(drive_fre,D_E[j],'o',linewidth=3,label=r'$k_{exp}$',color='blue',alpha=0.4)
axes1.plot(drive_fre,D_T[j],'-',linewidth=3,label=r'$k_{sim}$',color='red',alpha=0.4)
axes1.plot(drive_fre,D_X[j],'-',linewidth=3,label=r'$k_{xiuzheng}$',color='green',alpha=0.4)
axes1.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes1.set_ylabel(r'$\kappa/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=20)
plt.legend(loc=0)

axes2 = plt.subplot(312)
axes2.patch.set_alpha(0)
axes2.plot(drive_fre,D_X[j]-D_T[j],'-',linewidth=3,label=r'$\delta\kappa$',color='blue',alpha=0.4)
axes2.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes2.set_ylabel(r'$\delta_\kappa/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.legend(loc=0)


axes3 = plt.subplot(313)
axes3.patch.set_alpha(0)
axes3.plot(drive_fre,D_X[j]-D_E[j],'-',linewidth=3,label=r'$w_{exp}$',color='blue',alpha=0.4)
axes3.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes3.set_ylabel(r'$\omega_+/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.legend(loc=0)
plt.show()
#

