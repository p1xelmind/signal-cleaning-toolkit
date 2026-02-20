import mne 
from mne.preprocessing import ICA 
from typing import List

def fit_ica(
        raw: mne.io.BaseRaw,
        n_components: int = 20,
        random_state: int = 42
) -> ICA:
    ica = ICA(
        n_components=n_components,
        random_state=random_state,
        max_iter="auto"
    )

    ica.fit(raw)

    return ica


def apply_ica(
        raw: mne.io.BaseRaw,
        ica: ICA,
        exclude: List[int]
) -> mne.io.BaseRaw:
    raw_clean = raw.copy()

    ica.exclude = exclude
    ica.apply(raw_clean)

    return raw_clean