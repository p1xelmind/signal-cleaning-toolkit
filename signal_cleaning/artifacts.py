import mne
from mne.preprocessing import ICA

def apply_ica(
        raw: mne.io.BaseRaw,
        n_components: int = 20,
        random_state: int = 42
) -> tuple[mne.io.BaseRaw, ICA]:
    raw_copy = raw.copy()

    ica = ICA(
        n_components=n_components,
        random_state=random_state,
        max_iter='auto'
    )

    ica.fit(raw_copy)

    return raw_copy, ica