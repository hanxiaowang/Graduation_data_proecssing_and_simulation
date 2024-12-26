import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
f = np.linspace(8.14, 8.22, 801)

para = {'omega_a': 8.246,
        'omega_m': 8.184,
        'kaint': 3.39,
        'kaed': 2.974,
        'kmint': 1.011,
        'kmext': 0,
        'g_ma': 32.649,
        'K': 30,
        'branch': 'upper',
        'omega_d': f,
        'P_d': 0.1,
        }

forward, forwardf, backward, backwardf, unstable, unstablef=Bistability(**para).BS_fre_with_unstable()



plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot(forwardf, forward, 'o', linewidth=5,markersize=10,label=r'forward')
axes1.plot(backwardf, backward, '^', linewidth=5, label=r'backward')
axes1.plot(unstablef,unstable, '--', linewidth=5, label=r'unstable')
axes1.set_xlabel(r'$f_d$ [GHz]', fontsize=20)
axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()

fpindex = list(forwardf).index(8.18)
# print(fpindex)
bpindex = list(backwardf).index(8.18)
upindex = list(unstablef).index(8.18)


wminf=8.184*1e9*2*np.pi
wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz
# # print(wpinf/(1e9*2*np.pi))
#
# ##每个w+对应的wm,单位Hz
wmf=Bistability(**para).wplus_to_wm(wpinf+np.array(forward)*1e6*2*np.pi)
wmb=Bistability(**para).wplus_to_wm(wpinf+np.array(backward)*1e6*2*np.pi)
wmu=Bistability(**para).wplus_to_wm(wpinf+np.array(unstable)*1e6*2*np.pi)

# print(wmf/(1e9*2*np.pi))
##计算ms和as
msf,asf=Bistability(**para).cal_ms_as_f(wmf-wminf,forwardf)
msb,asb=Bistability(**para).cal_ms_as_f(wmb-wminf,backwardf)
msu,asu=Bistability(**para).cal_ms_as_f(wmu-wminf,unstablef)

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

#
# # plt.figure(figsize=(7, 6))
# # axes1 = plt.subplot(111)
# # axes1.plot(forwardp, msf.real, 'o', linewidth=5, label=r'forward')
# # axes1.plot(backwardp, msb.real, '^', linewidth=5, label=r'backward')
# # axes1.plot(unstablep,msu.real, '--', linewidth=5, label=r'unstable')
# # axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# # axes1.set_ylabel(r'$m_s$ ', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=4)
# # plt.show()
# #
# # plt.figure(figsize=(7, 6))
# # axes1 = plt.subplot(111)
# # axes1.plot(forwardp, msf.imag, 'o', linewidth=5, label=r'forward')
# # axes1.plot(backwardp, msb.imag, '^', linewidth=5, label=r'backward')
# # axes1.plot(unstablep,msu.imag, '--', linewidth=5, label=r'unstable')
# # axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# # axes1.set_ylabel(r'$m_s$ ', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=4)
# # plt.show()
#
# # plt.figure(figsize=(10, 6))
# #
# # axes1 = plt.subplot(131)
# # axes1.plot(msf.real, msf.imag, 'o', linewidth=5, label=r'forward',markerfacecolor='None')
# # axes1.plot(msf.real[fpindex], msf.imag[fpindex], 's', markersize=10)
# # axes1.set_xlabel(r'Real', fontsize=20)
# # axes1.set_ylabel(r'Imag', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=0)
# #
# # axes2 = plt.subplot(132)
# # axes2.plot(msb.real, msb.imag, 'o', linewidth=5, label=r'backward',markerfacecolor='None')
# # axes2.plot(msb.real[bpindex], msb.imag[bpindex], 's', markersize=10)
# # plt.legend(loc=0)
# #
# # axes3 = plt.subplot(133)
# # axes3.plot(msu.real,msu.imag, 'o', linewidth=5, label=r'unstable',markerfacecolor='None')
# # axes3.plot(msu.real[upindex],msu.imag[upindex], 's', markersize=10)
# # plt.legend(loc=0)
# # plt.show()
#
#
plt.figure(figsize=(10, 6))
axes1 = plt.subplot(111)
axes1.plot(msf.real, msf.imag, '^', linewidth=5, label=r'forward')
axes1.plot(msf.real[fpindex], msf.imag[fpindex], 's', markersize=10)


axes1.plot(msb.real, msb.imag, 'o', linewidth=5, markersize=8, label=r'backward',markerfacecolor='None')
axes1.plot(msb.real[bpindex], msb.imag[bpindex], 's', markersize=10)

axes1.plot(msu.real,msu.imag, 'o', linewidth=5, label=r'unstable',markerfacecolor='None')
axes1.plot(msu.real[upindex],msu.imag[upindex], 's', markersize=10)

axes1.set_xlabel(r'Real', fontsize=20)
axes1.set_ylabel(r'Imag', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()
#
#
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
# # plt.figure(figsize=(7, 6))
# # axes1 = plt.subplot(111)
# # axes1.plot(forwardp, forward, '--', linewidth=5, label=r'forward')
# # axes1.plot(forwardp, deltamsf2, 'o', linewidth=5, label=r'forward1',markerfacecolor='None')
# # axes1.plot(backwardp, backward, '--', linewidth=5, label=r'backward')
# # axes1.plot(backwardp, deltamsb2, 'o', linewidth=5, label=r'backward1',markerfacecolor='None')
# # axes1.plot(unstablep, unstable, '--', linewidth=5, label=r'unstable')
# # axes1.plot(unstablep, deltamsu2, 'o', linewidth=5, label=r'unstable1',markerfacecolor='None')
# #
# # axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# # axes1.set_ylabel(r'$\Delta_m$ ', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=4)
# # plt.show()
