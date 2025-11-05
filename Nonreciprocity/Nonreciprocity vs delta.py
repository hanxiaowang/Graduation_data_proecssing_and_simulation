import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json

voltagen=np.linspace(20,110,19)
tu=np.linspace(0,18,19)
# voltage=np.linspace(40,50,11)

phis=np.linspace(0,2,361)
# print(phi1[110])

#
de = 1
targets=[10,110,30]
if de==0:
    start =0
    stop = 10001
elif de==1:
    start = 5000
    stop = 15001
elif de==2:
    start = 10000
    stop = 20001


Isoe=[]
S12e=[]
S21e=[]
for i in range(len(voltagen)):
    print(i)
    if de==0:
        s12=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',delimiter=',')[start:stop]
        s21=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',delimiter=',')[start:stop]
    elif de==1:
        s12 = np.loadtxt(
            f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',
            delimiter=',')[start:stop]
        s21 = np.loadtxt(
            f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',
            delimiter=',')[start:stop]
    elif de==2:
        s12 = np.loadtxt(
            f'F:\\Nonreciprocity\\20210703\\m larger than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',
            delimiter=',')[start:stop]
        s21 = np.loadtxt(
            f'F:\\Nonreciprocity\\20210703\\m larger than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltagen[i])}.0 mV 2D.txt',
            delimiter=',')[start:stop]
    # print(np.shape(S12[:,110]))
    S12e.append(s12[:,targets[de]])
    S21e.append(s21[:,targets[de]])
    Isoe.append(s12[:,targets[de]]-s21[:,targets[de]])


np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\s12 vs delta.txt',S12e)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\s21 vs delta.txt',S21e)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\iso vs delta.txt',Isoe)

fe=np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]

fe_start=fe[0]
fe_stop=fe[-1]

omega_a = 8.247e9
delta_ms = [-32*1e6, -2*1e6, 63*1e6]


omega_m = omega_a+delta_ms[de]
omega_s = np.linspace(fe_start,fe_stop,10001)*1e9

k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

phiss = [phis[targets[0]],phis[targets[1]],phis[targets[2]]]
phi=phiss[de]
print(phi)
## deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2

deltass=[45,45,50]
delta=0.97*voltagen/deltass[de]
##  2.371(45) 2.134(50)
phi1 = 0.75
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2

delta1s=[0.97,0.97,0.92]
delta1=delta1s[de]


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


T12 = []
T21 = []
Isos = []
for i in range(len(delta)):
    delta_m = omega_m - omega_s
    delta_a = omega_a - omega_s
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta[i] * np.exp(
        -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta[i] * np.exp(
        -1j * (phi + phi21) * np.pi))
    fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta[i] * np.exp(
        -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta[i] * np.exp(
        -1j * (phi + phi12) * np.pi))

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu

    # T12.append(rf.mag_2_db(np.abs(t12)))
    # T21.append(rf.mag_2_db(np.abs(t21)))
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))

    T12.append(S12)
    T21.append(S21)
    Isos.append(S12-S21)


# plt.figure(figsize=(18,12))

# ax1 = plt.subplot(231)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax1.imshow(np.transpose(T12), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
#
# cmap='bwr'
#
# ax2 = plt.subplot(232)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax2.imshow(np.transpose(T21), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
#
# ax3 = plt.subplot(233)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax3.imshow(np.transpose(Isos), extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# #
#
# ax4 = plt.subplot(234)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax4.imshow(np.transpose(S12e), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
#
# #
# ax5 = plt.subplot(235)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax5.imshow(np.transpose(S21e), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
#
# ax6 = plt.subplot(236)
# extents=[delta[0],delta[-1],fe[0],fe[-1]]
# im = ax6.imshow(np.transpose(Isoe), extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
#
# plt.show()

print(np.min(Isos))
print(np.max(Isos))

print(np.min(Isoe))
print(np.max(Isoe))

plt.figure(figsize=(6,6))
extents=[delta[0],delta[-1],omega_s[0],omega_s[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(T12), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()


plt.figure(figsize=(6,6))
extents=[delta[0],delta[-1],omega_s[0],omega_s[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(T21), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()

plt.figure(figsize=(6,6))
extents=[delta[0],delta[-1],omega_s[0],omega_s[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(Isos), extent=extents, cmap="bwr",aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()

##### resonant
plt.figure(figsize=(6,6))
extents=[delta[0],delta[-1],fe[0],fe[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(S12e), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()


plt.figure(figsize=(6,6))
extents=[delta[0],delta[-1],fe[0],fe[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(S21e), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()

#
plt.figure(figsize=(6,6))
extents=[tu[0],tu[-1],fe[0],fe[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(Isoe), extent=extents, cmap="bwr",aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()