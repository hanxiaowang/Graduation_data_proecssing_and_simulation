import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os




mpart5=np.linspace(100,1000,10)
mpart4=np.linspace(10,100,10)
mpart3=np.linspace(1,10,10)
mpart2=np.linspace(0.1,1,10)
mpart1=np.linspace(0.01,0.1,10)
fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
min_position=np.loadtxt(f'F:\\change fre\\bistable date\\min.txt')

slopemin,interceptmin=np.polyfit(np.log10(fins),np.log10(min_position),1)
nihe1=slopemin*np.log10(fins)+interceptmin
print(f'slope is {slopemin} and offset is {interceptmin}')

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(np.log10(fins),nihe1,'-',linewidth=5,color='blue')
axes.plot(np.log10(fins),np.log10(min_position),'o',markersize=10,color='tomato',markerfacecolor='None')
axes.set_xlabel(r'$\Delta f_d$ [kHz]',fontsize=40)
axes.set_ylabel(r'$times$ [ns]',fontsize=40)
# plt.xscale('log')
# plt.yscale('log')
# plt.yticks([-10,0,10],['-10','0','10'])
plt.tick_params(labelsize=35)
plt.show()
