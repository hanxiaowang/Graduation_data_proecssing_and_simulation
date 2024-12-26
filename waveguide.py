import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

omega_1=8.25e9*2*np.pi
omega_2=8.25e9*2*np.pi

kin1=1.1e6*2*np.pi
kex1=2e6*2*np.pi
g1=np.sqrt(2*np.pi*kex1)
k1=kin1+kex1

kin2=1.1e6*2*np.pi
kex2=2e6*2*np.pi
g2=np.sqrt(2*np.pi*kex2)
k2=kin2+kex2

t=30/(3e8)

omega_p=np.linspace(8.2,8.3,1001)*1e9*2*np.pi
Phi=omega_p*t

g=5e6*2*np.pi
Gamma=2*np.pi*g1*g2

omega_1t=omega_1-1j*k1
omega_2t=omega_2-1j*k2

G=g-1j*Gamma*np.exp(1j*Phi)

fenzi=(omega_p-omega_1t)*(omega_p-omega_2t)-G**2

t11fenmu=1j*kex1*(omega_p-omega_2t)+1j*kex2*np.exp(1j*2*Phi)*(omega_p-omega_1t)+2*1j*Gamma*G*np.exp(1j*Phi)
t12fenmu=1j*kex1*(omega_p-omega_2t)+1j*kex2*(omega_p-omega_1t)+2*1j*Gamma*G*np.cos(Phi)
t21fenmu=1j*kex1*(omega_p-omega_2t)+1j*kex2*(omega_p-omega_1t)+2*1j*Gamma*G*np.cos(Phi)
t22fenmu=1j*kex1*(omega_p-omega_2t)+1j*kex2*np.exp(-1j*2*Phi)*(omega_p-omega_1t)+2*1j*Gamma*G*np.exp(-1j*Phi)

t11=-t11fenmu/fenzi
t12=1-t12fenmu/fenzi
t21=1-t21fenmu/fenzi
t22=t22fenmu/fenzi

S11=rf.mag_2_db(np.abs(t11))
S12=rf.mag_2_db(np.abs(t12))
S21=rf.mag_2_db(np.abs(t21))
S22=rf.mag_2_db(np.abs(t22))


# print(np.shape(S11))
# print(Phi/(2*np.pi))

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(omega_p/(1e9*2*np.pi),S11,'-',label=r'$S_{11}$',linewidth=5)
axes.plot(omega_p/(1e9*2*np.pi),S12,'-',label=r'$S_{12}$',linewidth=5)
axes.plot(omega_p/(1e9*2*np.pi),S21,'--',label=r'$S_{21}$',linewidth=5)
axes.plot(omega_p/(1e9*2*np.pi),S22,'--',label=r'$S_{22}$',linewidth=5)
axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
axes.set_ylabel(r'$S$ [dB]',fontsize=40)
plt.tick_params(labelsize=40)
plt.legend(loc=0,fontsize=40)
plt.show()
