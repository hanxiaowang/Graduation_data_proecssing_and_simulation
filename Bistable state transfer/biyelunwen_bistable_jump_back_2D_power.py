import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

P = np.linspace(0, 0.3, 301)
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
# forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()

# 双稳态图
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(forwardp, forward, 'o', color='orange',markersize=10,label=r'forward',markerfacecolor='None')
# axes1.plot(backwardp, backward, '^',  color='green',markersize=5,label=r'backward',markerfacecolor='None')
# axes1.plot(unstablep,unstable, '--', linewidth=5, color='purple',label=r'unstable')
# axes1.set_xlabel(r'$P_d$ [mW]', fontsize=20)
# axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=7,fontsize=10)
# plt.show()

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
init_path=f'F:\\change power\\bistable jump back 8.18 and 1mW'
#

mpart2=np.linspace(1,20,39)
mpart1=np.linspace(0,1,101)
jump_times = np.hstack((mpart1, np.delete(mpart2, 0)))

# jump_times = np.linspace(0,20,11)

# middle_number=20
M_srfs2=[]
M_srbs2=[]
for i in range(len(jump_times)):
    interval=1e-11
    jump_time=1e4*jump_times[i]
    sub_path = sf().creat_sub_file(init_path, f'jump back time={round(interval*jump_time*1e9, 10)}ns')

        ##总2e5
    M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo_and_back_P(msf[-2],asf[-2],interval,jump_time,forwardp[-1],2e5-jump_time,forwardp[-2],f)
    M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo_and_back_P(msb[1],asb[1],interval,jump_time,backwardp[0],2e5-jump_time,backwardp[1],f)
    # Excition=M_srf[::middle_number]**2+M_sif[::middle_number]**2
    Excitionf = M_srf ** 2 + M_sif ** 2
    # M_srfs2.append(Excitionf)

    Excitionb = M_srb ** 2 + M_sib ** 2
    # M_srbs2.append(Excitionb)

    sf().save_txt(sub_path, 'forwards', Excitionf, fmt="%.12f")
    sf().save_txt(sub_path, 'backwards', Excitionb, fmt="%.12f")

sf().save_txt(init_path, 'jump back time', jump_times, fmt="%.12f")
sf().save_txt(init_path, 'evo_times', Timeu, fmt="%.12f")

#
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# gci1 = ax1.pcolor(Timeu[::middle_number],jump_times,M_srfs2,cmap='bwr')
# # ax1.set_xlabel(r'$\varphi$[$\pi$]',fontsize=20)
# ax1.set_ylabel(r'$\omega_p/2\pi$ [GHz]',fontsize=20)
# plt.tick_params(labelsize=20)
# cbar = plt.colorbar(gci1)
#
# plt.show()
