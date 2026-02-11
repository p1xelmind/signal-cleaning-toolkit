import mne

def apply_average_reference(raw: mne.io.BaseRaw) -> mne.io.BaseRaw:
    raw_ref = raw.copy().set_eeg_reference('average')
    return raw_ref