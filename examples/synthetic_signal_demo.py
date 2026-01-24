import numpy as np

fs = 250
duration = 2
n_samples = int(fs * duration)

t = np.linspace(0 , duration, n_samples) 

signal_alpha = np.sin(2 * np.pi * 10 * t)