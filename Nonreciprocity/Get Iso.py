import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json

# voltage=np.linspace(20,110,19)
voltage=np.linspace(40,50,11)

phi1=np.linspace(0,2,361)

Iso=[]

for i in range(len(voltage)):
    S12=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\40-50\\S\\S12 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',delimiter=',')
    S21=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\40-50\\S\\S21 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',delimiter=',')
    # S12 = np.loadtxt(
    #     f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',
    #     delimiter=',')
    # S21 = np.loadtxt(
    #     f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',
    #     delimiter=',')

    iso = S12 - S21
    isoabs = np.abs(S12 - S21)

    isomiddle=[]
    for j in range(len(phi1)):
        isolie=[rows[j] for rows in iso]
        isolieabs = [rows[j] for rows in isoabs]
        index = np.where(isolieabs == max(isolieabs))
        # print(index)
        need = isolie[index[0][0]]
        isomiddle.append(need)
    Iso.append(isomiddle)

print(np.shape(Iso))

# np.savetxt(f'F:\\Nonreciprocity\\20210701\\Isore.txt',Iso)

# plt.figure(figsize=(6,6))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(voltage,phi1, np.transpose(Iso))
# ax1.set_xlabel(r'$voltage$',fontsize=20)
# ax1.set_ylabel(r'$phi$',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# # cmap='bwr'
# plt.show()

plt.figure(figsize=(6,6))
extents=[voltage[0],voltage[-1],phi1[0],phi1[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(Iso), extent=extents,cmap="bwr", aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()
