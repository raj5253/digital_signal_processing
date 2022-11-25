import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Generate a signal made up of 5 Hz and 20 Hz, sampled at 1 kHz
# 1second# from 0 to 1 generate 1000 samples for time.
t = np.linspace(0, 1, 1000, False)

sig = (np.sin(2 * np.pi * 5*t) + np.cos(2 * np.pi * 20*t)) * np.exp(-t)

fig, (first, second) = plt.subplots(2, 1, sharex=True)

first.plot(t, sig)
first.set_title("10 hz and 20 hz signal")
first.set_xticks([0, 1])
first.set_yticks([-2, 2])

sos = signal.cheby1(10, 20, 15, 'highpass', output='sos', fs=1000)
# sos = signal.cheby1(10, 10, 15, 'lowpass', output='sos', fs=1000)
fsig = signal.sosfilt(sos, sig)

second.plot(t, fsig)
second.set_xticks([0, 1])
second.set_yticks([-2, 2])
second.set_title("After  15hz high pass filter")
plt.show()

# order = 10, ripple =10, cutoff_freq= 15, sampling_freq= 1kHz
# if ripple= 1, then it behaves as butterworth.

#  omega = w
# freq = h
#  w = 2pi* h
#  sin(2 pi w t)
