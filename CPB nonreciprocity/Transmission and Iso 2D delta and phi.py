import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

omega_a = 8.25e9
# delta_ms=np.linspace(-100,100,41)

omega_m = omega_a
omega_s = np.linspace(omega_m - 50e6, omega_m + 50e6, 10001)
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
phis = np.linspace(-0.5, 1.5, 3601)

deltas = np.linspace(0, 7, 1401)


Iso = []
S12_max=[]
S21_max=[]

S12_0_delta=[]
S12_0_phi=[]

S21_0_delta=[]
S21_0_phi=[]

for i in range(len(phis)):
    phi = phis[i]
    isos = []
    s12_max = []
    s21_max = []
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

        s12_max.append(max(S12))
        s21_max.append(max(S21))
        wucha1=5e-3
        wucha2 = 3e-3
        if (np.abs(max(S12))<=wucha1):
            S12_0_delta.append(deltas[c])
            S12_0_phi.append(phis[i])

        if (np.abs(max(S21))<=wucha2):
            S21_0_delta.append(deltas[c])
            S21_0_phi.append(phis[i])
        ISO=S21-S12
        isoabs=np.abs(ISO)
        #
        index = np.where(isoabs==max(isoabs))
        # print(index)
        # print(index[0][0])
        need = ISO[index[0][0]]
        isos.append(need)
    Iso.append(isos)
    S12_max.append(s12_max)
    S21_max.append(s21_max)

pai=[]
for i in range(len(deltas)):
    pai.append(0.5)


omega_p_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\iso', 'omega_s.txt')
phis_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\iso', 'phis.txt')
deltas_delta_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\iso', 'deltas.txt')
Iso_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\iso', 'Iso.txt')


np.savetxt(omega_p_path , omega_s, fmt='%.4f')
np.savetxt(phis_path, phis, fmt='%.4f')
np.savetxt(deltas_delta_path, deltas, fmt='%.4f')
np.savetxt(Iso_path, Iso, fmt='%.4f')


print(len(S12_0_delta))
print(len(S21_0_delta))
extents=[deltas[0], deltas[-1], phis[0],phis[-1]]
plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
im = ax1.imshow(Iso, extent=extents, cmap="bwr",aspect='auto',origin='lower')
ax1.plot(deltas,pai,'--',color='green',linewidth=5)
plt.colorbar(im)
plt.show()


# plt.figure(figsize=(12,6))
# # ax1 = plt.subplot(111)
# # gci1 = ax1.pcolor(deltas, phis, S12_max)
# # ax1.plot(deltas,pai,'--',color='black',linewidth=5)
# # ax1.plot(S12_0_delta,S12_0_phi,'--',color='red',linewidth=5)
# # ax1.set_xlabel(r'$\delta$',fontsize=10)
# # ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=10)
# # plt.tick_params(labelsize=10)
# # cbar = plt.colorbar(gci1)
# ax2 = plt.subplot(111)
# im = ax2.imshow(S12_max, extent=extents,aspect='auto',origin='lower')
# ax2.plot(S12_0_delta,S12_0_phi,'--',color='red',linewidth=5)
# plt.colorbar(im)
# plt.show()
# # #
# #
# plt.figure(figsize=(12,6))
# ax3 = plt.subplot(111)
# # gci1 = ax1.pcolor(deltas, phis, S21_max)
# # # ax1.plot(deltas,pai,'--',color='black',linewidth=5)
# # ax1.plot(S21_0_delta,S21_0_phi,'--',color='red',linewidth=5)
# # ax1.set_xlabel(r'$\delta$',fontsize=10)
# # ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=10)
# # plt.tick_params(labelsize=10)
# # cbar = plt.colorbar(gci1)
# ax3 = plt.subplot(111)
# im = ax3.imshow(S21_max, extent=extents,aspect='auto',origin='lower')
# ax3.plot(S21_0_delta,S21_0_phi,'--',color='red',linewidth=5)
# plt.colorbar(im)
# plt.show()
