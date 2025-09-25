import numpy as np
import matplotlib.pyplot as plt
import Curve_decay_func



drive_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\drive fre.txt')
drive_power=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\drive power.txt')
vna_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\vna fre.txt')
Delta_omega_up=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\Delta omega up.txt',delimiter=',')

# print(len(drive_fre))

i=40

S_2D = np.loadtxt(
    f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\S_2D.txt',
    delimiter=',')
print(np.shape(S_2D))

plt.figure(figsize=(12 , 9))
axes1 = plt.subplot(111)
axes1.patch.set_alpha(0)
axes1.plot(vna_fre,S_2D[:,160],'o',linewidth=3,label=r'$k_{exp}$',color='blue',alpha=0.4)
axes1.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=10)
axes1.set_ylabel(r'$S$ [dB]',fontsize=10)
plt.tick_params(labelsize=20)
plt.legend(loc=0)
plt.show()
#
#
