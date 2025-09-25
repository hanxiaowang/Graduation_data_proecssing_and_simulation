import numpy as np
import matplotlib.pyplot as plt
from Prepare import *


pre_Pe=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 23-27-27\drive power.txt'));
pre_deltae=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 23-27-27\drive fre.txt'));
pre_Delta1e=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 23-27-27\Delta omega up.txt'));
pre_Delta2e=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change frequency first 21-43-0\Delta omega up.txt'));

pre_Ps=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 15-59-51\drive power.txt'));
pre_deltas=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 15-59-51\drive fre.txt'));
pre_Delta1s=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 15-59-51\Delta omega up.txt'));
pre_Delta2s=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change fre first at D 15-59-21\Delta omega up.txt'));

# print(len(pre_Pe))
# print(len(pre_Ps))
drive_power_in=np.concatenate((pre_Pe[::-1][90:560],pre_Pe[::-1][0:90]))
delta_m_in=np.concatenate((pre_deltae[::-1][90:560],pre_deltae[::-1][0:90]))
cpf_down_in=np.concatenate((pre_Delta2e[90:560],pre_Delta2e[0:90]))
cfp_down_in=np.concatenate((pre_Delta2e[90:0:-1],pre_Delta1e[0:470]))
print(len(cpf_down_in))
step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))



drive_power_up_in=np.concatenate((pre_Pe[90:560],pre_Pe[0:90]))
delta_m_up_in=np.concatenate((pre_deltae[90:560],pre_deltae[0:90]))
cpf_up_in=np.concatenate((pre_Delta1e[470:380:-1],pre_Delta2e[180:560],pre_Delta2e[0:90]))
cfp_up_in=np.concatenate((pre_Delta1e[470:560],pre_Delta1e[0:470]))
print(len(cpf_up_in))
# print(len(cfp_up_in))
#
step_up_in=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))


drive_powers=np.concatenate((pre_Ps[::-1][90:560],pre_Ps[::-1][0:90]))
delta_ms=np.concatenate((pre_deltas[::-1][90:560],pre_deltas[::-1][0:90]))
cpf_down_ins=np.concatenate((pre_Delta2s[90:560],pre_Delta2s[0:90]))
cfp_down_ins=np.concatenate((pre_Delta2s[90:0:-1],pre_Delta1s[0:470]))
print(len(cpf_down_ins))
step_downs=np.linspace(1,len(drive_powers)+1,len(drive_powers))


drive_power_up_ins=np.concatenate((pre_Ps[90:560],pre_Ps[0:90]))
delta_m_up_ins=np.concatenate((pre_deltas[90:560],pre_deltas[0:90]))
cpf_up_ins=np.concatenate((pre_Delta1s[470:380:-1],pre_Delta2s[180:560],pre_Delta2s[0:90]))
cfp_up_ins=np.concatenate((pre_Delta1s[470:560],pre_Delta1s[0:470]))
print(len(cpf_up_ins))







#
#
fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
fig.patch.set_alpha(0)
axes.patch.set_alpha(0)
# CW
# axes.scatter(step_in,cpf_up_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,cpf_up_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
axes.scatter(step_in,cpf_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
axes.plot(step_in,cpf_down_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.plot(step_in,cpf_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
axes.plot(step_in,cpf_up_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)




# CCW
# axes.scatter(step_in,cfp_up_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_in,cfp_up_ins,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

# axes.scatter(step_in,cfp_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_in,cfp_down_ins,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.plot(step_in,cfp_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
# axes.plot(step_in,cfp_up_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)

axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
plt.ylim(-1,50)
plt.tick_params(labelsize=10)
plt.legend(loc=9,fontsize=15)
plt.show()





# print(len(drive_power_in))
# # print(len(delta_m_in))
# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# # axes.plot(step_in,drive_power_up,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# # axes2 = axes.twinx()
# # axes2.plot(step_in,delta_m_up,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.plot(step_in,drive_power_in,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes2 = axes.twinx()
# axes2.plot(step_in,delta_m_in,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
#
# # axes.plot(pre_Pe,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# # axes2 = axes.twinx()
# # axes2.plot(pre_deltae,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
#
#
# axes.set_xlabel(r'$Step$',fontsize=10)
# axes.set_ylabel(r'$P_d$ [mW]',fontsize=10)
# axes2.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()


np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\p1.txt',drive_powers)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\f1.txt',delta_ms)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\d1.txt',cpf_down_ins)

np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\p2.txt',drive_power_up_ins)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\f2.txt',delta_m_up_ins)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\d2.txt',cpf_up_ins)

np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\p3.txt',drive_powers)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\f3.txt',delta_ms)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\d3.txt',cfp_down_ins)

np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\p4.txt',drive_power_up_ins)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\f4.txt',delta_m_up_ins)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop8\d4.txt',cfp_up_ins)


