from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

fs, signal = wavfile.read("audio.wav")

# Si le signal est stéréo, on garde un seul canal
if len(signal.shape) > 1:
    signal = signal[:, 0]

print("Fréquence d'échantillonnage :", fs)

signal_sous = signal[::10]

plt.specgram(signal, Fs=fs)
plt.title("Spectrogramme original")
plt.show()

plt.specgram(signal_sous, Fs=fs/10)
plt.title("Spectrogramme sous-échantillonné")
plt.show()
# 3-2
import cv2

img = cv2.imread("image.jpg", 0)

# 2 bits (4 niveaux)
img_2bits = (img // 64) * 64

# 1 bit (2 niveaux)
img_1bit = (img // 128) * 128

plt.imshow(img_2bits, cmap="gray")
plt.title("Quantification 2 bits")
plt.show()

plt.imshow(img_1bit, cmap="gray")
plt.title("Quantification 1 bit")
plt.show()