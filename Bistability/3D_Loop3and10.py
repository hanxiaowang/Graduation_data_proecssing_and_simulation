import numpy as np
import matplotlib.pyplot as plt
import math
from Prepare import *

## Loop 3

drive_power_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\drive power.txt'));
delta_m_down3=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\drive fre.txt'));
cpf_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change power first 21-37-55\Delta omega up.txt'));
cfp_down3=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230409\CP out and cross no side change frequency first 22-1-59\Delta omega up.txt'));
step_down3=np.linspace(1,len(drive_power_down3)+1,len(drive_power_down3))
print(len(step_down3))

drive_power_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\drive power.txt'));
delta_m_up10=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\drive fre.txt'));
cpf_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change power first 20-8-0\Delta omega up.txt'));
cfp_up10=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230427\CP out and cross no side change frequency first 20-32-5\Delta omega up.txt'));
step_up10=np.linspace(1,len(drive_power_up10)+1,len(drive_power_up10))
print(len(drive_power_up10))
print(len(step_up10))

# drive_power_up10=[]
# delta_m_up10=[]
# cpf_up10=[]
# cfp_up10=[]

# for i in range(len(drive_power_up10)):
#     if round(drive_power_up10[i]%2)==1:
#         pass
#
#     else:
#         drive_power_up10.append(drive_power_up10[i])
#         delta_m_up10.append(delta_m_up10[i])
#         cpf_up10.append(cpf_up10[i])
#         cfp_up10.append(cfp_up10[i])
#
# step_up3=np.linspace(1,len(drive_power_up10)+1,len(drive_power_up10))
# print(len(step_up3))
# #
# drive_power_down_roll=new_start_point(150,drive_power_down)
# delta_m_down_roll=new_start_point(150,delta_m_down)
# cpf_down_roll=new_start_point(150,cpf_down)
# cfp_down_roll=new_start_point(150,cfp_down)
#
# drive_power_up_roll=new_start_point(150,drive_power_up[::-1])
# delta_m_up_roll=new_start_point(150,delta_m_up[::-1])
# cpf_up_roll=new_start_point(150,cpf_up[::-1])
# cfp_up_roll=new_start_point(150,cfp_up[::-1])


# plot_p_and_f(step_up10,drive_power_up10,delta_m_up10)
# plot_p_and_f(step_down3,drive_power_down3,delta_m_down3)






plot_polar(step_down3,cpf_down3)
plot_polar(step_down3[::-1],cfp_down3)
plot_polar(step_up10,cpf_up10)
plot_polar(step_up10[::-1],cfp_up10)