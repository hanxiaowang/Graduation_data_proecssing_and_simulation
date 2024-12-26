import numpy as np
import matplotlib.pyplot as plt
import math


def new_start_point(n,arr):
    new_arr=[]
    lens=len(arr)
    for i in range(lens):
        if (n+i)<lens:
            new_arr.append(arr[n + i])
        else:
            new_arr.append(arr[n+i-lens])
    return new_arr

def plot_polar(x1,y):
    x=x1/(len(x1)-1)*2*np.pi
    plt.figure(figsize=(6, 6), dpi=300)
    ax3 = plt.subplot(111, projection='polar')
    ax3.scatter(x, y, marker='s', color='none', edgecolors='green', s=5, linewidth=0.5)
    ax3.scatter(x[0], y[0], marker='o', color='blue', edgecolors='blue', s=50, linewidth=0)
    ax3.scatter(x[-1], y[-1], marker='o', color='red', edgecolors='red', s=50, linewidth=0)
    if math.ceil(max(y))>=40:
        ax3.set_rgrids([-1, 60 ],
                       [f'-1', f'60'], fontweight="bold", fontsize=10,
                       c='black')
    # elif (math.ceil(max(y)) < 40) and (math.ceil(max(y)) >=30):
    #     ax3.set_rgrids([-1, 40],
    #                    [f'-1', f'40'], fontweight="bold", fontsize=10,
    #                    c='black')
    elif (math.ceil(max(y)) < 40) and (math.ceil(max(y)) >= 20):
        ax3.set_rgrids([-1, 40],
                       [f'-1', f'40'], fontweight="bold", fontsize=10,
                       c='black')
    elif (math.ceil(max(y)) < 20) and (math.ceil(max(y)) > 0):
        ax3.set_rgrids([-1, 20],
                       [f'-1', f'20'], fontweight="bold", fontsize=10,
                       c='black')
    else:
        ax3.set_rgrids([math.floor(min(y)), math.ceil(max(y))],
                       [f'{math.floor(min(y))}', f'{math.ceil(max(y))}'], fontweight="bold", fontsize=10,
                       c='black')
    ax3.set_thetagrids([0, 90, 180, 270],
                       [f'0/{round((len(x1)-1))}', f'{round((len(x1)-1)*0.25)}', f'{round((len(x1)-1)*0.5)}', f'{round((len(x1)-1)*0.75)}'],
                       fontweight="bold", fontsize=10, c='black')
    ax3.set_theta_zero_location('S')
    ax3.set_rlabel_position(215)
    ax3.set_theta_direction('clockwise')
    plt.show()


def plot_p_and_f(steps,power,fre):
    plt.figure(figsize=(12, 6))
    ax1 = plt.subplot(111)
    ax1.scatter(steps,power,color='blue',edgecolors='blue',s=10,linewidth=0,label=r'$P_d$')
    ax1.set_ylabel(r'$P_d$ [mW]',fontsize=30,color='blue')
    ax2=ax1.twinx()
    ax2.scatter(steps,fre*1e3,color='none',edgecolors='red',s=20,linewidth=1,label=r'$\delta_m/2\pi$')
    ax2.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=30,color='red')
    ax1.set_xlabel(r'Step',fontsize=30)
    ax1.tick_params(axis='y',labelsize=30,colors='blue')
    ax2.tick_params(axis='y',labelsize=30,colors='red')
    ax1.tick_params(axis='x',labelsize=30,colors='black')

    # plt.legend(loc=0,fontsize=20)
    plt.show()