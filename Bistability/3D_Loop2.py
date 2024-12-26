import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *

drive_power_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 12-21-25\drive power.txt'));
delta_m_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 12-21-25\drive fre.txt'));
cpf_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change power first 12-21-25\Delta omega up.txt'));
cfp_down_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross no side change frequency first 12-44-25\Delta omega up.txt'));
step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))
# print(len(step_in))
#
drive_power_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive power.txt'));
delta_m_up_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\drive fre.txt'));
cpf_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change power first 19-49-17\Delta omega up.txt'));
cfp_up_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230424\CP out and cross no side change frequency first 20-25-25\Delta omega up.txt'));
step_in_up=np.linspace(1,len(drive_power_up_in)+1,len(drive_power_up_in))
# print(len(cpf_up_in))
# print(delta_m_in)
# print(delta_m_up_in)
# print(drive_power_in)
# print(drive_power_up_in)
# print(len(step_in))
drive_power_up=[]
delta_m_up=[]
cpf_up=[]
cfp_up=[]
for i in range(len(drive_power_up_in)):
    if round(drive_power_up_in[i]%2)==1:
        pass

    else:
        drive_power_up.append(drive_power_up_in[i])
        delta_m_up.append(delta_m_up_in[i])
        cpf_up.append(cpf_up_in[i])
        cfp_up.append(cfp_up_in[::-1][i])


step_up=np.linspace(0,len(drive_power_up)-1,len(drive_power_up))
# print(len(step_in_up))
# print((step_in_up))

# print(len(cfp_up))
# print(len(step_in_up))
#
# plot_p_and_f(step_in,drive_power_in,delta_m_in)
# plot_polar(step_in,cpf_down_in)
# plot_polar(step_in[::-1],cfp_down_in)

# plot_polar(step_up,cpf_up)
plot_polar(step_up[::-1],cfp_up[::-1])

# print(drive_power_up-drive_power_in)
# print(drive_power_up[::-1])
# print(len(drive_power_up))
# print(step_in_up[::-1])
print()