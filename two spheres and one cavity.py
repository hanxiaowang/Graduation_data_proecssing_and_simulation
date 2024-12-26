import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

omega_a=8.25e9
kai=140e6
kae=1.5e6
ka=kai+kae

omega_1=8.2e9
k1=1.1e6
g1=20e6

omega_2s=np.linspace(-50,50,101)*1e6+omega_1
k2=1.1e6
g2=20e6

# omega_ps=np.linspace(8.15,8.25,2001)*1e9
omega_ps=np.linspace(8.15,8.3,3001)*1e9



S11=[]
for i,omega_2 in enumerate(omega_2s):
    delta_a=omega_a-omega_ps
    delta_1=omega_1-omega_ps
    delta_2=omega_2-omega_ps

    Sa=-1j*delta_a-ka/2
    S1=-1j*delta_1-k1/2
    S2=-1j*delta_2-k2/2

    A=-np.sqrt(kae)/(Sa+g1**2/S1+g2**2/S2)
    t=rf.mag_2_db(np.abs(1-np.sqrt(kae)*A))
    S11.append(t)


plt.figure(figsize=(12, 12))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(omega_2s/1e9, omega_ps/1e9, np.transpose(S11),cmap='bwr')
ax1.set_xlabel(r'$\omega_2/2\pi$',fontsize=30)
ax1.set_ylabel(r'$\omega_p/2\pi$',fontsize=30)
plt.tick_params(labelsize=30)
cbar = plt.colorbar(gci1)
plt.show()