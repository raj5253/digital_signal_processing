import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Generate a signal made up of 10 Hz and 20 Hz, sampled at 1 kHz
t = np.linspace(0, 1, 1000, False)   # 1000 saples in 1 sec
sig = (np.sin(2 * np.pi * 5*t) + np.cos(2 * np.pi * 20*t)) * np.exp(-t)

fig, (first, second) = plt.subplots(2, 1, sharex=True)  #

first.plot(t, sig)
first.set_title("10 hz and 20 hz signal")
first.set_xticks([0, 1])
first.set_yticks([-2, 2])


sos = signal.butter(10, 15, 'highpass', output='sos', fs=1000)  #
fsig = signal.sosfilt(sos, sig)

second.plot(t, fsig)
second.set_xticks([0, 1])
second.set_yticks([-2, 2])
second.set_title("After  15hz high pass filter")
plt.show()

# sos = signal.butter(10, 15, 'hp', output='sos', fs=1000)
# sos = signal.butter(10, ,[10, 20], 'bandpass', output='sos', fs=1000)
# sos = signal.butter(10, [10,20], 'bandstop', output='sos', fs=1000)
#  order =10, crtical_freq= 15, type= 'highpass', ouput='sos', sampling_freq= 1khz

# create time samples
# create a signal
# get sos fuction by signal.butter
# get fsignal by signal.sosfilter

# plot signal in first
# plot fsignal  in second
