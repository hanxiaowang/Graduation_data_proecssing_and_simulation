import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *

## Loop 3(Loop 10不要了)

drive_power_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\drive power.txt'));
delta_m_down3=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\drive fre.txt'));
cpf_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\Delta omega up.txt'));
cfp_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change frequency first 22-1-59\Delta omega up.txt'));
step_down3=np.linspace(1,len(drive_power_down3)+1,len(drive_power_down3))
print(len(step_down3))

#
drive_powers=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at A 14-16-55\drive power.txt'));
delta_ms=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at A 14-16-55\drive fre.txt'));
cpf_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at A 14-16-55\Delta omega up.txt'));
cfp_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change fre first at A 14-17-6\Delta omega up.txt'));
step_downs=np.linspace(1,len(drive_powers)+1,len(drive_powers))


# drive_power_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\drive power.txt'));
# delta_m_up10=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\drive fre.txt'));
# cpf_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\Delta omega up.txt'));
# cfp_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change frequency first 20-32-5\Delta omega up.txt'));
# step_up10=np.linspace(1,len(drive_power_up10)+1,len(drive_power_up10))
# print(len(drive_power_up10))
# print(len(step_up10))

# drive_power_up10=[]
# delta_m_up10=[]
# cpf_up10=[]
# cfp_up10=[]

# for i in range(len(drive_power_up10)):
#     if round(drive_power_up10[i]%2)==1:
#         pass
#
#     else:
#         drive_power_up10.append(drive_power_up10[i])
#         delta_m_up10.append(delta_m_up10[i])
#         cpf_up10.append(cpf_up10[i])
#         cfp_up10.append(cfp_up10[i])
#
# step_up3=np.linspace(1,len(drive_power_up10)+1,len(drive_power_up10))
# print(len(step_up3))
# #
# drive_power_down_roll=new_start_point(150,drive_power_down)
# delta_m_down_roll=new_start_point(150,delta_m_down)
# cpf_down_roll=new_start_point(150,cpf_down)
# cfp_down_roll=new_start_point(150,cfp_down)
#
# drive_power_up_roll=new_start_point(150,drive_power_up[::-1])
# delta_m_up_roll=new_start_point(150,delta_m_up[::-1])
# cpf_up_roll=new_start_point(150,cpf_up[::-1])
# cfp_up_roll=new_start_point(150,cfp_up[::-1])


# plot_p_and_f(step_up10,drive_power_up10,delta_m_up10)
# plot_p_and_f(step_down3,drive_power_down3,delta_m_down3)


# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# # axes.plot(step_in,Deltas,color='lime',label='Sim',linewidth=20,alpha=1)
# # axes.scatter(step_down3,cpf_down3,label='Exp',color='none',edgecolors='green',s=40)
# axes.scatter(step_up10,cpf_up10,label='Exp',color='none',edgecolors='green',s=40)
#
# # axes.plot(step_in,Deltas,color='gray',label='Sim',linewidth=10,alpha=0.3,zorder= 0)
# axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
# axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
# plt.ylim(-1,9)
# plt.tick_params(labelsize=10)
# plt.legend(loc=9,fontsize=15)
# plt.show()

fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
fig.patch.set_alpha(0)
axes.patch.set_alpha(0)
#CW
# axes.scatter(step_down3,cpf_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_down3,cpf_ups,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)

# axes.scatter(step_down3,cpf_down3,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_down3,cpf_down_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)

# axes.plot(step_down3,cpf_down_ins,color='black',linewidth=50,alpha=0.5,zorder= 0)
# axes.plot(step_down3,cpf_down_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)

# #CCW
# axes.scatter(step_down3,cfp_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_down3,cfp_ups,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.scatter(step_down3,cfp_down3,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_down3,cfp_down_ins,'--',color='yellow',label='Sim',linewidth=5,alpha=1,zorder= 2)

axes.plot(step_down3,cfp_down_ins,color='black',linewidth=50,alpha=0.5,zorder= 0)
axes.plot(step_down3,cfp_down_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)

axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
plt.ylim(-1,5)
plt.tick_params(labelsize=10)
plt.legend(loc=9,fontsize=15)
plt.show()







# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# axes.plot(step_down3,drive_power_down3,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes2 = axes.twinx()
# axes2.plot(step_down3,delta_m_down3,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
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



#
# plot_polar(step_down3,cpf_down3)
# plot_polar(step_down3[::-1],cfp_down3)
# plot_polar(step_up10,cpf_up10)
# plot_polar(step_up10[::-1],cfp_up10)