import mne
from pathlib import Path
import matplotlib.pyplot as plt

data_path = Path(__file__).parent.parent / "data" / "raw" / "S001R01.edf"
raw = mne.io.read_raw_edf(data_path, preload=True)

raw.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    block=True
)

raw.plot_psd(fmax=60)
plt.show(block=True)

raw_filt = raw.copy()

raw_filt.filter(
    l_freq=1.0,
    h_freq=40.0,
    picks="eeg",
    fir_design="firwin"
)

raw_filt.notch_filter(
    freqs=50,
    picks="eeg"
)

raw_filt.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    block=True
)

raw_filt.plot_psd(fmax=60)
plt.show(block=True)