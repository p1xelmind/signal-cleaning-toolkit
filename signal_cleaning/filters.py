from scipy import signal
import numpy as np
import mne

def highpass_filter(
        data: np.ndarray,
        cutoff: float,
        fs: int,
        order: int
) -> np.ndarray:
    nyquist = fs / 2
    normal_cutoff = cutoff / nyquist
    sos = signal.butter(order, normal_cutoff, btype='high', analog=False, output='sos')
    y = signal.sosfiltfilt(sos, data)
    return y


def notch_filter(
        data: np.ndarray,
        f: float,
        fs: int,
        q: float
) -> np.ndarray:
    b,a = signal.iirnotch(f, q, fs)
    sos = signal.tf2sos(b, a)
    y = signal.sosfiltfilt(sos, data)
    return y


def lowpass_filter(
        data: np.ndarray,
        cutoff: float,
        fs: int,
        order: int
) -> np.ndarray:
    nyquist = fs / 2
    normal_cutoff = cutoff / nyquist
    sos = signal.butter(order, normal_cutoff, btype='low', analog=False, output='sos')
    y = signal.sosfiltfilt(sos, data)
    return y


def filter_mne(data: mne.io.BaseRaw) -> mne.io.BaseRaw:
    filtered = data.copy()

    filtered.filter(
        l_freq = 1.0,
        h_freq = 40.0,
        picks='eeg',
        fir_design='firwin'
    )

    filtered.notch_filter(
        freqs=50,
        picks='eeg'
    )

    return filtered
