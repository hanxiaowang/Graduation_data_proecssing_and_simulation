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
forward_m, forwardp_m, backward_m, backwardp_m, unstable_m,unstablep_m=Bistability(**para).BS_power_inside_BS()
# up_min=round(unstablep[0],3)
# up_max=round(unstablep[-1],3)
up_min=unstablep_m[0]
up_max=unstablep_m[-1]
# print(up_min)
# print(up_max)
power_more=1e-3
floquet_start=up_min-power_more
floquet_stop=up_max+power_more
step=round((floquet_stop-floquet_start)*1e3)+1
P_floquet=np.linspace(floquet_start,floquet_stop,step)
para_after = {'omega_a': 8.246,
        'omega_m': 8.184,
        'kaint': 3.39,
        'kaed': 2.974,
        'kmint': 1.011,
        'kmext': 0,
        'g_ma': 32.649,
        'K': 30,
        'branch': 'upper',
        'omega_d': f,
        'P_d': P_floquet,
        }
forward, forwardp, backward, backwardp, unstable,unstablep=Bistability(**para_after).BS_power_inside_BS()

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

M_sr,M_si,A_sr,A_si,Time,P_ds=Bistability(**para).m_a_evo_Periodic_P(msf[0],asf[0],1e-11,1e6,floquet_stop,floquet_start,f,5e6)
mssquare = []
m_start=[]
m_stop=[]
for i in range(len(M_sr)):
        mssquare.append(M_sr[i] ** 2 + M_si[i] ** 2)
        m_start.append(np.abs(msf[0])**2)
        m_stop.append(np.abs(msf[-1])**2)
middle_number=20

axes4 = plt.subplot(111)
axes4.plot(Time[::middle_number], m_start[::middle_number], '--',color='orange', markersize=4,markerfacecolor='None')
axes4.plot(Time[::middle_number], m_stop[::middle_number], '--', color='green',markersize=4,markerfacecolor='None')
axes4.plot(Time[::middle_number], mssquare[::middle_number], 's', markersize=4,markerfacecolor='None')
# plt.legend(loc=0,fontsize=10)
plt.show()


axes4 = plt.subplot(111)
axes4.plot(msf.real, msf.imag, 'o',color='orange', markersize=4,markerfacecolor='None')
axes4.plot(msb.real, msb.imag, 'o', color='green',markersize=4,markerfacecolor='None')
axes4.plot(M_sr[::middle_number], M_si[::middle_number], 's', markersize=5,markerfacecolor='None')
axes4.plot(M_sr[0], M_si[0], 's', markersize=10,label='start point')
axes4.plot(M_sr[-1], M_si[-1], 's', markersize=10,label='stop point')

# axes4.plot(M_sr[-200], M_si[-200], 's', markersize=10,markerfacecolor='None')
plt.legend(loc=0,fontsize=10)
plt.show()

# axes4 = plt.subplot(111)
# axes4.plot(Time[::middle_number],P_ds[::middle_number], '-', markersize=4,markerfacecolor='None')
# # plt.legend(loc=0,fontsize=10)
# plt.show()
