import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

# ##定义计算参数
mpart5=np.linspace(100,1000,10)
mpart4=np.linspace(10,100,10)
mpart3=np.linspace(1,10,10)
mpart2=np.linspace(0.1,1,10)
mpart1=np.linspace(0.01,0.1,10)
fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# fins=[0.5,1]
# fins = np.hstack((mpart3,np.delete(mpart4, 0), np.delete(mpart5, 0)))

init_path=f'F:\\change fre\\bistable date'

pointWf = []
pointXf = []
pointYf = []
pointZf = []
pointWw = []
pointXw = []
pointYw = []
pointZw = []
for i in range(len(fins)):
    fin=fins[i]*1e-6

    # part1 = np.linspace(8.177, 8.178, 1001)
    # part2 = np.linspace(8.178, 8.206, 141)
    # part3 = np.linspace(8.206, 8.207, 1001)

    part1 = np.arange(8.177, 8.178, fin)
    part2 = np.linspace(8.178, 8.206, 141)
    part3 = np.arange(8.206, 8.207, fin)
    f = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))
    # P = np.linspace(0, 0.3, 301)
    P=0.1
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
    # forward, forwardf, backward, backwardf, unstablef, unstable=Bistability(**para).BS_fre_with_unstable()
    forward, forwardf, backward, backwardf, unstable, unstablef=Bistability(**para).BS_fre_inside_BS()
    pointWf.append(forwardf[-2])
    pointXf.append(forwardf[-1])
    pointYf.append(backwardf[1])
    pointZf.append(backwardf[0])
    pointWw.append(forward[-2])
    pointXw.append(forward[-1])
    pointYw.append(backward[1])
    pointZw.append(backward[0])
    ## 双稳态图
    # plt.figure(figsize=(7, 6))
    # axes1 = plt.subplot(111)
    # axes1.plot(forwardf, forward, 'o', color='orange',markersize=10,label=r'forward',markerfacecolor='None')
    # axes1.plot(backwardf, backward, '^',  color='green',markersize=5,label=r'backward',markerfacecolor='None')
    # axes1.plot(unstablef,unstable, '--', linewidth=5, color='purple',label=r'unstable')
    # axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
    # axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.legend(loc=7,fontsize=10)
    # plt.show()


sf().save_txt(init_path, 'W fre', pointWf, fmt="%.12f")
sf().save_txt(init_path, 'W deltaplus', pointWw, fmt="%.12f")
sf().save_txt(init_path, 'X fre', pointXf, fmt="%.12f")
sf().save_txt(init_path, 'X deltaplus', pointXw, fmt="%.12f")
sf().save_txt(init_path, 'Y fre', pointYf, fmt="%.12f")
sf().save_txt(init_path, 'Y deltaplus', pointYw, fmt="%.12f")
sf().save_txt(init_path, 'Z fre', pointZf, fmt="%.12f")
sf().save_txt(init_path, 'Z deltaplus', pointZw, fmt="%.12f")