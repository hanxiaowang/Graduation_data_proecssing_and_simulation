import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import cmath

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

# a上加驱动
Paa=[]
Pam=[]

#m上加驱动
Pma=[]
Pmm=[]


deltakchug=((kais+kap)-(kmi+kmp))/(4*g_ma)
index_need=np.where(deltakchug==1)
print(index_need)
OneforEP=np.ones(len(omega_ps))
# print(OneforEP)

for i in range(len(kais)):
    chi_a = 1j * delta_a + (kais[i]+kap) / 2
    chi_m = 1j * delta_m + kmi+kmp / 2

    aa=-np.sqrt(kap)/(chi_a+g_ma**2/chi_m)
    am=1j*g_ma/chi_m*aa
    Paa.append(np.abs(aa)**2)
    Pam.append(np.abs(am) ** 2)

    mm=-np.sqrt(kmp)/(chi_m+g_ma**2/chi_a)
    ma=1j*g_ma/chi_a*mm
    Pma.append(np.abs(mm) ** 2)
    Pmm.append(np.abs(ma) ** 2)

##  a in
plt.figure(figsize=(24,12))
extents=[deltakchug[0],deltakchug[-1],omega_ps [0],omega_ps [-1]]

ax1 = plt.subplot(221)
im1 = ax1.imshow(np.transpose(Paa), extent=extents, aspect='auto',origin='lower')
plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
plt.colorbar(im1)

ax2 = plt.subplot(222)
im2 = ax2.imshow(np.transpose(Pam), extent=extents, aspect='auto',origin='lower')
plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
plt.colorbar(im2)

ax3 = plt.subplot(223)
im3 = ax3.imshow(np.transpose(Pma), extent=extents, aspect='auto',origin='lower')
plt.plot(OneforEP,omega_ps,'--',color='red',linewidth=5)
plt.colorbar(im3)

ax4 = plt.subplot(224)
im4 = ax4.imshow(np.transpose(Pmm), extent=extents, aspect='auto',origin='lower')
plt.plot(OneforEP,omega_ps,'--',color='blue',linewidth=5)
plt.colorbar(im4)
plt.show()


target=200
#200 EP
fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_ps,Paa[target],'-',linewidth=10,label=r'$Paa$',color='red',alpha=1)
axes1.plot(omega_ps,Pam[target],'-',linewidth=3,label=r'$Pam$',color='blue',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()

fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_ps,Pma[target],'-',linewidth=10,label=r'$Pma$',color='red',alpha=1)
axes1.plot(omega_ps,Pmm[target],'-',linewidth=3,label=r'$Pmm$',color='blue',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$Phase$',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()

