import mne
from pathlib import Path

data_path = Path(__file__).parent.parent / "data" / "raw" / "S001R01.edf"

raw = mne.io.read_raw_edf(data_path, preload=True)

print(raw)

raw.info

raw.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    block=True
)