import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

omega_a=8.25e9
omega_m=8.25e9
omega_ps = np.linspace(8.23,8.27, 401) * 1e9
delta_a=omega_a-omega_ps
delta_m=omega_m-omega_ps
kais=np.linspace(1,31,301)*1e6
kap=2e6
kmi=1e6
kmp=2e6
km=kmi+kmp
g_ma = 5e6
Sa=[]
Sm=[]

deltakg=[]

wplus=[]
kplus=[]
wminus=[]
kminus=[]
keplus=[]
keminus=[]
Theta=[]

for i in range(len(kais)):
    ka=kap+kais[i]
    deltakappa=ka-km
    deltakg.append(deltakappa / (4*g_ma))
    chia=omega_a-1j*ka/2
    chim=omega_m-1j*km/2
    same=(chia+chim)/2
    diff=np.sqrt((chia-chim)**2+4*g_ma**2)/2
    chiplus=same+diff
    chiminus=same-diff

    wplus.append(np.real(chiplus)/1e9)
    kplus.append(np.imag(chiplus)*(-2)/1e6)
    wminus.append(np.real(chiminus)/1e9)
    kminus.append(np.imag(chiminus)*(-2)/1e6)