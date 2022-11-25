import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Generate a signal made up of 10 Hz and 20 Hz, sampled at 1 kHz
# 1second# from 0 to 1 generate 1000 samples for time.
t = np.linspace(0, 1, 1000, False)

sig = np.sin(2*np.pi * 10*t) + np.sin(2*np.pi * 20 * t)

fig, (first, second) = plt.subplots(2, 1, sharex=True)

first.plot(t, sig)
first.set_title("10 hz and 20 hz signal")
first.set_xticks([0, 1])
first.set_yticks([-2, 2])

sos = signal.cheby1(10, 1, 15, 'highpass', output='sos', fs=1000)
# sos = signal.cheby1(10, 1, 15, 'lowpass', output='sos', fs=1000)
fsig = signal.sosfilt(sos, sig)

second.plot(t, fsig)
second.set_xticks([0, 1])
second.set_yticks([-2, 2])
second.set_title("After  15hz high pass filter")
plt.show()


#  omega = w
# freq = h
#  w = 2pi* h
#  sin(2 pi w t)

# sos = signal.cheby1(10, 1, 15, 'highpass', output='sos', fs=1000)
# sos = signal.cheby1(10, 1, 15, 'lowpass', output='sos', fs=1000)
# sos = signal.cheby1(10, 1, [10, 20], 'bandpass', output='sos', fs=1000)
# sos = signal.cheby1(10, 1, [10, 20], 'bandstop', output='sos', fs=1000)
# order = 10, ripple =1, cutoff_freq= 15,output = 'sos', sampling_freq= 1kHz

# create time samples
# create a signal
# get sos fuction by signal.cheby1
# get fsignal by signal.sosfilter

# plot signal in first
# plot fsignal  in second
