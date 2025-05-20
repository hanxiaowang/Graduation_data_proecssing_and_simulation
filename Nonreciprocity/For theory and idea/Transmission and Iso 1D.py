import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

k_int = 1.4e6
# k_1 = 45.5e6
# k_2 = 4.5e6
k_1 = 45.5e6
k_2 = 4.5e6
# k_3 = 1.33e6
k_3 = 0e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6

omega_a = 8.25e9
omega_m=omega_a-0e6


##12>21 >>1.6016,0.81    10~-50, 20~-40  iso -40~20
##12<21 >>1.1383,0.08    10~-60, 50~-20  iso -20~50
# delta=1.6016
# phi=0.81

delta=1.1383
# phi=0.953
phi=0.08

# delta=2.9
# phi=0.9
##毕业观察对称情况
# delta=3
# phi=0.965#point1
# phi=0.035#point2
# phi=0.91#point3
# phi=0.09#point4



# omega_ps=8.25e9+np.linspace(-50,50,2001)*1e6
omega_ps=np.linspace(8.2,8.3,10001)*1e9



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


fenzi21r = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_2 * gamma_e) * 0 * np.exp(
    -1j * phi * np.pi)
fenzi12r = chi_m * np.sqrt(k_1 * k_2) - 1j * g * np.sqrt(k_1 * gamma_e) * 0 * np.exp(
    -1j * phi * np.pi)

t12r = fenzi12r / fenmu
t21r = fenzi21r / fenmu
S12r = rf.mag_2_db(np.abs(t12r))
S21r = rf.mag_2_db(np.abs(t21r))
ISOr=S12r-S21r


Diff12=S12-S12r
Diff21=S21-S21r

# plt.figure(figsize=(15, 10))
# axes1 = plt.subplot(221)
# axes1.plot(omega_ps/1e9,S12,'-',linewidth=5,label='S12',alpha=0.5)
# axes1.plot(omega_ps/1e9,S21,'-',linewidth=5,label='S21',alpha=0.5)
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0,fontsize=10)
#
# axes2 = plt.subplot(224)
# axes2.plot(omega_ps/1e9,ISO,'-',color='green',linewidth=5)
# axes2.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes2.set_ylabel(r'$ISO$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.show()

#
tneed=np.linspace(-60,30,901)
was=[]
wms=[]
for i in range(len(tneed)):
    was.append(0)
    wms.append((omega_a/1e9-omega_m/1e9)*1e3)


plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot((8.25-omega_ps/1e9)*1e3,S12,'-',linewidth=5,label=r'$S_{12}$',alpha=0.5)
axes1.plot((8.25-omega_ps/1e9)*1e3,S21,'-',linewidth=5,label=r'$S_{21}$',alpha=0.5)
# axes1.plot(was,tneed,'--',linewidth=2,color='black')
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# axes1.set_ylim(-50,10)## 毕业论文用
axes1.set_ylim(-110,10)
plt.xticks([-50,0,50],['-50','0','50'])
plt.yticks([-100,-50,0],['-100','-50','0'])

plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()

plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot((8.25-omega_ps/1e9)*1e3,ISO,'-',linewidth=5,label=r'Iso.',color='green')
# axes1.plot(was,tneed,'--',linewidth=2,color='black')
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# axes1.set_ylim(-50,10)## 毕业论文用
axes1.set_ylim(-110,110)
plt.xticks([-50,0,50],['-50','0','50'])
plt.yticks([-100,-50,0,50,100],['-100','-50','0','50','100'])

plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()


# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot((omega_a/1e9-omega_ps/1e9)*1e3,Diff12,'-',linewidth=5,label=r'$\delta S_{12}$',alpha=0.5)
# axes1.plot((omega_a/1e9-omega_ps/1e9)*1e3,Diff21,'-',linewidth=5,label=r'$\delta S_{21}$',alpha=0.5)
# axes1.plot(wms,tneed,'--',linewidth=2,color='black')
# axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# # axes1.set_ylim(-50,10)## 毕业论文用
# axes1.set_ylim(-40,30)
# # axes1.set_ylim(-60,10)
# plt.xticks([-50,0,50],['-50','0','50'])
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,prop={'family':'Cambria','size':20})
# plt.show()
#
# plt.figure(figsize=(6, 6))
# axes2 = plt.subplot(111)
# axes2.plot(omega_ps/1e9,ISO,'-',color='green',label='Iso.',linewidth=5)
# axes2.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# axes2.set_ylabel(r'$ISO$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,fontsize=20)
# plt.show()
max_index = list(ISO).index(max(ISO))
min_index = list(ISO).index(min(ISO))

print(f'min isolation {min(ISO)}')
print(f'min fre {8.25e9-omega_ps[min_index]}')
print(f'max isolation {max(ISO)}')
print(f'max fre {8.25e9-omega_ps[max_index]}')
