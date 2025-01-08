import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf
# mpart5=np.linspace(1,10,10)
# mpart4=np.linspace(0.1,1,10)
# mpart3=np.linspace(0.01,0.1,10)
# mpart2=np.linspace(0.001,0.01,10)
# mpart1=np.linspace(0.0001,0.001,10)
# mWins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))

# #  2D演化图
# forwardsin1=np.loadtxt(r'F:\change power\bistable date\Pd step=10.0mW\forwards.txt')
# backwardsin1=np.loadtxt(r'F:\change power\bistable date\Pd step=10.0mW\backwards.txt')
# evo_timesin1=np.loadtxt(r'F:\change power\bistable date\Pd step=10.0mW\evo_times.txt')
# delta_Psin1=np.loadtxt(r'F:\change power\bistable date\Pd step=10.0mW\delta_Ps.txt')
#
# forwardsin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.05mW\forwards.txt')
# backwardsin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.05mW\backwards.txt')
# evo_timesin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.05mW\evo_times.txt')
# delta_Psin2=np.loadtxt(r'F:\change power\bistable date\Pd step=0.05mW\delta_Ps.txt')
#
# forwardsin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\forwards.txt')
# backwardsin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\backwards.txt')
# evo_timesin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\evo_times.txt')
# delta_Psin3=np.loadtxt(r'F:\change power\bistable date\Pd step=0.0001mW\delta_Ps.txt')
# #
# # forwardsin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\forwards.txt')
# # backwardsin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\backwards.txt')
# # evo_timesin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\evo_times.txt')
# # delta_Psin4=np.loadtxt(r'F:\change power\bistable date\Pd step=0.01mW\delta_Ps.txt')
# middle_number=50
# print(np.shape(forwardsin1))
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin1[::middle_number], forwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],5mw$',markerfacecolor='None')
# ax1.plot(evo_timesin2[::middle_number], forwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.05mw$',markerfacecolor='None')
# ax1.plot(evo_timesin3[::middle_number], forwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.0005mw$',markerfacecolor='None')
# # ax1.plot(evo_timesin4[::middle_number], forwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend()
# plt.show()
#
# #
# plt.figure(figsize=(12,12))
# ax1 = plt.subplot(111)
# ax1.plot(evo_timesin1[::middle_number], backwardsin1[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
# ax1.plot(evo_timesin2[::middle_number], backwardsin2[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D]$',markerfacecolor='None')
# ax1.plot(evo_timesin3[::middle_number], backwardsin3[::middle_number], 's',  markersize=4, label=r'$Re[m,C \longrightarrow D],0.01mw$',markerfacecolor='None')
# # ax1.plot(evo_timesin4[::middle_number], backwardsin4[::middle_number], '--',  markersize=4, label=r'$Re[m,A \longrightarrow B],0.01mw$',markerfacecolor='None')
#
# ax1.set_xlabel(r'$times$ [s]',fontsize=20)
# ax1.set_ylabel(r'$\Delta_+/2\pi$',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend()
# plt.show()

# #  3D演化图
# mWins=[0.0001,0.001,0.01,0.1,1.0,10.0]
mWins=[0.001,0.01]
#
for i in range(len(mWins)):
    Pd=mWins[i]
    print(Pd)

    middle_number=200

    if Pd==0.0001:
        length_A_to_B=8e6
        length_C_to_D=8e6
    elif Pd==0.001:
        length_A_to_B = 3e6
        length_C_to_D = 3e6
    elif Pd == 0.01:
        length_A_to_B = 8e5
        length_C_to_D = 8e5
    elif Pd == 0.1:
        length_A_to_B = 4e5
        length_C_to_D = 4e5
    elif Pd == 1.0:
        length_A_to_B = 2e5
        length_C_to_D = 2e5
    elif Pd == 10.0:
        length_A_to_B = 2e5
        length_C_to_D = 2e5
    forwardsin1r=np.loadtxt(f'F:\\change power\\bistable date real and imag\\Pd step={Pd}mW\\forwards real.txt')
    forwardsin1i=np.loadtxt(f'F:\\change power\\bistable date real and imag\\Pd step={Pd}mW\\forwards imag.txt')
    backwardsin1r=np.loadtxt(f'F:\\change power\\bistable date real and imag\\Pd step={Pd}mW\\backwards real.txt')
    backwardsin1i=np.loadtxt(f'F:\\change power\\bistable date real and imag\\Pd step={Pd}mW\\backwards imag.txt')
    evo_timesin1=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.0001mW\evo_times.txt')
    delta_Psin1=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.0001mW\delta_Ps.txt')
    #
    # # forwardsin2r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.01mW\forwards.txt')
    # # forwardsin2i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.01mW\forwards.txt')
    # # backwardsin2r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.01mW\backwards.txt')
    # # backwardsin2i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=0.01mW\backwards.txt')
    # #
    # # forwardsin3r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=1.0mW\forwards.txt')
    # # forwardsin3i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=1.0mW\forwards.txt')
    # # backwardsin3r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=1.0mW\backwards.txt')
    # # backwardsin3i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=1.0mW\backwards.txt')
    # # #
    # # forwardsin4r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=10mW\forwards.txt')
    # # forwardsin4i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=10mW\forwards.txt')
    # # backwardsin4r=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=10mW\backwards.txt')
    # # backwardsin4i=np.loadtxt(r'F:\change power\bistable date real and imag\Pd step=10mW\backwards.txt')
    #

    fig=plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax=Axes3D(fig)
    fig.add_axes(ax)
    ax.set_box_aspect([1,2,1])
    ax.plot(forwardsin1i[0:int(length_A_to_B):middle_number],evo_timesin1[0:int(length_A_to_B):middle_number],forwardsin1r[0:int(length_A_to_B):middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$A \longrightarrow B$')
    ax.set_xlabel(r'Imag', fontsize=10)
    ax.set_ylabel(r'time', fontsize=10)
    ax.set_zlabel(r'Real', fontsize=10)
    # ax.set_ylim(0,10)
    # ax.set_xlim(-60,60)
    # plt.xticks([-50,0,50],['-50','0','50'])
    # ax.grid(None)
    ax.view_init(elev=14, azim=25)
    plt.legend(loc=0)
    plt.show()

    fig=plt.figure(figsize=(12, 6))
    ax=fig.add_subplot(1,1,1,projection='3d')
    ax=Axes3D(fig)
    fig.add_axes(ax)
    ax.set_box_aspect([1,2,1])
    ax.plot(backwardsin1i[0:int(length_C_to_D):middle_number],evo_timesin1[0:int(length_C_to_D):middle_number],backwardsin1r[0:int(length_C_to_D):middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$C \longrightarrow D$')
    ax.set_xlabel(r'Imag', fontsize=10)
    ax.set_ylabel(r'time', fontsize=10)
    ax.set_zlabel(r'Real', fontsize=10)
    # ax.set_ylim(0,10)
    # ax.set_xlim(-60,60)
    # plt.xticks([-50,0,50],['-50','0','50'])
    # ax.grid(None)
    ax.view_init(elev=14 ,azim=25)
    plt.legend(loc=0)
    plt.show()
#
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(forwardsin2i[::middle_number],evo_timesin1[::middle_number],forwardsin2r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$A \longrightarrow B$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()
# #
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(backwardsin2i[::middle_number],evo_timesin1[::middle_number],backwardsin2r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$C \longrightarrow D$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()
#
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(forwardsin3i[::middle_number],evo_timesin1[::middle_number],forwardsin3r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$A \longrightarrow B$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()
# #
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(backwardsin3i[::middle_number],evo_timesin1[::middle_number],backwardsin3r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$C \longrightarrow D$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()
# #
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(forwardsin1i[::middle_number],evo_timesin1[::middle_number],forwardsin1r[::middle_number],'-o', color='blue',markersize=4,markerfacecolor='None',label='$A \longrightarrow B$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()
# #
# # fig=plt.figure(figsize=(12, 6))
# # ax=fig.add_subplot(1,1,1,projection='3d')
# # ax=Axes3D(fig)
# # fig.add_axes(ax)
# # ax.set_box_aspect([1,2,1])
# # ax.plot(backwardsin4i[::middle_number],evo_timesin1[::middle_number],backwardsin4r[::middle_number],'-o', color='red',markersize=4,markerfacecolor='None',label='$C \longrightarrow D$')
# # ax.set_xlabel(r'Imag', fontsize=10)
# # ax.set_ylabel(r'time', fontsize=10)
# # ax.set_zlabel(r'Real', fontsize=10)
# # # ax.set_ylim(0,10)
# # # ax.set_xlim(-60,60)
# # # plt.xticks([-50,0,50],['-50','0','50'])
# # # ax.grid(None)
# # ax.view_init(elev=25, azim=40)
# # plt.legend(loc=0)
# # plt.show()