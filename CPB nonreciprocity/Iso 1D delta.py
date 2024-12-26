import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from mpl_toolkits.mplot3d import Axes3D
import os
import json

k_int = 1.4e6
# k_1 = 45.5e6
# k_2 = 4.5e6

k_2 = 4.5e6
k_1 = 45.5e6
# k_3 = 1.33e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a-0e6


##12<21 >>1.6,0.05    10~-50, 20~-40
##12>21 >>2.9,0.9     10~-60, 50~-20
# delta=1.6
# phi=0.05

# delta=2.035
# # phi=0.953
# phi=0.047


phi=0.5
##毕业观察对称情况
# delta=3
# phi=0.965#point1
# phi=0.035#point2
# phi=0.91#point3
# phi=0.09#point4



# omega_ps=8.25e9+np.linspace(-50,50,2001)*1e6
omega_ps=omega_m


def S_and_Iso(delta):
    delta_m = omega_m - omega_ps
    delta_a = omega_a - omega_ps
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)
    fenzi12 = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * phi * np.pi)

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))
    ISO=S12-S21

    return ISO

deltas=np.linspace(0,7,701)

Iso=[]
for i in range(len(deltas)):
    iso=S_and_Iso(deltas[i])
    Iso.append(iso)

plt.figure(figsize=(6, 6))
axes1 = plt.subplot(111)
axes1.plot(deltas,Iso,'-',color='green',linewidth=5,alpha=1)
axes1.set_xlabel(r'$\delta$',fontsize=20)
axes1.set_ylabel(r'$ISO$ [dB]',fontsize=20)
plt.tick_params(labelsize=20)
plt.show()

print(max(Iso))
print(min(Iso))
max_index = list(Iso).index(max(Iso))
min_index = list(Iso).index(min(Iso))
print(deltas[max_index])
print(deltas[min_index])