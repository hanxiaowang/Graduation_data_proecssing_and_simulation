import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

omega_a = 8.25e9
# delta_ms=np.linspace(-100,100,41)

omega_m = omega_a
omega_s = np.linspace(omega_m - 50e6, omega_m + 50e6, 2001)
# omega_s = np.linspace(8.16e9, 8.36e9, 20001)

k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

# phis = np.linspace(-0.5, 1.5, 361)
#
# deltas = np.linspace(0, 10, 1001)
phis = np.linspace(-0.5, 1.5, 181)

deltas = np.linspace(0, 7, 141)


Iso = []
for i in range(len(phis)):
    phi = phis[i]
    isos = []
    for c in range(len(deltas)):
        delta = deltas[c]
        # T12 = []
        # T21 = []
        iso = []
        isoabs = []

        delta_m = omega_m - omega_s
        delta_a = omega_a - omega_s
        chi_a = 1j * delta_a + k_c / 2
        chi_m = 1j * delta_m + gamma / 2
        fenmu = chi_a * chi_m + g ** 2

        fenzi21 =  (chi_m * (np.sqrt(k_1*k_2) ) - 1j * g * np.sqrt(k_2*gamma_e) * delta * np.exp(-1j * (phi)*np.pi))
        fenzi12 = (chi_m * (np.sqrt(k_1*k_2) ) - 1j * g * np.sqrt(k_1*gamma_e) * delta * np.exp(-1j * (phi)*np.pi))

        t12 = fenzi12 / fenmu
        t21 = fenzi21 / fenmu

        # T12.append(rf.mag_2_db(np.abs(t12)))
        # T21.append(rf.mag_2_db(np.abs(t21)))
        S12=rf.mag_2_db(np.abs(t12))
        S21=rf.mag_2_db(np.abs(t21))

        iso=S12-S21
        isoabs=np.abs(S12-S21)

        index = np.where(isoabs==max(isoabs))
        need = iso[index][0]
        isos.append(need)
    Iso.append(isos)

pai=[]
for i in range(len(deltas)):
    pai.append(0.5)

plt.figure(figsize=(14, 6))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(deltas, phis, Iso,cmap='bwr')
ax1.plot(deltas,pai,'--',color='black',linewidth=5)
ax1.set_xlabel(r'$\delta$',fontsize=30)
ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=30)
plt.tick_params(labelsize=30)
cbar = plt.colorbar(gci1)

plt.show()