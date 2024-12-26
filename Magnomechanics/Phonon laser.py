import numpy as np
import matplotlib.pyplot as plt
# omega_d=8.297734e9
#
# b1m=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\5.45\b1.txt')
# b2m=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\5.45\b2.txt')
# f1=[rows[0] for rows in b1m]
# f=[]
# for i in range(len(f1)):
#     f.append((f1[i]-omega_d)/1e6)
# b1=[rows[1] for rows in b1m]
# b2=[rows[1] for rows in b2m]
# # print(f[0])
# s1m=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\5.45\5.45\5\Specturm analyzer for reference21_35_3.txt')
# s2m=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\5.45\6\5\Specturm analyzer for reference16_43_22.txt')
# s1=[rows[1] for rows in s1m]
# s2=[rows[1] for rows in s2m]
#
# sf1=[]
# sf2=[]
# for i in range(len(f)):
#
#
#     sf1.append(s1[i]-b1[i]+b1[0])
#     sf2.append(s2[i]-b2[i]+b2[0])
#
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(f,sf1,'-',label='',color='blue',linewidth=2)
# axes.set_xlabel('$\delta_p/2\pi$ [MHz]',fontsize=40)
# axes.set_ylabel('$S$ [dBm]',fontsize=40)
# # axes.set_title('Before laser',fontsize=20)
# plt.xticks([-10.455,-10.454,-10.453,-10.452,-10.451],['-10.455','-10.454','-10.453','-10.452','-10.451'])
# plt.tick_params(labelsize=40)
# # plt.legend(loc=1,fontsize=20)
# plt.show()
#
# # fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(f,sf2,'-',color='blue',linewidth=2)
# # axes.set_xlabel('$\delta_p/2\pi$ [MHz]',fontsize=40)
# # axes.set_ylabel('$S$ [dBm]',fontsize=40)
# # # axes.set_title('Before laser',fontsize=20)
# # plt.tick_params(labelsize=40)
# # plt.xticks([-10.455,-10.454,-10.453,-10.452,-10.451],['-10.455','-10.454','-10.453','-10.452','-10.451'])
# # # plt.legend(loc=1,fontsize=20)
# # plt.show()


b1m=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cavity S11 for reference14_45_35.txt')
f1=[rows[0] for rows in b1m]
s1=[rows[1] for rows in b1m]
fig, axes = plt.subplots(1, 1, figsize=(15, 10))
axes.plot(f1,s1,'-',label='',color='blue',linewidth=2)
axes.set_xlabel(r'$\omega_p/2\pi$ [GHz]',fontsize=40)
axes.set_ylabel(r'$S_{11}$ [dB]',fontsize=40)
# axes.set_title('Before laser',fontsize=20)
plt.tick_params(labelsize=40)
# plt.legend(loc=1,fontsize=20)
plt.show()