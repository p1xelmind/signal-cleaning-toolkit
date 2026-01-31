import numpy as np
import matplotlib.pyplot as plt
from signal_cleaning.filters import highpass_filter, notch_filter, lowpass_filter
import mne


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

cutoff_1 = 1.0
order = 3

filtered_signal = highpass_filter(dirty_signal, cutoff_1, fs, order)

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
"""
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
"""

q = 30
cleaned_siganl = notch_filter(dirty_signal_2, f3, fs, q)

super_clean = notch_filter(filtered_signal, f3, fs, q)

"""
plt.figure()
plt.plot(t, dirty_signal_2, label="Dirty signal 2 (with network_noise and baseline drift)")
plt.plot(t, cleaned_siganl, label="Cleaned signal")
plt.plot(t, super_clean, label="Super cleaned signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signal")
plt.legend()
plt.show()

spectrum_full_dirty = np.fft.fft(dirty_signal_2)
freqs = np.fft.fftfreq(len(dirty_signal_2), 1/fs)
plt.figure()
plt.plot(freqs, abs(spectrum_full_dirty))
plt.xlabel("Freqs")
plt.ylabel("Spectrum")
plt.title("Inspection")
plt.show()

spectrum_full_clean = np.fft.fft(super_clean)
freqs = np.fft.fftfreq(len(super_clean), 1/fs)
plt.figure()
plt.plot(freqs, abs(spectrum_full_clean))
plt.xlabel("Freqs")
plt.ylabel("Spectrum")
plt.title("Inspection")
plt.show()
"""

white_noise = np.random.normal(loc=0.0, scale=1.0, size=n_samples)
ultra_dirty_signal = dirty_signal_2 + white_noise

"""
plt.figure()
plt.plot(t, white_noise, label="White noise")
plt.plot(t, ultra_dirty_signal, label="Ultra Dirty Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Dirty Signal")
plt.legend()
plt.show()
"""

cutoff_2 = 15.0

step_1 = highpass_filter(ultra_dirty_signal, cutoff_1, fs, order)
step_2 = notch_filter(step_1, f3, fs, q)
fully_cleaned_signal = lowpass_filter(step_2, cutoff_2, fs, order)

"""
plt.figure()
plt.plot(t, ultra_dirty_signal, label="Full dirty signal")
plt.plot(t, fully_cleaned_signal, label="Fully cleaned signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Signals before and after")
plt.legend()
plt.show()
"""

spectrum_clean_signal = np.fft.fft(fully_cleaned_signal)
freqs_clean_signal = np.fft.fftfreq(len(fully_cleaned_signal), 1/fs)
plt.figure()
plt.plot(freqs_clean_signal, np.abs(spectrum_clean_signal))
plt.xlim(0, 60)
plt.xlabel("Frequence (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of fully cleaned signal")
plt.show()


spectrum_dirty_signal = np.fft.fft(ultra_dirty_signal)
freqs_dirty_signal = np.fft.fftfreq(len(ultra_dirty_signal), 1/fs)
plt.figure()
plt.plot(freqs_dirty_signal, np.abs(spectrum_dirty_signal))
plt.xlim(0, 60)
plt.xlabel("Frequence (Hz)")
plt.ylabel("Magnitude")
plt.title("Spectrum of fully cleaned signal")
plt.show()

file_path = "S001R01.edf"

raw = mne.io.read_raw_edf(file_path, preload=True)

print(raw)
print(raw.info)

print(raw.ch_names)