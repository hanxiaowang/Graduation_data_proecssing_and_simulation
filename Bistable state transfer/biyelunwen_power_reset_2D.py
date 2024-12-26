import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D


##定义计算参数
part1=np.linspace(0.014,0.018,401)
part2=np.linspace(0.018,0.209,192)
part3=np.linspace(0.209,0.213,401)
P = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))
# P = np.linspace(0, 0.3, 301)
f=8.18
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
        'P_d': P,
        }

## Delta_+的双稳态求解
forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
# forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()

# 双稳态图
plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot(forwardp, forward, 'o', color='orange',markersize=10,label=r'forward',markerfacecolor='None')
axes1.plot(backwardp, backward, '^',  color='green',markersize=5,label=r'backward',markerfacecolor='None')
axes1.plot(unstablep,unstable, '--', linewidth=5, color='purple',label=r'unstable')
axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=7,fontsize=10)
plt.show()

## 根据Delta_+的双稳态求解m和a
wminf=8.184*1e9*2*np.pi
wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz
##每个w+对应的wm,单位Hz
wmf=Bistability(**para).wplus_to_wm(wpinf+np.array(forward)*1e6*2*np.pi)
wmb=Bistability(**para).wplus_to_wm(wpinf+np.array(backward)*1e6*2*np.pi)
wmu=Bistability(**para).wplus_to_wm(wpinf+np.array(unstable)*1e6*2*np.pi)
##计算ms和as
msf,asf=Bistability(**para).cal_ms_as_P(wmf-wminf,forwardp)
msb,asb=Bistability(**para).cal_ms_as_P(wmb-wminf,backwardp)
msu,asu=Bistability(**para).cal_ms_as_P(wmu-wminf,unstablep)