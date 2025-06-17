import numpy as np
import matplotlib.pyplot as plt
from matplotlib import *
import math as m
import cmath
from matplotlib import cm
import skrf as rf
import os
import json
import scipy
from sympy.printing.pretty.pretty_symbology import line_width

fre=np.linspace(8.2,8.4,20001)
S_average = np.loadtxt(r'F:\Nonreciprocity\Output_power 11-56-56\S_averge_all.txt',delimiter=',')
power=np.loadtxt(r'F:\Nonreciprocity\Output_power 11-56-56\power range.txt')
rr = np.where(fre ==8.276)

hengding=[]
for i in range(len(power)):
    hengding.append(8.276)
S_need=S_average[rr[0][0]]

power_mW=10**(power/10)
S_need_mW=10**(S_need/10)

Errorbarmax=[]
Errorbarmin=[]


Errorbar_mWmax=[]
Errorbar_mWmin=[]

for i in range(len(power)):
    ini=np.loadtxt(f'F:\\Nonreciprocity\\Output_power 11-56-56\\probe power={round(power[i],1)} dBm.txt',delimiter=',')
    Errorbarmax.append(max(ini[:,rr[0][0]]))
    Errorbarmin.append(min(ini[:,rr[0][0]]))

    Errorbar_mWmax.append(max(10**(ini[:, rr[0][0]]/10)))
    Errorbar_mWmin.append(min(10**(ini[:, rr[0][0]]/10)))

Errorbar=[np.abs(Errorbarmax-S_need),np.abs(Errorbarmin-S_need)]
Errorbar_mW=[np.abs(Errorbar_mWmax-S_need_mW),np.abs(Errorbar_mWmin-S_need_mW)]

# print(max(np.abs(Errorbarmin-S_need)))
# print(max(np.abs(Errorbarmax-S_need)))

pas=np.polyfit(power,S_need,1)
#
print(pas)
S_sim=pas[0]*power+pas[1]


pas_mW=np.polyfit(power_mW,S_need_mW,1)
print(pas_mW)
S_sim_mW=pas_mW[0]*power_mW+pas_mW[1]


# fig, axes1 = plt.subplots(1, 1, figsize=(6  , 6))
# axes1 = plt.subplot(111)
# fig.patch.set_alpha(0)
# axes1.patch.set_alpha(0)
# axes1.errorbar(power,S_need,yerr=(Errorbar),fmt='d',linewidth=1,ecolor='blue',capsize=3,
#                label=r'Experiment',color='blue',zorder=1)
# axes1.plot(power,S_sim,'-',linewidth=2,label=r'Curvefit',color='red',zorder=2)
# # axes1.errorbar(power_mW,S_need_mW,yerr=(Errorbar_mW),fmt='d',linewidth=1,ecolor='blue',capsize=3,
# #                label=r'Experiment',color='blue',zorder=1)
# # axes1.plot(power_mW,S_sim_mW,'-',linewidth=2,label=r'Curvefit',color='red',zorder=2)
# axes1.set_xlabel(r'$P in$ [dBm]',fontsize=20)
# axes1.set_ylabel(r'$P out$ [dBm]',fontsize=20)
# # plt.xscale('log')
# # plt.yscale('log')
# # axes1.set_ylim(-105,5)
# # plt.yticks([-100,-50,0,50,100],['-100','-50','0','50','100'])
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,prop={'family':'Cambria','size':20})
# plt.show()

#
plt.figure(figsize=(6,6))
extents=[power[0],power[-1],fre[0],fre[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow((S_average), extent=extents, aspect='auto',origin='lower')
# ax1.plot(power,hengding,'--',linewidth=2,color='red',alpha=0.5)
plt.colorbar(im)
plt.show()
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\input power_dBm.txt',power)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\input power_mW.txt',power_mW)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_average_dBm.txt',S_need)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_average_mW.txt',S_need_mW)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_sim_dBm.txt',S_sim)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_sim_mW.txt',S_sim_mW)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_max_dBm.txt',Errorbarmax-S_need)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_max_mW.txt',Errorbar_mWmax-S_need_mW)
#
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_min_dBm.txt',Errorbarmin-S_need)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_min_mW.txt',Errorbar_mWmin-S_need_mW)
# print(Errorbar_mWmax)
