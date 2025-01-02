import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf


final_evo=[]

mpart2=np.linspace(1,20,39)
mpart1=np.linspace(0,1,101)
jump_times = np.hstack((mpart1, np.delete(mpart2, 0)))

for i in range(len(jump_times)):
    interval = 1e-11
    jump_time = 1e4 * jump_times[i]
    forward = np.loadtxt(f'F:\\change power\\bistable jump back 8.18 and 1mW\\jump back time={round(interval*jump_time*1e9, 10)}ns\\forwards.txt')
    final_evo.append(forward[-1])
    # max_evo.append(max(forward))
    # max_index = list(forward).index(max(forward))
    # max_position.append(evo_times[max_index])

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(jump_times,final_evo,'o-',markersize=10,color='blue',markerfacecolor='None')
axes.set_xlabel(r'$times$ [ns]',fontsize=40)
axes.set_ylabel(r'$\Delta_{final}$ [MHz]',fontsize=40)
# plt.xscale('log')
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.show()
