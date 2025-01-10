import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D


##定义计算参数
# part1=np.linspace(8.177,8.178,1001)
# part2=np.linspace(8.178,8.206,141)
# part3=np.linspace(8.206,8.207,1001)
# f = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))

f = np.linspace(8.14, 8.22, 801)
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
print('Here is OK!1')
# print(forwardf)
# 双稳态图
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(forwardf, forward, 'o', color='orange',markersize=10,label=r'forward',markerfacecolor='None')
# axes1.plot(backwardf, backward, '^',  color='green',markersize=5,label=r'backward',markerfacecolor='None')
# axes1.plot(unstablef,unstable, '--', linewidth=5, color='purple',label=r'unstable')
# axes1.set_xlabel(r'$f_d$ [GHz]', fontsize=10)
# axes1.set_ylabel(r'$\Delta_m$ [MHz]', fontsize=10)
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

# plt.figure(figsize=(10, 6))
# axes1 = plt.subplot(111)
# axes1.plot(msf.real, msf.imag, '^', linewidth=5, color='orange',markersize=10,label=r'forward',markerfacecolor='None')
# axes1.plot(msb.real, msb.imag, 'o', linewidth=5,color='green', markersize=8, label=r'backward',markerfacecolor='None')
# axes1.plot(msu.real, msu.imag, '--', linewidth=5, color='purple',label=r'unstable')
# axes1.plot(asf.real, asf.imag, '^', linewidth=5, color='orange',markersize=10,label=r'forward',markerfacecolor='None')
# axes1.plot(asb.real, asb.imag, 'o', linewidth=5,color='green', markersize=8, label=r'backward',markerfacecolor='None')
# axes1.plot(asu.real, asu.imag, '--', linewidth=5, color='purple',label=r'unstable')
# axes1.set_xlabel(r'Real', fontsize=10)
# axes1.set_ylabel(r'Imag', fontsize=10)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0,fontsize=10)
# plt.show()


## 求解跳跃的演化
M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo(msf[-2],asf[-2],1e-11,6e5,P,forwardf[-1])
M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo(msb[1],asb[1],1e-11,6e5,P,backwardf[0])
print('Here is OK!2')

## m和a的跳跃演化图 3D
# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(M_sif,Timeu,M_srf,'^', color='green',markersize=4,markerfacecolor='None',label='$|m|^2$')
# # ax.plot(A_sif,Timeu,A_srf,'o', color='green',markersize=4,markerfacecolor='None',label='$|a|^2$')
# ax.set_xlabel(r'Imag', fontsize=10)
# ax.set_ylabel(r'time', fontsize=10)
# ax.set_zlabel(r'Real', fontsize=10)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=20, azim=-160)
# plt.legend(loc=0)
#
# plt.show()

# aaa=1.2
# xsmall1=2.75e-6
# xlarge1=4.25e-6
# ysmall1=min([min(M_srf),min(M_sif)])*aaa
# ylarge1=max([max(M_srf),max(M_sif)])*aaa
#
# xsmall2=0e-6
# xlarge2=2e-6
# ysmall2=min([min(M_srb),min(M_sib)])*aaa
# ylarge2=max([max(M_srb),max(M_sib)])*aaa
#
#
# ysmall3=min([min(A_srf),min(A_sif)])*aaa
# ylarge3=max([max(A_srf),max(A_sif)])*aaa
#
#
# ysmall4=min([min(A_srb),min(A_sib)])*aaa
# ylarge4=max([max(A_srb),max(A_sib)])*aaa
# # #
middle_number=50
# #
# # ## m和a的跳跃演化图 2D
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(Timeu[::middle_number], M_srf[::middle_number], 's',  markersize=4, label=r'$Re[m,W \longrightarrow X]$',markerfacecolor='None',color='fuchsia')
# axes1.plot(Timeu[::middle_number], M_sif[::middle_number], '^',  markersize=4, label=r'$Im[m,W \longrightarrow X]$',markerfacecolor='None',color='tomato')
# plt.xlim(xsmall1,xlarge1)
# plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0,fontsize=10)
# plt.show()
#
# plt.figure(figsize=(8, 6))
# axes2 = plt.subplot(111)
# axes2.plot(Timeu[::middle_number], M_srb[::middle_number], 's', markersize=4, label=r'$Re[m,Y \longrightarrow Z]$',markerfacecolor='None',color='royalblue')
# axes2.plot(Timeu[::middle_number], M_sib[::middle_number], '^', markersize=4, label=r'$Im[m,Y \longrightarrow Z]$',markerfacecolor='None',color='deepskyblue')
# plt.xlim(xsmall2,xlarge2)
#
# plt.ylim(ysmall2,ylarge2)
# plt.legend(loc=0,fontsize=10)
# axes2.set_xlabel(r'Time', fontsize=10)
# plt.tick_params(labelsize=20)
# plt.show()
#
#
# plt.figure(figsize=(8, 6))
# axes3 = plt.subplot(111)
# axes3.plot(Timeu[::middle_number], A_srf[::middle_number], 's', markersize=4, label=r'$Re[a,W \longrightarrow X]$',markerfacecolor='None',color='fuchsia')
# axes3.plot(Timeu[::middle_number], A_sif[::middle_number], '^', markersize=4, label=r'$Im[a,W \longrightarrow X]$',markerfacecolor='None',color='tomato')
# plt.xlim(xsmall1,xlarge1)
# plt.ylim(ysmall3,ylarge3)
# plt.legend(loc=0,fontsize=10)
# plt.show()
#
#
# plt.figure(figsize=(8, 6))
# axes4 = plt.subplot(111)
# axes4.plot(Timeu[::middle_number], A_srb[::middle_number], 's', markersize=4, label=r'$Re[a,Y \longrightarrow Z]$',markerfacecolor='None',color='royalblue')
# axes4.plot(Timeu[::middle_number], A_sib[::middle_number], '^', markersize=4, label=r'$Im[a,Y \longrightarrow Z]$',markerfacecolor='None',color='deepskyblue')
# plt.xlim(xsmall2,xlarge2)
#
# plt.ylim(ysmall4,ylarge4)
# plt.legend(loc=0,fontsize=10)
# plt.show()



## 计算跳跃演化过程的|m|^2和|a|^2以及Delta_+
msf2=[]
msb2=[]
msfsquare=[]
msbsquare=[]
asfsquare=[]
asbsquare=[]
sumfsquare=[]
sumbsquare=[]
Wdelta=np.zeros(len(Timeu))+forward[-2]
Xdelta=np.zeros(len(Timeu))+forward[-1]
Ydelta=np.zeros(len(Timeu))+backward[1]
Zdelta=np.zeros(len(Timeu))+backward[0]
#
for i in range(len(M_srf)):
    msfm=(M_srf[i]**2+M_sif[i]**2)*2*30*1e-9*2*np.pi
    msf2.append(msfm)
    msfsquare.append(M_srf[i]**2+M_sif[i]**2)
    asfsquare.append(A_srf[i] ** 2 + A_sif[i] ** 2)
    sumfsquare.append(M_srf[i]**2+M_sif[i]**2+A_srf[i] ** 2 + A_sif[i] ** 2)

for i in range(len(M_srb)):
    msbm=(M_srb[i]**2+M_sib[i]**2)*2*30*1e-9*2*np.pi
    msb2.append(msbm)
    msbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2)
    asbsquare.append(A_srb[i] ** 2 + A_sib[i] ** 2)
    sumbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2 + A_srb[i] ** 2 + A_sib[i] ** 2)

deltamsf2=(Bistability(**para).branch_fre(wminf+np.array(msf2))-wpinf)/(1e6*2*np.pi)
deltamsb2=(Bistability(**para).branch_fre(wminf+np.array(msb2))-wpinf)/(1e6*2*np.pi)
# #
#
# ## 激发数|m|^2,|a|^2,两者之和

plt.figure(figsize=(8, 6))
axes1 = plt.subplot(111)
axes1.plot(Timeu[::middle_number], msfsquare[::middle_number], 's', markersize=4, label=r'$W \longrightarrow X,|m|^2$',color='red')

# axes1.plot(Timeu[::middle_number], msfsquare[::middle_number], 's', markersize=4, label=r'$W \longrightarrow X,|m|^2$',color='fuchsia')
# axes1.plot(Timeu[::middle_number], asfsquare[::middle_number], '^', markersize=4, label=r'$W \longrightarrow X,|a|^2$',color='tomato')
# axes1.plot(Timeu[::middle_number], sumfsquare[::middle_number], '--', linewidth=5, label=r'$W \longrightarrow X,|m|^2+|a|^2$',color='green')
# plt.xlim(xsmall1,xlarge1)
plt.legend(loc=0,fontsize=15)
plt.show()


plt.figure(figsize=(8, 6))
axes1 = plt.subplot(111)
axes1.plot(Timeu[::middle_number], msbsquare[::middle_number], 's', markersize=4, label=r'$Y \longrightarrow Z,|m|^2$',color='blue')
# axes1.plot(Timeu[::middle_number], msbsquare[::middle_number], 's', markersize=4, label=r'$Y \longrightarrow Z,|m|^2$',color='royalblue')
# axes1.plot(Timeu[::middle_number], asbsquare[::middle_number], '^', markersize=4, label=r'$Y \longrightarrow Z,|a|^2$',color='deepskyblue')
# axes1.plot(Timeu[::middle_number], sumbsquare[::middle_number], '--', linewidth=5, label=r'$Y \longrightarrow Z,|m|^2+|a|^2$',color='green')
# plt.xlim(xsmall2,xlarge2)

plt.legend(loc=0,fontsize=15)
plt.show()


# print(deltamsf2[0])
# print(deltamsf2[-1])
# print(deltamsb2[0])
# print(deltamsb2[-1])


## m的虚部和实部分布，包含稳态、非稳态和跳跃演化
# plt.figure(figsize=(10, 6))
# axes1 = plt.subplot(111)
# axes1.plot(msf.real, msf.imag, '^', color='orange', markersize=4,label=r'forward',markerfacecolor='None')
# axes1.plot(msb.real, msb.imag, 'o', color='green', markersize=4, label=r'backward',markerfacecolor='None')
# axes1.plot(M_srf[::middle_number],M_sif[::middle_number], 's', color='red', markersize=4, label=r'$W \longrightarrow X$',markerfacecolor='None')
# # axes1.plot(M_srb[::middle_number],M_sib[::middle_number], 's',color='blue',  markersize=4, label=r'$Y \longrightarrow Z$',markerfacecolor='None')
# axes1.plot(msu.real,msu.imag, '--', color='purple', linewidth=4, label=r'unstable',markerfacecolor='None')
# axes1.set_xlabel(r'Real', fontsize=10)
# axes1.set_ylabel(r'Imag', fontsize=10)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0,fontsize=10)
# plt.show()

## Delta_+随时间的变化,在A和B、C和D之间
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(Timeu[::middle_number], Wdelta[::middle_number], '--', color='orange',linewidth=10, label=r'W')
# axes1.plot(Timeu[::middle_number], Xdelta[::middle_number], '--', color='green', linewidth=10, label=r'X')
# axes1.plot(Timeu[::middle_number],deltamsf2[::middle_number], 's', color='red',markersize=4,label=r'$W \longrightarrow X$',markerfacecolor='None')
# plt.xlim(xsmall1,xlarge1)
#
# axes1.set_xlabel(r'time', fontsize=10)
# axes1.set_ylabel(r'$\Delta_+$', fontsize=10)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0,fontsize=10)
# plt.show()
#
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(Timeu[::middle_number], Ydelta[::middle_number], '--', color='green',linewidth=10, label=r'Y')
# axes1.plot(Timeu[::middle_number], Zdelta[::middle_number], '--', color='orange', linewidth=10, label=r'Z')
# axes1.plot(Timeu[::middle_number],deltamsb2[::middle_number], 's', color='blue',markersize=4,label=r'$Y \longrightarrow Z$',markerfacecolor='None')
# plt.xlim(xsmall2,xlarge2)
# axes1.set_xlabel(r'time', fontsize=10)
# axes1.set_ylabel(r'$\Delta_+$', fontsize=10)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0,fontsize=10)
# plt.show()