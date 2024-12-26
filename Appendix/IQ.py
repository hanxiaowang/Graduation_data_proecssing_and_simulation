import numpy as np
import matplotlib.pyplot as plt


aftrtI = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\after I.txt')
aftrtQ = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\after Q.txt')
aftrtphi = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\after phi.txt')
aftrtalpha = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\after all.txt')

aftrtIs=[rows[1] for rows in aftrtI]
aftrtQs=[rows[1] for rows in aftrtQ]
aftrtphis=[rows[1] for rows in aftrtphi]
aftrtalphas=[rows[1] for rows in aftrtalpha]

f=[]
for i in range(len(aftrtalphas)):
 f.append([rows[0] for rows in aftrtalpha][i]/1e9)



fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(f, aftrtIs)
# axes.plot(f, aftrtQs)
# axes.plot(f, aftrtphis)
axes.plot(f, aftrtalphas)
axes.set_xlabel(r'$\omega_p$[GHz]', fontsize=40)
axes.set_ylabel('S[dBm]', fontsize=40)
# axes.set_title('dB_vs_frequency', fontsize=14)
plt.tick_params(labelsize=35)
# plt.legend(loc=2)
plt.show()







# # duringI = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\I_middle.txt')
# duringQ = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\Q_middle.txt')
# duringphi = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\Phi_low.txt')
# duringalpha = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\IQC 10_47_33\Amp_low.txt')
#
# # duringIx=[rows[0] for rows in duringI]
# duringQx=[rows[0] for rows in duringQ]
# duringphix=[rows[0] for rows in duringphi]
# duringalphax=[rows[0] for rows in duringalpha]
#
# # duringIs=[rows[1] for rows in duringI]
# duringQs=[rows[1] for rows in duringQ]
# duringphis=[rows[1] for rows in duringphi]
# duringalphas=[rows[1] for rows in duringalpha]
#
#
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(duringIx, duringIs)
# # axes.plot(duringQx, duringQs)
# # axes.set_xlabel(r'$V_{Q}$[V]', fontsize=40)
# # axes.set_ylabel(r'$S_{\omega_{LO}}$[dBm]', fontsize=40)
# axes.plot(duringphix, duringphis)
# axes.set_xlabel(r'$\Delta\phi$[$\pi$]', fontsize=40)
# axes.set_ylabel(r'$S_{\delta\omega}$[dBm]', fontsize=40)
# # axes.plot(duringalphax, duringalphas)
# # axes.set_xlabel(r'$\delta$', fontsize=40)
# # axes.set_ylabel(r'$S_{\delta\omega}$[dBm]', fontsize=40)
# # axes.set_title('dB_vs_frequency', fontsize=14)
# plt.tick_params(labelsize=35)
# # plt.legend(loc=2)
# plt.show()

#
# compare=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\compare.txt')
# f=[rows[0] for rows in compare]
# slow=[rows[1] for rows in compare]
# smid=[rows[2] for rows in compare]
# shigh=[rows[3] for rows in compare]
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
#
# axes.plot(f, slow,label=r'$S_{\delta\omega}$')
# axes.plot(f, smid,label=r'$S_{\omega_{LO}}$')
# axes.plot(f, shigh,label=r'$S_{\omega_\Sigma}$')
# axes.set_xlabel(r'$\omega_{LO}/2\pi$[GHz]', fontsize=40)
# axes.set_ylabel(r'$S$[dBm]', fontsize=40)
# plt.tick_params(labelsize=35)
# plt.legend(loc=6,fontsize=30)
# plt.show()