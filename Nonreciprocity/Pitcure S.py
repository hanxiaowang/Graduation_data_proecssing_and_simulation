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

start=0
stop=20000
omega_se = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]*1e9


for i in range(len(voltages)):
    voltage=voltages[i]
    S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')
    S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.txt',delimiter=',')


    plt.figure(figsize=(6,6))
    extents=[phis[0],phis[-1],omega_se[0],omega_se[-1]]
    ax1 = plt.subplot(111)
    im = ax1.imshow(S12e, extent=extents, aspect='auto',origin='lower')
    plt.colorbar(im)
    plt.savefig(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\picture\\S12 of coupling(experiment) with A={round(voltage)}.0 mV 2D.png')

    plt.figure(figsize=(6, 6))
    extents = [phis[0], phis[-1], omega_se[0], omega_se[-1]]
    ax1 = plt.subplot(111)
    im = ax1.imshow(S21e, extent=extents, aspect='auto', origin='lower')
    plt.colorbar(im)
    plt.savefig(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\picture\\S21 of coupling(experiment) with A={round(voltage)}.0 mV 2D.png')

