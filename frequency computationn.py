import numpy as np
import matplotlib.pyplot as plt

omega_a=8.25e9

omega_m=np.linspace(8.2,8.3,51)*1e9

g=10e6

omega_p=(omega_a+omega_m)/2+np.sqrt((omega_a-omega_m)**2/4+g**2)

# print(omega_p)

omega_mn=(omega_p*(omega_p-omega_a)-g**2)/(omega_p-omega_a)


plt.figure(figsize=(6, 6))

plt.plot(omega_m/1e9, omega_p/1e9, '--' )
plt.plot(omega_mn/1e9, omega_p/1e9, 'o' )

plt.show()