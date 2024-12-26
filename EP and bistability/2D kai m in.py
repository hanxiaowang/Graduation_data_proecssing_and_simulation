import sys
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(r'C:\Users\AORUS\OneDrive\little thing\Theory_WXH')
from Preparation_WXH import date_and_time as dt
from Preparation_WXH import save_file as sf
from Preparation_WXH import Read_file as ref
from Preparation_WXH import Plot_easy as pe
from Preparation_WXH import Combination
from Spectrum_WXH import Reflection
import os
from Computation_WXH import Power_Convert as pc
from Cycle_WXH import Square
from Cycle_WXH import Round
from Bistability_WXH_K import Change_surface
from Bistability_WXH_K import Bistability
from Spectrum_WXH import Reflection


wa=8.25
wm=wa-0.05

kais=np.linspace(2,41,39)
kae=2
# ka=kais+kae

kmi=1.1
kme=2
km=kmi+kme

g=5
K=30


# Ps=np.linspace(0,1000e-3,1001)
P=100e-3
fs=np.linspace(8.15,8.35,51)
delta_ad=(wa-fs)*1e3

Sfor=[]
Sback=[]
for i in range(len(kais)):
    magnon_in={
        'omega_a':wa,
        'omega_m':wm,
        'kaint':kais[i]+kae,
        'kaed':0,
        'kmint':kmi,
        'kmext':kme,
        'g_ma':g,
        'P_d':P,
        'omega_d':fs,
        'K':K,
        'branch':'none',
    }

    dfm, ffm, dbm, fbm,ljm,ujm=Bistability(**magnon_in).BS_fre()

    delta_amfm=[]
    delta_ambm=[]
    for j in range(len(dfm)):
        delta_amfm.append((-wa+wm)*1e3+dfm[i])
        delta_ambm.append((-wa+wm)*1e3+dbm[i])
    Sfor.append(delta_amfm)
    Sback.append(delta_ambm)

# print(Sfor[39])
# print(Sback[39])
print(np.shape(Sfor))

plt.figure(figsize=(12, 6))
# ax2 = plt.subplot(121)
# gci2 = ax2.pcolor(delta_ad, kais,Sback,cmap='bwr')
# ax2.set_xlabel(r'$\delta$',fontsize=30)
# ax2.set_ylabel(r'$\kappa_{a,int}$',fontsize=30)
# plt.tick_params(labelsize=30)
# cbar = plt.colorbar(gci2)

ax2 = plt.subplot(111)
gci2 = ax2.pcolor(delta_ad, kais,Sfor,cmap='bwr')
ax2.set_xlabel(r'$\delta$',fontsize=30)
ax2.set_ylabel(r'$\kappa_{a,int}$',fontsize=30)
plt.tick_params(labelsize=30)
cbar = plt.colorbar(gci2)


# ax1 = plt.subplot(121,projection='3d')
# gci1 = ax1.pcolor(delta_ad, kais,Sback,cmap='bwr')
# ax1.set_xlabel(r'$\delta$',fontsize=10)
# ax1.set_ylabel(r'$',fontsize=10)
# plt.tick_params(labelsize=10)
# cbar = plt.colorbar(gci1)
#
# ax2 = plt.subplot(122,projection='3d')
# gci2 = ax2.pcolor(delta_ad, kais,Sfor,cmap='bwr')
# ax2.set_xlabel(r'$\delta$',fontsize=10)
# ax2.set_ylabel(r'$',fontsize=10)
# plt.tick_params(labelsize=10)
# cbar = plt.colorbar(gci2)
plt.show()
