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
max_position=[]
min_position=[]
max_evo=[]
min_evo=[]


# evo_times=np.loadtxt(r'F:\change power\bistable date\Pd step=1.0mW\evo_times.txt')
# ## 正向演化
# for i in range(len(mWins)):
#     forward = np.loadtxt(f'F:\\change power\\bistable date\\Pd step={round(mWins[i],5)}mW\\forwards.txt')
#     max_evo.append(max(forward))
#     max_index = list(forward).index(max(forward))
#     max_position.append(evo_times[max_index])
#
# slopemax,interceptmax=np.polyfit(np.log10(mWins),np.log10(max_position),1)
# nihe1=slopemax*np.log10(mWins)+interceptmax
# print(f'slope is {slopemax} and offset is {interceptmax}')
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(np.log10(mWins),nihe1,'-',linewidth=5,color='blue')
# axes.plot(np.log10(mWins),np.log10(max_position),'o',markersize=10,color='deepskyblue',markerfacecolor='None')
# axes.set_xlabel(r'$\Delta P_d$ [mW]',fontsize=40)
# axes.set_ylabel(r'$times$ [ns]',fontsize=40)
# # plt.xscale('log')
# # plt.yscale('log')
# # plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.show()
#
#
# ## 反向演化
#
# for i in range(len(mWins)):
#     backward = np.loadtxt(f'F:\\change power\\bistable date\\Pd step={round(mWins[i], 5)}mW\\backwards.txt')
#     min_evo.append(min(backward))
#     min_index = list(backward).index(min(backward))
#     min_position.append(evo_times[min_index])
#
#
#
# slopemin,interceptmin=np.polyfit(np.log10(mWins),np.log10(min_position),1)
# nihe2=slopemin*np.log10(mWins)+interceptmin
# print(f'slope is {slopemin} and offset is {interceptmin}')
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(np.log10(mWins), nihe2, '-', linewidth=5, color='red')
# axes.plot(np.log10(mWins), np.log10(min_position), 'o', markersize=10, color='tomato', markerfacecolor='None')
# axes.set_xlabel(r'$\Delta P_d$ [mW]', fontsize=40)
# axes.set_ylabel(r'$times$ [ns]', fontsize=40)
# # plt.xscale('log')
# # plt.yscale('log')
# # plt.yticks([-10,0,10],['-10','0','10'])
# plt.tick_params(labelsize=35)
# plt.show()
#



# fig=plt.figure(figsize=(12, 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(mWins,max_position,max_evo,'^', color='green',markersize=4,markerfacecolor='None',label='forward $|m|^2$')
# # ax.plot(mWins,min_position,min_evo,'o', color='green',markersize=4,markerfacecolor='None',label='$backward |m|^2$')
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

for_max=np.loadtxt(r'F:\change power\bistable date\for max time.txt')
for_min=np.loadtxt(r'F:\change power\bistable date\for min time.txt')
back_max=np.loadtxt(r'F:\change power\bistable date\back max time.txt')
back_min=np.loadtxt(r'F:\change power\bistable date\back min time.txt')
## A to B
fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(np.log10(mWins), np.log10(for_max), 'o', markersize=10, color='deepskyblue', markerfacecolor='None')
axes.plot(mWins, for_min, 'o', markersize=10, color='deepskyblue', markerfacecolor='None')

axes.set_xlabel(r'$\Delta P_d$ [mW]', fontsize=40)
axes.set_ylabel(r'$times$ [ns]', fontsize=40)
# plt.xscale('log')
# plt.yscale('log')
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.show()