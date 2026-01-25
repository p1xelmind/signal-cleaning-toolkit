import numpy as np
import matplotlib.pyplot as plt

fs = 250
duration = 2
n_samples = int(fs * duration)
f = 10

t = np.linspace(0 , duration, n_samples) 

signal_alpha = np.sin(2 * np.pi * f * t)

plt.figure()
plt.plot(t, signal_alpha)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Pure 10 Hz Sinusoidal Signal (Alpha Component)")
plt.show()