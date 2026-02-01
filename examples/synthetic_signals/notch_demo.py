import numpy as np
import matplotlib.pyplot as plt
from signal_cleaning.filters import notch_filter

fs = 250 #Hz
f1 = 10 #Hz
f2 = 50 #Hz
duration = 2 #seconds
A = 1 # amplitude in arbitrary units (a.u.)
n_samples = int(duration * fs) #np.ndarray 
order = 3 
q = 30

t = np.linspace(0 , duration, n_samples, endpoint=False)

alpha_signal = A * np.sin(2 * np.pi * f1 * t)
network_noise = A * np.sin(2 * np.pi * f2 * t)

dirty_signal_with_netnoise = alpha_signal + network_noise

cleaned_signal = notch_filter(dirty_signal_with_netnoise, f2, fs, q)

plt.figure()
plt.plot(t, dirty_signal_with_netnoise, label="Dirty signal")
plt.plot(t, cleaned_signal, label="Clean signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal before/after")
plt.legend()
plt.show()

spectrum_dirty = np.fft.fft(dirty_signal_with_netnoise)
spectrum_clean = np.fft.fft(cleaned_signal)
freqs = np.fft.fftfreq(len(cleaned_signal), 1/fs)

plt.figure()
plt.plot(freqs, np.abs(spectrum_dirty), label="Before filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Signal Spectrum: Before Filtering")
plt.xlim(0, 70)
plt.legend()
plt.show()

plt.figure()
plt.plot(freqs, np.abs(spectrum_clean), label="After filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Signal Spectrum: After Filtering")
plt.xlim(0, 70)
plt.legend()
plt.show()