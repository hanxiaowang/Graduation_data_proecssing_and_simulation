import numpy as np
import matplotlib.pyplot as plt
from Prepare import *


drive_power_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 16-19-15\drive power.txt'));
delta_m_out=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 16-19-15\drive fre.txt'));
cpf_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 16-19-15\Delta omega up.txt'));
cfp_out=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change frequency first 16-52-3\Delta omega up.txt'));
# step_out=np.linspace(1,len(drive_power_out)+1,len(drive_power_out))
# print(len(step_out))
#
# plot_p_and_f(step_out,drive_power_out,delta_m_out)
# plot_polar(step_out,cpf_out)
# plot_polar(step_out[::-1],cfp_out)
# #

drive_power_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 20-36-2\drive power.txt'))[::-1];
delta_m_in=(8.184-np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 20-36-2\drive fre.txt'))[::-1];
cpf_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change power first 20-36-2\Delta omega up.txt'))[::-1];
cfp_in=(np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230403\CP out and cross two sides change frequency first 21-9-17\Delta omega up.txt'))[::-1];
step_in=np.linspace(1,len(drive_power_in)+1,len(drive_power_in))
print(len(step_in))


# plot_p_and_f(step_in,drive_power_in,delta_m_in)


#
q=90
print(drive_power_in[q])
print(delta_m_in[q])
#
# # print()


## 双稳态低能量面
# power1=drive_power_in[:90]
# power2=drive_power_in[90:]
# m1=delta_m_in[:90]
# m2=delta_m_in[90:]
# pf1=cpf_in[:90]
# pf2=cpf_in[90:]
# fp1=cfp_in[::-1][:90]
# fp2=cfp_in[::-1][90:]
#
# print(len(power1))
# print(len(power2))
#
#
# drive_down=np.concatenate((power2,power1))
# m_down=np.concatenate((m2,m1))



# plot_p_and_f(step_in,drive_down,m_down)


# pf_down=np.concatenate((fp2,fp1))
# plot_polar(step_in,pf_down)

# fp_down=np.concatenate((fp1[::-1],pf2[::-1]))
# plot_polar(step_in[::-1],fp_down)



## 双稳态高能量面
power1=drive_power_in[:90]
power2=drive_power_in[90:200]
power3=drive_power_in[200:]
m1=delta_m_in[:90]
m2=delta_m_in[90:200]
m3=delta_m_in[200:]
pf1=cpf_in[:90]
pf2=cpf_in[90:200]
pf3=cpf_in[200:]
fp1=cfp_in[::-1][:90]
fp2=cfp_in[::-1][90:200]
fp3=cfp_in[::-1][200:]


# fp_up=np.concatenate((pf2,fp3,fp1))
# plot_polar(step_in,fp_up)

pf_up=np.concatenate((pf1[::-1],pf3[::-1],pf2[::-1]))
plot_polar(step_in[::-1],pf_up)


# plt.figure()
# # plt.plot(step_in,pf_down)
# # plt.plot(step_in,fp_down)
# # plt.plot(step_in,fp_up)
# plt.plot(step_in,pf_up)
# plt.show()



# fp_down=np.concatenate(())

# pf_up=np.concatenate()
# fp_up=np.concatenate()
# print(power1[190])
# print(power2[0])
# print(m1[-1])
# print(m2[0])

# power2=drive_power_out-drive_power_out[0::190]
# power1,power2=np.split(drive_power_out,190)
# m1,m2=np.split(delta_m_out,190)
# pf1,pf2=np.split(cpf_out,190)
# fp1,fp2=np.split(cfp_out,190)
