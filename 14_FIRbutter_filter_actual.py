import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import cmath


# Generate a signal made up of 5 Hz and 20 Hz, sampled at 1 kHz
# 1second# from 0 to 1 generate 1000 samples for time.
t = np.linspace(0, 2, 1000, False)

sig = (np.sin(2 * np.pi * 5*t) + np.cos(2 * np.pi * 20*t)) * np.exp(-t)

fig, (first, second_magni, third, forth) = plt.subplots(4, 1)

first.plot(t, sig)
first.set_title("10 hz and 20 hz signal")
first.set_xticks([0, 2])
first.set_yticks([-2, 2])

sos = signal.butter(10,  15, 'highpass', output='sos', fs=1000)  # sos
[b, a] = signal.butter(4,  100, 'highpass', output='ba',
                       fs=1000)  # numerator and denominator
w, h = signal.freqs(b, a)


# sos = signal.butter(10,  15, 'lowpass', output='sos', fs=1000)
# sos = signal.butter(10, [10, 15], 'bandpass', output='sos', fs=1000)
# sos = signal.butter(10, [10, 15], 'bandstop', output='sos', fs=1000)
fsig = signal.sosfilt(sos, sig)

second_magni.plot(t, fsig)
second_magni.set_xticks([0, 2])
second_magni.set_yticks([-2, 2])
second_magni.set_title("After  15hz high pass filter")


# dB gain
third.semilogx(w, 20*np.log10(abs(h)))
third.set_title("Freq respone")
third.set_xlabel("Angular Freq[rad/sec]")
third.set_ylabel("Amplitude[dB]")

# phase
phase_li = []
for i in h:
    phase_li.append(cmath.phase(i))

forth.plot( phase_li)
forth.set_xlabel("")
forth.set_xlabel("Phase [rad]")


plt.show()

# order = 10, cutoff_freq= 15, sampling_freq= 1kHz

#  omega = w
# freq = h
#  w = 2pi* h
#  sin(2 pi w t)
