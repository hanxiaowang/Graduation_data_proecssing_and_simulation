import numpy as np
import matplotlib.pyplot as plt

steps=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum 22-26-10\motor steps.txt')
fres=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum 22-26-10\vna fre.txt')
S=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum 22-26-10\S_2D.txt',delimiter=',')
#



a1=400
a2=520
a3=833
a4=3534

print(steps[a1])
print(steps[a2])
print(fres[a3])
print(fres[a4])


intrs=5
intrf=10
steps1=steps[a1-1:a2+1:intrs]
S1=S[::intrf,a1-1:a2+1:intrs]
fres1=fres[::intrf]
print(np.shape(S1))
plt.figure(figsize=(8, 8))
ax2 = plt.subplot(111)
gci2 = ax2.pcolor(steps1,fres1,S1,cmap='viridis')
ax2.set_xlabel(r'$\delta$',fontsize=30)
ax2.set_ylabel(r'$\varphi$ [$\pi$]',fontsize=30)
# ax2.set(xlim=(92500, 94000))
plt.tick_params(labelsize=30)
cbar = plt.colorbar(gci2)
plt.show()