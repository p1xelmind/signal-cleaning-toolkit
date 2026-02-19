import mne
from pathlib import Path
import matplotlib.pyplot as plt
from signal_cleaning.normalization import apply_average_reference
from signal_cleaning.filters import filter_mne

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

raw_copy = raw.copy()

raw_copy = filter_mne(raw_copy)
raw_copy = apply_average_reference(raw_copy)

raw_copy.plot_psd(fmax=60)
plt.show(block=True)