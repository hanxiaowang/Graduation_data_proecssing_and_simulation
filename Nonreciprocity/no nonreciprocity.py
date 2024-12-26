import numpy as np
import matplotlib.pyplot as plt
import skrf as rf



##larger
Dl21=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\S21\cavity S21 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Dl21]
Sl21=[rows[2] for rows in Dl21]

Dl12=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\S12\cavity S12 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Dl12]
Sl12=[rows[2] for rows in Dl12]

# Dl21=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\S21\cavity S21 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Dl21]
# Sl21=[rows[2] for rows in Dl21]
#
# Dl12=np.loadtxt(r'F:\Nonreciprocity\20210703\m lager than a\S12\cavity S12 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Dl12]
# Sl12=[rows[2] for rows in Dl12]

##smaller
Ds21=np.loadtxt(r'F:\Nonreciprocity\20210703\m smaller than a\S21\cavity S21 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Ds21]
Ss21=[rows[2] for rows in Ds21]

Ds12=np.loadtxt(r'F:\Nonreciprocity\20210703\m smaller than a\S12\cavity S12 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Ds12]
Ss12=[rows[2] for rows in Ds12]


# Ds21=np.loadtxt(r'F:\Nonreciprocity\20210703\m smaller than a\S21\cavity S21 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Ds21]
# Ss21=[rows[2] for rows in Ds21]
#
# Ds12=np.loadtxt(r'F:\Nonreciprocity\20210703\m smaller than a\S12\cavity S12 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Ds12]
# Ss12=[rows[2] for rows in Ds12]

# ##resonant
Dr21=np.loadtxt(r'F:\Nonreciprocity\20210701\S21\cavity S21 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Dr21]
Sr21=[rows[2] for rows in Dr21]

Dr12=np.loadtxt(r'F:\Nonreciprocity\20210701\S12\cavity S12 with magnetic field without Drive.txt',dtype=complex)
f=[rows[0] for rows in Dr12]
Sr12=[rows[2] for rows in Dr12]
#
# Dr21=np.loadtxt(r'F:\Nonreciprocity\20210701\S21\cavity S21 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Dr21]
# Sr21=[rows[2] for rows in Dr21]
#
# Dr12=np.loadtxt(r'F:\Nonreciprocity\20210701\S12\cavity S12 with magnetic field with IQ off.txt',dtype=complex)
# f=[rows[0] for rows in Dr12]
# Sr12=[rows[2] for rows in Dr12]
isol=[]
isos=[]
isor=[]
fp=[]

for i in range(len(f)):
    isol.append(Sl21[i] - Sl12[i])
    isos.append(Ss21[i] - Ss12[i])
    isor.append(Sr21[i] - Sr12[i])
    fp.append(f[i]/1e9)




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

# omega_m = (8.247 - 0.032) * 1e9
# omega_m = (8.247 +0.063) * 1e9
# omega_m = (8.247 - 0.002) * 1e9

omega_m = (8.247 - 0.2) * 1e9

# omega_s = np.linspace(omega_m - 50e6, omega_m + 50e6, 1001)
# omega_s = np.linspace(omega_a - 50e6, omega_m + 50e6, 10001)
omega_s = np.linspace(omega_m - 50e6, omega_a + 50e6, 10001)
S21=[]

for i in range(len(omega_s)):
    delta_m = omega_m - omega_s[i]
    delta_a = omega_a - omega_s[i]

    delta1=0
    delta=0
    phi=0
    phi1=0

    chi_a = 1j * delta_a + k_c / 2
    chi_m = 1j * delta_m + gamma / 2
    fenmu = chi_a * chi_m + g ** 2
    t21 = np.sqrt(k_1) * (chi_m * (np.sqrt(k_2) + np.sqrt(k_3) * delta1 * delta * np.exp(
        -1j * (phi1) * np.pi - 1j * phi)) - 1j * g * np.sqrt(gamma_e) * delta * np.exp(-1j * phi)) / fenmu

    S21.append(rf.mag_2_db(np.abs(t21))-32.9)








fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(fp,isol,'--',linewidth=2)
# axes.plot(fp,isos,'--',linewidth=2)
# axes.plot(fp,isor,'--',linewidth=2)
# axes.plot(fp,Sl21,'--',linewidth=2,label='E')
# axes.plot(fp,Ss21,'--',linewidth=2,label='E')
axes.plot(fp,Sr21,'--',linewidth=2,label='E')
# axes.plot(omega_s/1e9,S21,'--',linewidth=2,label='S')
# axes.plot(omega_s/1e9,S21,'-',linewidth=5)
axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
axes.set_ylabel(r'$S_{21}$ [dB]',fontsize=40)

plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=40)
plt.show()