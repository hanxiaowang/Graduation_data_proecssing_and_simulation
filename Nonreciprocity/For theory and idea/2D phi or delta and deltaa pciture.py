import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
import os
import json




### phi

max_deltaa=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\max_deltaa.txt')
min_deltaa=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\min_deltaa.txt')
max_deltaa_phi=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\max_deltaa_phi.txt')
min_deltaa_phi=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\min_deltaa_phi.txt')
max_Iso=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\max_Iso.txt')
min_Iso=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\min_Iso.txt')
max_S12=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\max_S12.txt')
min_S12=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\min_S12.txt')
max_S21=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\max_S21.txt')
min_S21=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\phi\min_S21.txt')


plt.figure(figsize=(12, 6))
axes1 = plt.subplot(111)
axes1.plot(max_deltaa_phi,max_deltaa,'o',linewidth=5,label=r'$max$',alpha=0.5)
axes1.plot(min_deltaa_phi,min_deltaa,'o',linewidth=5,label=r'$min$',alpha=0.5)

# axes1.plot(max_deltaa_phi,max_Iso,'o',linewidth=5,label=r'$max$',alpha=0.5)
# axes1.plot(min_deltaa_phi,min_Iso,'o',linewidth=5,label=r'$min$',alpha=0.5)
axes1.set_xlabel(r'$\delta$',fontsize=20)
axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
plt.tick_params(labelsize=20)
plt.legend(loc=4,prop={'family':'Cambria','size':20})
plt.show()

max_index = []
min_index = []
max_iso=[]
min_iso=[]
max_phi=[]
min_phi=[]
max_f=[]
min_f=[]
max_s12=[]
min_s12=[]
max_s21=[]
min_s21=[]
# max_index = list(ISO).index(max(ISO))
# min_index = list(ISO).index(min(ISO))
maxvalue=max(max_Iso)
minvalue=min(min_Iso)

for i in range(len(max_deltaa_phi)):
    if max_Iso[i]==maxvalue:
        max_index.append(i)
        max_iso.append(max_Iso[i])
        max_phi.append(max_deltaa_phi[i])
        max_f.append((8.25e9-max_deltaa[i])/1e6)
        max_s12.append(max_S12[i])
        max_s21.append(max_S21[i])


for i in range(len(min_deltaa_phi)):
    if min_Iso[i]==minvalue:
        min_index.append(i)
        min_iso.append(min_Iso[i])
        min_phi.append(min_deltaa_phi[i])
        min_f.append((8.25e9-min_deltaa[i])/1e6)
        min_s12.append(min_S12[i])
        min_s21.append(min_S21[i])

print('max value')
print(max_index)
print(max_iso)
print(max_phi)
print(max_f)
print(max_s12)
print(max_s21)

print('min value')
print(min_index)
print(min_iso)
print(min_phi)
print(min_f)
print(min_s12)
print(min_s21)

#
# # zero_max_index = []
# # zero_min_index = []
# # zero_max_iso=[]
# # zero_min_iso=[]
# # zero_max_phi=[]
# # zero_min_phi=[]
# # zero_max_f=[]
# # zero_min_f=[]
# # # max_index = list(ISO).index(max(ISO))
# # # min_index = list(ISO).index(min(ISO))
# # maxvalue=max(max_Iso)
# # minvalue=min(min_Iso)
# # print(max_deltaa)
# # for i in range(len(max_deltaa_phi)):
# #     if (8.25e9-max_deltaa[i])==0:
# #         # print(max_deltaa[i])
# #         zero_max_index.append(i)
# #         zero_max_iso.append(max_Iso[i])
# #         zero_max_phi.append(max_deltaa_phi[i])
# #         zero_max_f.append((8.25e9-max_deltaa[i])/1e6)
# #
# #
# # for i in range(len(min_deltaa_phi)):
# #     if (8.25e9-min_deltaa[i])==0:
# #         zero_min_index.append(i)
# #         zero_min_iso.append(min_Iso[i])
# #         zero_min_phi.append(min_deltaa_phi[i])
# #         zero_min_f.append((8.25e9-min_deltaa[i])/1e6)
# #
# # print('max value')
# # print(zero_max_index)
# # print(zero_max_iso)
# # print(zero_max_phi)
# # print(zero_max_f)
# #
# # print('min value')
# # print(zero_min_index)
# # print(zero_min_iso)
# # print(zero_min_phi)
# # print(zero_min_f)


### delta

# max_deltaa=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\max_deltaa.txt')
# min_deltaa=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\min_deltaa.txt')
# max_deltaa_delta=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\max_deltaa_delta.txt')
# min_deltaa_delta=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\min_deltaa_delta.txt')
# max_Iso=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\max_Iso.txt')
# min_Iso=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\min_Iso.txt')
#
# max_S12=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\max_S12.txt')
# min_S12=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\min_S12.txt')
# max_S21=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\max_S21.txt')
# min_S21=np.loadtxt(r'C:\Users\AORUS\OneDrive\桌面\cpb nonreciprocity data\delta\min_S21.txt')
#
# plt.figure(figsize=(12, 6))
# axes1 = plt.subplot(111)
# # axes1.plot(max_deltaa_delta,max_deltaa,'o',linewidth=5,label=r'$max$',alpha=0.5)
# # axes1.plot(min_deltaa_delta,min_deltaa,'o',linewidth=5,label=r'$min$',alpha=0.5)
#
# axes1.plot(max_deltaa_delta,max_Iso,'o',linewidth=5,label=r'$max$',alpha=0.5)
# axes1.plot(min_deltaa_delta,min_Iso,'o',linewidth=5,label=r'$min$',alpha=0.5)
# axes1.set_xlabel(r'$\delta$',fontsize=20)
# axes1.set_ylabel(r'$S$ [dB]',fontsize=20)
# plt.tick_params(labelsize=20)
# plt.legend(loc=4,prop={'family':'Cambria','size':20})
# plt.show()
#
# max_index = []
# min_index = []
# max_iso=[]
# min_iso=[]
# max_delta=[]
# min_delta=[]
# max_f=[]
# min_f=[]
# max_s12=[]
# min_s12=[]
# max_s21=[]
# min_s21=[]
# # max_index = list(ISO).index(max(ISO))
# # min_index = list(ISO).index(min(ISO))
# maxvalue=max(max_Iso)
# minvalue=min(min_Iso)
#
# for i in range(len(max_deltaa_delta)):
#     if max_Iso[i]==maxvalue:
#         max_index.append(i)
#         max_iso.append(max_Iso[i])
#         max_delta.append(max_deltaa_delta[i])
#         max_f.append((8.25e9-max_deltaa[i])/1e6)
#         max_s12.append(max_S12[i])
#         max_s21.append(max_S21[i])
#
# for i in range(len(min_deltaa_delta)):
#     if min_Iso[i]==minvalue:
#         min_index.append(i)
#         min_iso.append(min_Iso[i])
#         min_delta.append(min_deltaa_delta[i])
#         min_f.append((8.25e9-min_deltaa[i])/1e6)
#         min_s12.append(min_S12[i])
#         min_s21.append(min_S21[i])
#
# print('max value')
# print(max_index)
# print(max_iso)
# print(max_delta)
# print(max_f)
# print(max_s12)
# print(max_s21)
#
# print('min value')
# print(min_index)
# print(min_iso)
# print(min_delta)
# print(min_f)
# print(min_s12)
# print(min_s21)
# # zero_max_index = []
# # zero_min_index = []
# # zero_max_iso=[]
# # zero_min_iso=[]
# # zero_max_phi=[]
# # zero_min_phi=[]
# # zero_max_f=[]
# # zero_min_f=[]
# # # max_index = list(ISO).index(max(ISO))
# # # min_index = list(ISO).index(min(ISO))
# # maxvalue=max(max_Iso)
# # minvalue=min(min_Iso)
# # print(max_deltaa)
# # for i in range(len(max_deltaa_phi)):
# #     if (8.25e9-max_deltaa[i])==0:
# #         # print(max_deltaa[i])
# #         zero_max_index.append(i)
# #         zero_max_iso.append(max_Iso[i])
# #         zero_max_phi.append(max_deltaa_phi[i])
# #         zero_max_f.append((8.25e9-max_deltaa[i])/1e6)
# #
# #
# # for i in range(len(min_deltaa_phi)):
# #     if (8.25e9-min_deltaa[i])==0:
# #         zero_min_index.append(i)
# #         zero_min_iso.append(min_Iso[i])
# #         zero_min_phi.append(min_deltaa_phi[i])
# #         zero_min_f.append((8.25e9-min_deltaa[i])/1e6)
# #
# # print('max value')
# # print(zero_max_index)
# # print(zero_max_iso)
# # print(zero_max_phi)
# # print(zero_max_f)
# #
# # print('min value')
# # print(zero_min_index)
# # print(zero_min_iso)
# # print(zero_min_phi)
# # print(zero_min_f)
