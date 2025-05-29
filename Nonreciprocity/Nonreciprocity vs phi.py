import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
de = 1

if de==0:
    start =0
    stop = 10001
elif de==1:
    start = 5000
    stop = 15001
elif de==2:
    start = 10000
    stop = 20001

voltages=[20,70,30]
voltage=voltages[de]

S12l=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m lager than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltages[2])}.0 mV 2D.txt',delimiter=',')[start:stop,:]
S21l=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m lager than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltages[2])}.0 mV 2D.txt',delimiter=',')[start:stop,:]
Isol=S12l-S21l

S12s=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltages[0])}.0 mV 2D.txt',delimiter=',')[start:stop,:]
S21s=np.loadtxt(f'F:\\Nonreciprocity\\20210703\\m smaller than a\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltages[0])}.0 mV 2D.txt',delimiter=',')[start:stop,:]
Isos=S12s-S21s


S12r=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltages[1])}.0 mV 2D.txt',delimiter=',')[start-400:stop-400,:]
S21r=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltages[1])}.0 mV 2D.txt',delimiter=',')[start-400:stop-400,:]
Isor=S12r-S21r



S12es=[]
S21es=[]
Isoes=[]

S12es.append(S12s)
S12es.append(S12r)
S12es.append(S12l)

S21es.append(S21s)
S21es.append(S21r)
S21es.append(S21l)

Isoes.append(Isos)
Isoes.append(Isor)
Isoes.append(Isol)

S12e=S12es[de]
S21e=S21es[de]
Isoe=Isoes[de]

fe=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\f.txt')[start:stop]

fe_start=fe[0]
fe_stop=fe[-1]
print(fe_start)
print(fe_stop)
phie=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\phi.txt')

print(np.shape(S12r))
print(np.shape(fe))
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

phis = np.linspace(0, 2, 361)

## deltas = 0.97 * voltage / 50  #63
# deltas = 0.97 * voltage / 45  #-32 -2
# deltas = 0.97 * voltage / 45  #-2

deltass=[45,45,50]
delta=0.97*voltage/deltass[de]
print(delta)

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
Iso = []
for i in range(len(phis)):
    phi = phis[i]

    delta_m = omega_m - omega_s
    delta_a = omega_a - omega_s
    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2

    fenzi21 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_2 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi21) * np.pi)) - 1j * g * np.sqrt(k_2 * gamma_e) * delta * np.exp(
        -1j * (phi + phi21) * np.pi))
    fenzi12 = (chi_m * (np.sqrt(k_1 * k_2) + np.sqrt(k_1 * k_3) * delta1 * delta * np.exp(
        -1j * (phi + phi1 + phi12) * np.pi)) - 1j * g * np.sqrt(k_1 * gamma_e) * delta * np.exp(
        -1j * (phi + phi12) * np.pi))

    t12 = fenzi12 / fenmu
    t21 = fenzi21 / fenmu

    # T12.append(rf.mag_2_db(np.abs(t12)))
    # T21.append(rf.mag_2_db(np.abs(t21)))
    S12 = rf.mag_2_db(np.abs(t12))
    S21 = rf.mag_2_db(np.abs(t21))

    T12.append(S12)
    T21.append(S21)
    Iso.append(S12-S21)

# -0.032
# +0.063

# plt.figure(figsize=(18,12))
# ax1 = plt.subplot(231)
# gci1 = ax1.pcolor(phis, fe, S12l)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# # cmap='bwr'
# #
# ax2 = plt.subplot(232)
# gci2 = ax2.pcolor(phis, fe,S21l)
# # ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci2)
#
# ax3 = plt.subplot(233)
# gci3 = ax3.pcolor(phis, fe,Isol)
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci3)
# #
#
# ax4 = plt.subplot(234)
# gci4 = ax4.pcolor(phis, omega_s/1e9, np.transpose(T12))
# ax4.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax4.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci4)
#
# #
# ax5 = plt.subplot(235)
# gci5 = ax5.pcolor(phis, omega_s/1e9,np.transpose(T21))
# ax5.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax5.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci5)
#
# ax6 = plt.subplot(236)
# gci6 = ax6.pcolor(phis, omega_s/1e9,np.transpose(Iso))
# ax6.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax6.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci6)
#
# plt.show()


# plt.figure(figsize=(18,12))
# ax1 = plt.subplot(231)
# gci1 = ax1.pcolor(phis, fe, S12s)
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
# # cmap='bwr'
# #
# ax2 = plt.subplot(232)
# gci2 = ax2.pcolor(phis, fe,S21s)
# # ax2.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax2.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci2)
#
# ax3 = plt.subplot(233)
# gci3 = ax3.pcolor(phis, fe,Isos)
# # ax3.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax3.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci3)
# #
#
# ax4 = plt.subplot(234)
# gci4 = ax4.pcolor(phis, omega_s/1e9, np.transpose(T12))
# ax4.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax4.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci4)
#
# #
# ax5 = plt.subplot(235)
# gci5 = ax5.pcolor(phis, omega_s/1e9,np.transpose(T21))
# ax5.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax5.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci5)
#
# ax6 = plt.subplot(236)
# gci6 = ax6.pcolor(phis, omega_s/1e9,np.transpose(Iso))
# ax6.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# # ax6.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci6)
#
# plt.show()


plt.figure(figsize=(18,12))

ax1 = plt.subplot(231)
extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
im = ax1.imshow(np.transpose(T12), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)

# cmap='bwr'
#
ax2 = plt.subplot(232)
extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
im = ax2.imshow(np.transpose(T21), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)

ax3 = plt.subplot(233)
extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
im = ax3.imshow(np.transpose(Iso), extent=extents, cmap="bwr",aspect='auto',origin='lower')
plt.colorbar(im)
#

ax4 = plt.subplot(234)
extents=[phis[0],phis[-1],fe[0],fe[-1]]
im = ax4.imshow(S12e, extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)

#
ax5 = plt.subplot(235)
extents=[phis[0],phis[-1],fe[0],fe[-1]]
im = ax5.imshow(S21e, extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)

ax6 = plt.subplot(236)
extents=[phis[0],phis[-1],fe[0],fe[-1]]
im = ax6.imshow(Isoe, extent=extents, cmap="bwr",aspect='auto',origin='lower')
plt.colorbar(im)

plt.show()


#
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(np.transpose(T12), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
#
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(np.transpose(T21), extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],omega_s[0],omega_s[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(np.transpose(Iso), extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
# ##### resonant
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],fe[0],fe[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(S12e, extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
#
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],fe[0],fe[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(S21e, extent=extents, aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#
#
# plt.figure(figsize=(6,6))
# extents=[phis[0],phis[-1],fe[0],fe[-1]]
# ax1 = plt.subplot(111)
# im = ax1.imshow(Isoe, extent=extents, cmap="bwr",aspect='auto',origin='lower')
# plt.colorbar(im)
# plt.show()
#

