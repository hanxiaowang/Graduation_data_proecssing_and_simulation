import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:\Users\AORUS\OneDrive\little thing\Theory_WXH')
from Preparation_WXH import date_and_time as dt
from Preparation_WXH import save_file as sf
from Preparation_WXH import Read_file as ref
from Preparation_WXH import Plot_easy as pe
from Preparation_WXH import Combination
from Spectrum_WXH import Reflection
import os
from Computation_WXH import Power_Convert as pc
from Cycle_WXH import Square
from Cycle_WXH import Round
from Bistability_WXH_K import Change_surface
from Bistability_WXH_K import Bistability
from Spectrum_WXH import Reflection


fPbl=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\frequency critical point\jump point large.txt')
ffbl=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\frequency critical point\jump point large fre.txt')
fPbs=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\frequency critical point\jump point small.txt')
ffbs=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\frequency critical point\jump point small fre.txt')

PPbl=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\power critical point\jump point large Power.txt')
Pfbl=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\power critical point\jump point large.txt')
PPbs=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\power critical point\jump point small Power.txt')
Pfbs=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\power critical point\jump point small.txt')

#2 20~-50
Ploop2=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change frequency first 15-29-24\drive power.txt')
floop2=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change frequency first 15-29-24\drive fre.txt')

#3 30~-50
Ploop3=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\CP out and cross no side change power first 10-51-44\drive power.txt')
floop3=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230410\CP out and cross no side change power first 10-51-44\drive fre.txt')

#4 20~-60
Ploop4=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross upper side change power first 16-26-41\drive power.txt')
floop4=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross upper side change power first 16-26-41\drive fre.txt')

#5 20~-60
Ploop5=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230406\CP out and cross upper side change power first 11-1-40\drive power.txt')
floop5=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230406\CP out and cross upper side change power first 11-1-40\drive fre.txt')

#6 40~-60
Ploop6=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change power first 18-34-3\drive power.txt')
floop6=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230402\CP out and cross lower side change power first 18-34-3\drive fre.txt')

#7 20~-60
Ploop7=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230404\CP out and cross low side change power first 16-25-6\drive power.txt')
floop7=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230404\CP out and cross low side change power first 16-25-6\drive fre.txt')

#8 40~-80
Ploop8=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 23-27-27\drive power.txt')
floop8=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 23-27-27\drive fre.txt')

#9 20~-60
Ploop9=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 16-44-10\drive power.txt')
floop9=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 16-44-10\drive fre.txt')

#10 20~-80
Ploop10=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230428\CP out and cross no side change power first 11-9-24\drive power.txt')
floop10=8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230428\CP out and cross no side change power first 11-9-24\drive fre.txt')



# print(max(Ploop10))
# print(min(Ploop10))
# print(max(floop10)*1e3)
# print(min(floop10)*1e3)

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.scatter(fPbl,ffbl*1e3,marker='s',color='blue',s=100,edgecolors='blue')
axes.scatter(fPbs,ffbs*1e3,marker='s',color='blue',s=100,edgecolors='blue')
axes.scatter(PPbl,Pfbl*1e3,marker='o',color='red',s=100,edgecolors='red')
axes.scatter(PPbs,Pfbs*1e3,marker='o',color='red',s=100,edgecolors='red')

# axes.plot(Ploop2,floop2*1e3,'--',label='Loop 2',color='black',linewidth=5)
# axes.plot(Ploop3,floop3*1e3,'--',label='Loop 3',color='black',linewidth=5)
# axes.plot(Ploop4,floop4*1e3,'--',label='Loop 4',color='black',linewidth=5)
# axes.plot(Ploop5,floop5*1e3,'--',label='Loop 5',color='black',linewidth=5)
# axes.plot(Ploop6,floop6*1e3,'--',label='Loop 6',color='black',linewidth=5)
# axes.plot(Ploop7,floop7*1e3,'--',label='Loop 7',color='black',linewidth=5)
axes.plot(Ploop8,floop8*1e3,'--',label='Loop 8',color='black',linewidth=5)
# axes.plot(Ploop9,floop9*1e3,'--',label='Loop 9',color='black',linewidth=5)
# axes.plot(Ploop10,floop10*1e3,'--',label='Loop 10',color='black',linewidth=5)

axes.set_xlabel(r'$P_d$ [mW]',fontsize=40)
axes.set_ylabel(r'$\delta_m/2\pi$ [MHz]',fontsize=40)
plt.ylim(-80,40)
plt.tick_params(labelsize=40)
plt.legend(loc=5,fontsize=40)
plt.show()


