import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

wR=8.3e9*2*np.pi
kRi=1.4e6*2*np.pi
kRe=1.4e6*2*np.pi
kR=kRi+kRe

wa=8.25e9*2*np.pi
ka=1.4e6*2*np.pi

w1=8.25e9*2*np.pi
k1=1.1e6*2*np.pi

w2=8.25e9*2*np.pi
k2=1.1e6*2*np.pi

g1=30e6*2*np.pi
g2=30e6*2*np.pi

Phis=np.linspace(0,2,361)

wp=np.linspace(8.2,8.4,2001)*1e9*2*np.pi

Delta_R=wR-wp
Delta_a=wa-wp
Delta_1=w1-wp
Delta_2=w2-wp

SR=-1j*Delta_R-kR/2
Sa=-1j*Delta_a-ka/2
S1=-1j*Delta_1-k1/2
S2=-1j*Delta_2-k2/2
S_sum=Sa+g1**2/S1+g2**2/S2

S11=[]

for i,Phi in enumerate(Phis):
    g=10e6*2*np.pi*np.exp(-1j*Phi*np.pi)
    R=-np.sqrt(kRe)/(SR+g**2/S_sum)
    t=1-np.sqrt(kRe)*R
    S11.append(rf.mag_2_db(np.abs(t)))

plt.figure(figsize=(12,12))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(Phis, wp/(1e9*2*np.pi), np.transpose(S11))
ax1.set_xlabel(r'$\Phi$ ',fontsize=20)
ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci1)
plt.show()