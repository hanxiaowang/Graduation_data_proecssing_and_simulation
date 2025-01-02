import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D


##定义计算参数

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

# jump_times=np.linspace(0,20,21)
#
jump_time=0.083e5
##总2e5
M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo_and_back_P(msf[-2],asf[-2],1e-11,jump_time,forwardp[-1],4e5-jump_time,forwardp[-2],f)
M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo_and_back_P(msb[1],asb[1],1e-11,jump_time,backwardp[0],4e5-jump_time,backwardp[1],f)

middle_number=20
plt.figure(figsize=(8, 6))
axes1 = plt.subplot(111)
axes1.plot(Timeu[::middle_number], M_srf[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B]$',markerfacecolor='None',color='royalblue')
axes1.plot(Timeu[::middle_number], M_sif[::middle_number], '^',  markersize=4, label=r'$Im[m,A \longrightarrow B]$',markerfacecolor='None',color='deepskyblue')
# plt.xlim(xsmall1,xlarge1)
plt.legend(loc=0,fontsize=10)
#
# axes2 = plt.subplot(111)
# axes2.plot(Timeu[::middle_number], M_srb[::middle_number], 's', markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None',color='fuchsia')
# axes2.plot(Timeu[::middle_number], M_sib[::middle_number], '^', markersize=4, label=r'$Im[m,C \longrightarrow D]$',markerfacecolor='None',color='tomato')
# # plt.xlim(xsmall1,xlarge1)
# plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0,fontsize=10)
# axes2.set_xlabel(r'Time', fontsize=20)
# plt.tick_params(labelsize=20)
#
# axes3 = plt.subplot(111)
# axes3.plot(Timeu[::middle_number], A_srf[::middle_number], 's', markersize=4, label=r'$Re[a,A \longrightarrow B]$',markerfacecolor='None',color='royalblue')
# axes3.plot(Timeu[::middle_number], A_sif[::middle_number], '^', markersize=4, label=r'$Im[a,A \longrightarrow B]$',markerfacecolor='None',color='deepskyblue')
# # plt.xlim(xsmall1,xlarge1)
# plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0,fontsize=10)
#
# axes4 = plt.subplot(111)
# axes4.plot(Timeu[::middle_number], A_srb[::middle_number], 's', markersize=4, label=r'$Re[a,C \longrightarrow D]$',markerfacecolor='None',color='fuchsia')
# axes4.plot(Timeu[::middle_number], A_sib[::middle_number], '^', markersize=4, label=r'$Im[a,C \longrightarrow D]$',markerfacecolor='None',color='tomato')
# # plt.xlim(xsmall1,xlarge1)
# plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0,fontsize=10)

plt.show()


# middle_number=20
# jump_times=np.linspace(0,20,401)
# M_srfs2=[]
# for i in range(len(jump_times)):
#         jump_time=1e4*jump_times[i]
#         ##总2e5
#         M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo_and_back(msf[-2],asf[-2],1e-11,jump_time,forwardp[-1],2e5-jump_time,forwardp[-2],f)
#         M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo_and_back(msb[1],asb[1],1e-11,jump_time,backwardp[0],2e5-jump_time,backwardp[1],f)
#         Excition=M_srf[::middle_number]**2+M_sif[::middle_number]**2
#         M_srfs2.append(Excition)
#
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
