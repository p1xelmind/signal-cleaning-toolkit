from scipy import signal
import numpy as np

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