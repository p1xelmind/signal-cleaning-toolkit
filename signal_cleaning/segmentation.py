import mne  

def segment_fixed_length(
        raw: mne.io.BaseRaw,
        window_length: float,
        overlap: float = 0.0
) -> mne.Epochs:
    if window_length <= 0:
        raise ValueError("window_length must be positive")
    
    if overlap < 0:
        raise ValueError("overlap cannot be negative")
    
    if overlap >= window_length:
        raise ValueError("overlap must be smaller than window_length")
    
    epochs = mne.make_fixed_length_epochs(
        raw,
        duration=window_length,
        overlap=overlap,
        preload=True,
        reject_by_annotation=True
    )

    return epochs