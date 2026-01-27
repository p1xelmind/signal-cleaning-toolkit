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