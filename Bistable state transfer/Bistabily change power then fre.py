
from Needfunctions import Bistability
import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from mpl_toolkits.mplot3d import Axes3D
import os
import json

P = np.linspace(0, 0.3, 301)
f=np.linspace(8.2,8.3,21)

Msf_r=[]
Msb_r=[]
Msu_r=[]
Msf_i=[]
Msb_i=[]
Msu_i=[]
Ff=[]
Fb=[]
Fu=[]

for i in range(len(f)):
    para = {'omega_a': 8.246,
            'omega_m': 8.184,
            'kaint': 3.39,
            'kaed': 2.974,
            'kmint': 1.011,
            'kmext': 0,
            'g_ma': 32.649,
            'K': 30,
            'branch': 'upper',
            'omega_d': f[i],
            'P_d': P,
            }


    forward, forwardp, backward, backwardp, unstablep, unstable=Bistability(**para).BS_power_with_unstable()
    wminf = 8.184 * 1e9 * 2 * np.pi
    wpinf = Bistability(**para).branch_fre(wminf)  ##初始的w+,单位Hz

    wmf = Bistability(**para).wplus_to_wm(wpinf + np.array(forward) * 1e6 * 2 * np.pi)
    wmb = Bistability(**para).wplus_to_wm(wpinf + np.array(backward) * 1e6 * 2 * np.pi)
    wmu = Bistability(**para).wplus_to_wm(wpinf + np.array(unstable) * 1e6 * 2 * np.pi)

    msf, asf = Bistability(**para).cal_ms_as_P(wmf - wminf, forwardp)
    msb, asb = Bistability(**para).cal_ms_as_P(wmb - wminf, backwardp)
    msu, asu = Bistability(**para).cal_ms_as_P(wmu - wminf, unstablep)

    Msf_r.append(msf.real)
    Msb_r.append(msb.real)
    Msu_r.append(msu.real)
    Msf_i.append(msf.imag)
    Msb_i.append(msb.imag)
    Msu_i.append(msu.imag)
    ff=np.zeros(len(msf.real))+f[i]
    fb = np.zeros(len(msb.real))+f[i]
    fu = np.zeros(len(msu.real))+f[i]
    Ff.append(ff)
    Fb.append(fb)
    Fu.append(fu)



fig=plt.figure(figsize=(12, 6))
ax=fig.add_subplot(1,1,1,projection='3d')
ax=Axes3D(fig)
fig.add_axes(ax)
ax.set_box_aspect([2,3,1])

#f=8.14
ax.plot(Msf_i[0],Ff[0], Msf_r[0],'^',color='red')
ax.plot(Msb_i[0],Fb[0], Msb_r[0],'o',color='blue')
ax.plot(Msu_i[0],Fu[0], Msu_r[0],'-',color='purple')

#f=8.15
ax.plot(Msf_i[1],Ff[1], Msf_r[1],'^',color='red')
ax.plot(Msb_i[1],Fb[1], Msb_r[1],'o',color='blue')
ax.plot(Msu_i[1],Fu[1], Msu_r[1],'-',color='purple')

#f=8.16
ax.plot(Msf_i[2],Ff[2], Msf_r[2],'^',color='red')
ax.plot(Msb_i[2],Fb[2], Msb_r[2],'o',color='blue')
ax.plot(Msu_i[2],Fu[2], Msu_r[2],'-',color='purple')

#f=8.17
ax.plot(Msf_i[3],Ff[3], Msf_r[3],'^',color='red')
ax.plot(Msb_i[3],Fb[3], Msb_r[3],'o',color='blue')
ax.plot(Msu_i[3],Fu[3], Msu_r[3],'-',color='purple')

#f=8.18
ax.plot(Msf_i[4],Ff[4], Msf_r[4],'^',color='red')
ax.plot(Msb_i[4],Fb[4], Msb_r[4],'o',color='blue')
ax.plot(Msu_i[4],Fu[4], Msu_r[4],'-',color='purple')

#f=8.19
ax.plot(Msf_i[5],Ff[5], Msf_r[5],'^',color='red')
ax.plot(Msb_i[5],Fb[5], Msb_r[5],'o',color='blue')
ax.plot(Msu_i[5],Fu[5], Msu_r[5],'-',color='purple')

#f=8.2
ax.plot(Msf_i[6],Ff[6], Msf_r[6],'^',color='red')
ax.plot(Msb_i[6],Fb[6], Msb_r[6],'o',color='blue')
ax.plot(Msu_i[6],Fu[6], Msu_r[6],'-',color='purple')

#f=8.21
ax.plot(Msf_i[7],Ff[7], Msf_r[7],'^',color='red')
ax.plot(Msb_i[7],Fb[7], Msb_r[7],'o',color='blue')
ax.plot(Msu_i[7],Fu[7], Msu_r[7],'-',color='purple')

#f=8.22
ax.plot(Msf_i[8],Ff[8], Msf_r[8],'^',color='red')
ax.plot(Msb_i[8],Fb[8], Msb_r[8],'o',color='blue')
ax.plot(Msu_i[8],Fu[8], Msu_r[8],'-',color='purple')

#f=8.23
ax.plot(Msf_i[9],Ff[9], Msf_r[9],'^',color='red')
ax.plot(Msb_i[9],Fb[9], Msb_r[9],'o',color='blue')
ax.plot(Msu_i[9],Fu[9], Msu_r[9],'-',color='purple')

#f=8.24
ax.plot(Msf_i[10],Ff[10], Msf_r[10],'^',color='red')
ax.plot(Msb_i[10],Fb[10], Msb_r[10],'o',color='blue')
ax.plot(Msu_i[10],Fu[10], Msu_r[10],'-',color='purple')

#f=8.25
ax.plot(Msf_i[11],Ff[11], Msf_r[11],'^',color='red')
ax.plot(Msb_i[11],Fb[11], Msb_r[11],'o',color='blue')
ax.plot(Msu_i[11],Fu[11], Msu_r[11],'-',color='purple')

#f=8.26
ax.plot(Msf_i[12],Ff[12], Msf_r[12],'^',color='red')
ax.plot(Msb_i[12],Fb[12], Msb_r[12],'o',color='blue')
ax.plot(Msu_i[12],Fu[12], Msu_r[12],'-',color='purple')

#f=8.27
ax.plot(Msf_i[13],Ff[13], Msf_r[13],'^',color='red')
ax.plot(Msb_i[13],Fb[13], Msb_r[13],'o',color='blue')
ax.plot(Msu_i[13],Fu[13], Msu_r[13],'-',color='purple')

#f=8.28
ax.plot(Msf_i[14],Ff[14], Msf_r[14],'^',color='red')
ax.plot(Msb_i[14],Fb[14], Msb_r[14],'o',color='blue')
ax.plot(Msu_i[14],Fu[14], Msu_r[14],'-',color='purple')

#f=8.29
ax.plot(Msf_i[15],Ff[15], Msf_r[15],'^',color='red')
ax.plot(Msb_i[15],Fb[15], Msb_r[15],'o',color='blue')
ax.plot(Msu_i[15],Fu[15], Msu_r[15],'-',color='purple')

#f=8.3
ax.plot(Msf_i[16],Ff[16], Msf_r[16],'^',color='red')
ax.plot(Msb_i[16],Fb[16], Msb_r[16],'o',color='blue')
ax.plot(Msu_i[16],Fu[16], Msu_r[16],'-',color='purple')

#f=8.31
ax.plot(Msf_i[17],Ff[17], Msf_r[17],'^',color='red')
ax.plot(Msb_i[17],Fb[17], Msb_r[17],'o',color='blue')
ax.plot(Msu_i[17],Fu[17], Msu_r[17],'-',color='purple')

#f=8.32
ax.plot(Msf_i[18],Ff[18], Msf_r[18],'^',color='red')
ax.plot(Msb_i[18],Fb[18], Msb_r[18],'o',color='blue')
ax.plot(Msu_i[18],Fu[18], Msu_r[18],'-',color='purple')

#f=8.33
ax.plot(Msf_i[19],Ff[19], Msf_r[19],'^',color='red')
ax.plot(Msb_i[19],Fb[19], Msb_r[19],'o',color='blue')
ax.plot(Msu_i[19],Fu[19], Msu_r[19],'-',color='purple')

#f=8.34
ax.plot(Msf_i[20],Ff[20], Msf_r[20],'^',color='red')
ax.plot(Msb_i[20],Fb[20], Msb_r[20],'o',color='blue')
ax.plot(Msu_i[20],Fu[20], Msu_r[20],'-',color='purple')

ax.set_zlabel(r'Real', fontsize=20)
ax.set_xlabel(r'Imag', fontsize=20)
ax.set_ylabel(r'fd', fontsize=20)
# ax.set_ylim(0,10)
# ax.set_xlim(-60,60)
# plt.xticks([-50,0,50],['-50','0','50'])
# ax.grid(None)
ax.view_init(elev=15, azim=17)
# ax.view_init(elev=7, azim=18)
plt.show()