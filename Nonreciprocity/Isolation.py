import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json

omega_a = 8.247e9
# delta_ms=np.linspace(-100,100,41)
delta_ms = [-32*1e6, -2*1e6, 63*1e6]

Exp=[]

phis = np.linspace(0, 2, 361)
voltage = np.linspace(20, 110, 19)

Isose = np.loadtxt(r'F:\Nonreciprocity\20210703\m smaller than a\Isos.txt')
# rs, cs = np.where(Isose == np.max(Isose))
rs, cs = np.where(Isose == np.min(Isose))
# print(f'rs={rs}')
# print(f'cs={cs}')
# print(Isose[rs[0]][cs[0]])
# print(voltage[rs[0]])
# print(phis[cs[0]])

Isole = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\Isol.txt')
# rl, cl = np.where(Isole == np.max(Isole))
rl, cl = np.where(Isole == np.min(Isole))
# print(f'rl={rl}')
# print(f'cl={cl}')
# print(Isole[rl[0]][cl[0]])
# print(voltage[rl[0]])
# print(phis[cl[0]])

Isore = np.loadtxt(r'F:\Nonreciprocity\20210701\Isor.txt')
# rr, cr = np.where(Isore == np.max(Isore))
rr, cr = np.where(Isore == np.min(Isore))
print(f'rr={rr}')
print(f'cr={cr}')
print(0.97*voltage[rr[0]]/45)
print(phis[cr[0]])
# print(type(Isose))
# print(np.shape(Isose))

print(np.min(Isose))
print(np.max(Isose))

print(np.min(Isole))
print(np.max(Isole))

print(np.min(Isore))
print(np.max(Isore))


Exp.append(np.transpose(Isose))
Exp.append(np.transpose(Isore))
Exp.append(np.transpose(Isole))

de = 1
omega_m = omega_a+delta_ms[de]
# print(omega_m)
Isoe=Exp[de]
omega_s = np.linspace(omega_m - 50e6, omega_m + 50e6, 10001)
# omega_s = np.linspace(8.16e9, 8.36e9, 20001)

k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6


# deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2

deltass=[45,45,50]
deltas=0.97*voltage/deltass[de]


phi1 = 0.75
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2

delta1s=[0.97,0.97,0.92]
delta1=delta1s[de]
# delta1=1



# zhengti=-0.26
# chazhi=0.06  #63

# zhengti=-0.18
# chazhi=0.08 #-32

# zhengti=-0.2
# chazhi=0.1 #-2

zhengtis=[-0.18,-0.2,-0.26]
chazhis=[0.08,0.1,0.06]


phi21=(zhengtis[de]+chazhis[de])
phi12=(zhengtis[de])

Iso = []
S12c = []
S21c = []
for i in range(len(phis)):
    phi = phis[i]
    isos = []
    s12c = []
    s21c = []
    for c in range(len(deltas)):
        delta = deltas[c]
        iso = []
        isoabs = []

        delta_m = omega_m - omega_s
        delta_a = omega_a - omega_s
        chi_a = 1j * delta_a + k_c / 2
        chi_m = 1j * delta_m + gamma / 2
        fenmu = chi_a * chi_m + g ** 2

        fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(-1j * (phi + phi1 + phi12) * np.pi))
                   - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(-1j * (phi + phi12) * np.pi))

        fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(-1j * (phi + phi1 + phi21) * np.pi))
                   - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(-1j * (phi + phi21) * np.pi))

        t12 = fenzi12 / fenmu
        t21 = fenzi21 / fenmu

        S12 = rf.mag_2_db(np.abs(t12))
        S21 = rf.mag_2_db(np.abs(t21))

        iso=(S12-S21)
        isoabs=np.abs(iso)
        index = list(isoabs).index(max(isoabs))
        need = iso[index]
        isos.append(need)
        s12c.append(S12[index])
        s21c.append(S21[index])
    Iso.append(isos)
    S12c.append(s12c)
    S21c.append(s21c)
# -0.032
# +0.063








delta_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'delta.txt')
phi_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'phi.txt')
voltage_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'voltage.txt')
vna_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'vna fre.txt')
np.savetxt(delta_path, deltas, fmt='%.4f')
np.savetxt(phi_path, phis, fmt='%.4f')
np.savetxt(voltage_path, voltage, fmt='%.4f')
np.savetxt(vna_path, omega_s, fmt='%.4f')
path = f'C:\\Users\\AORUS\\OneDrive\\桌面\\nonreciprocity\\{round(delta_ms[de])}'
if os.path.exists(path) == True:
    pass
else:
    os.mkdir(path)
para = {
    'omega_m': omega_m,
    'phi1': phi1,
    'delta1': delta1,
    'phi12': phi12,
    'phi21': phi21,
}
Iso_path = os.path.join(path, 'Iso.txt')
para_path = os.path.join(path, 'para.json')
np.savetxt(Iso_path, Iso, fmt='%.4f')

with open(para_path, 'w') as fp:
    json.dump(para, fp, indent=1)
    fp.close
picture_path = os.path.join(path, 'Iso.png')



# Vs = np.linspace(20, 110, 19)

#
# plt.figure(figsize=(12, 12))
# ax1 = plt.subplot(221)
# gci1 = ax1.pcolor(deltas, phis,Iso,cmap='bwr')
# ax1.set_xlabel(r'$\delta$',fontsize=15)
# ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=15)
# plt.tick_params(labelsize=15)
# cbar = plt.colorbar(gci1)
#
# #
# ax2 = plt.subplot(222)
# gci2 = ax2.pcolor(deltas, phis,Isoe,cmap='bwr')
# ax2.set_xlabel(r'$\delta$',fontsize=15)
# ax2.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=15)
# plt.tick_params(labelsize=15)
# cbar = plt.colorbar(gci2)
# # plt.savefig(picture_path)
#
#
# ax1 = plt.subplot(223)
# gci1 = ax1.pcolor(deltas, phis,S12c,cmap='bwr')
# ax1.set_xlabel(r'$\delta$',fontsize=15)
# ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=15)
# plt.tick_params(labelsize=15)
# cbar = plt.colorbar(gci1)
#
# #
# ax2 = plt.subplot(224)
# gci2 = ax2.pcolor(deltas, phis,S21c,cmap='bwr')
# ax2.set_xlabel(r'$\delta$',fontsize=15)
# ax2.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=15)
# plt.tick_params(labelsize=15)
# cbar = plt.colorbar(gci2)
#
# plt.show()
#
# plt.figure(figsize=(12, 6))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(deltas, phis, Iso,cmap='bwr')
# ax1.set_xlabel(r'$\delta$',fontsize=30)
# ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=30)
# plt.tick_params(labelsize=30)
# cbar = plt.colorbar(gci1)

#
# plt.figure(figsize=(12,6))
# extents=[deltas[0],deltas[-1],phis[0],phis[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(Isoe, extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
# plt.figure(figsize=(12,6))
# extents=[deltas[0],deltas[-1],phis[0],phis[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(Iso, extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()

# plt.figure(figsize=(12,6))
# extents=[deltas[0],deltas[-1],phis[0],phis[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(Isoe, extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
# plt.figure(figsize=(12,6))
# extents=[deltas[0],deltas[-1],phis[0],phis[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(Iso, extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()

# plt.figure(figsize=(18,12))
# ax1 = plt.subplot(231)
# gci1 = ax1.pcolor(phis, fe, S12l)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)

plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(deltas, phis, Isoe, cmap="bwr")
cbar = plt.colorbar(gci1)
plt.show()

plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(deltas, phis, Iso, cmap="bwr")
cbar = plt.colorbar(gci1)
plt.show()