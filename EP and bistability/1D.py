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

kai=21.1
kae=2
ka=kai+kae

kmi=1.1
kme=2
km=kmi+kme

g=5
K=30


##(ka-km)/4=g   ka=4g+km=4*5+3.1=23.1  21.1


# Ps=np.linspace(0,1000e-3,1001)
P=150e-3
fs=np.linspace(8.15,8.35,501)

# cavity_in={
#     'omega_a':wa,
#     'omega_m':wm,
#     'kaint':kai,
#     'kaed':kae,
#     'kmint':kmi+kme,
#     'kmext':0,
#     'g_ma':g,
#     'P_d':P,
#     'omega_d':fs,
#     'K':K,
#     'branch':'none',
# }

magnon_in={
    'omega_a':wa,
    'omega_m':wm,
    'kaint':ka,
    'kaed':0,
    'kmint':kmi,
    'kmext':kme,
    'g_ma':g,
    'P_d':P,
    'omega_d':fs,
    'K':K,
    'branch':'none',
}

# dfc, ffc, dbc, fbc,ljc,ujc=Bistability(**cavity_in).BS_fre()
dfm, ffm, dbm, fbm,ljm,ujm=Bistability(**magnon_in).BS_fre()


delta_adfm=[]
delta_adbm=[]
delta_amfm=[]
delta_ambm=[]

for i in range(len(dfm)):
    delta_adfm.append(wa-ffm[i])
    delta_adbm.append(wa-fbm[i])
    delta_amfm.append((-wa+wm)*1e3+dfm[i])
    delta_ambm.append((-wa+wm)*1e3+dbm[i])

# delta_adfc=[]
# delta_adbc=[]
# delta_amfc=[]
# delta_ambc=[]
#
# for i in range(len(dfc)):
#     delta_adfc.append(wa-ffc[i])
#     delta_adbc.append(wa-fbc[i])
#     delta_amfc.append((-wa+wm)*1e3+dfc[i])
#     delta_ambc.append((-wa+wm)*1e3+dbc[i])
#

Sa=wa-1j*ka/2
Sm=wa-1j*km/2
he=(Sa+Sm)/2
cha=np.sqrt((Sa-Sm)**2/4+g**2)/2
Shp=he+cha
Shm=he-cha

kappa1=-2*np.imag(Shp)
kappa2=-2*np.imag(Shm)
print(kappa1)
print(kappa2)


for i in range(len(dfm)-1):
    if (dfm[i+1]-dfm[i])<-5:
        print((-wa+wm)*1e3+dfm[i+1])
        print(ffm[i+1])
    if (dfm[i+1]-dfm[i])>5:
        print((-wa+wm)*1e3+dfm[i])
        print(ffm[i])


plt.figure(figsize=(6, 6))
# plt.plot(wa-ffc, wa-wm-dfc, '--', label='cavity in forward')
# plt.plot(wa-fbc, wa-wm-dbc, '--', label='cavity in backward')
plt.plot(delta_adfm, delta_amfm, '--', label='magnon in forward')
plt.plot(delta_adbm, delta_ambm, '--', label='magnon in backward')
plt.xlabel(r'$\delta_{ad}$[MHz]')
plt.ylabel(r'$\delta_{ma}$[MHz]')
plt.legend()
plt.show()


