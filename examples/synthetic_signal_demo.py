import numpy as np
import matplotlib.pyplot as plt
from signal_cleaning.filters import highpass_filter

fs = 250
duration = 2
n_samples = int(fs * duration)
f1 = 10
f2 = 0.5

t = np.linspace(0 , duration, n_samples) 

signal_alpha = np.sin(2 * np.pi * f1 * t)
baseline_drift = np.sin(2 * np.pi * f2 * t)

dirty_signal = signal_alpha + baseline_drift

'''
plt.figure()
plt.plot(t, signal_alpha, label="Alpha (10 Hz)")
plt.plot(t, baseline_drift, label="Baseline drift (0.5 Hz)")
plt.plot(t, dirty_signal, label="Dirty signal")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Dirty Signal")
plt.legend()
plt.show()
'''

cutoff = 1.0
order = 3

filtered_signal = highpass_filter(dirty_signal, cutoff, fs, order)

'''
plt.figure()
plt.plot(t, filtered_signal, label="Filtered Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("High-pass filtered signal (cutoff = 1 Hz)")
plt.legend()
plt.show()

spectrum = np.fft.fft(dirty_signal)
freqs = np.fft.fftfreq(len(dirty_signal), 1/fs)
plt.figure()
plt.plot(freqs, abs(spectrum))
plt.xlabel("Freqs")
plt.ylabel("Spectrum")
plt.title("Inspection")
plt.show()
'''

f3 = 50
network_noise = np.sin(2 * np.pi * f3 * t)

dirty_signal_2 = dirty_signal + network_noise
plt.figure()
plt.plot(t, dirty_signal_2, label="Dirty signal 2 (with network_noise and baseline drift)")
plt.plot(t, network_noise, label="Network noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Ditry Signal")
plt.legend()
plt.show()

spectrum_2 = np.fft.fft(network_noise)
freqs_2 = np.fft.fftfreq(len(network_noise), 1/fs)
plt.figure()
plt.plot(freqs_2, abs(spectrum_2))
plt.xlabel("Freqs")
plt.ylabel("Spectrum")
plt.title("Inspection")
plt.show()