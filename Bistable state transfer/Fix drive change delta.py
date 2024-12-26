import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability, Combination
# P = np.linspace(0, 0.25, 5001)
part1=np.linspace(0.014,0.018,401)
part2=np.linspace(0.018,0.209,192)
part3=np.linspace(0.209,0.213,401)
P = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))

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

# forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()
print(forward[-1])
print(forward[-2])
print(backward[0])
print(backward[1])

plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot(forwardp, forward, 'o', linewidth=5,markersize=10, color='orange',label=r'forward',markerfacecolor='None')
axes1.plot(backwardp, backward, '^', linewidth=5, color='blue',label=r'backward')
axes1.plot(unstablep,unstable, '--', linewidth=5,color='purple', label=r'unstable')
axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=4)
plt.show()

for i in range(len(forward)):
    if (forward[i+1]-forward[i])>2:
        jump_startf=forward[i]
        jump_stopf=forward[i+1]
        jump_powerf=forwardp[i+1]
        print(f'jump startf is {forward[i]}')
        print(f'jump stopf is {forward[i+1]}')
        print(f'jump powerf is {forwardp[i + 1]}')
        break

for i in range(len(backward)):
    if (backward[i+1]-backward[i])>1.5:
        jump_startb=backward[i+1]
        jump_stopb=backward[i]
        jump_powerb=backwardp[i]

        print(f'jump startf is {backward[i+1]}')
        print(f'jump stopf is {backward[i]}')
        print(f'jump powerf is {backwardp[i]}')
        break
#
jump_deltaf=np.linspace(jump_startf,jump_stopf,1001)
jump_deltab=np.linspace(jump_startb,jump_stopb,1001)

# #
wminf=8.184*1e9*2*np.pi
wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz

##每个w+对应的wm,单位Hz
wmft=Bistability(**para).wplus_to_wm(wpinf+np.array(jump_deltaf)*1e6*2*np.pi)
wmbt=Bistability(**para).wplus_to_wm(wpinf+np.array(jump_deltab)*1e6*2*np.pi)
# print(wmf/(1e9*2*np.pi))
##计算ms和as
msft,asft=Bistability(**para).cal_ms_as_P(wmft-wminf,jump_powerf)
msbt,asbt=Bistability(**para).cal_ms_as_P(wmbt-wminf,jump_powerb)

##计算\Delta_m,单位Hz
msft2=np.abs(msft)**2*2*30*1e-9*2*np.pi
msbt2=np.abs(msbt)**2*2*30*1e-9*2*np.pi

#
# # plt.figure(figsize=(7, 6))
# # axes1 = plt.subplot(211)
# # axes1.plot(jump_deltaf, msft.real, 'o', linewidth=5, label=r'forward re')
# # axes1.plot(jump_deltaf, msft.imag, '^', linewidth=5, label=r'forward im')
# # axes1.set_xlabel(r'$\Delta_+$ [MHz]', fontsize=20)
# # axes1.set_ylabel(r'$1$ ', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=0)
# #
# # axes2 = plt.subplot(212)
# # axes2.plot(jump_deltab, msbt.real, 'o', linewidth=5, label=r'backward re')
# # axes2.plot(jump_deltab, msbt.imag, '^', linewidth=5, label=r'backward im')
# # axes2.set_xlabel(r'$\Delta_+$ [MHz]', fontsize=20)
# # axes2.set_ylabel(r'$1$ ', fontsize=20)
# # plt.tick_params(labelsize=20)
# # plt.legend(loc=0)
# # plt.show()
#

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

# ##计算\Delta_m,单位Hz
# msf2=np.abs(msf)**2*2*30*1e-9*2*np.pi
# msb2=np.abs(msb)**2*2*30*1e-9*2*np.pi
# msu2=np.abs(msu)**2*2*30*1e-9*2*np.pi
#
## ms Re and Im
plt.figure(figsize=(10, 6))
axes1 = plt.subplot(111)
axes1.plot(msf.real, msf.imag, '^', linewidth=5, label=r'forward')
axes1.plot(msb.real, msb.imag, 'o', linewidth=5, markersize=8, label=r'backward',markerfacecolor='None')
axes1.plot(msft.real, msft.imag, 's', linewidth=3, label=r'forward transfor',markerfacecolor='None')
axes1.plot(msbt.real, msbt.imag, 's', linewidth=3, label=r'backward transfor',markerfacecolor='None')
axes1.plot(msu.real,msu.imag, '--', linewidth=5, label=r'unstable',markerfacecolor='None')

axes1.set_xlabel(r'Real', fontsize=20)
axes1.set_ylabel(r'Imag', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()