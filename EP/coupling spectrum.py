import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import sys

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


## 三振子模拟
omega_c = 8.246190999498149e9 * 2 * np.pi
kcint = 12.429387518053709e6 * 2 * np.pi
kcext = 11.783464821423435e6 * 2 * np.pi
kc = kcint + kcext

kA = 1.0021259402425182e6 * 2 * np.pi
gA = 30.923698690048464e6 * 2 * np.pi

kB = 2.026588034397236e6 * 2 * np.pi
gB = 4.954180265548075e6 * 2 * np.pi

# omega_c=8.246190999498149e9*2*np.pi
# kcint=12.429387518053709e6*2*np.pi
# kcext=11.783464821423435e6*2*np.pi
# kc=kcint+kcext

# kA=1.0021259402425182e6*2*np.pi
# gA=30.923698690048464e6*2*np.pi

# kB=2.026588034397236e6*2*np.pi
# gB=4.954180265548075e6*2*np.pi
# wa = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\upper branch\omegaAp.txt')
wa=np.linspace(8.0,8.5,501)
omega_As = wa * 1e9 * 2 * np.pi
omega_Bs = omega_c + np.linspace(-200, 200, 1001) * 1e6 * 2 * np.pi

Kplus = []
Kminus = []

Gplus = []
Gminus = []

Wplus = []
Wminus = []

Sin = []
Cos = []

Zero = []

for i, omega_A in enumerate(omega_As):
    Delta = omega_c - omega_A

    middle = np.sqrt(Delta ** 2 + 4 * gA ** 2)

    sintheta = np.sqrt((-Delta + middle) / (2 * middle))
    costheta = np.sqrt((Delta + middle) / (2 * middle))

    Sin.append(sintheta)
    Cos.append(costheta)

    kplus = costheta ** 2 * kc + sintheta ** 2 * kA
    kminus = sintheta ** 2 * kc + costheta ** 2 * kA

    gplus = gB * costheta
    gminus = gB * sintheta

    wplus = (omega_c + omega_A) / 2 + middle / 2
    wminus = (omega_c + omega_A) / 2 - middle / 2

    Kplus.append(kplus / (1e6 * 2 * np.pi))
    Kminus.append(kminus / (1e6 * 2 * np.pi))

    Gplus.append(np.abs(gplus) / (1e6 * 2 * np.pi))
    Gminus.append(np.abs(gminus) / (1e6 * 2 * np.pi))

    Wplus.append(wplus / (1e9 * 2 * np.pi))
    Wminus.append(wminus / (1e9 * 2 * np.pi))

# wp1 = np.linspace(8.25,8.35,141)
fprint = np.linspace(-100, 100, 4001) * 1e-3
S_2D_3 = []
S_2D_2 = []
for i in range(len(wa)):
    f = (Wplus[i] + fprint) * 1e9 * 2 * np.pi

    delta_c = omega_c - f
    delta_a = wa[i]* 1e9 * 2 * np.pi - f
    delta_b = Wplus[i] * 1e9 * 2 * np.pi - f

    mi = 1j * delta_c + kc / 2 + gA ** 2 / (1j * delta_a + kA / 2) + gB ** 2 / (1j * delta_b + kB / 2)

    r = 1 - kcext / mi

    S_2D_3.append(rf.mag_2_db(np.abs(r)))

# omega_c=8.246190999498149e9*2*np.pi
# kcint=12.429387518053709e6*2*np.pi
# kcext=11.783464821423435e6*2*np.pi
# kc=kcint+kcext


# kA=1.0021259402425182e6*2*np.pi
# gA=30.923698690048464e6*2*np.pi

# kB=2.026588034397236e6*2*np.pi
# gB=4.954180265548075e6*2*np.pi
# p2ds = {
#     'x1': wa,
#     'y1': fprint * 1e3,
#     'z1': np.transpose(S_2D_3),
#     'switch': 'on',
#     'xname': r'$\omega_A$',
#     'yname': r'$\omega_p-\omega_+$',
# }
# pe(**p2ds).Plot_2D(**p2ds)

#
# p1w = {
#     'x1': wa,
#     'y1': Wplus,
#     'label1':r'$\omega_+$',
#     'x2': wa,
#     'y2': Wminus,
#     'label2': r'$\omega_-$',
#     'switch': 'on',
#     'xname': r'$\omega_A$',
#     'yname': r'$\omega$',
# }
# pe(**p1w).Plot_1D(**p1w)
# #
# p1k = {
#     'x1': wa,
#     'y1': Kplus,
#     'label1':r'$\kappa_+$',
#     'x2': wa,
#     'y2': Kminus,
#     'label2': r'$\kappa_-$',
#     'switch': 'on',
#     'xname': r'$\omega_A$',
#     'yname': r'$\kappa$',
# }
# pe(**p1k).Plot_1D(**p1k)
#
p1g = {
    'x1': wa,
    'y1': Gplus,
    'label1':r'$g_+$',
    'x2': wa,
    'y2': Gminus,
    'label2': r'$g_-$',
    'switch': 'on',
    'xname': r'$\omega_A$',
    'yname': r'$g$',
}
pe(**p1g).Plot_1D(**p1g)

# print(Gplus)
# print(Gminus)