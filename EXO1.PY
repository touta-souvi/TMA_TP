import numpy as np
import matplotlib.pyplot as plt

# Paramètres
f0 = 10        # fréquence (Hz)
A = 1          # amplitude
phi = 0        # phase
fs = 100       # fréquence d'échantillonnage
T = 1          # durée (s)

t = np.arange(0, T, 1/fs)
x = A * np.sin(2*np.pi*f0*t + phi)

plt.plot(t, x)
plt.title("Signal sinusoïdal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# 1_2
bruit = np.random.normal(0, 0.3, len(t))
y = x + bruit

plt.plot(t, x, label="Signal pur")
plt.plot(t, y, label="Signal bruité")
plt.legend()
plt.show()

# 1_3
rect = np.zeros(100)
rect[20:40] = 1

conv = np.convolve(rect, rect)

plt.plot(conv)
plt.title("Convolution du signal porte")
plt.show()