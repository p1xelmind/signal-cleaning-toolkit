import numpy as np
import matplotlib.pyplot as plt
from signal_cleaning.filters import highpass_filter

fs = 250 #Hz
f1 = 10 #Hz
f2 = 0.5 #Hz
duration = 2 #seconds
A = 1 # amplitude in arbitrary units (a.u.)
n_samples = int(duration * fs) #np.ndarray 
cutoff = 1.0 #Hz
order = 3 

t = np.linspace(0 , duration, n_samples, endpoint=False)

alpha_signal = A * np.sin(2 * np.pi * f1 * t)
baseline_drift = A * np.sin(2 * np.pi * f2 * t)

dirty_signal_with_baseline = alpha_signal + baseline_drift

cleaned_signal = highpass_filter(dirty_signal_with_baseline, cutoff, fs, order)

plt.figure()
plt.plot(t, dirty_signal_with_baseline, label="Dirty signal")
plt.plot(t, cleaned_signal, label="Clean signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal before/after")
plt.legend()
plt.show()

spectrum_dirty = np.fft.fft(dirty_signal_with_baseline)
spectrum_clean = np.fft.fft(cleaned_signal)
freqs = np.fft.fftfreq(len(cleaned_signal), 1/fs)

plt.figure()
plt.plot(freqs, np.abs(spectrum_dirty), label="Before filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Signal Spectrum: Before Filtering")
plt.xlim(0, 60)
plt.legend()
plt.show()

plt.figure()
plt.plot(freqs, np.abs(spectrum_clean), label="After filtering")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Signal Spectrum: After Filtering")
plt.xlim(0, 60)
plt.legend()
plt.show()