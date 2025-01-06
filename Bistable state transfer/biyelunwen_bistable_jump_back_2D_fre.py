import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

P = 0.1
f=np.linspace(8.14, 8.22, 801)
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

# 双稳态图
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

## 根据Delta_+的双稳态求解m和a
wminf=8.184*1e9*2*np.pi
wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz
##每个w+对应的wm,单位Hz
wmf=Bistability(**para).wplus_to_wm(wpinf+np.array(forward)*1e6*2*np.pi)
wmb=Bistability(**para).wplus_to_wm(wpinf+np.array(backward)*1e6*2*np.pi)
wmu=Bistability(**para).wplus_to_wm(wpinf+np.array(unstable)*1e6*2*np.pi)
##计算ms和as
msf,asf=Bistability(**para).cal_ms_as_f(wmf-wminf,forwardf)
msb,asb=Bistability(**para).cal_ms_as_f(wmb-wminf,backwardf)
msu,asu=Bistability(**para).cal_ms_as_f(wmu-wminf,unstablef)
init_path=f'F:\\change fre\\bistable jump back 100mW and 100kHz'
init_path1=f'F:\\change fre\\bistable jump back 100mW and 100kHz real  and  imag'

#
#
# mpart2=np.linspace(30,60,31)
# mpart1=np.linspace(0,30,101)
# jump_times = np.hstack((mpart1, np.delete(mpart2, 0)))

jump_times = np.linspace(0,600000,60001)

# middle_number=20
M_srfstart=[]
M_srfstop=[]

M_srbstart=[]
M_srbstop=[]
Timeneed=[]
for i in range(len(jump_times)):
    interval=1e-11
    jump_time=jump_times[i]
    # sub_path = sf().creat_sub_file(init_path, f'jump back time={round(interval*jump_time*1e9, 10)}ns')
    # sub_path1 = sf().creat_sub_file(init_path1, f'jump back time={round(interval*jump_time*1e9, 10)}ns')

        ##总2e5
    M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo_and_back_f(msf[-2],asf[-2],interval,jump_time,forwardf[-1],6e5-jump_time,forwardf[-2],P)
    M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo_and_back_f(msb[1],asb[1],interval,jump_time,backwardf[0],6e5-jump_time,backwardf[1],P)
    # Excition=M_srf[::middle_number]**2+M_sif[::middle_number]**2
    # Excitionf = M_srf ** 2 + M_sif ** 2
    # M_srfs2.append(Excitionf)
    M_srfstart.append(M_srf[0] ** 2 + M_sif[0] ** 2)
    M_srfstop.append(M_srf[-1] ** 2 + M_sif[-1] ** 2)

    M_srbstart.append(M_srb[0] ** 2 + M_sib[0] ** 2)
    M_srbstop.append(M_srb[-1] ** 2 + M_sib[-1] ** 2)
    Timeneed.append(interval*jump_times[i])
    # Excitionb = M_srb ** 2 + M_sib ** 2
    # M_srbs2.append(Excitionb)

    # sf().save_txt(sub_path, 'forwards', Excitionf, fmt="%.12f")
    # sf().save_txt(sub_path, 'backwards', Excitionb, fmt="%.12f")

    # sf().save_txt(sub_path1, 'forwards real', M_srf, fmt="%.12f")
    # sf().save_txt(sub_path1, 'forwards imag', M_sif, fmt="%.12f")
    # sf().save_txt(sub_path1, 'backwards real', M_srb, fmt="%.12f")
    # sf().save_txt(sub_path1, 'backwards imag', M_sib, fmt="%.12f")

sf().save_txt(init_path, 'jump back time', jump_times, fmt="%.12f")
sf().save_txt(init_path, 'evo_times', Timeneed, fmt="%.12f")
sf().save_txt(init_path, 'jump start forward', M_srfstart, fmt="%.12f")
sf().save_txt(init_path, 'jump stop forward', M_srfstop, fmt="%.12f")
sf().save_txt(init_path, 'jump start backward', M_srbstart, fmt="%.12f")
sf().save_txt(init_path, 'jump stop backward', M_srbstop, fmt="%.12f")
# sf().save_txt(init_path1, 'jump back time', jump_times, fmt="%.12f")
# sf().save_txt(init_path1, 'evo_times', Timeu, fmt="%.12f")

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
