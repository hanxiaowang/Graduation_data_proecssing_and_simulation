import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D


part1=np.linspace(0.014,0.018,4001)
part2=np.linspace(0.018,0.209,192)
part3=np.linspace(0.209,0.213,4001)
P = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))

# P = np.linspace(0, 0.3, 3001)
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

# forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()

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
# wminf=8.184*1e9*2*np.pi
# wpinf=Bistability(**para).branch_fre(wminf)##初始的w+,单位Hz
# # print(wpinf/(1e9*2*np.pi))
#
# ##每个w+对应的wm,单位Hz
# wmf=Bistability(**para).wplus_to_wm(wpinf+np.array(forward)*1e6*2*np.pi)
# wmb=Bistability(**para).wplus_to_wm(wpinf+np.array(backward)*1e6*2*np.pi)
# wmu=Bistability(**para).wplus_to_wm(wpinf+np.array(unstable)*1e6*2*np.pi)
#
# # print(wmf/(1e9*2*np.pi))
# ##计算ms和as
# msf,asf=Bistability(**para).cal_ms_as_P(wmf-wminf,forwardp)
# msb,asb=Bistability(**para).cal_ms_as_P(wmb-wminf,backwardp)
# msu,asu=Bistability(**para).cal_ms_as_P(wmu-wminf,unstablep)

# fpindex = list(forwardp).index(0.1)
# # print(fpindex)
# bpindex = list(backwardp).index(0.1)
# upindex = list(unstablep).index(0.1)
# Ppindex = list(P).index(0.1)
# print(P[Ppindex])
# print(msu[upindex])
# M_sru,M_siu,A_sru,A_siu,Timeu=Bistability(**para).m_a_evo(msu[upindex],asu[upindex],1e-9,1e3,P[Ppindex],f)
# M_srf,M_sif,A_srf,A_sif,Timef=Bistability(**para).m_a_evo(msf[fpindex],asf[fpindex],1e-9,1e3,P[Ppindex],f)
# M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo(msb[bpindex],asb[bpindex],1e-9,1e3,P[Ppindex],f)
# M_sru,M_siu,A_sru,A_siu,Timeu=Bistability(**para).m_a_evo(msu[upindex],asu[upindex],1e-9,1e3,P[Ppindex],f)


# M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo(msf[-2],asf[-2],1e-9,1e3,forwardp[-1],f)
# M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo(msb[1],asb[1],1e-9,1e3,backwardp[0],f)

# M_srf,M_sif,A_srf,A_sif,Timeu=Bistability(**para).m_a_evo(msf[-2],asf[-2],1e-10,2e4,forwardp[-1],f)
# M_srb,M_sib,A_srb,A_sib,Timeb=Bistability(**para).m_a_evo(msb[1],asb[1],1e-10,2e4,backwardp[0],f)

# print(M_srf[0])
# print(M_srf[-1])
# print(M_sif[0])
# print(M_sif[-1])
#
# print(M_srb[0])
# print(M_srb[-1])
# print(M_sib[0])
# print(M_sib[-1])
#
#
# Fstablemr=[]
# Bstablemr=[]
# Fstablear=[]
# Bstablear=[]
# Fstablemi=[]
# Bstablemi=[]
# Fstableai=[]
# Bstableai=[]
# print(len(M_sr))
# print(len(M_si))


# print(M_si[0])
# print(M_si[1])
#
# print(A_sr[0])
# print(A_sr[1])
#
# print(A_si[0])
# print(A_si[1])

#
# print(M_sr[10])
# print(M_si[10])
# print(A_sr[10])
# print(A_si[10])
# print(M_sr[2])
# print(M_sr[3])
# print(M_sr[4])
# print(M_sr[5])
# print(M_sr[6])
# print(M_sr[7])

# print(len(M_si))
# for i in range(len(Timeu)):
#     Fstablemr.append(msf[fpindex].real)
#     Bstablemr.append(msb[fpindex].real)
#     Fstablear.append(asf[bpindex].real)
#     Bstablear.append(asb[bpindex].real)
#     Fstablemi.append(msf[fpindex].imag)
#     Bstablemi.append(msb[fpindex].imag)
#     Fstableai.append(asf[bpindex].imag)
#     Bstableai.append(asb[bpindex].imag)


# xsmall1=0.2e-6
# xlarge1=0.3e-6
# ysmall1=-5e7
# ylarge1=5e7
#
# xsmall2=0.2e-6
# xlarge2=0.3e-6
# ysmall2=-5e7
# ylarge2=5e7
#
# xsmall3=0.2e-6
# xlarge3=0.3e-6
# ysmall3=-5e7
# ylarge3=5e7
#
# xsmall4=0.2e-6
# xlarge4=0.3e-6
# ysmall4=-5e7
# ylarge4=5e7
#
# #
# #
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(221)
# # axes1.plot(Timeu, M_sru, 'o', linewidth=5, label=r'Msru')
# axes1.plot(Timeu, M_srf, 's', linewidth=5, label=r'Msrf')
# axes1.plot(Timeu, M_srb, '^', linewidth=5, label=r'Msrb')
# # axes1.plot(Timeu, Fstablemr, '--', linewidth=5, label=r'fMsr')
# # axes1.plot(Timeu, Bstablemr, '--', linewidth=5, label=r'bMsr')
# # plt.xlim(xsmall1,xlarge1)
# # plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0)
#
# axes2 = plt.subplot(222)
# # axes2.plot(Timeu, M_siu, 'o', linewidth=5, label=r'Msiu')
# axes2.plot(Timeu, M_sif, 's', linewidth=5, label=r'Msif')
# axes2.plot(Timeu, M_sib, '^', linewidth=5, label=r'Msib')
# # axes2.plot(Timeu, Fstablemi, '--', linewidth=5, label=r'fMsi')
# # axes2.plot(Timeu, Bstablemi, '--', linewidth=5, label=r'bMsi')
# # plt.xlim(xsmall2,xlarge2)
# # plt.ylim(ysmall2,ylarge2)
# plt.legend(loc=0)
# # axes2.set_xlabel(r'Time', fontsize=20)
# # plt.tick_params(labelsize=20)
# axes3 = plt.subplot(223)
# # axes3.plot(Timeu, A_sru, 'o', linewidth=5, label=r'Asru')
# axes3.plot(Timeu, A_srf, 's', linewidth=5, label=r'Asrf')
# axes3.plot(Timeu, A_srb, '^', linewidth=5, label=r'Asrb')
# # axes3.plot(Timeu, Fstablear, '--', linewidth=5, label=r'fAsr')
# # axes3.plot(Timeu, Bstablear, '--', linewidth=5, label=r'bAsr')
# # plt.xlim(xsmall3,xlarge3)
# # plt.ylim(ysmall3,ylarge3)
# plt.legend(loc=0)
#
# axes4 = plt.subplot(224)
# # axes4.plot(Timeu, A_siu, 'o', linewidth=5, label=r'Asiu')
# axes4.plot(Timeu, A_sif, 's', linewidth=5, label=r'Asif')
# axes4.plot(Timeu, A_sib, '^', linewidth=5, label=r'Asib')
# # axes4.plot(Timeu, Fstableai, '--', linewidth=5, label=r'fAsi')
# # axes4.plot(Timeu, Bstableai, '--', linewidth=5, label=r'bAsi')
# # plt.xlim(xsmall4,xlarge4)
# # plt.ylim(ysmall4,ylarge4)
# plt.legend(loc=0)
# plt.show()

# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# axes1.plot(Time, A_s, 'o', linewidth=5, label=r'As')
# axes1.set_xlabel(r'Time', fontsize=20)
# axes1.set_ylabel(r'$m_s$ ', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()

# msf2=[]
# msb2=[]
# msfsquare=[]
# msbsquare=[]
# asfsquare=[]
# asbsquare=[]
# sumfsquare=[]
# sumbsquare=[]
# for i in range(len(M_srf)):
#     msfm=(M_srf[i]**2+M_sif[i]**2)*2*30*1e-9*2*np.pi
#     msf2.append(msfm)
#     msfsquare.append(M_srf[i]**2+M_sif[i]**2)
#     asfsquare.append(A_srf[i] ** 2 + A_sif[i] ** 2)
#     sumfsquare.append(M_srf[i]**2+M_sif[i]**2+A_srf[i] ** 2 + A_sif[i] ** 2)
#
# for i in range(len(M_srb)):
#     msbm=(M_srb[i]**2+M_sib[i]**2)*2*30*1e-9*2*np.pi
#     msb2.append(msbm)
#     msbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2)
#     asbsquare.append(A_srb[i] ** 2 + A_sib[i] ** 2)
#     sumbsquare.append(M_srb[i] ** 2 + M_sib[i] ** 2 + A_srb[i] ** 2 + A_sib[i] ** 2)
#
# deltamsf2=(Bistability(**para).branch_fre(wminf+np.array(msf2))-wpinf)/(1e6*2*np.pi)
# deltamsb2=(Bistability(**para).branch_fre(wminf+np.array(msb2))-wpinf)/(1e6*2*np.pi)

# msfsquare=[]
# msbsquare=[]
# asfsquare=[]
# asbsquare=[]
# sumfsquare=[]
# sumbsquare=[]
## m2,a2,m2+a2
# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# # axes1.plot(Timeu, M_sru, 'o', linewidth=5, label=r'Msru')
# # axes1.plot(Timeu, msfsquare, 's', linewidth=5, label=r'forward $|m|^2$')
# # axes1.plot(Timeu, asfsquare, '^', linewidth=5, label=r'forward $|a|^2$')
# # axes1.plot(Timeu, sumfsquare, '--', linewidth=5, label=r'forward $|m|^2+|a|^2$')
#
# axes1.plot(Timeu, msbsquare, 's', linewidth=5, label=r'backward $|m|^2$')
# axes1.plot(Timeu, asbsquare, '^', linewidth=5, label=r'backward $|a|^2$')
# axes1.plot(Timeu, sumbsquare, '--', linewidth=5, label=r'backward $|m|^2+|a|^2$')
# plt.legend(loc=0)
# plt.show()



# plt.figure(figsize=(7, 6))
# axes1 = plt.subplot(111)
# # axes1.plot(Timeu, M_sru, 'o', linewidth=5, label=r'Msru')
# axes1.plot(Timeu, deltamsf2, 's', linewidth=5, label=r'forward')
# axes1.plot(Timeu, deltamsb2, '^', linewidth=5, label=r'backward')
# # axes1.plot(Timeu, Fstablemr, '--', linewidth=5, label=r'fMsr')
# # axes1.plot(Timeu, Bstablemr, '--', linewidth=5, label=r'bMsr')
# # plt.xlim(xsmall1,xlarge1)
# # plt.ylim(ysmall1,ylarge1)
# plt.legend(loc=0)
# plt.show()

# print(deltamsf2[0])
# print(deltamsf2[-1])
# print(deltamsb2[0])
# print(deltamsb2[-1])

# plt.figure(figsize=(10, 6))
# axes1 = plt.subplot(111)
# axes1.plot(msf.real, msf.imag, '^', color='blue',linewidth=5, label=r'forward')
# axes1.plot(msb.real, msb.imag, 'o', color='orange', linewidth=5, markersize=8, label=r'backward',markerfacecolor='None')
# axes1.plot(M_srf,M_sif, 's', color='green', linewidth=3, label=r'forward transfor',markerfacecolor='None')
# axes1.plot(M_srb,M_sib, 's', color='red', linewidth=3, label=r'backward transfor',markerfacecolor='None')
# axes1.plot(msu.real,msu.imag, '--', color='purple', linewidth=5, label=r'unstable',markerfacecolor='None')
# axes1.set_xlabel(r'Real', fontsize=20)
# axes1.set_ylabel(r'Imag', fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
# plt.show()


# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([2,2,1])
# ax.plot(msf.real, msf.imag,forward,'^', color='blue',markersize=4,markerfacecolor='None',label='forward')
# ax.plot(msb.real, msb.imag,backward,'o', color='orange',markersize=4,markerfacecolor='None',label='backward')
# ax.plot(M_srf,M_sif,deltamsf2,'s',color='green',markersize=2,markerfacecolor='None',label='forward transform')
# ax.plot(M_srb,M_sib,deltamsb2,'s',color='red',markersize=2,markerfacecolor='None',label='backward transform')
# ax.plot(msu.real,msu.imag,unstable,'--',color='purple', linewidth=5,label='unstable')
# ax.set_xlabel(r'Real', fontsize=20)
# ax.set_ylabel(r'Imag', fontsize=20)
# ax.set_zlabel(r'$\Delta_+/2\pi$ [MHz]', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# # ax.view_init(elev=15, azim=17)
# ax.view_init(elev=30, azim=-20)
# # ax.view_init(elev=7, azim=18)
# # plt.legend(loc=0)
#
# plt.show()