
import numpy as np
import skrf as rf
import scipy
import matplotlib.pyplot as plt
from Preparation_WXH import save_file as sf
from Preparation_WXH import Plot_easy as pe




def One_oscillator(omega_p1, omega_a1, kain1, kaep1, shift=0):
    omega_p = omega_p1 * 1e9 * 2 * np.pi
    omega_a = omega_a1 * 1e9 * 2 * np.pi
    kaint = kain1 * 1e6 * 2 * np.pi
    kaext = kaep1 * 1e6 * 2 * np.pi
    ka = kaint + kaext
    R = 1 - kaext / (-1j * (omega_p - omega_a) + ka / 2)
    return (rf.mag_2_db(np.abs(R)) + shift)

def Get_decay(fre,S,omega_1_init,k1int_init=5,k1ext_init=1.087,shift_init=-57):
    omega_1_min=omega_1_init-10e-3
    omega_1_max = omega_1_init + 10e-3
    k1int_min=1
    k1int_max=10
    k1ext_min=0
    k1ext_max=1.5
    shift_min=shift_init-5
    shift_max=shift_init+5
    result1, result2 = scipy.optimize.curve_fit(One_oscillator, fre, S,
                                                p0=(omega_1_init, k1int_init, k1ext_init,shift_init),
                                                bounds=(
                                                    [omega_1_min, k1int_min, k1ext_min,shift_min],
                                                    [omega_1_max, k1int_max, k1ext_max,shift_max]),
                                                maxfev=10000)

    omega=result1[0]
    k_int = result1[1]
    k_ext = result1[2]
    kappa = k_int + k_ext
    shift=result1[3]

    return omega,k_int,k_ext,shift,kappa

def Rebulid_list(target_list,target_index):
    for i in range(len(target_list)):
        if i<target_index:
            target_list[i]=0
    return target_list

def Find_target_index(target_list,target_value):
    if type(target_list)=='list':
        index=target_list.index(target_value)[0][0]
    else:
        index=np.where(target_list==target_value)[0][0]

    return index

def Find_theory_decay(target_fre):
    omega_a=8.246e9
    ka=(3.39+2.974)*1e6
    kaprobe=1.087*1e6
    km=1.011*1e6
    g=32.649*1e6
    omega_m=target_fre-g**2/(target_fre-omega_a)
    delta=omega_a-omega_m
    Delta=np.sqrt(4*g**2+delta**2)
    costheta=np.sqrt((delta+Delta)/(2*Delta))
    sintheta=np.sqrt((-delta+Delta)/(2*Delta))

    # print(omega_m)
    # print(costheta)
    # print(sintheta)
    k_plus=costheta**2*ka+sintheta**2*km
    k_plus_probe=costheta**2*kaprobe
    # k_plus=costheta**2*km+sintheta**2*ka

    return k_plus/1e6,k_plus_probe/1e6



