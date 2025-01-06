import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

##定义计算参数
mpart5=np.linspace(100,1000,10)
mpart4=np.linspace(10,100,10)
mpart3=np.linspace(1,10,10)
mpart2=np.linspace(0.1,1,10)
mpart1=np.linspace(0.01,0.1,10)
fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# fins=[0.02,0.01]
max_position=[]
min_position=[]
max_evo=[]
min_evo=[]


# evo_times=np.loadtxt(r'F:\change fre\bistable date\fd step=1.0kHz\evo_times.txt')
# ## 正向演化
# for i in range(len(fins)):
#     forward = np.loadtxt(f'F:\\change fre\\bistable date\\fd step={round(fins[i],5)}kHz\\forwards.txt')
#     min_evo.append(min(forward))
#     min_index = list(forward).index(min(forward))
#     min_position.append(evo_times[min_index])
#
# slopemin,interceptmin=np.polyfit(np.log10(fins),np.log10(min_position),1)
# nihe1=slopemin*np.log10(fins)+interceptmin
# print(f'slope is {slopemin} and offset is {interceptmin}')
# np.savetxt(f'F:\\change fre\\bistable date\\min.txt',min_position)
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(np.log10(fins),nihe1,'-',linewidth=5,color='blue')
# axes.plot(np.log10(fins),np.log10(min_position),'o',markersize=10,color='tomato',markerfacecolor='None')
# axes.set_xlabel(r'$\Delta f_d$ [kHz]',fontsize=40)
# axes.set_ylabel(r'$times$ [ns]',fontsize=40)
# # plt.xscale('log')
# # plt.yscale('log')
# # plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.show()

## 反向演化
# for i in range(len(fins)):
#     backward = np.loadtxt(f'F:\\change fre\\bistable date\\fd step={round(fins[i],5)}kHz\\backwards.txt')
#     max_evo.append(max(backward))
#     max_index = list(backward).index(max(backward))
#     max_position.append(evo_times[max_index])
#
# slopemax,interceptmax=np.polyfit(np.log10(fins),np.log10(max_position),1)
# nihe2=slopemax*np.log10(fins)+interceptmax
# print(f'slope is {slopemax} and offset is {interceptmax}')
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(np.log10(fins), nihe2, '-', linewidth=5, color='blue')
# axes.plot(np.log10(fins), np.log10(max_position), 'o', markersize=10, color='deepskyblue', markerfacecolor='None')
# axes.set_xlabel(r'$\Delta f_d$ [kHz]', fontsize=40)
# axes.set_ylabel(r'$times$ [ns]', fontsize=40)
# # plt.xscale('log')
# # plt.yscale('log')
# # plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.show()



# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(fins,max_position,max_evo,'^', color='green',markersize=4,markerfacecolor='None',label='forward $|m|^2$')
# # ax.plot(fins,min_position,min_evo,'o', color='green',markersize=4,markerfacecolor='None',label='$backward |m|^2$')
# ax.set_xlabel(r'$\Delta P$ [mW]', fontsize=20)
# ax.set_ylabel(r'$times$ [ns]', fontsize=20)
# ax.set_zlabel(r'|m|^2', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=20, azim=-160)
# plt.legend(loc=0)
#
# plt.show()

for_max=np.loadtxt(r'F:\change fre\bistable date\for max time.txt')
for_min=np.loadtxt(r'F:\change fre\bistable date\for min time.txt')
back_max=np.loadtxt(r'F:\change fre\bistable date\back max time.txt')
back_min=np.loadtxt(r'F:\change fre\bistable date\back min time.txt')
## A to B
fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(np.log10(fins), np.log10(for_min), 'o', markersize=10, color='deepskyblue', markerfacecolor='None')
# axes.plot(fins, for_max, 'o', markersize=10, color='deepskyblue', markerfacecolor='None')

axes.set_xlabel(r'$\Delta P_d$ [mW]', fontsize=40)
axes.set_ylabel(r'$times$ [ns]', fontsize=40)
# plt.xscale('log')
# plt.yscale('log')
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.show()