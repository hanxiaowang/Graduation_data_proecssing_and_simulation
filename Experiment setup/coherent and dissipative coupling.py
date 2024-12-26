import numpy as np
import matplotlib.pyplot as plt

omega_a = 8.25e9
omega_ms = np.linspace(8.2, 8.3, 10001) * 1e9
kaint = 2.58e6
kaext = 10e6
ka = kaint + kaext
gamma = 5.1e6
g_ma1 = 4e6 * 1j

g_ma2 = 10e6

omega11 = (omega_a + omega_ms) / 2 + np.sqrt((omega_a - omega_ms) ** 2 + g_ma1 ** 2) / 2
omega21 = (omega_a + omega_ms) / 2 - np.sqrt((omega_a - omega_ms) ** 2 + g_ma1 ** 2) / 2

omega12 = (omega_a + omega_ms) / 2 + np.sqrt((omega_a - omega_ms) ** 2 + g_ma2 ** 2) / 2
omega22 = (omega_a + omega_ms) / 2 - np.sqrt((omega_a - omega_ms) ** 2 + g_ma2 ** 2) / 2

plt.figure(figsize=(7, 7))
# plt.plot(omega_ms / 1e9, omega11 / 1e9, label=r'$\omega_+$', color='blue', linewidth=5)
# plt.plot(omega_ms / 1e9, omega21 / 1e9, label=r'$\omega_+$', color='red', linewidth=5)
plt.plot(omega_ms / 1e9, omega12 / 1e9, label=r'$\omega_+$', color='blue', linewidth=5)
plt.plot(omega_ms / 1e9, omega22 / 1e9, label=r'$\omega_+$', color='red', linewidth=5)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()