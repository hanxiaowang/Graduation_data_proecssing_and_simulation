import numpy as np
import matplotlib.pyplot as plt
#8.27~8.31
#93690~93730


# S=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D 20_45_6\2D 20_45_6\2D spectrum 20_45_6.txt',delimiter=',')
# # a,b=np.shape(S)
# # print(a)
# # print(b)
# f=np.linspace(8.27,8.31,16001)
# step=np.linspace(93690,93730,41)
# omega_p=[]
# omega_m=[]
# delta=[]
# omega=[]
# S1=[rows[0] for rows in S]
# qian=S1[:8000]
# hou=S1[8001:]
#
# for i in range(len(step)):
#     S1=[rows[i] for rows in S]
#     qian=S1[:8400]
#     hou=S1[8401:]
#
#     min_qian=min(qian)
#     min_hou=min(hou)
#
#     min_qian_index=qian.index(min_qian)
#     min_hou_index = hou.index(min_hou)
#     omega_m.append(f[min_qian_index])
#     omega_p.append(f[min_hou_index+8000])
#     delta.append(f[min_hou_index+8000]-f[min_qian_index])
#     omega.append(f[min_hou_index+8000]+f[min_qian_index]-8.29)
#
# fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# # axes.plot(step, omega_m, '-', label='', color='blue', linewidth=2)
# # axes.plot(step, omega_p, '-', label='', color='blue', linewidth=2)
# # axes.plot(step, delta, '-', label='', color='blue', linewidth=2)
# axes.plot(step, omega, '-', label='', color='blue', linewidth=2,marker='o',markersize=15)
# axes.set_xlabel('Motor step', fontsize=40)
# axes.set_ylabel('$\omega_m$ [GHz]', fontsize=40)
# # axes.set_title('Before laser',fontsize=20)
# # plt.xticks([-10.455, -10.454, -10.453, -10.452, -10.451], ['-10.455', '-10.454', '-10.453', '-10.452', '-10.451'])
# plt.tick_params(labelsize=40)
# # plt.legend(loc=1,fontsize=20)
# plt.show()



S=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum vs double voltage 21-32-6\S_2D.txt',delimiter=',')
a,b=np.shape(S)
print(a)
print(b)
f=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum vs double voltage 21-32-6\vna fre.txt')
step=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\2D spectrum vs double voltage 21-32-6\steps.txt')
omega_p=[]
omega_m=[]
delta=[]
omega=[]
need_step=[]
for i in range(22):
    S1=[rows[i] for rows in S]
    if i<9:
        q=3100
    if i==9:
        q=3500
    if i==10:
        q=4500
    if (i>10)&(i<15):
        q=5300
    if (i>15)&(i<19):
        q=6000
    if (i>=19)&(i<22):
        q=7100
    if i>=22:
        q=8000
    qian=S1[:q]
    hou=S1[q+1:]
    need_step.append(step[i])

    min_qian=min(qian)
    min_hou=min(hou)

    min_qian_index=qian.index(min_qian)
    min_hou_index = hou.index(min_hou)
    omega_m.append(f[min_qian_index])
    omega_p.append(f[min_hou_index+q])
    delta.append(f[min_hou_index+q]-f[min_qian_index])
    omega.append(f[min_hou_index+q]+f[min_qian_index]-8.202)

fig, axes = plt.subplots(1, 1, figsize=(15, 10))
# axes.plot(need_step, omega_m, '-', label='', color='blue', linewidth=2,marker='o',markersize=15)
# axes.plot(need_step, omega_p, '-', label='', color='red', linewidth=2,marker='o',markersize=15)
# axes.plot(need_step, delta, '-', label='', color='blue', linewidth=2,marker='o',markersize=15)
axes.plot(need_step, omega, '-', label='', color='blue', linewidth=2,marker='o',markersize=15)
axes.set_xlabel('Voltage[V]', fontsize=40)
axes.set_ylabel('$\omega_m$ [GHz]', fontsize=40)
# axes.set_title('Before laser',fontsize=20)
# plt.xticks([-10.455, -10.454, -10.453, -10.452, -10.451], ['-10.455', '-10.454', '-10.453', '-10.452', '-10.451'])
plt.tick_params(labelsize=40)
# plt.legend(loc=1,fontsize=20)
plt.show()