import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json

omega_a = 8.247e9
# delta_ms=np.linspace(-100,100,41)
delta_ms = [-500*1e6,-300*1e6,-100*1e6,-50*1e6,50*1e6,100*1e6,300*1e6,500*1e6]

de = 0
omega_m = omega_a+delta_ms[de]
omega_s = np.linspace(omega_m - 60e6, omega_m + 60e6, 2001)
# omega_s = np.linspace(8.16e9, 8.36e9, 20001)

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
voltage = np.linspace(20, 110, 19)
deltas = 0.97 * voltage / 45


phi1 = 0.77
delta1 = 1

zhengti=0
chazhi=0  #63
phi12=(zhengti+chazhi)
phi21=(zhengti)

Iso = []
for i in range(len(phis)):
    phi = phis[i]
    isos = []
    for c in range(len(deltas)):
        delta = deltas[c]
        # T12 = []
        # T21 = []
        iso = []
        isoabs = []

        delta_m = omega_m - omega_s
        delta_a = omega_a - omega_s
        chi_a = 1j * delta_a + k_c / 2
        chi_m = 1j * delta_m + gamma / 2
        fenmu = chi_a * chi_m + g ** 2

        fenzi21 =  (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_2*k_3) * delta1 * delta * np.exp(
            -1j * (phi + phi1 + phi12)*np.pi)) - 1j * g * np.sqrt(k_2*gamma_e) * delta * np.exp(-1j * (phi + phi12)*np.pi))
        fenzi12 = (chi_m * (np.sqrt(k_1*k_2) + np.sqrt(k_1*k_3) * delta1 * delta * np.exp(
            -1j * (phi + phi1 + phi21)*np.pi)) - 1j * g * np.sqrt(k_1*gamma_e) * delta * np.exp(-1j * (phi + phi21)*np.pi))

        t12 = fenzi12 / fenmu
        t21 = fenzi21 / fenmu

        # T12.append(rf.mag_2_db(np.abs(t12)))
        # T21.append(rf.mag_2_db(np.abs(t21)))
        S12=rf.mag_2_db(np.abs(t12))
        S21=rf.mag_2_db(np.abs(t21))

        iso=S12-S21
        isoabs=np.abs(S12-S21)

        index = np.where(isoabs==max(isoabs))
        need = iso[index][0]
        isos.append(need)
    Iso.append(isos)

# -0.032
# +0.063








delta_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'delta.txt')
phi_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'phi.txt')
voltage_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'voltage.txt')
vna_path = os.path.join(r'C:\Users\AORUS\OneDrive\桌面\nonreciprocity', 'vna fre.txt')
np.savetxt(delta_path, deltas, fmt='%.4f')
np.savetxt(phi_path, phis, fmt='%.4f')
np.savetxt(voltage_path, voltage, fmt='%.4f')
np.savetxt(vna_path, omega_s, fmt='%.4f')
path = f'C:\\Users\\AORUS\\OneDrive\\桌面\\nonreciprocity\\{round(delta_ms[de])}'
if os.path.exists(path) == True:
    pass
else:
    os.mkdir(path)
para = {
    'omega_m': omega_m,
    'phi1': phi1,
    'delta1': delta1,
    'phi12': phi12,
    'phi21': phi21,
}
Iso_path = os.path.join(path, 'Iso.txt')
para_path = os.path.join(path, 'para.json')
np.savetxt(Iso_path, Iso, fmt='%.4f')

with open(para_path, 'w') as fp:
    json.dump(para, fp, indent=1)
    fp.close
picture_path = os.path.join(path, 'Iso.png')



Vs = np.linspace(20, 110, 19)
phie = np.linspace(0, 2, 361)

plt.figure(figsize=(12, 12))
ax1 = plt.subplot(111)
gci1 = ax1.pcolor(deltas, phis, Iso,cmap='bwr')
ax1.set_xlabel(r'$\delta$',fontsize=30)
ax1.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=30)
plt.tick_params(labelsize=30)
cbar = plt.colorbar(gci1)
plt.savefig(picture_path)

plt.show()
