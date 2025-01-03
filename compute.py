import numpy as np
import matplotlib.pyplot as plt
xneed=[0.034]
rneed=[0.0578]
steps=1000001
start=36*np.pi/180
thetas=np.linspace(start,0,steps)

interval=(start-0)/steps


for i in range(len(thetas)-1):
    f1 =-0.0928*((np.exp(-1.15*(thetas[i]/start)**2))**2*np.sin(thetas[i]))/((1.65+21.34*xneed[i]+190.37*xneed[i]**2-766.35*xneed[i]**3+1614.65*xneed[i]**4-1868.68*xneed[i]**5+1127.61*xneed[i]**6-197.83*xneed[i]**7)**2*xneed[i])
    f2 = rneed[i]*(xneed[i]+(0.1152-2*rneed[i])*np.tan(thetas[i]/2))/(0.1152-xneed[i]*np.tan(thetas[i]/2))
    xmiddle=xneed[i]+f1*interval
    rmiddle=rneed[i]+f2*interval
    xneed.append(xmiddle)
    rneed.append(rmiddle)


xs=[]
zs=[]
for i in range(len(rneed)):
    xs.append(rneed[i]*np.sin(thetas[i]))
    zs.append(rneed[i]*np.cos(thetas[i]))

plt.figure(figsize=(10, 6))
axes1 = plt.subplot(111)
# axes1.plot(thetas, xneed, '-o',  markersize=4,label=r'x',markerfacecolor='None')
# axes1.plot(thetas, rneed, '-o',  markersize=4,label=r'r',markerfacecolor='None')
axes1.plot(zs, xs, '-o',  markersize=4,label=r'zs',markerfacecolor='None')
axes1.set_xlabel(r'theta', fontsize=20)
# axes1.set_ylabel(r'x', fontsize=20)
# axes1.set_ylabel(r'r', fontsize=20)

plt.tick_params(labelsize=20)
plt.legend(loc=0,fontsize=10)
plt.show()
