import numpy as np
import matplotlib.pyplot as plt
import skrf as rf

voltages=np.linspace(20,110,19)
phis=np.linspace(0,2,361)

v_index=16#Iso min
phi_index=107#phi min
phi=phis[phi_index]    ### 0.594pi


voltage=91.79
# voltage=voltages[v_index]
print(voltage)

delta=0.97*voltage/45
print(delta)
print(phi)
start=00000
stop=20000

S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltages[v_index])}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
S21e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltages[v_index])}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
Isoe=S12e-S21e

omega_a = 8.247e9
omega_m12 = omega_a-31e6
omega_m21 = omega_a-30e6

omega_se = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop]*1e9
k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3

gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e

g = 8e6


phi1 = 0.75
# delta1 = 0.92 #63
# delta1 = 0.97 #-32 -2
delta1=0.97

phi21=-0.11
phi12=-0.330

omega_ss = np.linspace(omega_se[0],omega_se[-1],20001)
delta_m12 = omega_m12 - omega_ss
delta_m21 = omega_m21 - omega_ss

delta_a = omega_a - omega_ss
chi_a = 1j * delta_a + k_c / 2
chi_m12 = 1j * delta_m12 + gamma / 2
chi_m21 = 1j * delta_m21 + gamma / 2

fenmu12 = chi_a * chi_m12 + g ** 2
fenmu21 = chi_a * chi_m21 + g ** 2


fenzi21 = (chi_m21 * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
    -1j * (phi + phi21) * np.pi))
fenzi12 = (chi_m12 * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
    -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
    -1j * (phi + phi12) * np.pi))

t12 = fenzi12 / fenmu12
t21 = fenzi21 / fenmu21


S12s = rf.mag_2_db(np.abs(t12))
S21s = rf.mag_2_db(np.abs(t21))
Isos=S12s-S21s



print(min(S12e))
print(min(S12s))
print(min(Isoe))
print(min(Isos))

# print(omega_ss)
# print(omega_se)

fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_se,S12e,'-',linewidth=10,label=r'$S_{12,exp}$',color='green',alpha=0.4)
axes1.plot(omega_ss,S12s,'-',linewidth=3,label=r'$S_{12,sim}$',color='green',zorder=2)
axes1.plot(omega_se,S21e,'-',linewidth=10,label=r'$S_{21,exp}$',color='orange',alpha=0.4)
axes1.plot(omega_ss,S21s,'-',linewidth=3,label=r'$S_{21,sim}$',color='orange',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-75,-50,-25,0],['-100','-75','-50','-25','0'])
plt.tick_params(labelsize=20)
plt.legend(loc=3,prop={'family':'Cambria','size':20})
plt.show()


fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_se,Isoe,'-',linewidth=10,label=r'$Iso._{exp}$',color='blue',alpha=0.4)
axes1.plot(omega_ss,Isos,'-',linewidth=3,label=r'$Iso._{sim}$',color='blue',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-50,0,50,100],['-100','-50','0','50','100'])
plt.tick_params(labelsize=20)
plt.legend(loc=3,prop={'family':'Cambria','size':20})
plt.show()
