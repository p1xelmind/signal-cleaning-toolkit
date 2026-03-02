import mne
from pathlib import Path
import matplotlib.pyplot as plt
from signal_cleaning.normalization import apply_average_reference
from signal_cleaning.filters import filter_mne
from signal_cleaning.artifacts import fit_ica, apply_ica
from signal_cleaning.segmentation import segment_fixed_length

data_path = Path(__file__).parent.parent / "data" / "raw" / "S001R01.edf"
raw = mne.io.read_raw_edf(data_path, preload=True)

raw.set_montage(None)
raw.rename_channels(lambda name: name.strip('.').upper())

mapping = {}
for ch in raw.ch_names:
    if ch == 'FP1':
        mapping[ch] = 'Fp1'
    elif ch == 'FP2':
        mapping[ch] = 'Fp2'
    elif ch == 'FPZ':
        mapping[ch] = 'Fpz'
    elif ch.endswith('Z') and len(ch) > 1:
        mapping[ch] = ch[:-1] + 'z'
    else:
        mapping[ch] = ch
raw.rename_channels(mapping)

montage = mne.channels.make_standard_montage("standard_1005")
raw.set_montage(montage, on_missing="warn") 
'''
raw.plot(
    duration=5,
    n_channels=10,
    scalings="auto",
    block=True
)

raw.plot_psd(fmax=60)
plt.show(block=True)
'''
raw_copy = raw.copy()

raw_copy = filter_mne(raw_copy)
raw_copy = apply_average_reference(raw_copy)

ica = fit_ica(raw_copy, 20, 42)
'''
ica.plot_components()
plt.show(block=True)
ica.plot_sources(raw_copy)
plt.show(block=True)
ica.plot_properties(raw_copy, picks=[9])
plt.show(block=True)
'''
ica.exclude = [0, 3, 5, 13, 19]
raw_copy = apply_ica(raw_copy, ica, ica.exclude)


# raw siganl
raw.plot(picks=['Fp1', 'Fp2', 'O1', 'O2'], duration=10, scalings=dict(eeg=100e-6), block=True, title='Raw EEG')

# cleaned signal (after ICA)
raw_copy.plot(picks=['Fp1', 'Fp2', 'O1', 'O2'], duration=10, scalings=dict(eeg=100e-6), block=True, title='Cleaned EEG')

epochs = segment_fixed_length(raw_copy, window_length=2.0)
print(epochs)

epochs.plot(n_epochs=5, n_channels=10, scalings="auto", block=True)

data = epochs.get_data()
print(data.shape)