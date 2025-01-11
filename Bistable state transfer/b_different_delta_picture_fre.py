import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf
# mpart5=np.linspace(100,1000,10)
# mpart4=np.linspace(10,100,10)
# mpart3=np.linspace(1,10,10)
# mpart2=np.linspace(0.1,1,10)
# mpart1=np.linspace(0.01,0.1,10)
# fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
## 2D演化图
# forwardsin1=np.loadtxt(r'f:\change fre\bistable date\fd step=0.01kHz\forwards.txt')
# backwardsin1=np.loadtxt(r'f:\change fre\bistable date\fd step=0.01kHz\backwards.txt')
# evo_timesin1=np.loadtxt(r'f:\change fre\bistable date\fd step=0.01kHz\evo_times.txt')
# delta_Psin1=np.loadtxt(r'f:\change fre\bistable date\fd step=0.01kHz\delta_fs.txt')
#
# forwardsin2=np.loadtxt(r'f:\change fre\bistable date\fd step=1.0kHz\forwards.txt')
# backwardsin2=np.loadtxt(r'f:\change fre\bistable date\fd step=1.0kHz\backwards.txt')
# evo_timesin2=np.loadtxt(r'f:\change fre\bistable date\fd step=1.0kHz\evo_times.txt')
# delta_Psin2=np.loadtxt(r'f:\change fre\bistable date\fd step=1.0kHz\delta_fs.txt')
#
# forwardsin3=np.loadtxt(r'f:\change fre\bistable date\fd step=100.0kHz\forwards.txt')
# backwardsin3=np.loadtxt(r'f:\change fre\bistable date\fd step=100.0kHz\backwards.txt')
# evo_timesin3=np.loadtxt(r'f:\change fre\bistable date\fd step=100.0kHz\evo_times.txt')
# delta_Psin3=np.loadtxt(r'f:\change fre\bistable date\fd step=100.0kHz\delta_fs.txt')
# #
forwardsin4=np.loadtxt(r'f:\change fre\bistable date\fd step=1000.0kHz\forwards.txt')
backwardsin4=np.loadtxt(r'f:\change fre\bistable date\fd step=1000.0kHz\backwards.txt')
evo_timesin4=np.loadtxt(r'f:\change fre\bistable date\fd step=1000.0kHz\evo_times.txt')
delta_Psin4=np.loadtxt(r'f:\change fre\bistable date\fd step=1000.0kHz\delta_fs.txt')




end_point=1e7
middle_number=400
# # print(np.shape(forwardsin1))
plt.figure(figsize=(8,6))
ax1 = plt.subplot(111)
# ax1.plot(evo_timesin1[0:int(end_point):middle_number], forwardsin1[0:int(end_point):middle_number], 's',  markersize=4, color='red',label=r'$\Delta f_d=0.01$ kHz',markerfacecolor='None')
# ax1.plot(evo_timesin2[0:int(end_point):middle_number], forwardsin2[0:int(end_point):middle_number], 's',  markersize=4, color='red',label=r'$\Delta f_d=1$ kHz',markerfacecolor='None')
# ax1.plot(evo_timesin3[0:int(end_point):middle_number], forwardsin3[0:int(end_point):middle_number], 's',  markersize=4, color='red',label=r'$\Delta f_d=100$ kHz',markerfacecolor='None')
ax1.plot(evo_timesin4[0:int(end_point):middle_number], forwardsin4[0:int(end_point):middle_number], 's',  markersize=4, color='red',label=r'$\Delta f_d=1000$ kHz',markerfacecolor='None')

ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$|m|^2$',fontsize=20)
plt.tick_params(labelsize=20)
plt.xscale('log')
plt.legend(loc=6,fontsize=15)
plt.show()
# #
plt.figure(figsize=(8,6))
ax1 = plt.subplot(111)
# ax1.plot(evo_timesin1[0:int(end_point):middle_number], backwardsin1[0:int(end_point):middle_number], 's',  markersize=4, color='blue',label=r'$\Delta f_d=0.01$ kHz',markerfacecolor='None')
# ax1.plot(evo_timesin2[0:int(end_point):middle_number], backwardsin2[0:int(end_point):middle_number], 's',  markersize=4, color='blue',label=r'$\Delta f_d=1$ kHz',markerfacecolor='None')
# ax1.plot(evo_timesin3[0:int(end_point):middle_number], backwardsin3[0:int(end_point):middle_number], 's',  markersize=4, color='blue',label=r'$\Delta f_d=100$ kHz',markerfacecolor='None')
ax1.plot(evo_timesin4[0:int(end_point):middle_number], backwardsin4[0:int(end_point):middle_number], 's',  markersize=4, color='blue',label=r'$\Delta f_d=1000$ kHz',markerfacecolor='None')
ax1.set_xlabel(r'$times$ [s]',fontsize=20)
ax1.set_ylabel(r'$|m|^2$',fontsize=20)
plt.tick_params(labelsize=20)
plt.xscale('log')
plt.legend(loc=6,fontsize=15)
plt.show()

# #  3D演化图
# fins=[0.01,0.1,1.0,10.0,100.0,1000.0]
# fins=[100.0]
#
# for i in range(len(fins)):
#     fd=fins[i]
#     print(fd)
#
#     middle_number=200
#     if fd==0.01:
#         length_W_to_X=8e6
#         length_Y_to_Z=8e6
#     elif fd==0.1:
#         length_W_to_X = 4e6
#         length_Y_to_Z = 4e6
#     elif fd == 1.0:
#         length_W_to_X = 2e6
#         length_Y_to_Z = 2e6
#     elif fd == 10.0:
#         length_W_to_X = 5e5
#         length_Y_to_Z = 5e5
#     elif fd == 100.0:
#         length_W_to_X = 3e5
#         length_Y_to_Z = 3e5
#     elif fd == 1000.0:
#         length_W_to_X = 2e5
#         length_Y_to_Z = 2e5
#     forwardsin1r=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step={fd}kHz\\forwards real.txt')
#     forwardsin1i=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step={fd}kHz\\forwards imag.txt')
#     backwardsin1r=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step={fd}kHz\\backwards real.txt')
#     backwardsin1i=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step={fd}kHz\\backwards imag.txt')
#     evo_timesin1=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step=0.01kHz\evo_times.txt')
#     delta_Psin1=np.loadtxt(f'F:\\change fre\\bistable date real and imag\\fd step=0.01kHz\delta_fs.txt')
#
#     # forwardsin2r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1.0kHz\forwards.txt')
#     # forwardsin2i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1.0kHz\forwards.txt')
#     # backwardsin2r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1.0kHz\backwards.txt')
#     # backwardsin2i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1.0kHz\backwards.txt')
#     #
#     # forwardsin3r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=10.0kHz\forwards.txt')
#     # forwardsin3i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=10.0kHz\forwards.txt')
#     # backwardsin3r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=10.0kHz\backwards.txt')
#     # backwardsin3i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=10.0kHz\backwards.txt')
#     # #
#     # forwardsin4r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1000.0kHz\forwards.txt')
#     # forwardsin4i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1000.0kHz\forwards.txt')
#     # backwardsin4r=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1000.0kHz\backwards.txt')
#     # backwardsin4i=np.loadtxt(r'F:\change fre\bistable date real and imag\fd step=1000.0kHz\backwards.txt')
#
#
#
#     fig=plt.figure(figsize=(8 6))
#     ax=fig.add_subplot(1,1,1,projection='3d')
#     ax=Axes3D(fig)
#     fig.add_axes(ax)
#     ax.set_box_aspect([1,2,1])
#     ax.plot(forwardsin1i[0:int(length_W_to_X):middle_number],evo_timesin1[0:int(length_W_to_X):middle_number],forwardsin1r[0:int(length_W_to_X):middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$W \longrightarrow X$')
#     ax.set_xlabel(r'Imag', fontsize=20)
#     ax.set_ylabel(r'time', fontsize=20)
#     ax.set_zlabel(r'Real', fontsize=20)
#     # ax.set_ylim(0,10)
#     # ax.set_xlim(-60,60)
#     # plt.xticks([-50,0,50],['-50','0','50'])
#     # ax.grid(None)
#     ax.view_init(elev=14 ,azim=25)
#     plt.legend(loc=0)
#     plt.show()
#
#     fig=plt.figure(figsize=(8 6))
#     ax=fig.add_subplot(1,1,1,projection='3d')
#     ax=Axes3D(fig)
#     fig.add_axes(ax)
#     ax.set_box_aspect([1,2,1])
#     ax.plot(backwardsin1i[0:int(length_Y_to_Z):middle_number],evo_timesin1[0:int(length_Y_to_Z):middle_number],backwardsin1r[0:int(length_Y_to_Z):middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$Y \longrightarrow Z$')
#     ax.set_xlabel(r'Imag', fontsize=20)
#     ax.set_ylabel(r'time', fontsize=20)
#     ax.set_zlabel(r'Real', fontsize=20)
#     # ax.set_ylim(0,10)
#     # ax.set_xlim(-60,60)
#     # plt.xticks([-50,0,50],['-50','0','50'])
#     # ax.grid(None)
#     ax.view_init(elev=14 ,azim=25)
#     plt.legend(loc=0)
#     plt.show()
#
# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(forwardsin2i[::middle_number],evo_timesin1[::middle_number],forwardsin2r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$W \longrightarrow X$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()
#
# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(backwardsin2i[::middle_number],evo_timesin1[::middle_number],backwardsin2r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$Y \longrightarrow Z$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()

# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(forwardsin3i[::middle_number],evo_timesin1[::middle_number],forwardsin3r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$W \longrightarrow X$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()
#
# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(backwardsin3i[::middle_number],evo_timesin1[::middle_number],backwardsin3r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$Y \longrightarrow Z$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()
#
# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(forwardsin4i[::middle_number],evo_timesin1[::middle_number],forwardsin4r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$W \longrightarrow X$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()
#
# fig=plt.figure(figsize=(8 6))
# ax=fig.add_subplot(1,1,1,projection='3d')
# ax=Axes3D(fig)
# fig.add_axes(ax)
# ax.set_box_aspect([1,2,1])
# ax.plot(backwardsin4i[::middle_number],evo_timesin1[::middle_number],backwardsin4r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$Y \longrightarrow Z$')
# ax.set_xlabel(r'Imag', fontsize=20)
# ax.set_ylabel(r'time', fontsize=20)
# ax.set_zlabel(r'Real', fontsize=20)
# # ax.set_ylim(0,10)
# # ax.set_xlim(-60,60)
# # plt.xticks([-50,0,50],['-50','0','50'])
# # ax.grid(None)
# ax.view_init(elev=25, azim=40)
# plt.legend(loc=0)
# plt.show()
