import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *

drive_power_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 13-54-42\drive power.txt'));
delta_m_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 13-54-42\drive fre.txt'));
cpf_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 13-54-42\Delta omega up.txt'));
cfp_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change frequency first 14-17-43\Delta omega up.txt'));


#
drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 22-19-11\drive power.txt'));
delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 22-19-11\drive fre.txt'));
cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 22-19-11\Delta omega up.txt'));
cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change frequency first 22-54-2\Delta omega up.txt'));




drive_power_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-36-49\drive power.txt'));
delta_m_down_ins=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-36-49\drive fre.txt'));
cpf_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-36-49\Delta omega up.txt'));
cfp_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change fre first at C 13-36-59\Delta omega up.txt'));



drive_power_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-23-37\drive power.txt'));
delta_m_up_ins=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-23-37\drive fre.txt'));
cpf_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change power first at C 13-23-37\Delta omega up.txt'));
cfp_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\change fre first at C 13-23-53\Delta omega up.txt'));


# pdele=np.linspace(9,199,100)
# for i in range(len(pdele)):
#     index=np.where()
#
step_in = np.linspace(1, len(drive_power_in) + 1, len(drive_power_in))
step_in_up = np.linspace(1, len(drive_power_up_in) + 1, len(drive_power_up_in))
step_in_downs=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))
step_in_ups=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))
# print(len(step_in))
# print(len(step_in_up))
# print(len(step_in_downs))
# print(len(step_in_ups))
# print(len(cpf_up_in))
# print(delta_m_in)
# print(delta_m_up_in)
# print(drive_power_in)
# print(drive_power_up_in)
# print(len(step_in))
drive_power_up=[]
delta_m_up=[]
cpf_up=[]
cfp_up=[]
drive_power_ups=[]
delta_m_ups=[]
cpf_ups=[]
cfp_ups=[]
for i in range(len(drive_power_up_in)):
    if round(drive_power_up_in[i]%2)==1:
        pass

    else:
        drive_power_up.append(drive_power_up_in[i])
        delta_m_up.append(delta_m_up_in[i]*1e3)
        cpf_up.append(cpf_up_in[i])
        cfp_up.append(cfp_up_in[i])

        drive_power_ups.append(drive_power_up_ins[i])
        delta_m_ups.append(delta_m_up_ins[i]*1e3)
        cpf_ups.append(cpf_up_ins[i])
        cfp_ups.append(cfp_up_ins[i])


step_up=np.linspace(0,len(drive_power_up)-1,len(drive_power_up))
# print(len(step_in_up))
# print((step_in_up))

# print(len(cfp_up))
# print(len(step_in_up))
#
# plot_p_and_f(step_in,drive_power_in,delta_m_in)
# plot_polar(step_in,cpf_down_in)
# plot_polar(step_in[::-1],cfp_down_in)

# plot_polar(step_up,cpf_up)
# plot_polar(step_up[::-1],cfp_up[::-1])

# print(drive_power_up-drive_power_in)
# print(drive_power_up[::-1])
# print(len(drive_power_up))
# print(step_in_up[::-1])

fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
fig.patch.set_alpha(0)
axes.patch.set_alpha(0)
#CW
# axes.scatter(step_in,cpf_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,cpf_ups,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)

# axes.scatter(step_in,cpf_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,cpf_down_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.plot(step_in,cpf_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
# axes.plot(step_in,cpf_ups,color='red',linewidth=10,alpha=0.3,zorder= 0)

#CCW
# axes.scatter(step_in,cfp_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_in,cfp_ups,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.scatter(step_in,cfp_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
axes.plot(step_in,cfp_down_ins,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.plot(step_in,cfp_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
axes.plot(step_in,cfp_ups,color='red',linewidth=10,alpha=0.3,zorder= 0)

axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
plt.ylim(-1,20)
plt.tick_params(labelsize=10)
plt.legend(loc=9,fontsize=15)
plt.show()






# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# # axes.plot(step_in,drive_power_in,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# # axes2 = axes.twinx()
# # axes2.plot(step_in,delta_m_in*1e3,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.plot(step_in,drive_power_up,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes2 = axes.twinx()
# axes2.plot(step_in,delta_m_up,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.set_xlabel(r'$Step$',fontsize=10)
# axes.set_ylabel(r'$P_d$ [mW]',fontsize=10)
# axes2.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()
# drive_power_up.append(drive_power_up_in[i])
# delta_m_up.append(delta_m_up_in[i])
# cpf_up.append(cpf_up_in[i])
# cfp_up.append(cfp_up_in[i])
#
# drive_power_ups.append(drive_power_up_ins[i])
# delta_m_ups.append(delta_m_up_ins[i])
# cpf_ups.append(cpf_up_ins[i])
# cfp_ups.append(cfp_up_ins[i])