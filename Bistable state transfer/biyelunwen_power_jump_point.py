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
# mWins = np.hstack((mpart3,np.delete(mpart4, 0), np.delete(mpart5, 0)))

init_path=f'F:\\change power\\bistable date'
init_path1=f'F:\\change power\\bistable date real and imag'

pointAp=[]
pointBp=[]
pointCp=[]
pointDp=[]
pointAw=[]
pointBw=[]
pointCw=[]
pointDw=[]
for i in range(len(mWins)):
    mWin=mWins[i]*1e-3
    sub_path=sf().creat_sub_file(init_path, f'Pd step={round(mWins[i],5)}mW')
    sub_path1=sf().creat_sub_file(init_path1, f'Pd step={round(mWins[i],5)}mW')

    part1=np.arange(0.010,0.020,mWin)
    part2=np.linspace(0.020,0.205,186)
    part3=np.arange(0.205,0.215,mWin)

    # part1 = np.linspace(0.014, 0.018, 201)
    # part2 = np.linspace(0.018, 0.209, 192)
    # part3 = np.linspace(0.209, 0.213, 201)
    P = np.hstack((part1, np.delete(part2, 0), np.delete(part3, 0)))
    # print(P)
    # P = np.linspace(0, 0.3, 301)
    f=8.18
    para = {'omega_a': 8.246,
            'omega_m': 8.184,
            'kaint': 3.39,
            'kaed': 2.974,
            'kmint': 1.011,
            'kmext': 0,
            'g_ma': 32.649,
            'K': 30,
            'branch': 'upper',
            'omega_d': f,
            'P_d': P,
            }

    ## Delta_+的双稳态求解
    # forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
    forward, forwardp, backward, backwardp, unstable, unstablep=Bistability(**para).BS_power_inside_BS()
    pointAp.append(forwardp[-2])
    pointBp.append(forwardp[-1])
    pointCp.append(backwardp[1])
    pointDp.append(backwardp[0])
    pointAw.append(forward[-2])
    pointBw.append(forward[-1])
    pointCw.append(backward[1])
    pointDw.append(backward[0])

sf().save_txt(init_path, 'A power', pointAp, fmt="%.12f")
sf().save_txt(init_path, 'A deltaplus', pointAw, fmt="%.12f")
sf().save_txt(init_path, 'B power', pointBp, fmt="%.12f")
sf().save_txt(init_path, 'B deltaplus', pointBw, fmt="%.12f")
sf().save_txt(init_path, 'C power', pointCp, fmt="%.12f")
sf().save_txt(init_path, 'C deltaplus', pointCw, fmt="%.12f")
sf().save_txt(init_path, 'D power', pointDp, fmt="%.12f")
sf().save_txt(init_path, 'D deltaplus', pointDw, fmt="%.12f")