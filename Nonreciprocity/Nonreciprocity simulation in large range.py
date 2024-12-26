import numpy as np
import matplotlib.pyplot as plt
import skrf as rf



omega_a = 8.247e9
delta_ms = [-500*1e6, 500*1e6]

# omega_s = np.linspace(omega_a - 50e6, omega_m + 50e6, 10001)


k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

phis = np.linspace(0, 2, 361)
voltage = 20
delta= 0.97 * voltage / 45




phi1 = 0.77
delta1 = 1

zhengti=0
chazhi=0  #63
phi12=(zhengti+chazhi)
phi21=(zhengti)

T12s = []
T21s = []
Isos = []

de = 0
omega_m = omega_a+delta_ms[de]
omega_s1 = np.linspace(omega_m - 50e6, omega_m + 50e6, 1001)
for i in range(len(phis)):
    phi = phis[i]

    delta_m = omega_m - omega_s1
    delta_a = omega_a - omega_s1
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * (phi + phi12) * np.pi))
    fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * (phi + phi21) * np.pi))

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu

    # T12.append(rf.mag_2_db(np.abs(t12)))
    # T21.append(rf.mag_2_db(np.abs(t21)))
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))

    T12s.append(S12)
    T21s.append(S21)
    Isos.append(S12-S21)

T12l = []
T21l = []
Isol = []
de = 1
omega_m = omega_a+delta_ms[de]
omega_s2 = np.linspace(omega_m - 50e6, omega_m + 50e6, 1001)
for i in range(len(phis)):
    phi = phis[i]

    delta_m = omega_m - omega_s2
    delta_a = omega_a - omega_s2
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * (phi + phi12) * np.pi))
    fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * (phi + phi21) * np.pi))

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu

    # T12.append(rf.mag_2_db(np.abs(t12)))
    # T21.append(rf.mag_2_db(np.abs(t21)))
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))

    T12l.append(S12)
    T21l.append(S21)
    Isol.append(S12-S21)

plt.figure(figsize=(18,12))
ax1 = plt.subplot(231)
gci1 = ax1.pcolor(phis,omega_s1/1e9, np.transpose(T12s))
# ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci1)
# cmap='bwr'
#
ax2 = plt.subplot(232)
gci2 = ax2.pcolor(phis, omega_s1/1e9,np.transpose(T21s))
# ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci2)

ax3 = plt.subplot(233)
gci3 = ax3.pcolor(phis, omega_s1/1e9,np.transpose(Isos))
# ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci3)

ax4 = plt.subplot(234)
gci4 = ax4.pcolor(phis,omega_s2/1e9, np.transpose(T12l))
ax4.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
ax4.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci4)
# cmap='bwr'
#
ax5 = plt.subplot(235)
gci5 = ax5.pcolor(phis, omega_s2/1e9,np.transpose(T21l))
ax5.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax5.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci5)

ax6 = plt.subplot(236)
gci6 = ax6.pcolor(phis, omega_s2/1e9,np.transpose(Isol))
ax6.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax6.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
plt.tick_params(labelsize=20)
cbar = plt.colorbar(gci6)
#

plt.show()