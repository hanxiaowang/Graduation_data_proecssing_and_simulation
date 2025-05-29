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

voltage=np.linspace(20,110,19)
# voltage=np.linspace(40,50,11)

phi1=np.linspace(0,2,361)

de=1

deltass=[45,45,50]
deltas=0.97*voltage/deltass[de]
#
#
S12max=[]
S21max=[]

phi120=[]
phi210=[]

delta120=[]
delta210=[]
#
for i in range(len(voltage)):
    print(i)
    S12=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S12\\20-110\\S\\S12 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',delimiter=',')
    S21=np.loadtxt(f'F:\\Nonreciprocity\\20210701\\S21\\20-110\\S\\S21 of coupling(experiment) with A={round(voltage[i])}.0 mV 2D.txt',delimiter=',')

    s12max=[]
    s21max=[]
    for j in range(len(phi1)):
        s12max.append(max(S12[:,j]))
        s21max.append(max(S21[:,j]))
        cha=0.2
        if np.abs((max(S12[:,j])+33))<=cha:
            phi120.append(phi1[j])
            delta120.append(deltas[i])

        if (np.abs((max(S21[:,j])+33))<=cha)&((max(S21[:,j])+33)<0):
            phi210.append(phi1[j])
            delta210.append(deltas[i])

    S12max.append(s12max)
    S21max.append(s21max)

print(np.max(S12max))
print(np.max(S21max))
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\S12max.txt',S12max,fmt="%.9f")
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\S21max.txt',S21max,fmt="%.9f")
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\phi120.txt',phi120,fmt="%.9f")
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\delta120.txt',delta120,fmt="%.9f")
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\phi210.txt',phi210,fmt="%.9f")
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\delta210.txt',delta210,fmt="%.9f")
#
# S12max = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\S12max.txt')
# S21max = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\S21max.txt')
# phi120 = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\phi120.txt').tolist()
# delta120 = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\delta120.txt').tolist()

# print(phi120)
# print(delta120)
print(np.shape(phi120))
print(np.shape(delta120))
#
extents=[deltas[0],deltas[-1],phi1[0],phi1[-1]]
# # extents=[phi1[0],phi1[-1],deltas[0],deltas[-1]]
#
phi120s=[]
delta120s=[]
#
phi210s=[]
delta210s=[]


for i in range(len(phi120)):
    index=phi120.index(min(phi120))

    phi120s.append(phi120[index])
    delta120s.append(delta120[index])

    del phi120[index]
    del delta120[index]

for i in range(len(phi210)):
    index=phi210.index(min(phi210))

    phi210s.append(phi210[index])
    delta210s.append(delta210[index])

    del phi210[index]
    del delta210[index]
#
# def function_curvefit(xdata,a1,a2,a3,a4):
#     ydata=a1*np.cos(a2*xdata*np.pi+a3)+a4
#     return ydata
#
# t=scipy.optimize.curve_fit(function_curvefit,phi120s,delta120s,maxfev = 80000)
# print(t)

# A=t[0][0]
# B=t[0][1]
# C=t[0][2]
# D=t[0][3]

# delta_cur=[]
# for i in range(len(phi1)):
#     delta_cur.append(A*np.cos(B*phi1[i]*np.pi+C)+D)

# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\delta curvefit.txt',delta_cur,fmt="%.9f")
delta_cur = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Nonreciprocity thesis\delta curvefit.txt')


# plt.figure(figsize=(12,6))
# ax1 = plt.subplot(111)
# im = ax1.imshow((S12max), extent=extents,aspect='auto',origin='lower')
# ax1.plot(phi120s,delta120s,'o-',color='red')
# ax1.plot(phi120s[0],delta120s[0],'o',color='black')
# # ax1.plot(phi120[5],delta120[5],'o',color='black')
# ax1.plot(phi120s[-1],delta120s[-1],'o',color='black')
# plt.colorbar(im)
# plt.show()

plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(S12max), extent=extents,aspect='auto',origin='lower')
ax1.plot(delta120s,phi120s,'-',color='red',linewidth=5)
# ax1.plot(delta_cur,phi1,'--',color='blue',linewidth=5)

# ax1.plot(delta120s[0],phi120s[0],'o',color='black')
# ax1.plot(phi120[5],delta120[5],'o',color='black')
# ax1.plot(delta120s[-1],phi120s[-1],'o',color='black')
plt.colorbar(im)
plt.show()


plt.figure(figsize=(12,6))
ax1 = plt.subplot(111)
im = ax1.imshow(np.transpose(S21max), extent=extents, aspect='auto',origin='lower')
plt.plot(delta210s,phi210s,'-',color='red',linewidth=5)
plt.colorbar(im)
plt.show()



