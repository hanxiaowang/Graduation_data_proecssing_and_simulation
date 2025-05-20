import numpy as np
import matplotlib.pyplot as plt
import sys

S=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230327\2D spectrum 18-20-29\S_2D.txt',delimiter=',')
wm=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230327\2D spectrum 18-20-29\motor steps.txt')
wp=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230327\2D spectrum 18-20-29\vna fre.txt')

plt.figure(figsize=(6,6))
extents=[wm[0],wm[-1],wp[0],wp[-1]]
ax1 = plt.subplot(111)
im = ax1.imshow((S), extent=extents, aspect='auto',origin='lower')
plt.colorbar(im)
plt.show()
