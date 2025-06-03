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

v_index=9#Iso min
phi_index=76#phi min

voltage=voltages[v_index]
delta=0.97*voltage/50
# print(delta)
phi=phis[phi_index]
start=10000
stop=20000

# S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
# S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33

# S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
# S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33

S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m larger than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m larger than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33


Isoe=S12e-S21e

omega_a = 8.247e9
omega_m = omega_a+63e6
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
delta1=0.92


# zhengti=-0.26
# chazhi=0.06  #63

# zhengti=-0.18
# chazhi=0.08 #-32

# zhengti=-0.2
# chazhi=0.1 #-2

# phi21=(-0.2+0.1)
# phi12=(-0.2)

phi21s=np.linspace(-0.2,0,2)
phi12s=np.linspace(-0.5,-0.1,4001)
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

