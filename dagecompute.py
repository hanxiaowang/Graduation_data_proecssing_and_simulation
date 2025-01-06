import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

Es=5#um/min
D0=0.09#um/min
A_taper=14
sigma=0.1*180/np.pi#rad
S=0.4
beta=0.7
eta=4.5
RN0=1.02#um/min
a_s=np.linspace(26,27,1001)
solve_set=[]
for j,a in enumerate(a_s):
    Dk=D0/np.sqrt(1+4*a**2)
    Gamma_N=1/np.sqrt(1+4*a**2)
    int_set=np.linspace(0,np.arctan(1/(2*a)),1001)
    int_final=0
    for i in range(len(int_set)):
        interval=int_set[1]-int_set[0]
        int_final=int_final+np.exp(-int_set[i]**2/(2*sigma**2))*interval
    Gamma=np.sqrt(2/(np.pi*sigma))*int_final

    Ep=(RN0*Gamma*Gamma_N)/(Gamma+eta*Gamma_N)*np.exp(-a/A_taper)
    if (beta*Dk-Ep)==0:
        print(a)
        solve_set.append(a)


print(solve_set)
