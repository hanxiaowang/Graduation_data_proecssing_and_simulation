import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json
voltages=np.linspace(20,110,19)
phis=np.linspace(0,2,361)

v_index=16#Iso min
phi_index=107#phi min

voltage=91.8
delta=0.97*voltage/45
phi=phis[phi_index]
start=00000
stop=20000


omega_a = 8.247e9
omega_m = omega_a-32e6
omega_s = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]*1e9
k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6


## deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2



phi1 = 0.75
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2
delta1=0.97


phi21s=np.linspace(-0.2,0,2)
phi12s=np.linspace(-0.4,-0.3,4001)
# phi21s=np.linspace(-0.3,-0.1,4001)
# phi12s=np.linspace(-0.5,-0.1,2)

S12min=np.zeros((len(phi21s),len(phi12s)))
# S21min=np.zeros((len(phi21s),len(phi12s)))
for i in range(len(phi21s)):
    print(i)
    phi21=phi21s[i]
    for j in range(len(phi12s)):
        phi12 = phi12s[j]
        delta_m = omega_m - omega_s
        delta_a = omega_a - omega_s
        chi_a = 1j * delta_a + k_c / 2
        chi_m = 1j * delta_m + gamma / 2
        fenmu = chi_a * chi_m + g ** 2

        # fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
        #     -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        #     -1j * (phi + phi21) * np.pi))
        # t21 = fenzi21 / fenmu
        # S21s = rf.mag_2_db(np.abs(t21))
        # S21min[i][j] = min(S21s)


        fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
            -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
            -1j * (phi + phi12) * np.pi))

        t12 = fenzi12 / fenmu
        S12s = rf.mag_2_db(np.abs(t12))
        S12min[i][j] = min(S12s)


        # T12.append(rf.mag_2_db(np.abs(t12)))
        # T21.append(rf.mag_2_db(np.abs(t21)))


        # Isos=S12s-S21s


rr, cr = np.where(S12min == np.min(S12min))
print(f'rr={rr}')
print(f'cr={cr}')
print(phi12s[cr[0]])

print(np.min(S12min))
plt.figure(figsize=(6,6))
extents=[phi12s[0],phi12s[-1],phi21s[0],phi21s[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(S12min, extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()

# rr, cr = np.where(S21min == np.min(S21min))
# print(f'rr={rr}')
# print(f'cr={cr}')
# print(phi12s[cr[0]])
# print(phi21s[rr[0]])
# print(np.min(S21min))
# plt.figure(figsize=(6,6))
# extents=[phi12s[0],phi12s[-1],phi21s[0],phi21s[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(S21min, extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()

