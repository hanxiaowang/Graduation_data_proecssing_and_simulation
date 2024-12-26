import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

omega_a=8.25e9
omega_m=8.25e9
omega_ps = np.linspace(8.23,8.27, 401) * 1e9
delta_a=omega_a-omega_ps
delta_m=omega_m-omega_ps
kais=np.linspace(1,31,301)*1e6
kap=2e6
kmi=1e6
kmp=2e6
km=kmi+kmp
g_ma = 5e6
Sa=[]
Sm=[]

deltakg=[]

wplus=[]
kplus=[]
wminus=[]
kminus=[]
Sum=[]
for i in range(len(kais)):
    ka=kap+kais[i]
    deltakappa=ka-km
    deltakg.append(deltakappa / (4*g_ma))
    Ra = 1 - kap / (-1j * (omega_ps  - omega_a) + ka / 2 + g_ma ** 2 / (
            -1j * (omega_ps - omega_m) + km / 2))
    Sa.append(rf.mag_2_db(np.abs(Ra)))
    Rm = 1 - kmp / (-1j * (omega_ps - omega_m) + km / 2 + g_ma ** 2 / (
            -1j * (omega_ps - omega_a) + ka / 2))
    Sm.append(rf.mag_2_db(np.abs(Rm)))

    Sum.append(np.abs(Rm)**2+np.abs(Ra)**2)

    chia=omega_a-1j*ka/2
    chim=omega_m-1j*km/2
    same=(chia+chim)/2
    diff=np.sqrt((chia-chim)**2+4*g_ma**2)/2
    chiplus=same+diff
    chiminus=same-diff

    wplus.append(np.real(chiplus)/1e9)
    kplus.append(np.imag(chiplus)*(-2)/1e6)
    wminus.append(np.real(chiminus)/1e9)
    kminus.append(np.imag(chiminus)*(-2)/1e6)

#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(deltakg,wplus,'-',label=r'$\omega_+/2\pi$',color='blue',linewidth=5)
# # axes.plot(deltakg,wminus,'-',label=r'$\omega_-/2\pi$',color='red',linewidth=5)
# # axes.set_ylabel(r'$\omega/2\pi$ [GHz]',fontsize=40)
# axes.plot(deltakg,kplus,'-',label=r'$\kappa_+/2\pi$',color='blue',linewidth=5)
# axes.plot(deltakg,kminus,'-',label=r'$\kappa_-/2\pi$',color='red',linewidth=5)
# axes.set_ylabel(r'$\kappa/2\pi$ [MHz]',fontsize=40)
# axes.set_xlabel(r'$|\kappa_a-\kappa_m|/4g$',fontsize=40)
# plt.tick_params(labelsize=40)
# plt.legend(loc=0,fontsize=40)
# plt.show()


# plt.figure(figsize=(9, 9))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(deltakg,omega_ps/1e9,np.transpose(Sa))
# # gci1 = ax1.pcolor(deltakg,omega_ps/1e9,np.transpose(Sm))
# # gci1 = ax1.pcolor(deltakg,omega_ps/1e9,np.transpose(Sum))
# ax1.set_xlabel(r'$|\kappa_a-\kappa_m|/4g$',fontsize=40)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
# plt.xticks([0,0.2,0.4,0.6,0.8,1,1.2,1.4],['0','0.2','0.4','0.6','0.8','1','1.2','1.4'])
# plt.yticks([8.23,8.24,8.25,8.26,8.27],['8.23','8.24','8.25','8.26','8.27'])
# ax1.tick_params(labelsize=35)
# cbar = plt.colorbar(gci1)
# plt.show()

need_index = deltakg.index(1)

cr=Sa[need_index]
mr=Sm[need_index]

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(deltakg,wplus,'-',label=r'$\omega_+/2\pi$',color='blue',linewidth=5)
# axes.plot(deltakg,wminus,'-',label=r'$\omega_-/2\pi$',color='red',linewidth=5)
# axes.set_ylabel(r'$\omega/2\pi$ [GHz]',fontsize=40)
axes.plot(omega_ps/1e9,cr,'-',label=r'$\kappa_+/2\pi$',color='blue',linewidth=5)
axes.plot(omega_ps/1e9,mr,'-',label=r'$\kappa_-/2\pi$',color='red',linewidth=5)
axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
axes.set_ylabel(r'$S_{11}$ [dB]',fontsize=40)
plt.tick_params(labelsize=40)
# plt.legend(loc=0,fontsize=40)
plt.show()
