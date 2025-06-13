import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import scipy

voltages=np.linspace(20,110,19)
phis=np.linspace(0,2,361)
start=00000
stop=20000
v_index=16#Iso min
phi_index=107#phi min
phi=phis[phi_index]    ### 0.594pi
voltage=voltages[v_index]
delta_inf=0.97*voltage/45
S12e=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltages[v_index])}.0 mV 2D.txt',delimiter=',')[start:stop,phi_index]+33
omega_se = np.loadtxt(r'F:\Nonreciprocity\20210703\m larger than a\f.txt')[start:stop] * 1e9
# omega_ss = np.linspace(omega_se[0], omega_se[-1], 20001)

omega_a = 8.247e9
k_int = 1.4e6
k_1 = 45.5e6
k_2 = 4.5e6
k_3 = 1.33e6
k_c = k_int + k_1 + k_2 + k_3
gamma_int = 1.14e6
gamma_e = 1.13e6
gamma = gamma_int + gamma_e
g = 8e6

def S12cur(omega_ss,delta,phi1,delta1,phi12,delta_m12):
    omega_m12=omega_a+delta_m12*1e6
    delta_m12 = omega_m12 - omega_ss
    delta_a = omega_a - omega_ss
    chi_a = 1j * delta_a + k_c / 2
    chi_m12 = 1j * delta_m12 + gamma / 2
    fenmu12 = chi_a * chi_m12 + g ** 2
    fenzi12 = (chi_m12 * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * (phi + phi12) * np.pi))
    t12 = fenzi12 / fenmu12
    S12 = rf.mag_2_db(np.abs(t12))
    return S12


a1,a2=scipy.optimize.curve_fit(S12cur,omega_se,S12e,
                         p0=[delta_inf,0.75,0.97,-0.2,-32],
                         bounds=([delta_inf*0.8,0.6,0.95,-0.5,-35],
                                 [delta_inf*1.2,0.9,1,0,-30]))


print(a1)
# print(a2)
# phi1 = 0.75
#
# delta1 = 0.97
#
# phi12 = -0.330

S12s=S12cur(omega_se,a1[0],a1[1],a1[2],a1[3],a1[4])
fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.plot(omega_se,S12e,'-',linewidth=10,label=r'$S_{12,exp}$',color='green',alpha=0.4)
axes1.plot(omega_se,S12s,'-',linewidth=3,label=r'$S_{12,sim}$',color='green',zorder=2)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
axes1.set_ylim(-105,5)
plt.yticks([-100,-75,-50,-25,0],['-100','-75','-50','-25','0'])
plt.tick_params(labelsize=20)
plt.legend(loc=3,prop={'family':'Cambria','size':20})
plt.show()