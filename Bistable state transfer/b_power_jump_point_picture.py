import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf

mpart5=np.linspace(1,10,10)
mpart4=np.linspace(0.1,1,10)
mpart3=np.linspace(0.01,0.1,10)
mpart2=np.linspace(0.001,0.01,10)
mpart1=np.linspace(0.0001,0.001,10)
mWins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# mWins=[2,1]

pointAp=np.loadtxt(r'F:\change power\bistable date\A power.txt')
pointAw=np.loadtxt(r'F:\change power\bistable date\A deltaplus.txt')
pointBp=np.loadtxt(r'F:\change power\bistable date\B power.txt')
pointBw=np.loadtxt(r'F:\change power\bistable date\B deltaplus.txt')
pointCp=np.loadtxt(r'F:\change power\bistable date\C power.txt')
pointCw=np.loadtxt(r'F:\change power\bistable date\C deltaplus.txt')
pointDp=np.loadtxt(r'F:\change power\bistable date\D power.txt')
pointDw=np.loadtxt(r'F:\change power\bistable date\D deltaplus.txt')

index_1mw= list(mWins).index(1)
print(pointAp[index_1mw])
print(pointBp[index_1mw])
print(pointCp[index_1mw])
print(pointDp[index_1mw])

# print((pointAp[0]+pointBp[0])/2)
# print((pointCp[0]+pointDp[0])/2)

# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(mWins ,pointAp, 's',  markersize=4, label=r'A',markerfacecolor='None',color='orange')
# axes1.plot(mWins ,pointBp, 's',  markersize=4, label=r'B',markerfacecolor='None',color='green')
# plt.xscale('log')
# plt.legend(loc=0,fontsize=20)
# plt.show()
# #
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(mWins ,pointDp, 's',  markersize=4, label=r'D',markerfacecolor='None',color='orange')
# axes1.plot(mWins ,pointCp,  's',  markersize=4, label=r'C',markerfacecolor='None',color='green')
# plt.legend(loc=0,fontsize=20)
# plt.xscale('log')
# plt.show()
