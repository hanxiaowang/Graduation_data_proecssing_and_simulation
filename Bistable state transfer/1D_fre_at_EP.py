import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D


##定义计算参数
# part1=np.linspace(8.177,8.178,1001)
# part2=np.linspace(8.178,8.206,141)
# part3=np.linspace(8.206,8.207,1001)
# f = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))

f = np.linspace(8.2, 8.8, 1001)
P=0.2
para = {'omega_a': 8.25,
        'omega_m': 8.25,
        'kaint': 26,
        'kaed': 0,
        'kmint': 1,
        'kmext': 1,
        'g_ma': 5,
        'K': 38,
        'omega_d': f,
        'P_d': P,
        }

## Delta_+的双稳态求解
forward, forwardf, backward, backwardf, unstable, unstablef=Bistability(**para).BS_fre_with_unstable()
print(len(unstable))
# forward, forwardf, backward, backwardf, unstable, unstablef=Bistability(**para).BS_fre_inside_BS()
print('Here is OK!1')
# print(forwardf)
# 双稳态图
plt.figure(figsize=(7, 6))
axes1 = plt.subplot(111)
axes1.plot(forwardf, forward, 'o', color='orange',markersize=10,label=r'forward',markerfacecolor='None')
axes1.plot(backwardf, backward, '^',  color='green',markersize=5,label=r'backward',markerfacecolor='None')
axes1.plot(unstablef,unstable, '--', linewidth=5, color='purple',label=r'unstable')
axes1.set_xlabel(r'$f_d$ [GHz]', fontsize=10)
axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=10)
plt.tick_params(labelsize=20)
plt.legend(loc=7,fontsize=10)
plt.show()
