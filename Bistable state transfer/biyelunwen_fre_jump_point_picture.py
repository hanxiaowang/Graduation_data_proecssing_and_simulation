import numpy as np
import matplotlib.pyplot as plt
from Needfunctions import Bistability
from mpl_toolkits.mplot3d import Axes3D
import os
from Preparation_WXH import save_file as sf
mpart5=np.linspace(100,1000,10)
mpart4=np.linspace(10,100,10)
mpart3=np.linspace(1,10,10)
mpart2=np.linspace(0.1,1,10)
mpart1=np.linspace(0.01,0.1,10)
fins = np.hstack((mpart1, np.delete(mpart2, 0), np.delete(mpart3, 0), np.delete(mpart4, 0), np.delete(mpart5, 0)))
# fins=[0.5,1]



pointWf=np.loadtxt(r'F:\change fre\bistable date\W fre.txt')
pointWw=np.loadtxt(r'F:\change fre\bistable date\W deltaplus.txt')
pointXf=np.loadtxt(r'F:\change fre\bistable date\X fre.txt')
pointXw=np.loadtxt(r'F:\change fre\bistable date\X deltaplus.txt')
pointYf=np.loadtxt(r'F:\change fre\bistable date\Y fre.txt')
pointYw=np.loadtxt(r'F:\change fre\bistable date\Y deltaplus.txt')
pointZf=np.loadtxt(r'F:\change fre\bistable date\Z fre.txt')
pointZw=np.loadtxt(r'F:\change fre\bistable date\Z deltaplus.txt')


index_1mw= list(fins).index(100)
print(pointWf[index_1mw])
print(pointXf[index_1mw])
print(pointYf[index_1mw])
print(pointZf[index_1mw])
# print((pointWf[0]+pointXf[0])/2)
# print((pointYf[0]+pointZf[0])/2)
#
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(fins ,pointWf, 's',  markersize=5, label=r'W',markerfacecolor='None',color='orange')
# axes1.plot(fins ,pointXf, 's',  markersize=5, label=r'X',markerfacecolor='None',color='green')
# # plt.xlim(0.01,0.1)
# plt.xscale('log')
# plt.legend(loc=0,fontsize=20)
# plt.show()
# #
# plt.figure(figsize=(8, 6))
# axes1 = plt.subplot(111)
# axes1.plot(fins ,pointZf, 's',  markersize=5, label=r'Z',markerfacecolor='None',color='orange')
# axes1.plot(fins ,pointYf,  's',  markersize=5, label=r'Y',markerfacecolor='None',color='green')
# plt.legend(loc=0,fontsize=20)
# # plt.xlim(0.01,0.1)
# plt.xscale('log')
# plt.show()