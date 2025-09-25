import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *
from mpl_toolkits.mplot3d import Axes3D

#
drive_power_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change power first 18-34-3\drive power.txt'));
delta_m_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change power first 18-34-3\drive fre.txt'));
cpf_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change power first 18-34-3\Delta omega up.txt'));
cfp_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change frequency first 18-10-47\Delta omega up.txt'));
print(len(cpf_down_in))
step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))



drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross lower side change power first 17-19-29\drive power.txt'));
delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross lower side change power first 17-19-29\drive fre.txt'));
cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross lower side change power first 17-19-29\Delta omega up.txt'));
cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross lower side change frequency first 16-54-39\Delta omega up.txt'));
print(len(cpf_up_in))
print((len(drive_power_up_in)))
#
step_up_in=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))


drive_powers=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-31-2\drive power.txt'));
delta_ms=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-31-2\drive fre.txt'));
cpf_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-31-2\Delta omega up.txt'));
cfp_down_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change fre first at D 16-29-40\Delta omega up.txt'));
step_downs=np.linspace(1,len(drive_powers)+1,len(drive_powers))


drive_power_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-29-53\drive power.txt'));
delta_m_up_ins=(8.184-np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-29-53\drive fre.txt'));
cpf_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change power first at D 16-29-53\Delta omega up.txt'));
cfp_up_ins=(np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability thesis\change fre first at D 16-30-49\Delta omega up.txt'));

# print(len(step_down_out))
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


# step_in_up=np.linspace(1,len(drive_power_up)+1,len(drive_power_up))
#
# #
fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
fig.patch.set_alpha(0)
axes.patch.set_alpha(0)


# CCW
# axes.scatter(step_in,cpf_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_in,cpf_up_ins,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)
# #
axes.scatter(step_in,cpf_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
axes.plot(step_in,cpf_down_ins,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.plot(step_in,cpf_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
axes.plot(step_in,cpf_up_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)


# #CW
# axes.scatter(step_in,cfp_up,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,cfp_up_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.scatter(step_in,cfp_down_in,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,cfp_down_ins,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.plot(step_in,cfp_down_ins,color='blue',linewidth=10,alpha=0.3,zorder= 0)
# axes.plot(step_in,cfp_up_ins,color='red',linewidth=10,alpha=0.3,zorder= 0)

axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
plt.ylim(-1,12)
plt.tick_params(labelsize=10)
plt.legend(loc=9,fontsize=15)
plt.show()





# fig = plt.figure()
# axes = fig.add_subplot(111, projection='3d')
# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# # axes.plot(step_in,drive_power_up_in,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# # axes2 = axes.twinx()
# # axes2.plot(step_in,delta_m_up_in,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.plot(step_in,drive_power_in[::-1],color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes2 = axes.twinx()
# axes2.plot(step_in,delta_m_in[::-1],color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.set_xlabel(r'$Step$',fontsize=10)
# axes.set_ylabel(r'$P_d$ [mW]',fontsize=10)
# axes2.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\p1.txt',drive_power_ups)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\f1.txt',delta_m_ups)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\d1.txt',cpf_down_ins)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\p2.txt',drive_power_ups)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\f2.txt',delta_m_ups)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\d2.txt',cpf_up_ins)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\p3.txt',drive_power_up_ins)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\f3.txt',delta_m_up_ins)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\d3.txt',cfp_down_ins)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\p4.txt',drive_power_up_ins)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\f4.txt',delta_m_up_ins)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\chirality\loop6\d4.txt',cfp_up_ins)