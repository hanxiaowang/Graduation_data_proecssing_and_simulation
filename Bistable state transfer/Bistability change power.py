import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
P = np.linspace(0, 0.3, 301)

para = {'omega_a': 8.246,
        'omega_m': 8.184,
        'kaint': 3.39,
        'kaed': 2.974,
        'kmint': 1.011,
        'kmext': 0,
        'g_ma': 32.649,
        'K': 30,
        'branch': 'upper',
        'omega_d': 8.18,
        'P_d': P,
        }

forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_inside_BS()

fpindex = list(forwardp).index(0.1)
# print(fpindex)
bpindex = list(backwardp).index(0.1)
upindex = list(unstablep).index(0.1)

# print(forwardp)
# print(forwardp[100])
plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot(forwardp, forward, 'o', linewidth=5,color='orange',markersize=10,label=r'forward')
axes1.plot(backwardp, backward, '^', linewidth=5, color='blue',label=r'backward')
axes1.plot(unstablep,unstable, '--', linewidth=5, color='purple',label=r'unstable')
axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=4)
plt.show()

wminf=8.184*1e9*2*np.pi
wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz
# print(wpinf/(1e9*2*np.pi))

##每个w+对应的wm,单位Hz
wmf=Bistability(**para).wplus_to_wm(wpinf+np.array(forward)*1e6*2*np.pi)
wmb=Bistability(**para).wplus_to_wm(wpinf+np.array(backward)*1e6*2*np.pi)
wmu=Bistability(**para).wplus_to_wm(wpinf+np.array(unstable)*1e6*2*np.pi)

# print(wmf/(1e9*2*np.pi))
##计算ms和as
msf,asf=Bistability(**para).cal_ms_as_P(wmf-wminf,forwardp)
msb,asb=Bistability(**para).cal_ms_as_P(wmb-wminf,backwardp)
msu,asu=Bistability(**para).cal_ms_as_P(wmu-wminf,unstablep)

##计算\Delta_m,单位Hz
msf2=np.abs(msf)**2*2*30*1e-9*2*np.pi
msb2=np.abs(msb)**2*2*30*1e-9*2*np.pi
msu2=np.abs(msu)**2*2*30*1e-9*2*np.pi

##计算\Delta_plus,单位MHz
deltamsf2=(Bistability(**para).branch_fre(wminf+msf2)-wpinf)/(1e6*2*np.pi)
deltamsb2=(Bistability(**para).branch_fre(wminf+msb2)-wpinf)/(1e6*2*np.pi)
deltamsu2=(Bistability(**para).branch_fre(wminf+msu2)-wpinf)/(1e6*2*np.pi)

# print((wpinf+np.array(forward)*1e6*2*np.pi)/(1e9*2*np.pi))
# print((Bistability(**para).branch_fre(wmf+msf2))/(1e9*2*np.pi))

# ## ms的实部随着power变化
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(forwardp, msf.real, 'o', linewidth=5, label=r'forward')
# axes1.plot(backwardp, msb.real, '^', linewidth=5, label=r'backward')
# axes1.plot(unstablep,msu.real, '--', linewidth=5, label=r'unstable')
# axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes1.set_ylabel(r'$m_s$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4)
# plt.show()
#
# ## ms的虚部随着power变化
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(forwardp, msf.imag, 'o', linewidth=5, label=r'forward')
# axes1.plot(backwardp, msb.imag, '^', linewidth=5, label=r'backward')
# axes1.plot(unstablep,msu.imag, '--', linewidth=5, label=r'unstable')
# axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes1.set_ylabel(r'$m_s$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4)
# plt.show()

# # ## ms的实部随着power变化
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(211)
# axes1.plot(forwardp, msf.real, 'o', linewidth=5, label=r'forward')
# axes1.plot(backwardp, msb.real, '^', linewidth=5, label=r'backward')
# axes1.plot(unstablep,msu.real, '--', linewidth=5, label=r'unstable')
# axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes1.set_ylabel(r'$Re$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4)
#
# ## ms的虚部随着power变化
# axes2 = plt.subplot(212)
# axes2.plot(forwardp, msf.imag, 'o', linewidth=5, label=r'forward')
# axes2.plot(backwardp, msb.imag, '^', linewidth=5, label=r'backward')
# axes2.plot(unstablep,msu.imag, '--', linewidth=5, label=r'unstable')
# axes2.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes2.set_ylabel(r'$Im$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4)
# plt.show()

## ms的实部虚部分布
plt.figure(figsize=(10, 6))
axes1 = plt.subplot(111)
axes1.plot(msf.real, msf.imag, '^', linewidth=5, color='orange',label=r'forward')
axes1.plot(msf.real[fpindex], msf.imag[fpindex], 's', markersize=10)


axes1.plot(msb.real, msb.imag, 'o', linewidth=5,color='blue', markersize=8, label=r'backward',markerfacecolor='None')
axes1.plot(msb.real[bpindex], msb.imag[bpindex], 's', markersize=10)

axes1.plot(msu.real,msu.imag, 'o', linewidth=5, color='purple',label=r'unstable',markerfacecolor='None')
axes1.plot(msu.real[upindex],msu.imag[upindex], 's', markersize=10)

axes1.set_xlabel(r'Real', fontsize=20)
axes1.set_ylabel(r'Imag', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()

## as的实部虚部分布
# plt.figure(figsize=(10, 6))
# axes1 = plt.subplot(111)
# axes1.plot(asf.real, asf.imag, '^', linewidth=5, label=r'forward')
# axes1.plot(asf.real[fpindex], asf.imag[fpindex], 's', markersize=10)
#
#
# axes1.plot(asb.real, asb.imag, 'o', linewidth=5, markersize=8, label=r'backward',markerfacecolor='None')
# axes1.plot(asb.real[bpindex], asb.imag[bpindex], 's', markersize=10)
#
# axes1.plot(asu.real,asu.imag, 'o', linewidth=5, label=r'unstable',markerfacecolor='None')
# axes1.plot(asu.real[upindex],asu.imag[upindex], 's', markersize=10)
#
# axes1.set_xlabel(r'Real', fontsize=20)
# axes1.set_ylabel(r'Imag', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()

##Delta_m的验算
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(forwardp, forward, '--', linewidth=5, label=r'forward')
# axes1.plot(forwardp, deltamsf2, 'o', linewidth=5, label=r'forward1',markerfacecolor='None')
# axes1.plot(backwardp, backward, '--', linewidth=5, label=r'backward')
# axes1.plot(backwardp, deltamsb2, 'o', linewidth=5, label=r'backward1',markerfacecolor='None')
# axes1.plot(unstablep, unstable, '--', linewidth=5, label=r'unstable')
# axes1.plot(unstablep, deltamsu2, 'o', linewidth=5, label=r'unstable1',markerfacecolor='None')
#
# axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes1.set_ylabel(r'$\Delta_m$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4)
# plt.show()
