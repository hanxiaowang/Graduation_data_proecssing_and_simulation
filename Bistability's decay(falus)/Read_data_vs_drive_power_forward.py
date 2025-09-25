import numpy as np
import matplotlib.pyplot as plt
import Curve_decay_func



drive_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\drive fre.txt')
drive_power=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\drive power.txt')
vna_fre=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\vna fre.txt')
Delta_omega_up=np.loadtxt(r'F:\Chirality of encycling bistability critical point(20220726-20230503)\20230407\Bistability UP change power 2D forward 23-54-37\Delta omega up.txt',delimiter=',')


# print(len(drive_fre))
# print(len(drive_power))
# print(len(vna_fre))
for i in range(len(drive_fre)):
    print(i)
    S_2D=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\S_2D.txt',delimiter=',')

    Kappa_experiment = []
    Kappa_probe_experiment = []
    Kappa_xiuzheng = []
    Kappa_probe_xiuzheng = []
    Kappa_theory = []
    Kappa_probe_theory = []

    for j in range(len(drive_power)):
        Target_index=np.where(vna_fre==8.25)[0][0]+10
        S_1D = Curve_decay_func.Rebulid_list(S_2D[:, j], Target_index)
        min_index = Curve_decay_func.Find_target_index(S_1D, min(S_1D))

        S_1D_part = S_2D[Target_index:-1, j]
        vna_fre_part = vna_fre[Target_index:-1]
        omega_t, k_int_t, k_ext_t, shift_t, kappa = Curve_decay_func.Get_decay(vna_fre_part, S_1D_part,
                                                                               vna_fre[min_index])
        Kappa_theory.append(Curve_decay_func.Find_theory_decay(vna_fre[min_index] * 1e9)[0])
        Kappa_probe_theory.append(Curve_decay_func.Find_theory_decay(vna_fre[min_index] * 1e9)[1])
        Kappa_experiment.append(kappa)
        Kappa_probe_experiment.append(k_ext_t)
        theory_S = Curve_decay_func.One_oscillator(vna_fre_part, omega_t, k_int_t, k_ext_t, shift_t)
        np.savetxt(
            f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\drive power={round(drive_power[j], 1)}mW S_experiment.txt',
            S_1D_part, fmt='%.6f')
        np.savetxt(
            f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\drive power={round(drive_power[j], 1)}mW S_theory.txt',
            theory_S, fmt='%.6f')
        np.savetxt(
            f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\drive power={round(drive_power[j], 1)}mW vna_fre_part.txt',
            vna_fre_part, fmt='%.6f')
        if j == 0:
            Kappa_xiuzheng.append(Kappa_theory[0])
            first_kappa = kappa
            chazhi = Kappa_theory[0] - first_kappa

            Kappa_probe_xiuzheng.append(Kappa_probe_theory[0])
            first_kappa_probe = k_ext_t
            chazhi_probe = Kappa_theory[0] - first_kappa_probe
        else:
            Kappa_xiuzheng.append(kappa + chazhi)
            Kappa_probe_xiuzheng.append(k_ext_t + chazhi_probe)
        fig_path = f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\drive power={round(drive_power[j], 1)}mW.png'
        plt.figure()
        plt.plot(vna_fre_part, S_1D_part, 'o', color='blue', label='exp')
        plt.plot(vna_fre_part, theory_S, '-', color='red', label='sim')
        plt.xlabel(r'$\omega_p/2\pi$ [GHz]', size=10)
        plt.ylabel(r'$S_{11}$ [dB]', size=10)
        plt.legend()
        plt.savefig(fig_path)
        plt.close()


    np.savetxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_theory.txt',Kappa_theory,fmt='%.6f')
    np.savetxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_experiment.txt',Kappa_experiment,fmt='%.6f')
    np.savetxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_xiuzheng.txt',Kappa_xiuzheng,fmt='%.6f')
    np.savetxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_probe_theory.txt',Kappa_probe_theory, fmt='%.6f')
    np.savetxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_probe_experiment.txt',Kappa_probe_experiment, fmt='%.6f')
    np.savetxt(
        f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency={drive_fre[i]}GHz\\Kappa_probe_xiuzheng.txt',Kappa_probe_xiuzheng, fmt='%.6f')


# S_2D=np.loadtxt(f'F:\\Chirality of encycling bistability critical point(20220726-20230503)\\20230407\\Bistability UP change power 2D forward 23-54-37\\drive frequency=8.184GHz\\S_2D.txt',delimiter=',')
# Kappa=[]
# Omega=[]
# Kappa_theory=[]
# for j in range(len(drive_power)):
#     S_1D=Curve_decay_func.Rebulid_list(S_2D[:,j],round(len(vna_fre)/2))
#     min_index=Curve_decay_func.Find_target_index(S_1D,min(S_1D))
#
#     S_1D_part=S_2D[round(len(vna_fre)/2):-1,j]
#     vna_fre_part=vna_fre[round(len(vna_fre)/2):-1]
#
#     kappa=Curve_decay_func.Get_decay(vna_fre_part,S_1D_part,vna_fre[min_index])
#     Omega.append((vna_fre[min_index]-8.26)*1e3)
#     Kappa_theory.append(Curve_decay_func.Find_theory_decay(vna_fre[min_index]*1e9))
#     if j==0:
#         Kappa.append(Kappa_theory[0])
#         first_kappa=kappa
#         chazhi=Kappa_theory[0]-first_kappa
#     else:
#         Kappa.append(kappa+chazhi)
# # print(Kappa_theory)
#
# print(Kappa[0])
# print(Kappa_theory[0])
# k_delta=[]
# for i in range(len(Kappa)):
#     k_delta.append(Kappa[i]-Kappa_theory[i])
#
# plt.figure(figsize=(12 , 9))
# axes1 = plt.subplot(311)
# axes1.patch.set_alpha(0)
# axes1.plot(drive_power,Kappa,'o',linewidth=3,label=r'$k_{exp}$',color='blue',alpha=0.4)
# axes1.plot(drive_power,Kappa_theory,'-',linewidth=3,label=r'$k_{sim}$',color='red',alpha=0.4)
# axes1.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
# axes1.set_ylabel(r'$\kappa/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=20)
# plt.legend(loc=0)
#
# axes2 = plt.subplot(312)
# axes2.patch.set_alpha(0)
# axes2.plot(drive_power,k_delta,'-',linewidth=3,label=r'$\delta\kappa$',color='blue',alpha=0.4)
# axes2.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
# axes2.set_ylabel(r'$\delta_\kappa/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.legend(loc=0)
#
#
# axes3 = plt.subplot(313)
# axes3.patch.set_alpha(0)
# axes3.plot(drive_power,Omega,'-',linewidth=3,label=r'$w_{exp}$',color='blue',alpha=0.4)
# axes3.set_xlabel(r'$\omega_d/2\pi$ [GHz]',fontsize=10)
# axes3.set_ylabel(r'$\omega_+/2\pi$ [MHz]',fontsize=10)
# plt.tick_params(labelsize=10)
# plt.legend(loc=0)
# plt.show()
#
#
