import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

##定义计算参数
mpart5=np.linspace(1,10,10)
mpart4=np.linspace(0.1,1,10)
mpart3=np.linspace(0.01,0.1,10)
mpart2=np.linspace(0.001,0.01,10)
mpart1=np.linspace(0.0001,0.001,10)
mWins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# mWins=[2,1]
# mWins = np.hstack((mpart3,np.delete(mpart4, 0), np.delete(mpart5, 0)))

init_path=f'F:\\change power\\bistable date'
init_path1=f'F:\\change power\\bistable date real and imag'
A_B=0.21108145
C_D=0.01552785
pointAp=[]
pointBp=[]
pointCp=[]
pointDp=[]
pointAw=[]
pointBw=[]
pointCw=[]
pointDw=[]

min_for=[]
max_for=[]
min_back=[]
max_back=[]

time_min_for=[]
time_max_for=[]
time_min_back=[]
time_max_back=[]
for i in range(len(mWins)):
    mWin=mWins[i]*1e-3
    sub_path=sf().creat_sub_file(init_path, f'Pd step={round(mWins[i],5)}mW')
    sub_path1=sf().creat_sub_file(init_path1, f'Pd step={round(mWins[i],5)}mW')

    # part1=np.arange(0.010,0.020,mWin)
    # part2=np.linspace(0.020,0.205,186)
    # part3=np.arange(0.205,0.215,mWin)

    # part1 = np.linspace(0.014, 0.018, 201)
    # part2 = np.linspace(0.018, 0.209, 192)
    # part3 = np.linspace(0.209, 0.213, 201)
    # P = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))
    part2 = [A_B-mWin/2,A_B+mWin/2]
    part1 = [C_D-mWin/2,C_D+mWin/2]
    P = np.hstack((part1,part2))
    print(P)

    # print(P)
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
    # forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
    forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()
    # pointAp.append(forwardp[-2])
    # pointBp.append(forwardp[-1])
    # pointCp.append(backwardp[1])
    # pointDp.append(backwardp[0])
    # pointAw.append(forward[-2])
    # pointBw.append(forward[-1])
    # pointCw.append(backward[1])
    # pointDw.append(backward[0])
    ## 双稳态图
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

    # plt.figure(figsize=(10, 6))
    # axes1 = plt.subplot(111)
    # # axes1.plot(msf().real, msf().imag, '^', linewidth=5, color='orange',markersize=10,label=r'forward',markerfacecolor='None')
    # # axes1.plot(msb.real, msb.imag, 'o', linewidth=5,color='green', markersize=8, label=r'backward',markerfacecolor='None')
    # # axes1.plot(msu.real, msu.imag, '--', linewidth=5, color='purple',label=r'unstable')
    # axes1.plot(asf().real, asf().imag, '^', linewidth=5, color='orange',markersize=10,label=r'forward',markerfacecolor='None')
    # axes1.plot(asb.real, asb.imag, 'o', linewidth=5,color='green', markersize=8, label=r'backward',markerfacecolor='None')
    # axes1.plot(asu.real, asu.imag, '--', linewidth=5, color='purple',label=r'unstable')
    # axes1.set_xlabel(r'Real', fontsize=20)
    # axes1.set_ylabel(r'Imag', fontsize=20)
    # plt.tick_params(labelsize=20)
    # plt.legend(loc=0,fontsize=10)
    # plt.show()
#
#
#     ## 求解跳跃的演化
    M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo(msf[-2],asf[-2],1e-11,1e7,forwardp[-1],f)
    M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo(msb[1],asb[1],1e-11,1e7,backwardp[0],f)

    msfsquare = []
    msbsquare = []
    asfsquare = []
    asbsquare = []
    sumfsquare = []
    sumbsquare = []
    for i in range(len(M_srf)):
        # msfm = (M_srf[i] ** 2 + M_sif[i] ** 2) * 2 * 30 * 1e-9 * 2 * np.pi
        msfsquare.append(M_srf[i] ** 2 + M_sif[i] ** 2)
        # asfsquare.append(A_srf[i] ** 2 + A_sif[i] ** 2)
        # sumfsquare.append(M_srf[i] ** 2 + M_sif[i] ** 2 + A_srf[i] ** 2 + A_sif[i] ** 2)

    for i in range(len(M_srb)):
        # msbm = (M_srb[i] ** 2 + M_sib[i] ** 2) * 2 * 30 * 1e-9 * 2 * np.pi
        msbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2)
        # asbsquare.append(A_srb[i] ** 2 + A_sib[i] ** 2)
        # sumbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2 + A_srb[i] ** 2 + A_sib[i] ** 2)

    delta_p=np.zeros(len(Timeu))+mWin

    for_max_index=list(msfsquare).index(max(msfsquare))
    for_min_index=list(msfsquare).index(min(msfsquare))
    back_max_index = list(msbsquare).index(max(msbsquare))
    back_min_index = list(msbsquare).index(min(msbsquare))

    min_for.append(msfsquare[for_min_index])
    max_for.append(msfsquare[for_max_index])
    min_back.append(msbsquare[back_min_index])
    max_back.append(msbsquare[back_max_index])

    time_min_for.append(Timeu[for_min_index])
    time_max_for.append(Timeu[for_max_index])
    time_min_back.append(Timeu[back_min_index])
    time_max_back.append(Timeu[back_max_index])


    sf().save_txt(sub_path, 'forwards', msfsquare, fmt = "%.12f")
    sf().save_txt(sub_path, 'backwards', msbsquare, fmt = "%.12f")
    sf().save_txt(sub_path, 'evo_times', Timeu, fmt="%.12f")
    sf().save_txt(sub_path, 'delta_Ps', delta_p, fmt="%.12f")

    # sf().save_txt(sub_path1, 'forwards real', M_srf, fmt="%.12f")
    # sf().save_txt(sub_path1, 'forwards imag', M_sif, fmt="%.12f")
    # sf().save_txt(sub_path1, 'backwards real', M_srb, fmt="%.12f")
    # sf().save_txt(sub_path1, 'backwards imag', M_sib, fmt="%.12f")
    # sf().save_txt(sub_path1, 'evo_times', Timeu, fmt="%.12f")
    # sf().save_txt(sub_path1, 'delta_Ps', delta_p, fmt="%.12f")
#
# sf().save_txt(init_path1, 'A power', pointAp, fmt="%.12f")
# sf().save_txt(init_path1, 'A deltaplus', pointAw, fmt="%.12f")
# sf().save_txt(init_path1, 'B power', pointBp, fmt="%.12f")
# sf().save_txt(init_path1, 'B deltaplus', pointBw, fmt="%.12f")
# sf().save_txt(init_path1, 'C power', pointCp, fmt="%.12f")
# sf().save_txt(init_path1, 'C deltaplus', pointCw, fmt="%.12f")
# sf().save_txt(init_path1, 'D power', pointDp, fmt="%.12f")
# sf().save_txt(init_path1, 'D deltaplus', pointDw, fmt="%.12f")
#
# sf().save_txt(init_path, 'A power', pointAp, fmt="%.12f")
# sf().save_txt(init_path, 'A deltaplus', pointAw, fmt="%.12f")
# sf().save_txt(init_path, 'B power', pointBp, fmt="%.12f")
# sf().save_txt(init_path, 'B deltaplus', pointBw, fmt="%.12f")
# sf().save_txt(init_path, 'C power', pointCp, fmt="%.12f")
# sf().save_txt(init_path, 'C deltaplus', pointCw, fmt="%.12f")
# sf().save_txt(init_path, 'D power', pointDp, fmt="%.12f")
# sf().save_txt(init_path, 'D deltaplus', pointDw, fmt="%.12f")


sf().save_txt(init_path, 'for min', min_for, fmt="%.12f")
sf().save_txt(init_path, 'for max', max_for, fmt="%.12f")
sf().save_txt(init_path, 'back min', min_back, fmt="%.12f")
sf().save_txt(init_path, 'back max', max_back, fmt="%.12f")
sf().save_txt(init_path, 'for min time', time_min_for, fmt="%.12f")
sf().save_txt(init_path, 'for max time', time_max_for, fmt="%.12f")
sf().save_txt(init_path, 'back min time', time_min_back, fmt="%.12f")
sf().save_txt(init_path, 'back max time', time_max_back, fmt="%.12f")
# # # xsmall1=0.2e-6
# # # xlarge1=0.3e-6
# # # ysmall1=min([-np.abs(M_srf[0]*3),-np.abs(M_sif[0]*3)])
# # # ylarge1=max([np.abs(M_srf[0]*3),np.abs(M_sif[0]*3)])
# # #
# # # xsmall2=0.2e-6
# # # xlarge2=0.3e-6
# # # ysmall2=min([-np.abs(M_srb[0]*2),-np.abs(M_sib[0]*2)])
# # # ylarge2=max([np.abs(M_srb[0]*2),np.abs(M_sib[0]*2)])
# # #
# # # xsmall3=0.2e-6
# # # xlarge3=0.3e-6
# # # ysmall3=min([-np.abs(A_srf[0]*2),-np.abs(A_sif[0]*2)])
# # # ylarge3=max([np.abs(A_srf[0]*2),np.abs(A_sif[0]*2)])
# # #
# # # xsmall4=0.2e-6
# # # xlarge4=0.3e-6
# # # ysmall4=min([-np.abs(A_srb[0]*2),-np.abs(A_sib[0]*2)])
# # # ylarge4=max([np.abs(A_srb[0]*2),np.abs(A_sib[0]*2)])
# # #
# # # middle_number=5
# # #
# # # ## m和a的跳跃演化图 2D
# # # plt.figure(figsize=(8, 6))
# # # axes1 = plt.subplot(111)
# # # axes1.plot(Timeu[::middle_number], M_srf[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B]$',markerfacecolor='None',color='royalblue')
# # # axes1.plot(Timeu[::middle_number], M_sif[::middle_number], '^',  markersize=4, label=r'$Im[m,A \longrightarrow B]$',markerfacecolor='None',color='deepskyblue')
# # # # plt.xlim(xsmall1,xlarge1)
# # # plt.ylim(ysmall1,ylarge1)
# # # plt.legend(loc=0,fontsize=10)
# # #
# # # # axes2 = plt.subplot(111)
# # # # axes2.plot(Timeu[::middle_number], M_srb[::middle_number], 's', markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None',color='fuchsia')
# # # # axes2.plot(Timeu[::middle_number], M_sib[::middle_number], '^', markersize=4, label=r'$Im[m,C \longrightarrow D]$',markerfacecolor='None',color='tomato')
# # # # # plt.xlim(xsmall1,xlarge1)
# # # # plt.ylim(ysmall1,ylarge1)
# # # # plt.legend(loc=0,fontsize=10)
# # # # axes2.set_xlabel(r'Time', fontsize=20)
# # # # plt.tick_params(labelsize=20)
# # #
# # # # axes3 = plt.subplot(111)
# # # # axes3.plot(Timeu[::middle_number], A_srf[::middle_number], 's', markersize=4, label=r'$Re[a,A \longrightarrow B]$',markerfacecolor='None',color='royalblue')
# # # # axes3.plot(Timeu[::middle_number], A_sif[::middle_number], '^', markersize=4, label=r'$Im[a,A \longrightarrow B]$',markerfacecolor='None',color='deepskyblue')
# # # # # plt.xlim(xsmall1,xlarge1)
# # # # plt.ylim(ysmall1,ylarge1)
# # # # plt.legend(loc=0,fontsize=10)
# # #
# # # # axes4 = plt.subplot(111)
# # # # axes4.plot(Timeu[::middle_number], A_srb[::middle_number], 's', markersize=4, label=r'$Re[a,C \longrightarrow D]$',markerfacecolor='None',color='fuchsia')
# # # # axes4.plot(Timeu[::middle_number], A_sib[::middle_number], '^', markersize=4, label=r'$Im[a,C \longrightarrow D]$',markerfacecolor='None',color='tomato')
# # # # # plt.xlim(xsmall1,xlarge1)
# # # # plt.ylim(ysmall1,ylarge1)
# # # # plt.legend(loc=0,fontsize=10)
# # #
# # # plt.show()

