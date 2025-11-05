import numpy as np
import matplotlib.pyplot as plt
import Curve_decay_func

drive_fre_for=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\drive fre.txt')
drive_power_for=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\drive power.txt')
vna_fre_for=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\vna fre.txt')
Delta_omega_up_for=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\Bistability UP change fre 2D forward 11-21-59\Delta omega up.txt',delimiter=',')


drive_fre_back=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230411\Bistability UP change fre 2D backward 0-35-21\drive fre.txt')
drive_power_back=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230411\Bistability UP change fre 2D backward 0-35-21\drive power.txt')
vna_fre_back=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230411\Bistability UP change fre 2D backward 0-35-21\vna fre.txt')
Delta_omega_up_back=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230411\Bistability UP change fre 2D backward 0-35-21\Delta omega up.txt',delimiter=',')

D_E_for=[]
D_T_for=[]
D_X_for=[]

D_E_back=[]
D_T_back=[]
D_X_back=[]


D_E_delta=[]
D_T_delta=[]
D_X_delta=[]
for i in range(len(drive_power_for)):
    Decay_exp_for=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power_for[i],1)}mW\\Kappa_experiment.txt')
    Decay_th_for=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power_for[i],1)}mW\\Kappa_theory.txt')
    Decay_xz_for=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230410\\Bistability UP change fre 2D forward 11-21-59\\drive power={round(drive_power_for[i],1)}mW\\Kappa_xiuzheng.txt')
    D_E_for.append(Decay_exp_for)
    D_T_for.append(Decay_th_for)
    D_X_for.append(Decay_xz_for)

    Decay_exp_back = np.loadtxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230411\\Bistability UP change fre 2D backward 0-35-21\\drive power={round(drive_power_back[i], 1)}mW\\Kappa_experiment.txt')
    Decay_th_back = np.loadtxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230411\\Bistability UP change fre 2D backward 0-35-21\\drive power={round(drive_power_back[i], 1)}mW\\Kappa_theory.txt')
    Decay_xz_back = np.loadtxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230411\\Bistability UP change fre 2D backward 0-35-21\\drive power={round(drive_power_back[i], 1)}mW\\Kappa_xiuzheng.txt')
    D_E_back.append(Decay_exp_back)
    D_T_back.append(Decay_th_back)
    D_X_back.append(Decay_xz_back)

    D_E_delta.append(Decay_exp_for-Decay_exp_back)
    D_T_delta.append(Decay_th_for-Decay_th_back)
    D_X_delta.append(Decay_xz_for-Decay_xz_back)





plt.figure(figsize=(18,6))
ax1 = plt.subplot(231)
gci1 = ax1.pcolor(drive_fre_for,drive_power_for, D_E_for)
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax1.set_ylabel(r'$\omega_d/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci1)
# cmap='bwr'
#
ax2 = plt.subplot(232)
gci2 = ax2.pcolor(drive_fre_for,drive_power_for, D_T_for)
ax2.set_xlabel(r'$P_d$[mW]',fontsize=20)
# ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci2)

ax3 = plt.subplot(233)
gci3 = ax3.pcolor(drive_fre_for,drive_power_for, D_X_for)
# ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci3)

ax4 = plt.subplot(234)
gci4 = ax4.pcolor(drive_fre_back,drive_power_back, D_E_back)
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax4.set_ylabel(r'$\omega_d/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci4)
# cmap='bwr'
#
ax5 = plt.subplot(235)
gci5 = ax5.pcolor(drive_fre_back,drive_power_back, D_T_back)
ax5.set_xlabel(r'$P_d$[mW]',fontsize=20)
# ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci5)

ax6 = plt.subplot(236)
gci6 = ax6.pcolor(drive_fre_back,drive_power_back, D_X_back)
# ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci6)

plt.show()



plt.figure(figsize=(18,6))
ax1 = plt.subplot(131)
gci1 = ax1.pcolor(drive_fre_for,drive_power_for, D_E_delta)
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax1.set_ylabel(r'$\omega_d/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci1)
# cmap='bwr'
#
ax2 = plt.subplot(132)
gci2 = ax2.pcolor(drive_fre_for,drive_power_for, D_T_delta)
ax2.set_xlabel(r'$P_d$[mW]',fontsize=20)
# ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci2)

ax3 = plt.subplot(133)
gci3 = ax3.pcolor(drive_fre_for,drive_power_for, D_X_delta)
# ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=10)
cbar = plt.colorbar(gci3)

plt.show()


j=20
plt.figure(figsize=(12 , 9))
axes1 = plt.subplot(311)
axes1.patch.set_alpha(0)
axes1.plot(drive_fre_for,D_E_delta[j],'o',linewidth=3,label=r'$k_{exp}$',color='blue',alpha=0.4)
axes1.plot(drive_fre_for,D_T_delta[j],'-',linewidth=3,label=r'$k_{sim}$',color='red',alpha=0.4)
axes1.plot(drive_fre_for,D_X_delta[j],'-',linewidth=3,label=r'$k_{xiuzheng}$',color='green',alpha=0.4)
axes1.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes1.set_ylabel(r'$\kappa/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=20)
plt.legend(loc=0)

axes2 = plt.subplot(312)
axes2.patch.set_alpha(0)
axes2.plot(drive_fre_for,D_X_delta[j]-D_T_delta[j],'-',linewidth=3,label=r'$\delta\kappa$',color='blue',alpha=0.4)
axes2.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes2.set_ylabel(r'$\delta_\kappa/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.legend(loc=0)


axes3 = plt.subplot(313)
axes3.patch.set_alpha(0)
axes3.plot(drive_fre_for,D_X_delta[j]-D_E_delta[j],'-',linewidth=3,label=r'$w_{exp}$',color='blue',alpha=0.4)
axes3.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
axes3.set_ylabel(r'$\omega_+/2\pi$ [MHz]',fontsize=10)
plt.tick_params(labelsize=10)
plt.legend(loc=0)
plt.show()
#