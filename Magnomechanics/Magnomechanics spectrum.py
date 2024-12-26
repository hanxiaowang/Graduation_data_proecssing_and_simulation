import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
# D=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\multi\cavity S11 for reference21_33_38.txt')
# f=[rows[0] for rows in D]
# S=[rows[1] for rows in D]
# #
# # D=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\multi\cavity S11 for reference21_30_33.txt')
# # f=[rows[0] for rows in D]
# # S=[rows[1] for rows in D]
#
# # D=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\multi\cavity S11 for reference21_16_51.txt')
# # f=[rows[0] for rows in D]
# # S=[rows[1] for rows in D]
#
#
#
# deltad=[]
# for i in range(len(f)):
#     deltad.append((f[i]-8.275735e9)/1e6)
#
#
# hbar = 6.626e-34/(2*np.pi)
# omega_p1=f
# P_d=23.4
# P_p=-10
# omega_a=8.290443e9* 2 * np.pi
# omega_m= 8.29195e9* 2 * np.pi
# # omega_m= 8.2918e9* 2 * np.pi
# kai=1.31e6* 2 * np.pi
# kaep=1.32e6* 2 * np.pi
# kaed=1.15e6* 2 * np.pi
# omega_d=8.275735e9* 2 * np.pi
# g_ma=4.85e6* 2 * np.pi
# km=1.56e6* 2 * np.pi
# kmed=0
# omega_b=10.48182e6* 2 * np.pi
# g_mb=5e-3* 2 * np.pi
# kb=4500* 2 * np.pi
# # omega_b=10.45295e6* 2 * np.pi
# # g_mb=3e-3* 2 * np.pi
# # kb=450* 2 * np.pi
# P_d1 = 10 ** (P_d / 10 - 3)  # W
# P_p1 = 10 ** (P_p / 10 - 3)  # W
#
#
# delta_a = omega_a - omega_d
# delta_m = omega_m - omega_d
#
# Simulation = []
# ka=kai+kaed+kaep
# # shift=-21.58
# shift=-21.62
# for i in range(len(omega_p1)):
#     e_d = np.sqrt(P_d1 / (hbar * omega_d))
#     e_p = np.sqrt(P_p1 / (hbar * omega_p1[i] * 2 * np.pi))
#     E_d = np.sqrt(kaed) * e_d+np.sqrt(kmed)*e_d*np.abs(g_ma/(1j*delta_a+ka/2))**2
#     E_p = np.sqrt(kaep) * e_p
#
#     delta = omega_p1[i] * 2 * np.pi - omega_d
#
#     ms = (-1j * g_ma * E_d) / (
#             (1j * delta_m + km / 2) * (1j * delta_a + ka / 2) + g_ma ** 2)
#     G = ms * g_mb
#
#     h_ap = -1j * (delta_a + delta) - ka / 2
#     h_am = -1j * (delta_a - delta) - ka / 2
#     h_mp = -1j * (delta_m + delta) - km / 2
#     h_mm = -1j * (delta_m - delta) - km / 2
#     h_bp = -1j * (omega_b + delta) - kb / 2
#     h_bm = -1j * (omega_b - delta) - kb / 2
#
#     H = 1 / h_bp - 1 / h_bm.conjugate()
#
#     W_p = h_ap * (h_mp + H * np.abs(G) ** 2)
#     W_m = h_am * (h_mm - H.conjugate() * np.abs(G) ** 2)
#
#     X_p = h_ap * H * G ** 2
#     X_m = h_am * H.conjugate() * G ** 2
#
#     A_m = (g_ma ** 2 * E_p * (W_p.conjugate() + g_ma ** 2)) / (
#             h_am * (X_m * X_p.conjugate() + (W_m + g_ma ** 2) * (
#             W_p.conjugate() + g_ma ** 2))) - E_p / h_am
#     t = 1 - (kaep * A_m) / E_p
#     Simulation.append(rf.mag_2_db(np.abs(t))+shift)
#
#
#
#
#
#
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.scatter(deltad,S,label='Experiment',color='none',edgecolors='red',s=100,linewidth=1)
# # axes.plot(deltad,S,'--',color='red',linewidth=2)
# # axes.plot(deltad,S,'--',label='Experiment',color='red',linewidth=2)
# axes.plot(deltad,Simulation,'-',label='Simulation',color='blue',linewidth=5)
# axes.set_xlabel('$\delta_p/2\pi$ [MHz]',fontsize=40)
# axes.set_ylabel('$S_{11}$ [dB]',fontsize=40)
# plt.yticks([-28.15, -28.20, -28.25, -28.30,], ['-28.15', '-28.20', '-28.25', '-28.30'])
# # plt.yticks([-27.8, -27.9, -28.0, -28.1,-28.2], ['-27.80', '-27.90', '-28.00', '-28.10','-28.20'])
# # plt.yticks([ -28.3, -28.0, -28.1,-28.2], [ '-28.30', '-28.00', '-28.10','-28.20'])
# plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=40)
# plt.show()
#


D1=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\single\cavity S11 for reference13_18_1.txt')
f1=[rows[0] for rows in D1]
S1=[rows[1] for rows in D1]
delta1=[]
for i in range(len(f1)):
    delta1.append((f1[i]-8.2877)*1e3)

D2=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\single\cavity S11 for reference13_22_54.txt')
f2=[rows[0] for rows in D2]
S2=[rows[1] for rows in D2]
delta2=[]
for i in range(len(f2)):
    delta2.append((f2[i]-8.2877)*1e3)

D3=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\single\cavity S11 for reference14_50_12.txt')
f3=[rows[0] for rows in D3]
S3=[rows[1] for rows in D3]
delta3=[]
for i in range(len(f3)):
    delta3.append((f3[i]-8.28788)*1e3)

D4=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Magnomechanics spectrum\single\cavity S11 for reference14_50_52.txt')
f4=[rows[0] for rows in D4]
S4=[rows[1] for rows in D4]
delta4=[]
for i in range(len(f4)):
    delta4.append((f4[i]-8.28788)*1e3)

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(delta1,S1,'--',color='blue',linewidth=2)
# axes.plot(delta2,S2,'--',color='blue',linewidth=2)
# axes.plot(delta3,S3,'--',color='blue',linewidth=2)
axes.plot(delta4,S4,'--',color='blue',linewidth=2)
# axes.plot(deltad,S,'--',label='Experiment',color='red',linewidth=2)
axes.set_xlabel('$\delta_p/2\pi$ [MHz]',fontsize=40)
axes.set_ylabel('$S_{11}$ [dB]',fontsize=40)
plt.xticks([-10.47, -10.46, -10.45, -10.44,-10.43], ['-10.47', '-10.46', '-10.45', '-10.44','-10.43'])

plt.tick_params(labelsize=35)
# plt.legend(loc=1,fontsize=40)
plt.show()
