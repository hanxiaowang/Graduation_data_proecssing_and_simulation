import numpy as np
import matplotlib.pyplot as plt


WBp_up_e = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\WBp_up_e.txt')
WBp_down_e = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\WBp_down_e.txt')
KBp_up_e = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\KBp_up_e.txt')
KBp_down_e = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\KBp_down_e.txt')
WAE = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\wAE.txt') - 0.0075
# WAE = np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\w_amd_k\wAE.txt') - 0.007


wyavg = []
wymax = []
wymin = []
wd1 = []
wd2 = []

for i in range(len(WBp_up_e)):
    wymax.append(max(np.abs(WBp_up_e)[i], np.abs(WBp_down_e)[i]))
    wymin.append(min(np.abs(WBp_up_e)[i], np.abs(WBp_down_e)[i]))
    wyavg.append((np.abs(WBp_up_e)[i] + np.abs(WBp_down_e)[i]) / 2)
    wd1.append(wymax[i] - wyavg[i])
    wd2.append(wyavg[i] - wymin[i])

wyerror = []
wyerror.append(wd1)
wyerror.append(wd2)

Kyavg = []
Kymax = []
Kymin = []
Kd1 = []
Kd2 = []

for i in range(len(KBp_up_e)):
    Kymax.append(max(np.abs(KBp_up_e)[i], np.abs(KBp_down_e)[i]))
    Kymin.append(min(np.abs(KBp_up_e)[i], np.abs(KBp_down_e)[i]))
    Kyavg.append((np.abs(KBp_up_e)[i] + np.abs(KBp_down_e)[i]) / 2)
    Kd1.append(Kymax[i] - Kyavg[i])
    Kd2.append(Kyavg[i] - Kymin[i])

Kyerror = []
Kyerror.append(Kd1)
Kyerror.append(Kd2)


omega_c = 8.246190999498149e9 * 2 * np.pi
kcint = 12.429387518053709e6 * 2 * np.pi
kcext = 11.783464821423435e6 * 2 * np.pi
kc = kcint + kcext

kA = 1.0021259402425182e6 * 2 * np.pi
gA = 30.923698690048464e6 * 2 * np.pi

kB = 2.026588034397236e6 * 2 * np.pi
gB = 4.954180265548075e6 * 2 * np.pi

wa = np.linspace(8, 8.4, 400001)
omega_As = wa * 1e9 * 2 * np.pi
omega_Bs = omega_c + np.linspace(-210, 200, 1001) * 1e6 * 2 * np.pi

Kplus = []
Kminus = []

Keplus = []
Keminus = []

Gplus = []
Gminus = []

Wplus = []
Wminus = []

Sin = []
Cos = []

Zero = []

for i, omega_A in enumerate(omega_As):
    Delta = omega_c - omega_A

    middle = np.sqrt(Delta ** 2 + 4 * gA ** 2)

    sintheta = np.sqrt((-Delta + middle) / (2 * middle))
    costheta = np.sqrt((Delta + middle) / (2 * middle))

    Sin.append(sintheta)
    Cos.append(costheta)

    kplus = costheta ** 2 * kc + sintheta ** 2 * kA
    kminus = sintheta ** 2 * kc + costheta ** 2 * kA

    keplus = costheta ** 2 * kcext
    keminus = sintheta ** 2 * kcext

    gplus = gB * costheta
    gminus = gB * sintheta

    wplus = (omega_c + omega_A) / 2 + middle / 2
    wminus = (omega_c + omega_A) / 2 - middle / 2

    Kplus.append(kplus / (1e6 * 2 * np.pi))
    Kminus.append(kminus / (1e6 * 2 * np.pi))

    Keplus.append(keplus / (1e6 * 2 * np.pi))
    Keminus.append(keminus / (1e6 * 2 * np.pi))

    Gplus.append(gplus / (1e6 * 2 * np.pi))
    Gminus.append(gminus / (1e6 * 2 * np.pi))

    Wplus.append(wplus / (1e9 * 2 * np.pi))
    Wminus.append(wminus / (1e9 * 2 * np.pi))

WBp_up_s = []
WBp_down_s = []

KBp_up_s = []
KBp_down_s = []


#计算有干涉的理论值
for i in range(len(wa)):
    Wp = Wplus[i] * 1e9 * 2 * np.pi
    Kp = Kplus[i] * 1e6 * 2 * np.pi
    gp = Gplus[i] * 1e6 * 2 * np.pi
    WB = Wp
    chi_b = WB - 1j * kB / 2
    chi_p = Wp - 1j * Kp / 2

    qian = (chi_b + chi_p) / 2
    hou = np.sqrt((chi_b - chi_p) ** 2 / 4 + gp ** 2)

    middle_p = qian + hou
    middle_m = qian - hou

    WBp_up_s.append((np.real(middle_p) - Wp) / (1e6 * 2 * np.pi))
    WBp_down_s.append((np.real(middle_m) - Wp) / (1e6 * 2 * np.pi))

    KBp_up_s.append(-np.imag(middle_p) / (1e6 * 2 * np.pi))
    KBp_down_s.append(-np.imag(middle_m) / (1e6 * 2 * np.pi))

WBp_up_s1 = []
WBp_down_s1 = []

KBp_up_s1 = []
KBp_down_s1 = []

#计算没干涉的理论值
for i in range(len(wa)):
    Wp = Wplus[i] * 1e9 * 2 * np.pi
    Kp = Kplus[196067] * 1e6 * 2 * np.pi
    gp = Gplus[i] * 1e6 * 2 * np.pi

    WB = Wp

    chi_b = WB - 1j * kB / 2
    chi_p = Wp - 1j * Kp / 2

    qian = (chi_b + chi_p) / 2
    hou = np.sqrt((chi_b - chi_p) ** 2 / 4 + gp ** 2)

    middle_p = qian + hou
    middle_m = qian - hou

    WBp_up_s1.append((np.real(middle_p) - Wp) / (1e6 * 2 * np.pi)) #MHz
    WBp_down_s1.append((np.real(middle_p) - Wp) / (1e6 * 2 * np.pi)) #MHz

    KBp_up_s1.append(-np.imag(middle_p) / (1e6 * 2 * np.pi))
    KBp_down_s1.append(-np.imag(middle_p) / (1e6 * 2 * np.pi))

Simulation_chazhi=[]
Simulation_chazhi_slope=[]

f_chazhi=[]
f_chazhi_slope=[]
#计算两者的理论差值
for i in range(len(wa)):
    if i>100000:
        Simulation_chazhi.append(WBp_up_s[i]-WBp_up_s1[196067+196067-i])
        f_chazhi.append(wa[i]-wa[196067])

for i in range(len(Simulation_chazhi)-1):
    f_chazhi_slope.append(f_chazhi[i])
    Simulation_chazhi_slope.append(Simulation_chazhi[i+1]-Simulation_chazhi[i])

Kpluse = []
Wpluse = []
Gpluse =[]

Kpluses = []
Wpluses = []
Gpluses =[]

WBp_down_es=[]
#计算实验数据和无干涉的对应理论值
for i, omega_A in enumerate(WAE):
    Delta = omega_c - omega_A* 1e9 * 2 * np.pi
    middle = np.sqrt(Delta ** 2 + 4 * gA ** 2)
    sintheta = np.sqrt((-Delta + middle) / (2 * middle))
    costheta = np.sqrt((Delta + middle) / (2 * middle))
    kplus = costheta ** 2 * kc + sintheta ** 2 * kA
    gplus = gB * costheta
    Kpluse.append(kplus / (1e6 * 2 * np.pi))
    Gpluse.append(gplus / (1e6 * 2 * np.pi))
    Wpluse.append(((omega_c+omega_A* 1e9 * 2 * np.pi)/2+middle/2) / (1e9 * 2 * np.pi))


    Deltas = omega_c - (2*wa[196067]-omega_A) * 1e9 * 2 * np.pi

    # print(omega_A)
    # print(2*Wplus[196067]-omega_A)
    middles = np.sqrt(Deltas ** 2 + 4 * gA ** 2)
    sinthetas = np.sqrt((-Deltas + middles) / (2 * middles))
    costhetas = np.sqrt((Deltas + middles) / (2 * middles))
    kpluss = costhetas ** 2 * kc + sinthetas ** 2 * kA
    gpluss= gB * costhetas
    Kpluses.append(kpluss / (1e6 * 2 * np.pi))
    Gpluses.append(gpluss / (1e6 * 2 * np.pi))
    Wpluses.append(((omega_c + (2*wa[196067]-omega_A) * 1e9 * 2 * np.pi)/2 + middles / 2) / (1e9 * 2 * np.pi))

# print(Kplus[196067])
# print(Wpluses)
Experiment_show=[]
Simulation_cha=[]

#计算实验和理论的差值
for i in range(len(WAE)):
    #实验值计算
    Wp = Wpluse[i] * 1e9 * 2 * np.pi
    Kp = Kpluse[i] * 1e6 * 2 * np.pi
    gp = Gpluse[i] * 1e6 * 2 * np.pi
    WB = Wp
    chi_b = WB - 1j * kB / 2
    chi_p = Wp - 1j * Kp / 2
    qian = (chi_b + chi_p) / 2
    hou = np.sqrt((chi_b - chi_p) ** 2 / 4 + gp ** 2)
    middle_p = qian + hou
    middle_m = qian - hou
    jizhun1=(np.real(middle_p) - Wp) / (1e6 * 2 * np.pi)
    jizhun2 = (np.real(middle_p) - Wp) / (1e6 * 2 * np.pi)
    bijiao1 = np.abs(np.abs(WBp_up_e)[i] - jizhun1)
    bijiao2 = np.abs(np.abs(WBp_down_e)[i] - jizhun2)

    #无干涉理论值计算
    Wps = Wpluses[i] * 1e9 * 2 * np.pi
    Kps = Kplus[196067] * 1e6 * 2 * np.pi
    gps = Gpluses[i] * 1e6 * 2 * np.pi
    WBs = Wps
    chi_bs = WBs - 1j * kB / 2
    chi_ps = Wps - 1j * Kps / 2
    qians = (chi_bs + chi_ps) / 2
    hous = np.sqrt((chi_bs - chi_ps) ** 2 / 4 + gps ** 2)
    middle_ps = qians + hous
    jizhun1s = (np.real(middle_ps) - Wps) / (1e6 * 2 * np.pi)
    # print(np.real(middle_ps))
    # print((middle_ps))
    # print(Wps)
    # print(jizhun1s)
    # print(np.abs(WBp_up_e)[i])
    if bijiao1>bijiao2:
        Experiment_show.append(np.abs(WBp_down_e)[i])
        Simulation_cha.append(np.abs(WBp_down_e)[i]-jizhun1s)
    if bijiao2>bijiao1:
        Experiment_show.append(np.abs(WBp_up_e)[i])
        Simulation_cha.append(np.abs(WBp_up_e)[i]-jizhun1s)

    # Simulation_cha_up1 = []
    # Simulation_cha_down1 = []
    # WBp_up_s1.append((np.real(middle_p) - Wp) / (1e6 * 2 * np.pi))  # MHz
    # WBp_down_s1.append((np.real(middle_m) - Wp) / (1e6 * 2 * np.pi))  # MHz
# print(Kplus[196067])
# print(Gplus[196067])
# for i in range(len(WAE)):
# 差和商


WDPLC=[]
WDPSC=[]
for i in range(len(Wplus)):
    WDPLC.append((Wplus[i]-Wplus[196067])*1e3)
    WDPSC.append(-Wplus[i]+Wplus[196067])

# print((WAE))
# print((WAE-wa[196067]))
# print((WAE-wa[196067])/wa[196067])
# print(Experiment_show)

# #########ehance 数值对比图
# plt.figure(figsize=(6, 6))
# # # plt.plot(-((wa - wa[196067])/wa[196067]), WBp_up_s1, '--', label=r'$|\Delta_{ni}|/2\pi$')
# # # plt.plot(((wa - wa[196067])/wa[196067]), WBp_up_s, '--', label=r'$|\Delta_{i}|/2\pi$,Sim')
# # # plt.plot(((wa - wa[196067])/wa[196067]), WDPLC, '--', label=r'$|\Delta_{DP}|/2\pi$,Sim')
# #
# # # plt.plot(((wa - wa[196067])/wa[196067]), Gplus, '--', label=r'$g_+/2\pi$,Sim')
#
# # plt.errorbar(((WAE - wa[196067])/wa[196067])*1e2, wyavg/Wplus[196067], wyerror/Wplus[196067], marker='s', mec='k', linestyle='none', mew=1, ms=10, capthick=3,
# #              capsize=6,label=r'$\kappa_A\neq\kappa_c$,Exp')
# # plt.errorbar(((WAE - wa[196067])/wa[196067]), wyavg, wyerror, marker='o', mec='k', linestyle='none', mew=1, ms=7, capthick=3,
# #              capsize=6,label=r'$|\Delta_{c}|$,Exp')
# # plt.xlim(((0.001/wa[196067]), (0.1/wa[196067])))
# # plt.ylim((-1, 3))
# # plt.scatter(((WAE - wa[196067])/wa[196067]), wymax,s=50,facecolors='blue')
# # plt.scatter(((WAE - wa[196067])/wa[196067]), wymin,s=50,facecolors='red')
# # plt.scatter(((WAE - wa[196067])/wa[196067]), Experiment_show,s=150,facecolors='green',label=r'$|\Delta_{i}|/2\pi$,Exp')
# #
# # plt.plot(((f_chazhi)/wa[196067]), Simulation_chazhi, '--',color='red', label=r'Sim')
# # plt.scatter(((WAE - wa[196067])/wa[196067]), Simulation_cha,s=150,facecolors='green',label=r'Exp')
# # print(max(Simulation_chazhi))
# # index_need=Simulation_chazhi.index(max(Simulation_chazhi))
# # print(f_chazhi[index_need]/wa[196067])
# #
# plt.plot(-((wa - wa[196067])*1e3), WBp_up_s1, '--', label=r'$|\Delta_{ni}|/2\pi$')
# plt.plot(((wa - wa[196067])*1e3), WBp_up_s, '--', label=r'$|\Delta_{i}|/2\pi$,Sim')
# plt.scatter(((WAE - wa[196067])*1e3),   Experiment_show,s=150,facecolors='green',label=r'$|\Delta_{i}|/2\pi$,Exp')
#
# # #
# # plt.xlim(((-0.001/wa[196067]), (0.1/wa[196067])))
# plt.xlim(-1,100)
#
# # plt.ylim((-0.1, 0.75))
# plt.ylim((-0.1, 2.5))
# plt.legend(loc=4,fontsize=16)
# #
# # plt.xlim(((0.005/wa[196067]), (0.1/wa[196067])))
# # plt.ylim((0.6, 2.5))
# #
# # plt.xscale('log')
# # plt.yscale('log')
#
# plt.xlabel(r'$|\delta_{A,EP}|$')
# plt.ylabel(r'$|\Delta|//\omega_{+,EP}$[MHz]')
# plt.show()
#
# index=[196067]
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\wa sim.txt',wa)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\wa exp.txt',WAE)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\delta_i exp.txt',Experiment_show)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\delta_ni sim.txt',WBp_up_s1)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\delta_i sim.txt',WBp_up_s)
# np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(1)\ep index.txt',index)


##### 总的频率对比
Wsum=[]
Wsum1=[]
# print(len(WBp_up_s))
# print(len(Wplus))
# print(len(WBp_up_s1))
for i in range(len(Wplus)):
    # Wsum.append((WBp_up_s[i]*1e6+np.abs(Wplus[i]-Wplus[196067])*1e9)/1e9*1e3)
    # Wsum1.append((WBp_up_s1[i]*1e6 + np.abs(Wplus[i]-Wplus[196067])*1e9)/1e9*1e3)
    Wsum.append((WBp_up_s[i] * 1e6 ) / 1e9 * 1e3)
    Wsum1.append((WBp_up_s1[i] * 1e6  ) / 1e9 * 1e3)

Wsume=[]
# print(Experiment_show)
print(Wpluse)
print(len(Wpluse))
for i in range(len(WAE)):
    Wsume.append((Experiment_show[i]*1e6+np.abs(Wpluse[i]-Wplus[196067])*1e9)/1e9*1e3)

WDPL=[]
WDPS=[]
for i in range(len(Wplus)):
    # WDPL.append(Wplus[196067]+np.abs(Wplus[i]-Wplus[196067])/2)
    # WDPS.append(Wplus[196067]-np.abs(Wplus[i]-Wplus[196067])/2)
    WDPL.append( np.abs(Wplus[i] - Wplus[196067])*1e3)
    WDPS.append( - np.abs(Wplus[i] - Wplus[196067])*1e3)

WaDPL = []
WaDPS = []
for i in range(len(wa)):
    # WDPL.append(Wplus[196067]+np.abs(Wplus[i]-Wplus[196067])/2)
    # WDPS.append(Wplus[196067]-np.abs(Wplus[i]-Wplus[196067])/2)
    WaDPL.append(np.abs(wa[i] - wa[196067]) * 1e3 )
    WaDPS.append(- np.abs(wa[i] - wa[196067]) * 1e3)

# WDPLL=[]
# WDPLS=[]
# for i in range(len(Wplus)):
#     WDPLL.append(Wplus[196067]+np.abs(wa[i]-wa[196067])/2)
#     WDPLS.append(Wplus[196067]-np.abs(wa[i]-wa[196067])/2)
# print(len(Experiment_show))
# print(len(Wpluse))

# print(len(Wsum))
# print(len(Wsum1))
# print(min(-((Wplus - Wplus[196067])*1e3)))
# print(max(-((Wplus - Wplus[196067])*1e3)))
# #
plt.figure(figsize=(6, 6))
# plt.plot(-((Wplus - Wplus[196067])*1e3), Wsum1, '--', label=r'$|\delta_{EP,ni}|/2\pi$')
# plt.plot(((Wplus - Wplus[196067])*1e3), Wsum, '--', label=r'$|\delta_{EP,i}|/2\pi$,Sim')
# plt.plot(((Wplus - Wplus[196067])*1e3), WDPL, '--', label=r'$|\delta_{DP}|/2\pi$,Sim')
# # plt.plot(((Wplus - Wplus[196067])*1e3), WDPS, '--', label=r'$|\Delta_{DPS}|/2\pi$,Sim')
# # plt.plot(((Wplus - Wplus[196067])*1e3), WDPLL, '--', label=r'$|\Delta_{DPLL}|/2\pi$,Sim')
# # plt.plot(((Wplus - Wplus[196067])*1e3), WDPLS, '--', label=r'$|\Delta_{DPLS}|/2\pi$,Sim')

# plt.scatter(((Wpluse - Wplus[196067])*1e3), Wsume,s=150,facecolors='green',label=r'$|\delta_{EP,i}|/2\pi$,Exp')
# plt.xlim(((-0.001/wa[196067]), (0.1/wa[196067])))

#
plt.plot(-((wa - wa[196067])*1e3), Wsum1, '--', label=r'$|\Delta_{ni}|/2\pi$')
plt.plot(((wa - wa[196067])*1e3), Wsum, '--', label=r'$|\Delta_{i}|/2\pi$')
plt.plot(((wa - wa[196067])*1e3), WDPL, '--', color='black',label=r'$|\Delta_{DP}|/2\pi$')
# plt.plot(((wa - wa[196067])*1e3),WaDPL, '--', label=r'$|\delta_{aDP}|/2\pi$')

# plt.plot(((Wplus - Wplus[196067])*1e3), WDPS, '--', label=r'$|\Delta_{DPS}|/2\pi$,Sim')
# plt.plot(((Wplus - Wplus[196067])*1e3), WDPLL, '--', label=r'$|\Delta_{DPLL}|/2\pi$,Sim')
# plt.plot(((Wplus - Wplus[196067])*1e3), WDPLS, '--', label=r'$|\Delta_{DPLS}|/2\pi$,Sim')
#
# plt.scatter(((WAE - wa[196067])*1e3), Wsume,s=150,facecolors='green',label=r'$|\delta_{EP,i}|/2\pi$,Exp')

# plt.xscale('log')
# plt.yscale('log')
# plt.xlim(0.001, 2)
# plt.ylim((0, 1))

plt.xlim(-0.01, 2)
plt.ylim((0, 0.5))
# plt.ylim((-0.1, 0.75))

plt.legend(loc=4,fontsize=16)
plt.xlabel(r'$|\delta_{A,EP}|$')
plt.ylabel(r'$|\Delta|//\omega_{+,EP}$[MHz]')
plt.show()

index=[196067]
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(2)\wa sim.txt',wa)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(2)\delta_i sim.txt',Wsum)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(2)\delta_ni sim.txt',Wsum1)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(2)\delta_dp sim.txt',WDPL)
np.savetxt(r'C:\Users\AORUS\OneDrive\桌面\EP and sensitivity data\data(2)\ep index.txt',index)

# target=40000
# print(Wsum1[40000-target])
# print(Wsum[target])
# print(WDPL[target])


######差值对比




##斜率对比
# waless=[]
# waless1=[]
# xielv=[]
# xielv1=[]
# #计算理论斜率
# for i in range(len(wa)-1):
#     ff=(wa[i+1]-wa[i])*1e9
#     xie=(WBp_up_s[i+1]-WBp_up_s[i])*1e6
#     xie1=(WBp_up_s1[i]-WBp_up_s1[i+1])*1e6
#
#     waless.append(wa[i+1])
#     waless1.append(wa[i])
#     xielv.append(xie/ff*wa[196067]*1e9)
#     xielv1.append(xie1/ff*wa[196067]*1e9)
#
#     if (xie==0)&(i>19700):
#         print(i)
#
#
# WAEless=[]
# xielvE=[]
# #计算实验斜率
# for i in range(len(WAE)-1):
#     ww=(WAE[i+1]-WAE[i])*1e9
#     xie=(Experiment_show[i+1]-Experiment_show[i])*1e6
#
#     WAEless.append(WAE[i+1])
#     xielvE.append(xie/ww*wa[196067]*1e9)
#
#斜率对比图
#
# plt.figure(figsize=(4, 9))
# plt.plot(-((waless1 - wa[196067])/wa[196067]), np.abs(xielv1)/1e6, '--', label=r'$|\Delta_{ni}|/2\pi$')
# plt.plot(((waless - wa[196067])/wa[196067]), np.abs(xielv)/1e6, '--', label=r'$|\Delta_{i}|/2\pi$,Sim')
# plt.scatter(((WAEless - wa[196067])/wa[196067]), np.abs(xielvE)/1e6,s=150,facecolors='green',label=r'$|\Delta_{i}|/2\pi$,Exp')
#
# plt.xlim(((0.001/wa[196067]), (0.1/wa[196067])))
# # plt.ylim((-0.00001, 0.0005))
# plt.ylim((-100,2000))
# plt.legend(loc=1,fontsize=16)
#
# plt.xlabel(r'$|\delta_{A,EP}|$')
# plt.ylabel(r'$|\Delta|//\omega_{+,EP}$[MHz]')
# plt.show()
#
# print(wa[196067])
# print(max(WBp_up_s))

