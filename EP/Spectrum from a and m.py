import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import cmath

omega_a=8.25e9
omega_m=8.25e9
omega_ps = np.linspace(8.23,8.27, 401) * 1e9
delta_a=omega_a-omega_ps
delta_m=omega_m-omega_ps
kais=np.linspace(1,101,1001)*1e6
kap=2e6
kmi=1e6
kmp=2e6
km=kmi+kmp
g_ma = 5e6
Sa=[]
Sm=[]
Pa=[]
Pm=[]

Tam=[]
Tma=[]
PTam=[]
PTma=[]

Tauam=[]
Tauma=[]



deltakchug=((kais+kap)-(kmi+kmp))/(4*g_ma)
index_need=np.where(deltakchug==1)
print(index_need)
OneforEP=np.ones(len(omega_ps))
# print(OneforEP)

for i in range(len(kais)):


    chi_a = 1j * delta_a + (kais[i]+kap) / 2
    chi_m = 1j * delta_m + kmi+kmp / 2

    ta=1-kap/(chi_a+g_ma**2/chi_m)
    tm=1-kmp/(chi_m+g_ma**2/chi_a)

    tam=np.sqrt(kap*kmp)/(chi_a+g_ma**2/chi_m)
    tma = np.sqrt(kap * kmp) / (chi_m + g_ma ** 2 / chi_a)

    Sa.append(rf.mag_2_db(np.abs(ta)))
    Sm.append(rf.mag_2_db(np.abs(tm)))
    Tam.append(rf.mag_2_db(np.abs(tam)))
    Tma.append(rf.mag_2_db(np.abs(tma)))
    pa=[]
    pm=[]
    pam = []
    pma = []
    for j in range(len(omega_ps)):
        pa.append(cmath.phase(ta[j]))
        pm.append(cmath.phase(tm[j]))
        pam.append(cmath.phase(tam[j]))
        pma.append(cmath.phase(tma[j]))

    tauam=[]
    tauma=[]
    for k in range(len(omega_ps)-1):
        tauam.append((pam[k+1]-pam[k])/(omega_ps[k+1]-omega_ps[k]))
        tauma.append((pma[k+1]-pma[k])/(omega_ps[k+1]-omega_ps[k]))

    Tauam .append(tauam)
    Tauma .append(tauma)
    Pa.append(pa)
    Pm.append(pm)
    PTam.append(pam)
    PTma.append(pma)

##  反射
# plt.figure(figsize=(24,12))
# extents=[deltakchug[0],deltakchug[-1],omega_ps [0],omega_ps [-1]]
#
# ax1 = plt.subplot(221)
# im1 = ax1.imshow(np.transpose(Sa), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
# plt.colorbar(im1)
#
# ax2 = plt.subplot(222)
# im2 = ax2.imshow(np.transpose(Sm), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
# plt.colorbar(im2)
#
# ax3 = plt.subplot(223)
# im3 = ax3.imshow(np.transpose(Pa), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
# plt.colorbar(im3)
#
# ax4 = plt.subplot(224)
# im4 = ax4.imshow(np.transpose(Pm), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
# plt.colorbar(im4)
# plt.show()
#
#
# target=200
# #200 EP
# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,Sa[target],'-',linewidth=10,label=r'$Sa$',color='red',alpha=1)
# axes1.plot(omega_ps,Sm[target],'-',linewidth=3,label=r'$Sm$',color='blue',zorder=2)
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()
#
# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,Pa[target],'-',linewidth=10,label=r'$Pa$',color='red',alpha=1)
# axes1.plot(omega_ps,Pm[target],'-',linewidth=3,label=r'$Pm$',color='blue',zorder=2)
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$Phase$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()

## 透射
# plt.figure(figsize=(24,12))
# extents=[deltakchug[0],deltakchug[-1],omega_ps [0],omega_ps [-1]]
#
# ax1 = plt.subplot(221)
# im1 = ax1.imshow(np.transpose(Tam), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
# plt.colorbar(im1)
#
# ax2 = plt.subplot(222)
# im2 = ax2.imshow(np.transpose(Tma), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
# plt.colorbar(im2)
#
# ax3 = plt.subplot(223)
# im3 = ax3.imshow(np.transpose(PTam), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
# plt.colorbar(im3)
#
# ax4 = plt.subplot(224)
# im4 = ax4.imshow(np.transpose(PTma), extent=extents, aspect='auto',origin='lower')
# plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
# plt.colorbar(im4)
# plt.show()
#
#
target=300
# #200 EP
# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,Tam[target],'-',linewidth=10,label=r'$Tam$',color='red',alpha=1)
# axes1.plot(omega_ps,Tma[target],'-',linewidth=3,label=r'$Tma$',color='blue',zorder=2)
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()
#
# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,PTam[target],'-',linewidth=10,label=r'$PTam$',color='red',alpha=1)
# axes1.plot(omega_ps,PTma[target],'-',linewidth=3,label=r'$PTma$',color='blue',zorder=2)
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$Phase$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()
#
# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,PTma[0],'-',linewidth=3,label=r'$0$')
# axes1.plot(omega_ps,PTma[100],'-',linewidth=3,label=r'$1$')
# axes1.plot(omega_ps,PTma[200],'-',linewidth=3,label=r'$2$')
# axes1.plot(omega_ps,PTma[1000],'-',linewidth=3,label=r'$3$')
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$Phase$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()

# fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.plot(omega_ps,PTam[0],'-',linewidth=3,label=r'$0$')
# axes1.plot(omega_ps,PTam[100],'-',linewidth=3,label=r'$1$')
# axes1.plot(omega_ps,PTam[200],'-',linewidth=3,label=r'$2$')
# axes1.plot(omega_ps,PTam[1000],'-',linewidth=3,label=r'$3$')
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$Phase$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()


omega_pa1=omega_ps[0:-2]
fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(Tauam[0],'-',linewidth=3,label=r'$0$')
axes1.plot(Tauam[100],'-',linewidth=3,label=r'$1$')
axes1.plot(Tauam[200],'-',linewidth=3,label=r'$2$')
axes1.plot(Tauam[300],'-',linewidth=3,label=r'$3$')
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$Phase$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()

fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(Tauma[0],'-',linewidth=3,label=r'$0$')
axes1.plot(Tauma[100],'-',linewidth=3,label=r'$1$')
axes1.plot(Tauma[200],'-',linewidth=3,label=r'$2$')
axes1.plot(Tauma[300],'-',linewidth=3,label=r'$3$')
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$Phase$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()