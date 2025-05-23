import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *
#
drive_power_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 16-44-10\drive power.txt'));
delta_m_out=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 16-44-10\drive fre.txt'));
cpf_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 16-44-10\Delta omega up.txt'));
cfp_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change frequency first 16-6-47\Delta omega up.txt'));
step_out=np.linspace(1,len(drive_power_out)+1,len(drive_power_out))
print(len(step_out))

# plot_p_and_f(step_out,drive_power_out,delta_m_out)
plot_polar(step_out,cpf_out)
# plot_polar(step_out[::-1],cfp_out)
#
# drive_power_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 14-47-43\drive power.txt'));
# delta_m_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 14-47-43\drive fre.txt'));
# cpf_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change power first 14-47-43\Delta omega up.txt'));
# cfp_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross two sides change frequency first 15-22-56\Delta omega up.txt'));
# step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))
# print(len(step_in))
# #
# drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross two sides change power first 10-39-53\drive power.txt'));
# delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross two sides change power first 10-39-53\drive fre.txt'));
# cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross two sides change power first 10-39-53\Delta omega up.txt'));
# cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230426\CP out and cross two sides change frequency first 11-17-42\Delta omega up.txt'));
# step_in_up=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))
# print(len(cpf_up_in))
# # #
# print(len(step_in))
# drive_power_up=[]
# delta_m_up=[]
# cpf_up=[]
# cfp_up=[]
# for i in range(len(drive_power_up_in)):
#     if round(drive_power_up_in[::-1][i]%2)==1:
#         pass
#
#     else:
#         drive_power_up.append(drive_power_up_in[i])
#         delta_m_up.append(delta_m_up_in[i])
#         cpf_up.append(cpf_up_in[i])
#         cfp_up.append(cfp_up_in[i])
#
#
# step_in_up=np.linspace(1,len(drive_power_up)+1,len(drive_power_up))

#
# plot_p_and_f(step_in,drive_power_in,delta_m_in)
# plot_polar(step_in,cpf_down_in)
# plot_polar(step_in[::-1],cfp_down_in)
# #
# plot_polar(step_in_up,cpf_up_in)
# plot_polar(step_in_up[::-1],cfp_up_in)
#
#
# plot_polar(step_in_up,cfp_up_in)
# print(len(step_in_up))
# # print(len(cfp_up_in))
# # print(len(drive_power_up_in))
# # print(drive_power_up[::-1]-drive_power_in)
# # print(drive_power_in)
# # print(drive_power_up[::-1])