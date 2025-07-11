import numpy as np
import matplotlib.pyplot as plt
power_mW=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\input power_mW.txt')
receive_average_mW=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_average_mW.txt')
receive_sim_mW=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\receive_sim_mW.txt')
Error_max_mW=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_max_mW.txt')
Error_min_mW=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\Linear response\Error_min_mW.txt')
Errorbar_mW=[Error_max_mW,-Error_min_mW]

fig, axes1 = plt.subplots(1, 1, figsize=(8  , 6))
axes1 = plt.subplot(111)
fig.patch.set_alpha(0)
axes1.patch.set_alpha(0)
axes1.errorbar(power_mW,receive_average_mW,yerr=(Errorbar_mW),fmt='d',linewidth=1,ecolor='blue',capsize=3,
               label=r'Experiment',color='blue',zorder=1)
axes1.plot(power_mW,receive_sim_mW,'-',linewidth=2,label=r'Curvefit',color='red',zorder=2)
axes1.set_xlabel(r'$P in$ [mW]',fontsize=20)
axes1.set_ylabel(r'$P out$ [mW]',fontsize=20)

plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()