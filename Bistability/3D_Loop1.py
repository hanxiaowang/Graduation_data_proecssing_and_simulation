import matplotlib.pyplot as plt

from Prepare import *

j=4
drive_power_in1=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 1\\e\\drive power.txt'));
delta_m_in1=(8.184-np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 1\\e\\drive fre.txt'));
Deltae1=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 1\\e\\Delta omega UP.txt'));
Deltas1=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 1\\s\\Delta omega UP.txt'));

drive_power_in2=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 2\\e\\drive power.txt'));
delta_m_in2=(8.184-np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 2\\e\\drive fre.txt'));
Deltae2=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 2\\e\\Delta omega UP.txt'));
Deltas2=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 2\\s\\Delta omega UP.txt'));

drive_power_in3=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 3\\e\\drive power.txt'));
delta_m_in3=(8.184-np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 3\\e\\drive fre.txt'));
Deltae3=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 3\\e\\Delta omega UP.txt'));
Deltas3=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 3\\s\\Delta omega UP.txt'));

drive_power_in4=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 4\\e\\drive power.txt'));
delta_m_in4=(8.184-np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 4\\e\\drive fre.txt'));
Deltae4=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 4\\e\\Delta omega UP.txt'));
Deltas4=(np.loadtxt(f'C:\\Users\\AORUS\\OneDrive\\桌面\\CP in 20231013\\CP in path 4\\s\\Delta omega UP.txt'));

step_in=np.linspace(1,len(drive_power_in1)+1,len(drive_power_in1))
# # print(len(step_in))
# #
# drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive power.txt'));
# delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive fre.txt'));
# cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\Delta omega up.txt'));
# cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change frequency first 20-25-25\Delta omega up.txt'));
# step_in_up=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))


# plot_p_and_f(step_in,drive_power_in[::-1]*1e3,delta_m_in[::-1])

# print(len(step_in))
# print(len(Deltae))


# colore=['red','blue','red','blue']
fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
fig.patch.set_alpha(0)
axes.patch.set_alpha(0)
#CCW
# axes.scatter(step_in,Deltae1,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
# axes.plot(step_in,Deltas1,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.scatter(step_in,Deltae2,label='Exp',marker='s',color='none',linewidth=2,edgecolors='darkorange',s=80)
axes.plot(step_in,Deltas2,'--',color='yellow',label='Sim',linewidth=3,alpha=1,zorder= 2)

axes.plot(step_in,Deltas2,color='blue',linewidth=10,alpha=0.3,zorder= 0)
axes.plot(step_in,Deltas3,color='red',linewidth=10,alpha=0.3,zorder= 0)

#CW
# axes.scatter(step_in,Deltae3[::-1],label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,Deltas3[::-1],'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)

# axes.scatter(step_in,Deltae4,label='Exp',marker='s',color='none',linewidth=2,edgecolors='green',s=80)
# axes.plot(step_in,Deltas4,'--',color='lime',label='Sim',linewidth=3,alpha=1,zorder= 2)
#
# axes.plot(step_in,Deltas2[::-1],color='blue',linewidth=10,alpha=0.3,zorder= 0)
# axes.plot(step_in,Deltas3[::-1],color='red',linewidth=10,alpha=0.3,zorder= 0)

axes.set_xlabel(r'$f_d$ [GHz]',fontsize=10)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=10)
plt.ylim(-1,9)
plt.tick_params(labelsize=10)
plt.legend(loc=9,fontsize=15)
plt.show()


# fig, axes = plt.subplots(1, 1, figsize=(12  , 6))
# fig.patch.set_alpha(0)
# axes.patch.set_alpha(0)
# axes.plot(step_in,drive_power_in*1e3,color='peru',label=r'$P_d$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes2 = axes.twinx()
# axes2.plot(step_in,delta_m_in*1e3,color='purple',label=r'$\delta_m/2\pi$',linewidth=1,alpha=1,marker='o',markersize=5)
# axes.set_xlabel(r'$Step$',fontsize=10)
# axes.set_ylabel(r'$P_d$ [mW]',fontsize=10)
# axes2.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.show()
