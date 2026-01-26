import numpy as np
import matplotlib.pyplot as plt

fs = 250
duration = 2
n_samples = int(fs * duration)
f1 = 10
f2 = 0.5

t = np.linspace(0 , duration, n_samples) 

signal_alpha = np.sin(2 * np.pi * f1 * t)
baseline_drift = np.sin(2 * np.pi * f2 * t)

dirty_signal = signal_alpha + baseline_drift

plt.figure()
plt.plot(t, signal_alpha, label="Alpha (10 Hz)")
plt.plot(t, baseline_drift, label="Baseline drift (0.5 Hz)")
plt.plot(t, dirty_signal, label="Dirty signal")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Dirty Signal")
plt.legend()
plt.show()