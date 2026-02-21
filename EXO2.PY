import numpy as np
import matplotlib.pyplot as plt


# 2-1
fs = 44100
t = np.arange(0, 1, 1/fs)

f1 = 440
f2 = 880

signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

fft = np.fft.fft(signal)
freqs = np.fft.fftfreq(len(signal), 1/fs)

plt.plot(freqs[:len(freqs)//2], np.abs(fft[:len(fft)//2]))
plt.xlim(0, 2000)
plt.show()


# 2-2
signal_bruit = signal + 0.5*np.sin(2*np.pi*5000*t)

fft_bruit = np.fft.fft(signal_bruit)
freqs = np.fft.fftfreq(len(signal_bruit), 1/fs)

# Suppression autour de 5000 Hz
fft_bruit[np.abs(freqs - 5000) < 50] = 0
fft_bruit[np.abs(freqs + 5000) < 50] = 0

signal_filtre = np.fft.ifft(fft_bruit)

plt.plot(t[:1000], signal_filtre.real[:1000])
plt.show()


