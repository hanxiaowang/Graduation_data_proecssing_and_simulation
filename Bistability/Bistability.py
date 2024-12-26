import numpy as np
import matplotlib.pyplot as plt
hbar = 6.626e-34 / (2 * np.pi)
fre=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change fre 1D backward 12-30-14\drive fre.txt')
Dfreb=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change fre 1D backward 12-30-14\Delta omega up.txt')
Dfref=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change fre 1D forward 11-58-48\Delta omega up.txt')

power=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change power 1D forward 19-25-6\drive power.txt')
Dpowerf=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change power 1D forward 19-25-6\Delta omega up.txt')
Dpowerb=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\Bistability UP change power 1D backward 19-54-36\Delta omega up.txt')



fx0=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\x0.txt')
fx1=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\x1.txt')
fx2=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\x2.txt')
fy0=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\y0.txt')
fy1=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\y1.txt')
fy2=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\fre\y2.txt')

px0=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\x0.txt')*1e3
px1=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\x1.txt')*1e3
px2=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\x2.txt')*1e3
py0=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\y0.txt')
py1=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\y1.txt')
py2=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Bistability\power\y2.txt')



fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.scatter(power,Dpowerf,label='Scan forward',color='none',edgecolors='blue',s=100,linewidth=3)
axes.scatter(power[::-1],Dpowerb,label='Scan backward',color='none',edgecolors='red',s=100,linewidth=3)

axes.plot(px0,py0,'.',label='Simulation',color='black',markersize=15)
axes.plot(px1,py1,'.',label='',color='black',markersize=15)
axes.plot(px2,py2,'.',label='',color='black',markersize=15)

axes.set_xlabel(r'$P_d$ [mW]',fontsize=40)
axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=40)
plt.tick_params(labelsize=40)
plt.legend(loc=5,fontsize=30)
plt.show()

# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.scatter(fre[::-1],Dfref,label='Scan forward',color='none',edgecolors='blue',s=100,linewidth=3)
# axes.scatter(fre,Dfreb,label='Scan backward',color='none',edgecolors='red',s=100,linewidth=3)
#
# axes.plot(fx0,fy0,'.',label='Simulation',color='black',markersize=15)
# axes.plot(fx1,fy1,'.',label='',color='black',markersize=15)
# axes.plot(fx2,fy2,'.',label='',color='black',markersize=15)
#
# axes.set_xlabel(r'$f_d$ [GHz]',fontsize=40)
# axes.set_ylabel(r'$\Delta_+/2\pi$ [MHz]',fontsize=40)
# plt.tick_params(labelsize=40)
# plt.legend(loc=5,fontsize=30)
# plt.show()

